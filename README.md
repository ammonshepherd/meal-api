# Basic API for Meal app
- https://obscure-refuge-91043.herokuapp.com/


Following this tutorial: https://realpython.com/flask-by-example-part-1-project-setup/

## Virtual Env
- This uses the default, built-in module 'venv'. To create your virtual
  environment set up, do
  - `python -m venv .venv`
  - This will create a .venv directory and put all the needed stuff in it.
- To get into python virtual environment 
  - while in the flask-api directory (where the '.venv' folder is located)
  - `source .venv/bin/activate`
- Get out of python virtual environment
  - `deactivate`

## Local Environment Variables
- A couple of environment variables are needed to set if the app is in
  developer or production mode, and to set the database URL.

  ```
    #.env file
    export APP_SETTINGS="config.DevelopmentConfig"
    export DATABASE_URL="postgresql://mealer:mealer@localhost:5432/mealer"
  ```
- Run `source .env` to create those environment variables.

## Start Local Development
- Start Postgres locally, unless connecting to remote Postgres server
- Make sure you are in the virtual env (see above), then start Flask
  - `flask run`
- The site is now available at [http://localhost:5000 ](http://localhost:5000)
### Local Development: Docker version
- just run `docker-compose up -d` and this will set up your development
  environment:
  - pgAdmin: http://pga.lvh.me
  - Flask: http://lvh.me or http://pfp.lvh.me

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
      generated. Sometimes it doesn't quite know what you want. 
    - For example, changing a table name will automatically drop the old table
      and create a new one. 
    - Instead, change that to use the rename_table command for the upgrade and
      downgrade.
- Delete the changes from the database, then run the upgrade command to redo
  the changes
  - `python manage.py db upgrade`

### Run the changes
- Run the upgrade locally
  - `python manage.py db upgrade head`
- Run the upgrade on heroku
  - `heroku run python manage.py db upgrade`

