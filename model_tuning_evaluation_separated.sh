# run with default hyperparameters (defined in config.yaml)
# mlflow run model_tuning_evaluation_separated

# run with custom hyperparameters (those defined in this script will replace default values)
mlflow run model_tuning_evaluation_separated \
  -P hydra_options="random_forest_pipeline.random_forest.max_depth=5"
# mlflow run model_tuning_evaluation_separated \
#   -P hydra_options="random_forest_pipeline.random_forest.n_estimators=10"
# mlflow run model_tuning_evaluation_separated \
#   -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=1,5,10"
# mlflow run model_tuning_evaluation_separated \
#   -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=range(1,10,2)"
# mlflow run model_tuning_evaluation_separated \
#     -P hydra_options="-m random_forest_pipeline.random_forest.max_depth=range(10,50,3) random_forest_pipeline.tfidf.max_features=range(50,200,50) hydra/launcher=joblib"