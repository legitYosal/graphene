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

Run server in debug mode:
```
$ python3 app.py
# graphene endpoint is running on :5000/graphql
```

Flask graphene uses graphiql for web client to interact with exposed graphql interface, but it does not support sending extra headers, and we need to send token to authenticate.  
I have used [Altair tool](https://altair.sirmuel.design/) to send graphql requests and add auth header.  

Follow these steps to register a user
```
mutation {
  registerUser(email: "example@gmail.com", password: "123") {
    user {
      id
      email
      isActive
    }
  }
}

mutation {
  activateUser(id: $id) {
    user {
      id
      email
      isActive
    }
  }
}
```

You can obtain a JWT by the following mutation
```
mutation {
  tokenAuth(email:"example@gmail.com", password: "123") {
    payload
    token
    refreshExpiresIn
  }
}
```

And after adding the provided token in the request header you can interact with tasks using these queries and mutations
```
# Add Authorization: JWT <token> to request headers


mutation{
	createTask(title: "nnn", dueDate: "2020-04-01T00:00:00Z") {
    task {
      id
      title
      createdAt
      dueDate
      status
    }
  }
}

query{
  tasks{
    id
    title
    createdAt
    dueDate
  }
}

mutation{
	updateTask(status: INPROGRESS, id: 1) {
    task {
      id
      title
      createdAt
      dueDate
      status
    }
  }
}

mutation{
  deleteTask(id:3){
    task{
      id
      title
    }
  }
}
```

# Resources and Notes
Here are some good articles and documentations that I found useful:  
* [How to create a one to many relation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/#simple-relationships)
* [Using migrations for sqlalchemy](https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/)  
* [Hashing passwords in flask](https://github.com/maxcountryman/flask-bcrypt)

And Here are some usefull snippets:
* Initation of migrations using flask cli:
```
$ flask db init # initate migrations
$ flask db migrate # create migration files
```

