# Create project
## Go the project folder
run "poetry init"
it creates pyproject.toml file

run "poetry add fastapi uvicorn"
it adds dependency of fastapi,uvicorn in pyproject.toml

## create .env file and .gitignore file
## create 2 folders src , tests
## add main.py file in src folder


## create a virtual env """python -m venv venv
##                     .\venv\Scripts\Activate"""


# Project structure
my_project/
├── pyproject.toml
├── README.md
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── router.py
│   │   ├── v1/routes
│   │   │   ├── __init__.py
│   │   │   ├── healthCheck.py
└── tests/ 


### To run project
run "poetry install"
run "python src/main.py"

## to setup tests
run "pip install pytest"
"poetry add pytest"

## to run test
cd to tests folder run "pytest"

## setup sonar can be done
