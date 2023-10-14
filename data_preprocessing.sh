mlflow run data_preprocessing -P input_artifact=sample_ml_pipeline/genres_mod.parquet:latest \
      -P artifact_name=preprocessed_data.csv \
      -P artifact_type=cleaned_data \
      -P artifact_description="Data after preprocessing"