wandb artifact put ./data_preprocessing/genres_mod.parquet \
      --name sample_ml_pipeline/genres_mod.parquet \
      --type raw_data \
      --description "A modified version of the songs dataset"