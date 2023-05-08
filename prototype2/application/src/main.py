from flask import Blueprint, render_template, request, session, make_response, url_for, redirect
from src.common.database import Database
from src.models.blog import Blog
from src.models.post import Post
from src.models.user import User
from newsapi import NewsApiClient
# import config

main = Blueprint('main', __name__)

@main.route('/')
def home_template():
    
    if not session.get("email"):
        return redirect("login")
    
    newsapi = NewsApiClient('c8f4bcf0d4814a4dbe2544d097202089')
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
    
    articles = topheadlines['articles']
    
    desc = []
    news = []
    img = []
    
    for i in range(len(articles)):
        
        news.append(articles[i]['title'])
        desc.append(articles[i]['description'])
        img.append(articles[i]['urlToImage'])
        
    mylist = zip(news, desc, img)
    
    return render_template('home.html', context = mylist)


@main.route('/profile')
def profile():
    if not session.get("email"):
        return redirect("/login")
    
    # display all of a user blogs for them
    user  = User.get_by_email(session['email'])
    blogs = user.get_blogs()
    
    
    return render_template('profile.html', email=session['email'], blogs=blogs)


@main.route('/blogs/<string:user_id>')
@main.route('/blogs')
def user_blogs(user_id=None):
    if user_id is not None:
        user = User.get_by_id(user_id)
    else:
        user = User.get_by_email(session['email'])

    blogs = user.get_blogs()

    return render_template("user_blogs.html", blogs=blogs)


@main.route('/blogs/new', methods=['POST', 'GET'])
def create_new_blog():
    if request.method == 'GET':
        return render_template('new_blog.html')
    else:
        title = request.form['title']
        description = request.form['description']
        user = User.get_by_email(session['email'])

        new_blog = Blog(user.email, title, description, user._id)
        new_blog.save_to_mongo()

        return make_response(user_blogs(user._id))
    
@main.route('/blog/delete', methods=['GET', 'POST'])
def remove_blog():
    if request.method == 'GET':
        
        user = User.get_by_email(session['email'])
        blogs = user.get_blogs()
        
        return render_template('remove_blog.html', blogs=blogs)
    else:
        # get blog id
        blog_id = request.form['blog_id']
        # find blog
        blog = Blog.from_mongo(blog_id)
        # remove it from the db
        blog.remove_from_mongo()
        
        return redirect(url_for('main.profile'))

# to show blogs from all users to each other
@main.route('/blogs/all')
def display_all_blogs():
    
    user_ids = []
    blogs = []
    
    # counts the amount of users in the db
    count = Database.DATABASE['users'].count_documents({})
    print(count)
    
    # got user id
    
    for user_id in Database.DATABASE['users'].find({}, {"_id": 1}): # 2 rn
        # now that we have the user id as value in dicts we need to append to list
        user_ids.append(user_id['_id'])
        
    # now that i have all user ids in a list i need to use them to get each users blog
    for user_id in user_ids:
        blogs.append(Blog.find_by_author_id(user_id))
    
    
    # blogs[user 1][blog 1]
    blog_titles = []
    blog_descriptions = []
    blog_authors = []
    
    # blog_created = [] (Huge Mess)
    
    '''
        Current issue is getting all blogs of each user to
        iterate. not one blog per usually. Until i come up with
        dictionary solution, I might be able to brute force it
        with double for loop in jinja. ALL code here needs to
        be reoptimized with Dictionary
    '''
    
    
    for user in range(count):
        for blog in range(len(blogs[user])):
            print(len(blogs[user]))
            blog_titles.append(blogs[user][blog].title)
            blog_descriptions.append(blogs[user][blog].description)
            blog_authors.append(blogs[user][blog].author)
            
            
    print(blog_titles, " ")
    print(blog_descriptions, " ")
    
    return render_template("all_blogs.html", blog_titles=blog_titles, blog_descriptions = blog_descriptions,
                           blog_authors=blog_authors, count = count)
    

@main.route('/posts/<string:blog_id>')
def blog_posts(blog_id):
    blog = Blog.from_mongo(blog_id)
    posts = blog.get_posts()

    return render_template('posts.html', posts=posts, blog_title=blog.title, blog_id=blog._id)


@main.route('/posts/new/<string:blog_id>', methods=['POST', 'GET'])
def create_new_post(blog_id):
    if request.method == 'GET':
        return render_template('new_post.html', blog_id=blog_id)
    else:
        title = request.form['title']
        content = request.form['content']
        user = User.get_by_email(session['email'])

        new_post = Post(blog_id, title, content, user.email)
        new_post.save_to_mongo()

        return make_response(blog_posts(blog_id))
    
@main.route('/pricing')
def pricing():
    return render_template('pricing.html')


