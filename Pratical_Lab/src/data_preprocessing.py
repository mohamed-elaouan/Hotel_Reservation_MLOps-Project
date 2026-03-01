import os
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml, load_data
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE


logger = get_logger(__name__)


class DataProcessor:
    def __init__(self, train_path, test_path, processed_dir, config_path):
        self.train_path = train_path
        self.test_path = test_path
        self.processed_dir = processed_dir
        self.config = read_yaml(config_path)
        if not os.path.exists(self.processed_dir):
            os.makedirs(self.processed_dir)

    def preprocess_data(self, df):
        try:
            logger.info("Starting data preprocessing step")
            logger.info("Dropping the Columns ")
            df.drop(columns=["Unnamed: 0", "Booking_ID"], inplace=True)
            df.drop_duplicates(inplace=True)
            cat_cols = self.config["data_processing"]["categorical_features"]
            num_cols = self.config["data_processing"]["numerical_features"]

            logger.info("Applying Label Encoding")
            label_encoder = LabelEncoder()
            mappings = {}

            for col in cat_cols:
                df[col] = label_encoder.fit_transform(df[col])
                mappings[col] = {
                    label: code
                    for label, code in zip(
                        label_encoder.classes_,
                        label_encoder.transform(label_encoder.classes_),
                    )
                }

            logger.info("Label Mapping are : ")
            for col, mapping in mappings.items():
                logger.info(f"{col} : {mapping}")

            # *MultiColinality
            # logger.info("Applying MultiColinality")

            logger.info("Doing Skewness Handling")
            skew_threshold = self.config["data_processing"]["skewness_threshold"]
            skewness = df[num_cols].apply(lambda x: x.skew())

            for column in skewness[skewness > skew_threshold].index:
                df[column] = np.log1p(df[column])
            return df
        except Exception as e:
            logger.error(f"Error in data preprocessing: {e}")
            raise CustomException(f"Error during preprocessing , {e}")

    def balance_data(self, df):
        try:
            logger.info("Handling Imbalancing Data target")
            X = df.drop("booking_status", axis=1)
            y = df["booking_status"]
            smote = SMOTE(random_state=42)
            X_res, y_res = smote.fit_resample(X, y)

            logger.info("Data balancing completed")

            balanced_df = pd.DataFrame(X_res, columns=X.columns)
            balanced_df["booking_status"] = y_res

            # balanced_df.to_csv(
            #     os.path.join(self.processed_dir, "balanced_data.csv"), index=False
            # )
            return balanced_df
        except Exception as e:
            logger.error(f"Error in balancing data step: {e}")
            raise CustomException(f"Error during data balancing , {e}")

    def feature_selection(self, df):
        try:
            logger.info("Starting feature selection step")

            X = df.drop("booking_status", axis=1)
            y = df["booking_status"]

            model = RandomForestClassifier(random_state=42)
            model.fit(X, y)

            feature_importances = model.feature_importances_
            feature_importance_df = pd.DataFrame(
                {"feature": X.columns, "importance": feature_importances}
            ).sort_values(by="importance", ascending=False)
            num_features_to_select = self.config["data_processing"]["no_of_features"]
            top_features = feature_importance_df.head(num_features_to_select)[
                "feature"
            ].tolist()
            logger.info(
                f"Top {num_features_to_select} features selected: {top_features}"
            )
            top_features_df = df[top_features + ["booking_status"]]

            logger.info(f"Feature selection completed successfully.")

            return top_features_df
        except Exception as e:
            logger.error(f"Error in feature selection step: {e}")
            raise CustomException(f"Error during feature selection , {e}")

    def save_data(self, df, file_path):
        try:
            df.to_csv(file_path, index=False)
            logger.info(f"Data saved successfully at {file_path}")
        except Exception as e:
            logger.error(f"Error in saving data: {e}")
            raise CustomException(f"Error during saving data , {e}")

    def preprocess(self):
        try:
            train_df = load_data(self.train_path)
            test_df = load_data(self.test_path)

            train_df = self.preprocess_data(train_df)
            test_df = self.preprocess_data(test_df)

            train_df = self.balance_data(train_df)
            test_df = self.balance_data(test_df)

            train_df = self.feature_selection(train_df)
            test_df = test_df[train_df.columns]

            self.save_data(train_df, PROCESSED_TRAIN_FILE_PATH)
            self.save_data(test_df, PROCESSED_TEST_FILE_PATH)

            logger.info("Data preprocessing completed successfully.")
        except Exception as e:
            logger.error(f"Error in preprocessing pipeline: {e}")
            raise CustomException(f"Error during preprocessing pipeline , {e}")

if __name__ == "__main__":
    data_processor = DataProcessor(
        train_path=TRAIN_FILE_PATH,
        test_path=TEST_FILE_PATH,
        processed_dir=PROCESSED_DIR,
        config_path=CONFIG_PATH,
    )
    data_processor.preprocess()
