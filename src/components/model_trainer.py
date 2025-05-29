import os
import sys
from dataclasses import dataclass
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from src.exception import CustomException 
from src.logger import logging
from src.utils import save_object

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array, preprocessor_path):
        try:
            logging.info("Split training and testing input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1],
            )

            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "K-Neighbors": KNeighborsRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "XGBoost": XGBRegressor(),
                "AdaBoost": AdaBoostRegressor()
                "CatBoosting": CatBoostRegressor(verbose=False)
            }

            best_model = None
            best_score = 0
            for name, model in models.items():
                model.fit(X_train, y_train)
                predictions = model.predict(X_test)
                score = r2_score(y_test, predictions)
                logging.info(f"{name} R2 score: {score}")

                if score > best_score:
                    best_score = score
                    best_model = model

            if best_model is None:
                raise CustomException("No model performed better than baseline", sys)

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )

            return best_model, best_score

        except Exception as e:
            raise CustomException(e, sys)
