# A basic blogging app<br>
Learning how to use flask<br>
Flask uses Jinja2 for templates<br>
Using Werkzeug for hashing<br>
Using virtual environment.

# Some commands:
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

# Refrence:
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
