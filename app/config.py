import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "Flipnetic"
APP_VERSION = "0.1.0"
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")