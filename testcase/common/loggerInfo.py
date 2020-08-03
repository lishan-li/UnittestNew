import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))
from testcase.common.logger import get_logger

logger = get_logger(__name__)

def logInfo(self,res):
    logger.info(self)
    logger.info(res.text.encode('utf8'))
    logger.info(res.status_code)