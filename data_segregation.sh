mlflow run data_segregation -P input_artifact="sample_ml_pipeline/preprocessed_data.csv:latest" \
    -P artifact_root="data" \
    -P test_size=0.3 \
    -P stratify="genre"