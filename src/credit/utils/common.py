from pathlib import Path
from credit.exception import credits_exception
import sys
import yaml
import os
from credit.logger import logging

def read_yaml(yaml_file:Path):
    """"
    Read yaml file from path
    """
    try:
        with open(yaml_file, 'r') as f:
            content=yaml.safe_load(f)
            return content
    except Exception as e:
        raise credits_exception(e,sys) from e



def create_directories(paths:list,verbose=True):
    try:
        base_paths=set()
        for path in paths:
            path=Path(path)
            base_path=path.parent
            if base_path not in base_paths:
                os.makedirs(base_path,exist_ok=True)
                base_paths.add(base_path)
            os.makedirs(path,exist_ok=True)
            if verbose:
                logging.info(f"Directory created at {path}")
    except Exception as e:
        raise credits_exception(e,sys) from e