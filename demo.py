from delivery_time.pipeline.training_pipeline import Training_Pipeline
from delivery_time.logger import logging
import os

def main():
    try:
        pipeline = Training_Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
            logging.error(f"{e}")
            print(e)


if __name__ == "__main__":
    main()