"""
Library to simplify data transfer between databases
"""
import logging

from importlib.metadata import (
    PackageNotFoundError,
    version,
)

# Import helper functions here for more convenient access
# flake8: noqa
from etlhelper.abort import abort_etlhelper_threads
from etlhelper.db_params import DbParams
from etlhelper.etl import (
    copy_rows,
    execute,
    executemany,
    fetchone,
    fetchmany,
    fetchall,
    generate_insert_sql,
    get_rows,
    iter_chunks,
    iter_rows,
    load,
    copy_table_rows,
)
from etlhelper.connect import (
    connect,
    get_connection_string,
    get_sqlalchemy_connection_string,
)
from etlhelper.utils import (
    table_info,
)

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.0.0"

# Prepare log handler.  See this StackOverflow answer for details:
# https://stackoverflow.com/a/27835318/3508733
class CleanDebugMessageFormatter(logging.Formatter):
    default_fmt = logging.Formatter('%(asctime)s %(funcName)s: %(message)s')
    debug_fmt = logging.Formatter('%(message)s')

    def format(self, record):
        if record.levelno < logging.INFO:
            return self.debug_fmt.format(record)
        else:
            return self.default_fmt.format(record)

handler = logging.StreamHandler()
handler.setFormatter(CleanDebugMessageFormatter())

# Configure logger
logger = logging.getLogger('etlhelper')
logger.addHandler(handler)
logger.setLevel(level=logging.WARN)
