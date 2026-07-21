from Car_Price_Prediction_System import logger
from Car_Price_Prediction_System.pipelines.stage_01_data_ingestion import DataIngestionPipeline

Stage_Name = "Data Ingestion Stage"

try:
    logger.info(f">>> {Stage_Name} Started! <<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>> {Stage_Name} Finished!")
except Exception as e:
    logger.info(e)
    raise e