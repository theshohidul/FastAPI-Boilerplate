
# FastAPI Boilerplate

A dockerized FastAPI Boilerplate with JWT, Loguru logging middleware, Role based authorization, SQLAlchemy ORM with AsyncSession.

Some endpoints are added as demo purpose, like: auth, register and login.


## Dependencies
In this project [poetry](https://python-poetry.org/) is used as package dependency manager. Below python packages are used in this project.
 
- python = "^3.9"
- uvicorn = {version = "0.17.6", extras = ["standard"]}
- fastapi = {version = "0.80.0", extras = ["all"]}
- json-log-formatter = "0.4.0" 
- SQLAlchemy = "^1.4.40"
- alembic = "^1.8.1"
- databases = {extras = ["aiomysql"], version = "^0.6.1"}
- loguru = "^0.6.0"
- cryptography = "^38.0.1"
- bcrypt = "^4.0.0"
- PyJWT = "^2.5.0"

## How To Run Locally

Clone the project

```bash
  git clone https://github.com/theshohidul/FastAPI-Boilerplate.git
```

Go to the project directory

```bash
  cd FastAPI-Boilerplate
```

To run this project locally, go to `/docker` folder and edit `.env` file if required. 
Then open a terminal inside the `/docker` folder and run the below command in the terminal.

```bash
  docker compose up 
```
After docker containers are up, you can access the application in: http://localhost:8080

Then  exec inside the app container, and go to /app/core/db/migrations - run below command: 
```bash
  alembic upgrade head
```

This will create all required tables.

## Contributing

Contributions are always welcome!


## Authors

- [@theshohidul](https://github.com/theshohidul)


## 🚀 About Me
I'm a full stack developer...

