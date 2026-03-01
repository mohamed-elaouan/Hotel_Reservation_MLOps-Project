# import classes 
from src.model_training import ModelTraining
from src.data_preprocessing import DataProcessor
from src.data_ingestion import DataIngestion

from utils.common_functions import read_yaml
from config.paths_config import *

if __name__ == "__main__":
    # Data Ingestion
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    # Data Preprocessing
    data_processor = DataProcessor(
        train_path=TRAIN_FILE_PATH,
        test_path=TEST_FILE_PATH,
        processed_dir=PROCESSED_DIR,
        config_path=CONFIG_PATH,
    )
    data_processor.preprocess()

    # Model Training
    trainer = ModelTraining(
        PROCESSED_TRAIN_FILE_PATH, PROCESSED_TEST_FILE_PATH, MODEL_OUTPUT_PATH
    )
    trainer.run()
