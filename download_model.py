import gdown
import os
from dotenv import load_dotenv

# Load .env file (local only)
load_dotenv()

file_id = os.environ.get('FILE_ID')
if not file_id:
    raise ValueError("FILE_ID not set in environment variables.")

# Use fuzzy URL to support confirmation bypass
url = f'https://drive.google.com/uc?id={file_id}'
output = os.path.join('model', 'plant-disease-recognition.hdf5')

os.makedirs('model', exist_ok=True)
gdown.download(url, output, quiet=False, fuzzy=True)
