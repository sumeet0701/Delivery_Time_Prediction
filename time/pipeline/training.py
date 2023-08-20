from time.components.model_trainer import ModelTrainer
from time.logger import logging
from time.exception import ApplicationException
from time.components.data_ingestion import DataIngestion
from time.components.data_validation import DataValidation
from time.components.data_transformation import DataTransformation
from time.config.Configuration import Configuration
from time.entity.config_entity import DataIngestionConfig
from time.entity.artifact_entity import DataIngestionArtifact
import os,sys


class Training_Pipeline:

    def __init__(self,config: Configuration=Configuration())->None:
        try:
            logging.info(f"\n{'*'*20} Initiating the Training Pipeline {'*'*20}\n\n")
            self.config = config
        except Exception as e:
            raise ApplicationException(e,sys) from e

    def start_data_ingestion(self,data_ingestion_config:DataIngestionConfig)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = data_ingestion_config)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise ApplicationException(e,sys) from e
    def run_training_pipeline(self):
        try:
            data_ingestion_config=self.config.get_data_ingestion_config()

            data_ingestion_artifact = self.start_data_ingestion(data_ingestion_config)
        except Exception as e:
            raise ApplicationException(e,sys) from e

    def __del__(self):
        logging.info(f"\n{'*'*20} Training Pipeline Complete {'*'*20}\n\n")