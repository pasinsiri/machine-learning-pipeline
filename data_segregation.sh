mlflow run . -P input_artifact="sample-ml-pipeline/preprocessed_data.csv:latest" \
    -P artifact_root="data" \
    -P test_size=0.3 \
    -P stratify="genre"