mlflow run data_validation \
    -P reference_artifact="sample_ml_pipeline/data_train.csv:latest" \
    -P sample_artifact="sample_ml_pipeline/data_test.csv:latest" \
    -P ks_alpha=0.05