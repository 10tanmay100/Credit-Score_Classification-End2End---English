from credit.entity import DataIngestionConfig
from credit.config import ConfigurationManager
from credit.utils import read_yaml
from pathlib import Path
import gdown
from credit.constants import *

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
        self.cfg_y=read_yaml(CONFIG_FILEPATH)
    
    def __fetch_data_from_drive(self,url:str,raw_folder_path:Path):
        gdown.download_folder(url,output=raw_folder_path)
    
    def get_data(self):
        self.__fetch_data_from_drive(url=self.cfg_y['data_ingestion']['url'],raw_folder_path=self.config.raw_folder_path)



