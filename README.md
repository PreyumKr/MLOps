# MLOps Tutorial Learning

## DVC ( Data Version Control )

* first intall dvc using `pip install dvc`
* initialize dvc in your project using `dvc init`
* Set the remote storage for dvc using `dvc remote add -d <remote_name> <remote_url>` in first example we are using local storage so the command will be `dvc remote add -d myremote S3`
* Add data folder to dvc using `dvc add <data_folder>` in our case it will be `dvc add data/`
* Then we commit the dvc files using `dvc commit`
* Finally push the data to remote storage using `dvc push`
* After some changes `dvc status` to check the status of dvc tracked files

# YAML Crash Course

* Indentation based markup language
* Key value pair with : 
* Supports list like 
```YAML
	  Fruit:
		  - Apple
		  - Orange
		  - Banana
  ```

* Multiline String as 
```YAML
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
* The difference between an experiment and a run - 
* Using `mlflow.log_artifact` we can save the figures and code of the script `(__file__)` as well in mlflow
* Use `mlflow.set_experiment("Name")` to create a custom experiment name 
* Using `mlflow.log_model()` we can save the model details as well and that gives us the requirements.txt, pickle file and other creation files for the model as well.
* For using it in the best way use `AWS` or `DagsHub`
* For using in ***AWS*** we will need `IAM` User to access to and from, `EC2 Server` it can store the light metadata and `S3 Bucket` will save the `Model Data or Artifacts` 
* For Using ***DagsHub***  create a account and link your github repository, and it will give you the `mlflow remote tracking id` and everything needed for using remote mlflow
* Use `pip install dagshub` to use the dagshub code in the scripts
* Using `mlflow.autolog()` to log all the parameters, metrics, model and dataset of the experiment. While script data and tags need to be added manually.

# Continuous Integration (CI)

* To use `CI using Github actions` we first need to create a folder pattern in our repository like `.github/workflows`
* We need to create a yaml file inside with the actions rules, can be found on github actions as well

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