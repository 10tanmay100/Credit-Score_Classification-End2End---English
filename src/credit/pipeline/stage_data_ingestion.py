from credit.components import DataIngestion
from credit.config import ConfigurationManager
from credit.exception import credits_exception
from credit.logger import logging
import sys

STAGE_NAME="Data Ingestion Stage"


def main():
    try:
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.get_data()
    except Exception as e:
        raise credits_exception(e,sys) from e
    

if __name__=="__main__":
    logging.info(f">>>>>>>{STAGE_NAME} has created<<<<<<<<<")
    main()
    logging.info(f">>>>>>>{STAGE_NAME} has finished<<<<<<<<<")