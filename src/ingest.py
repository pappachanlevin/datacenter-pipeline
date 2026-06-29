import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def download_dataset():
    """Download dataset from Kaggle API"""
    
    dataset_slug = "ashyou09/global-data-center-and-ai-waterelectricity-usage"
    output_path = "data/raw/"
    
    logger.info(f"Starting download of dataset: {dataset_slug}")
    
    try:
        import kaggle
        kaggle.api.authenticate()
        kaggle.api.dataset_download_files(
            dataset_slug,
            path=output_path,
            unzip=True
        )
        logger.info(f"Dataset downloaded to {output_path}")
        
        # Log file info
        files = os.listdir(output_path)
        for file in files:
            size = os.path.getsize(f"{output_path}/{file}")
            logger.info(f"File: {file} | Size: {size/1024/1024:.2f} MB")
            
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise

if __name__ == "__main__":
    download_dataset()