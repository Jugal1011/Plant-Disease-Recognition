import gdown
import os

# Google Drive shareable link (replace with your actual link)
url = 'https://drive.google.com/uc?id=1ueTaKohf3BccqmopOrEYFCT1SqrAundH'

output = os.path.join('model', 'plant-disease-recognition.hdf5')
os.makedirs('model', exist_ok=True)
gdown.download(url, output, quiet=False)
