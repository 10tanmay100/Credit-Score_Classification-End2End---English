from dataclasses import dataclass
from pathlib import Path


#define data ingestion config
@dataclass(frozen=True)
class DataIngestionConfig:
    raw_folder_path: Path







