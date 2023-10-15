mlflow run download \
    -P file_url="https://github.com/udacity/nd0821-c2-build-model-workflow-exercises/blob/master/lesson-2-data-exploration-and-preparation/exercises/exercise_4/starter/genres_mod.parquet?raw=true" \
    -P artifact_name="raw_data.parquet" \
    -P artifact_type="raw_data" \
    -P artifact_description="Downloaded raw data"