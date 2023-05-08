# Welcome to my blog

## Technologies Used
---
* Python (Flask)
* MongoDB
* HTML/Bootstrap

## Purpose
---
Gain an understanding of using api's, webservers, routing HTTPS requests and creating a project using a modular approach.

## Layout
---
* flask_blog
    * .venv
    * flask_session
    * .flaskenv
    * requirements.txt
    * src
        * common
        * models
            * blog.py
            * post.py
            * user.py
        * static
            * css
            * img
            * vids
        * templates (html)
            * Going to add soon. Need to reduce some.
        * app.py (No longer in use)
        * __init__.py (leverages blueprint)
        * auth.py   (handles authorization blueprint)
        * config.py (handles configuration keys)
        * main.py   (handles main authorization files )



## Directions
---
Before you proceed, I will state that I have a config.py file to maintain my newsapiclient key. You most likely will have to go to newsapi and get it to utilze the project similarly
> Okay, so this how I run it. Enter the flask_blog directory. (Assuming only powershell for now).
>
>```shell
>cd flask_blog
>```
>
> Create an environment using python
>>```Python
>>python -m venv .venv
>>```
>
> Download requirements
>>```
>>pip install -r requirements.txt
>>```
>
> Run the app
>>```Python
>>flask run
>>```
>



# Current focus

* Upgrading database features to be more interactive with the site
    * delete

* Adding subpost capability to blog.
* Clean up blueprint logic with auth and main
* Think about deployment
    * Heroku
    * Netlify
    * Docker
    * K8 image

* Strengthening blueprints logic
    * Authentication Blueprint (login, logout, recover password)
    * Blog Blueprint 
    * General Blueprint
    * API for blog blue print?
    
