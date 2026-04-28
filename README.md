# Data Version Control - DVC

* First intall dvc using `pip install dvc`

* Initialize dvc in your project using `dvc init`

* Set the remote storage for dvc using `dvc remote add -d <remote_name> <remote_url>` in first example we are using local storage so the command will be `dvc remote add -d myremote S3`

* Add data folder to dvc using `dvc add <data_folder>` in our case it will be `dvc add data/`

* Then we commit the dvc files using `dvc commit`

* Finally push the data to remote storage using `dvc push`

* After some changes `dvc status` to check the status of dvc tracked files

# YAML Crash Course

* Indentation based markup language
* Key value pair with : 
* Supports list like 
* ```YAML
	  Fruit:
		  - Apple
		  - Orange
		  - Banana
  ```
  * Multiline String as 
  * ```YAML
	    This is a example |
		    of multiline String
		    of YAML
    ```

# AWS S3 with DVC

* Create a **`dvc.yaml`** file and add the stages in it for automation
* Run `dvc repro` to test the automation of the `dvc.yaml` file's stages, use `dvc repro -f` to force the rerun
* It will run and create a `dvc.lock` file with all the stage's data hash and config
* Use `dvc dag` to get  the visual representation of the pipeline stages (Directed Acyclic Graph)
* To track the metrics for the experiments with different parameters we will use `dvclive`
* To use *dvclive* use the code `dvc exp run`
* Add `Params` in the `dvc.yaml` file so that dvc can track the changes, else it will not track changes and say the files are unchanged even if you change the parameters
* Create a `AWS Account`
* Create a `IAM User` and create its `access key`
* Create a `S3 Bucket` 
* Install pip packages i.e `pip install dvc[s3]` and `pip install awscli`
* Then type `aws configure` and add AWS Key, Secret key and Account Region for the `iam user` created
* Then type `dvc remote add -d dvcstore s3://mlops-dvc-pk` *i.e s3://<bucket_name>*
* Run `dvc exp apply <exp_name>` to reproduce the experiment
* Run `dvc commit` and `dvc push` to upload the data in `S3 bucket`
* We can add a stage to the `dvc yaml` file using one line command as well like `dvc stage add -n data_ingestion -d src/data_ingestion.py -o data/raw python src/data_ingestion.py`

# MLFlow

* First to start with run `pip install mlflow`
* Then tryout `mlflow ui`
* The mlflow default database is depreciated while I started using the module so I used `mlflow ui --backend-store-uri sqlite:///mlflow.db` to switch the database to sqlite for the demo
* The difference between an experiment and a run - Run is a single instance of the code execution while the experiment is all the runs that were made under it to tune the results. Experiment can be different types of ML Models like RandomForest or CNN and runs can be iterations of those.
* Using `mlflow.log_artifact` we can save the figures and code of the script `(__file__)` as well in mlflow
* Use `mlflow.set_experiment("Name")` to create a custom experiment name 
* Using `mlflow.log_model()` we can save the model details as well and that gives us the requirements.txt, pickle file and other creation files for the model as well.
  ![[Mlflow_ss.png]] 
* For using it in the best way use `AWS` or `DagsHub`
* For using in ***AWS*** we will need `IAM` User to access to and from, `EC2 Server` it can store the light metadata and `S3 Bucket` will save the `Model Data or Artifacts` 
* For Using ***DagsHub***  create a account and link your github repository, and it will give you the `mlflow remote tracking id` and everything needed for using remote mlflow
* Use `pip install dagshub` to use the dagshub code in the scripts
* Using `mlflow.autolog()` to log all the parameters, metrics, model and dataset of the experiment. While script data and tags need to be added manually.

# Continuous Integration (CI)

* To use `CI using Github actions` we first need to create a folder pattern in our repository like `.github/workflows`
* We need to create a `yaml` file inside with the actions rules, can be found on github actions as well

# Docker Details

* Create a `dockerfile` to place the `instructions` and the `blueprints` of the image
* `FROM` specifies the base image
* `COPY` or `ADD` adds the files from the host system into the building image
* `RUN` executes the command in the image such as installing a software
* `CMD` or `ENTRYPOINT` defines the command that executes when the new image starts
* `EXPOSE` specifies the port the image container listens to
* Use `docker build -t <name> .` to build a docker image from a `dockerfile` in the current folder with the `tag` name and version `latest` by default
* `Containers` are an instance of the `images`
* To pull someone else's image from a registry use `docker pull` i.e. `docker pull vikash95/flask-docker-demo`

# Project 1 - Vehicle Insurance Domain

* We used a `template_generator` script to generate the skeleton of the project. 
* We will learn the use of `-e .` in `pip install` or `uv add -r req.txt --dev` know as editable mode, we need a setup.py file to install the local code as python package
* We can use `conda create -n vehicle python=3.10 -y`  and then `conda activate vehicle` to create venv with python 3.10 and use it, even if its not already there in the system which is not possible with uv. 
* We created a account in `MongoDB Atlas` Create a `Organization` and `Project`
* Then we want to `create a cluster` in the Project, there we currently chose a `free tier` and default options that comes with it.
* This Cluster will be our `cloud mongoDB` where we will create our `databases` and `collections`
* After cluster creation the UI will prompt to `create a database user`, we copied that credentials and adjusted it as needed
* Then from `Database and Network access` we `add ip address` of `our machine` or `0.0.0.0` i.e. allow access from anywhere. We can create database user from here as well.
* In the project page, scroll down and click on get connection string and get something like `mongodb+srv://preyumkr:<db_password>@cluster0.teb8wrs.mongodb.net/?appName=Cluster0` after selecting `python` and appropriate version matching
* Created own custom exception module while using `import traceback` and doing `tb = traceback.format_exc()` in exception part should be enough
* We looked at a `ML_DataScience` Notebook and will be going to replicate a `MLOps Pipeline` replicating that notebook
* Then we created a `constants init file` to enable the variables to be edited at a single point and be used everywhere in the code and any change needs change only in the single file.
* We have `__init__.py` in all folders so that we can use all of them as package modules
* To save env variables for testing in `powershell` use `$env:AWS_ACCESS_KEY_ID="value"`
* To verify we can do `echo $env:AWS_ACCESS_KEY_ID`
* Created docker image file for the project, `.dockerignore` excludes the files or directories mentioned in it from the docker build context. So, if we do `docker build` with a `.dockerignore` file there in the same directory the files mentioned in it will not be visible to the `docker build` command so even if there is a `copy .` command in the `dockerfile` the build command can't see the ignored files and those will not be copied.
* We created a `AWS ECR` repository for our `docker image`, Created a `AWS EC2` instance and installed docker in it and then used Github Actions for **`AWS EC2`** deployment
* In my case I had to use the `/train` route to create the `model.pkl` before being able to get the predictions.
* To restart the runner service in the instance again we need to go to the runner directory and then run `sudo ./svc.sh install` and then `sudo ./svc.sh start` 

# FastAPI

* **API** - These are mechanisms that enable two software components to communicate, be it a frontend and a backend or multiple clients and a central backend. It uses a defined set of rules e.g. REST, protocols e.g. HTTP and data formats e.g. JSON.
* **SGI** - **Server Gateway Interface** is a specification that enables an Application Server (like Gunicorn) to communicate with a Web Application (written in Python, Ruby, etc.) using a defined set of rules and protocols.
    * **WSGI (Web Server Gateway Interface)** - The legacy standard for Python web applications. It is **synchronous**, meaning it handles one request at a time per worker process. It is used by frameworks like Flask and Django (standard). Server: **Gunicorn**.
    * **ASGI (Asynchronous Server Gateway Interface)** - The spiritual successor to WSGI, designed to support **asynchronous** Python features (async/await). It can handle multiple concurrent connections, WebSockets, and HTTP/2. It is used by modern frameworks like FastAPI and Starlette. Server: **Uvicorn**.
* **Automatic Documentation** - FastAPI automatically generates interactive API documentation using **OpenAPI** standards. This means you don't have to manually write documentation; it stays in sync with your code.
    * **Swagger UI** (available at `/docs`) - Provides an interactive interface where you can test your API endpoints directly from the browser.
    * **ReDoc** (available at `/redoc`) - Provides a clean, organized, and professional-looking layout for your API documentation.

## GET Request

* **Path Parameters** - Dynamic segments of a URL (e.g., `/items/{item_id}`).
* **Query Parameters** - Optional key-value pairs appended to the URL (e.g., `/items/?skip=0`).
* **Path & Query Modules** - Used to add metadata (title, description) and validation (gt, max_length) to parameters.
* **Error Handling (`HTTPException`)** - Used to return proper HTTP status codes (like 404) for failures.

### Consolidated GET Example:
```python
from fastapi import FastAPI, Path, Query, HTTPException
from typing import Annotated

app = FastAPI()

# 1. Basic GET & Path Parameters with Path Module
@app.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(title="The ID of the item", gt=0)],
    q: Annotated[str | None, Query(max_length=50)] = None
):
    # 2. Error Handling using HTTPException
    if item_id == 100:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "query": q}

# 3. Query Parameters with defaults
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

* **Running the Server**: To start the server locally, we use **Uvicorn**:
    `uvicorn main:app --reload`
    * `main`: The name of the Python file (e.g., `main.py`).
    * `app`: The name of the FastAPI object.
    * `--reload`: Automatically restarts on code changes.

## Pydantic

* **BaseModel** - The "schema" or "template" for your data.
* **Field Class** - Adds validation and metadata to individual fields.
* **Annotated** - The preferred way to attach metadata while keeping type hints clean.
* **Strict Mode** - `strict=True` suppresses type coercion.
* **Custom Validators**:
    * **`@field_validator`**: Validates a single field (`mode='before'` or `'after'`).
    * **`@model_validator`**: Validates the entire model (cross-field logic).
* **Computed Fields (`@computed_field`)** - Calculated properties included in `model_dump()`.
* **Nested Models** - Hierarchical data structures (models within models).

### Comprehensive Pydantic Example:
```python
from typing import Annotated, List, Dict, Optional
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field

# 1. Nested Model
class Address(BaseModel):
    city: str
    state: str
    country: str = "India"

# 2. Main Model
class UserProfile(BaseModel):
    username: Annotated[str, Field(min_length=3, max_length=20)]
    bio: Optional[str] = Field(None, max_length=150)
    address: Optional[Address] = None
    email: EmailStr
    age: Annotated[int, Field(ge=18, strict=True)]
    
    @field_validator('email')
    @classmethod
    def email_must_be_gmail(cls, value: str):
        if "@gmail.com" not in value:
            raise ValueError("Only Gmail addresses are allowed")
        return value

    @model_validator(mode='after')
    def validate_profile(self) -> 'UserProfile':
        if self.age > 100 and "senior" not in (self.bio or "").lower():
            raise ValueError("Users over 100 must have 'senior' in their bio")
        return self

    @computed_field
    @property
    def is_adult(self) -> bool:
        return self.age >= 18

    tags: List[str] = []
    metadata: Dict[str, str] = {}
```

## POST Request

* 

#  Kubernetes

* Control Plane
* 