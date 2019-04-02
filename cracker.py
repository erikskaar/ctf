import os, glob, zipfile
from zipfile import ZipFile

def crack():
	for file in glob.glob("*.zip"):
		with ZipFile(file) as zf:
			inputtext = "fcrackzip -v -b -l 0-5 -u -c 1 " + str(file).strip()
			print(inputtext)
			text = os.popen(inputtext).readlines()[-1].strip().split(" ")[-1]
			zf.extractall(pwd=str(text))
			os.remove(file)
			crack()
crack()

