from src.logger import get_logger
from src.custom_exception import CustomException
import sys

logger = get_logger(__name__)


def divide_numbers(a, b):
    try:
        result = a / b
        logger.info(f"Division successful: {a} / {b} = {result}")
        return result
    except Exception as e:
        logger.error(f"Error occurred")
        raise CustomException("Custom Error zero", sys)


if __name__ == "__main__":
    try:
        logger.info("Starting division operation")
        divide_numbers(10, 0)
    except CustomException as ce:
        logger.error(f"Caught a CustomException: {ce}")
