web project

prototype
| 
|-- src
|   |
|   |-- common
|   |      |
|   |      |-- database. py
|   |
|   |-- models
|   |     |
|   |     |-- blog.py
|   |     |
|   |     |-- post.py
|   |     |
|   |     |-- user.py
|   |
|   |-- static
|   |     |
|   |     |-- img/vid
|   |
|   |-- templates (all html templates)
|
|-- init.py (main application)
|
|-- app.py (old main application to be removed)
|
|-- auth.py (blue print, deals with app auth)
|
|-- main.py (deals with main pages need to auth)
|
|-- .flaskenv (environment variables)
|
|-- .venv (environment to take avoid dependencies)


What to focus on?

Upgrading database features to be more interactive with the site?
- delete

Do I want subposts under blogs? Or do i want a blog
post to be the main point.

Make sure logic is intact between authorization and main pages. Do I want users to have to sign in? Make sure cookies are being stored properlly as well and dont forget to find a safer place for api key in news posts.

Pages that need design.
- web dev page
- support page
- contact page