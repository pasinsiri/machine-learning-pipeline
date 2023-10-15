# machine-learning-pipeline
A repository for reproducible machine learning pipeline utilizing Weights and Biases and MLFlow tools

## Here are the steps in the workflow
### Step 0: Upload sample data (if needed)
The sample data that was used is `genres_mod.parquet` which is stored in `data_preprocessing` (you can use whatever sample data you want since the sample data is not tracked by git). The upload script is `upload_raw_data.sh` which you can change the data path there (from `./data_preprocessing/genres_mod.parquet` to yours).

### Step 1: Data Preprocessing
All codes are stored in the `data_preprocessing` folder. The respective `mlflow` script is `data_preprocessing.sh`.
In `./data_preprocessing/clean_data.py` there are two simple data preprocessing steps:<br>
    1. Drop duplicates<br>
    2. Fill values, i.e. fill null `song_name` with an empty string, and create a new column called `text_feature`<br>

### Step 2: Data Segregation
In this part we will split the raw data into train and test datasets. Codes are in `data_segregation` which you can run using `data_segregation.py` where you can adjust `test_size` and `stratify`.

### Step 3: Hyperparameter Tuning
If you want to perform the **hyperparameter tuning**, you can run the `model_tuning_evaluation_separated.sh` file which triggers MLflow in the `model_tuning_evaluation_separated` folder. In the shell script you can parse the lists of hyperparameters you want to perform the grid search method to find the best hyperparameter configuration (there are examples provided in the shell script). We use AUC score as the default metric for model evaluation. The evaluation result will be sent to Weights and Bias where you can compare to other configurations.
<br>

## Run the entire workflow
Suppose you have done all the trial and error processes and want to perform an end-to-end machine learning pipeline. You can simply run the `mlflow run .` in the main directory (or you can choose to run only a subset of processes, e.g. only preprocessing and validation, by parsing a parameter). You can see the configuration in `config.yaml` and the script in `main.py` in the main directory.