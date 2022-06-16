# Template: Basic tools for setting up loggers in Python programs
import logging
import sys

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

print(logging.DEBUG)        # provides detailed information that is useful for debugging the application. It has a numeric value of 10.
print(logging.INFO)         # for general operations where expected information or output is logged. It has a numeric value of 20.
print(logging.WARNING)      # alerts us to a current or impending, unexpected issue or error. Software or application will continue to run despite the warning message. It has a numeric value of 30.
print(logging.ERROR)        # indicates serious problems that cause functionality within the software or application to break. It has a numeric value of 40.
print(logging.CRITICAL)     # for the most severe of errors and issues. Indicates that the software or application may stop running altogether. It has a numeric value of 50.
print(logging.NOTSET)       # searches for the first non-NOTSET ancestor logger and inherits its logging level. If there is none, our output threshold will be zero.
