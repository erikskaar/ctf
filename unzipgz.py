import os, glob, zipfile, gzip
from zipfile import ZipFile
import time
count = 0
def zip():
	time.sleep(0.5)
	for file in glob.glob("*.gz"):
		os.remove(file)
	for file in glob.glob("*.zip"):
		print(file +  " found")
		with ZipFile(file, "r") as zf:
			zf.extractall()
			zf.close()
			#os.remove(file)
			gz()


def gz():
	time.sleep(0.5)
	for file in glob.glob("*.zip"):
		os.remove(file)
	for file in glob.glob("*.gz"):
		print(file +  " found")
		input = gzip.GzipFile(file, 'rb')
		s = input.read()
		input.close()
		output = open("flag.zip", "wb")
		output.write(s)
		output.close()
		#os.remove(file)
		zip()


gz()
