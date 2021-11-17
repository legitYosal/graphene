# Welcome to the graphql by flask playground

This project intends to implement a task manager application using graphql, sqlalchemy and flask.  
Challenges I am trying to solve are:
* using SQLAlchemy ORM in a professional way(Using alembic for migrations).


# Installation
Setup project environment:
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ flask db upgrade
```

You can run tests:
```
$ pytest
```


# Resources and Notes
Here are some good articles and documentations that I found useful:  
* [How to create a one to many relation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships)
* [Using migrations for sqlalchemy](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)  
* [Using multi choice in sqlalchemy](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.choice)
* [Hashing passwords in flask](https://github.com/maxcountryman/flask-bcrypt)

And Here are some usefull snippets:
* Initation of migrations using flask cli:
```
$ flask db init # initate migrations
$ flask db migrate # create migration files
```

