from credit.constants import CONFIG_FILEPATH
from credit.utils import read_yaml,create_directories
from credit.entity import DataIngestionConfig
from datetime import datetime
from credit.exception import credits_exception
import os
import sys


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILEPATH):
        #read the configuration yaml file
        self.config=read_yaml(config_filepath)
        create_directories([self.config['artifacts-root']])
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            config=self.config['data_ingestion']['root_directory']
            #detecting the current datetime
            now=datetime.now()
            #creating data ingestion subfolder name
            date_folder=now.strftime("%Y-%m-%d-%H-%M-%S")
            #path of the raw folder
            raw_folder_path=os.path.join(config,date_folder)
            print(raw_folder_path)
            #create that directory
            create_directories([raw_folder_path])
            data_ingestion_config=DataIngestionConfig(raw_folder_path=raw_folder_path)
            return data_ingestion_config
        except Exception as e:
            raise credits_exception(e,sys) from e







