from pathlib import Path
import dj_database_url
from dotenv import load_dotenv 
import os

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG=os.environ.get('DEBUG')=='True'
#print(DEBUG)
