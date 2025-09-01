from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__ == "__main__":
    # Step 1: Data Ingestion
    ingestion = DataIngestion()
    train_data_path, test_data_path = ingestion.initiate_data_ingestion()

    # Step 2: Data Transformation
    transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = transformation.initiate_data_transformation(
        train_data_path, test_data_path
    )

    # Step 3: Model Training
    trainer = ModelTrainer()
    score = trainer.initiate_model_trainer(train_arr, test_arr)
    print(f"Best model test score: {score}")
