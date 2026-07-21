from Car_Price_Prediction_System import logger
from Car_Price_Prediction_System.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from Car_Price_Prediction_System.pipelines.stage_02_data_validation import DataValidationPipeline
from Car_Price_Prediction_System.pipelines.stage_03_data_transformation import DataTransformationPipeline

Stage_Name = "Data Ingestion Stage"

try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished!")
except Exception as e:
    logger.info(e)
    raise e

Stage_Name = "Data Validation Stage"

try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.info(e)
    raise e

Stage_Name = "Data Transformation Stage"

try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished! <<<")
except Exception as e:
    logger.info(e)
    raise e