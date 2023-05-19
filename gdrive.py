import gdown
import sys

url = sys.argv[1]

file_id = url.split('/')[-1]

gdown.download(url)
