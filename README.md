# Microblog
A blogging application with following features:
1. Allows user to log in and out.<br>
2. Register new users.<br>
3. Password recovery.<br>
4. Users can post blogs.<br>
5. User profile page containing their bio(user bio, last seen, followers, users followed).<br>
6. Post by users followed(pagination that allows going back and forth the list).
7. Able to see all the posts made by other users.<br>
8. Follow other users.
9. Search posts.
10. Translate blogs in different language.
11. Send private message to others.

# Some commands and extensions used:
1. python3 -m venv venv (virtual environment)
2. virtualenv venv (for python2; first install virtualenv)
3. source venv/bin/activate (activate venv)
4. pip install flask (flask install)
5. export FLASK_APP=microblog.py (set up environment)
6. flask run
7. pip install flask-wtf (extension to handle web-forms)
8. app.config contains the configurations of the frameworks as a configuration variable
9. pip install flask-sqlalchemy (database)
10. pip install flask-migrate (database migration)
11. pip install flask-login (different functionalities which help in user log-in)
12. export FLASK_DEBUG=1 (for debugging mode and reloader)
13. flask db migrate -m \<comment\> (make changes in the database)
14. flask db upgrade (migration)
15. Use jinja2 to render templates.
