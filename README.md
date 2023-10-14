# machine-learning-pipeline
A repository for reproducible machine learning pipeline utilizing Weights and Biases and MLFlow tools

# Here are the steps needed to complete the workflow
## Step 0: Upload sample data (if needed)
The sample data that was used is `genres_mod.parquet` which is stored in `data_preprocessing` (you can use whatever sample data you want since the sample data is not tracked by git). The upload script is `upload_raw_data.sh` which you can change the data path there (from `./data_preprocessing/genres_mod.parquet` to yours).

## Step 1: Data Preprocessing
All codes are stored in the `data_preprocessing` folder. The respective `mlflow` script is `data_preprocessing.sh`.
In `./data_preprocessing/clean_data.py` there are two simple data preprocessing steps:<br>
    1. Drop duplicates<br>
    2. Fill values, i.e. fill null `song_name` with an empty string, and create a new column called `text_feature`<br>