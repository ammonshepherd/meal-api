# Basic API for Meal app
- https://obscure-refuge-91043.herokuapp.com/


Following this tutorial: https://realpython.com/flask-by-example-part-1-project-setup/

## Virtual Env
- With autoenv set up, it should automatically enter the virtual environment
  when you 'cd' into the directory. If it doesn't, check that this line is in
  .bashrc or .profile. (You can find the path to activate.sh with `which
  activate.sh` if autoenv is installed.)
  - `source /usr/local/bin/activate.sh`
- Get into python virtual environment manually and set the required local
  environment variables
  - while in the flask-api directory (where the 'env' folder is located)
  - `source .env`
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


## Database Management
- using Flask-Migrate (which uses Alembic and SQLAlchemy)

### Manual migration file
  - Create a new migration (to add a new column)
    - `python manage.py db revision -m "Add new column"`
    - This will create a new file in `migrations/versions/` named like `<hash>-add-new-column.py`
    - Then add commands to the 'upgrade' and 'downgrade' functions.
    - A list of commands are found here: https://alembic.sqlalchemy.org/en/latest/ops.html#ops

### Autogenerate migration file
- Make the changes in the database (using a graphical database tool or command
  line)
- Back in the terminal, in this directory, run
  - `python manage.py db migrate`
- This will generate a migration file in `migrations/versions/` with the
    changes you made in the database. 
    - **NOTE** You'll definitely want to double check what is automatically
    generated. Sometimes it doesn't quite know what you want. For example,
    changing a table name will automatically drop the old table and create a
    new one. Instead, change that to use the rename_table command for the
    upgrade and downgrade.
    
### Run the changes
- Run the upgrade locally
  - `python manage.py db upgrade head`
- Run the upgrade on heroku
  - `heroku run python manage.py db upgrade`

