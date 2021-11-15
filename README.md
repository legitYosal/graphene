# Welcome

This is a minimal project using graphene with django and user authentication to expose a graphql endpoint.  
Definitely checkout how I have managed Authentication using graphene_jwt...  

# Start this up

Setup project environment
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Run server
```
python3 manage.py runserver 0.0.0.0:8000
```
Next go to [graphql GUI](http://localhost:8000/graphql) and you are able to send graphql requests...  

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
# Actually you can add this header in graphene GUI

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

# Resources
Here are some good articles and documentations I have found.  
[How to create a simple graphql endpoint?](https://www.moesif.com/blog/technical/graphql/Getting-Started-with-Python-GraphQL-Part1/)  
[JWT authentication on graphene](https://django-graphql-jwt.domake.io/authentication.html)