# Basic API for Meal app
- https://obscure-refuge-91043.herokuapp.com/


Following this tutorial: https://realpython.com/flask-by-example-part-1-project-setup/

## Virtual Env
- With autoenv set up, it should automatically enter the virtual environment
  when you 'cd' into the directory. If it doesn't, check that this line is in
  .bashrc or .profile. (You can find the path to activate.sh with `which
  activate.sh` if autoenv is installed.)
  - `source /usr/local/bin/activate.sh`
- Get into python virtual environment
  - while in the flask-api directory (where the 'env' folder is located)
  - `source env/bin/activate`
- Get out of python virtual environment
  - `deactivate`


## Start local development
- Start Postgres locally, unless connecting to remote Postgres server
- Make sure you are in the virtual env (see above)
  - `python manage.py runserver`
- The site is now available at [http://localhost:5000 ](http://localhost:5000)

## Push to heroku
- Add and commit any changes, then
  - `git push -u heroku master`
