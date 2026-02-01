# MLOps Tutorial Learning

## DVC ( Data Version Control )

* first intall dvc using `pip install dvc`
* initialize dvc in your project using `dvc init`
* Set the remote storage for dvc using `dvc remote add -d <remote_name> <remote_url>` in first example we are using local storage so the command will be `dvc remote add -d myremote S3`
* Add data folder to dvc using `dvc add <data_folder>` in our case it will be `dvc add data/`
* Then we commit the dvc files using `dvc commit`
* Finally push the data to remote storage using `dvc push`
* After some changes `dvc status` to check the status of dvc tracked files