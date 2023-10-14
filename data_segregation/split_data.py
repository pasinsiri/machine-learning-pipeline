import argparse
import logging
import os
import tempfile
import pandas as pd
import wandb
from sklearn.model_selection import train_test_split

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()

def split_data(df):
    # * split data
    logger.info("Splitting data into train, val and test")
    splits = {}

    splits["train"], splits["test"] = train_test_split(
        df,
        test_size=args.test_size,
        random_state=args.random_state,
        stratify=df[args.stratify] if args.stratify != 'null' else None,
    )
    return splits

def main(args):
    run = wandb.init(project="sample-ml-pipeline", job_type="split_data")
    
    # * download artifact
    logger.info("Downloading and reading artifact")
    artifact = run.use_artifact(args.input_artifact)
    artifact_path = artifact.file()
    df = pd.read_csv(artifact_path, low_memory=False)

    # * split data
    splits = split_data(df)

    # * save the results
    # using tempfile.TemporaryDirectory helps the working directory cleaned after all processes have been done
    # otherwise we need to cleanup the directory after we finish our job
    with tempfile.TemporaryDirectory() as tmp_dir:

        for split, df in splits.items():

            # make the artifact name from the provided root plus the name of the split
            artifact_name = f"{args.artifact_root}_{split}.csv"

            # get the path on disk within the temp directory
            temp_path = os.path.join(tmp_dir, artifact_name)

            logger.info(f"Uploading the {split} dataset to {artifact_name}")

            # Save then upload to W&B
            df.to_csv(temp_path)

            artifact = wandb.Artifact(
                name=artifact_name,
                type=args.artifact_type,
                description=f"{split} split of dataset {args.input_artifact}",
            )
            artifact.add_file(temp_path)

            logger.info("Logging artifact")
            run.log_artifact(artifact)

            # This waits for the artifact to be uploaded to W&B. If you
            # do not add this, the temp directory might be removed before
            # W&B had a chance to upload the datasets, and the upload
            # might fail
            artifact.wait()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a dataset into train and test",
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "--input_artifact",
        type=str,
        help="Fully-qualified name for the input artifact",
        required=True,
    )

    parser.add_argument(
        "--artifact_root",
        type=str,
        help="Root for the names of the produced artifacts. The script will produce 2 artifacts: "
             "{root}_train.csv and {root}_test.csv",
        required=True,
    )

    parser.add_argument(
        "--artifact_type", type=str, help="Type for the produced artifacts", required=True
    )

    parser.add_argument(
        "--test_size",
        help="Fraction of dataset or number of items to include in the test split",
        type=float,
        required=True
    )

    parser.add_argument(
        "--random_state",
        help="An integer number to use to init the random number generator. It ensures repeatibility in the"
             "splitting",
        type=int,
        required=False,
        default=42
    )

    parser.add_argument(
        "--stratify",
        help="If set, it is the name of a column to use for stratified splitting",
        type=str,
        required=False,
        default='null'  # unfortunately mlflow does not support well optional parameters
    )

    args = parser.parse_args()

    main(args)