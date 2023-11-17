import logging
import os
from datetime import datetime

dir_name = f"{datetime.now().strftime('%d_%m_%Y')}"
DIR_PATH = os.path.join(os.getcwd(),'logs',dir_name)
os.makedirs(DIR_PATH,exist_ok = True)

file_name = f"{datetime.now().strftime('%H_%M_%S')}.log"
FILE_PATH = os.path.join(DIR_PATH,file_name)


logging.basicConfig(
    filename=FILE_PATH,
    level=logging.INFO,
    format = "[ %(asctime)s ] - %(lineno)d - %(module)s - %(levelname)s - %(message)s"
)


if __name__ == "__main__":
    logging.info('Done Logger.py')

