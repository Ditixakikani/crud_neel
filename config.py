from dotenv import load_dotenv
import os
load_dotenv()

DATABASE_URL = os.environ.get("DB_URL")