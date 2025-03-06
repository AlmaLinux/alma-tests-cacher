import os
from pathlib import Path

DEFAULT_REQUESTS_LIMIT = 5
DEFAULT_SLEEP_TIMEOUT = 600  # 10 minutes
DEFAULT_BS_API_URL = 'http://web_server:8000'
DEFAULT_LOGGING_LEVEL = 'DEBUG'
DEFAULT_CONFIG_PATH = os.getenv('CONFIG_PATH', 'vars.yaml')

workdir_path = Path.cwd().parent / "alma-cacher-workdir"
DEFAULT_WORKDIR_PATH = workdir_path
