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