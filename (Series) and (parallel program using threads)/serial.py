import re
import datetime
import logging 

def clean(inp):
    inp = inp.lower()
    matches = re.findall(r'(\b[^\s]+\b)', inp)
    return matches
#Madhu_Patel
LOG_FILE = "logs/serial.log"
import os 

count = {}

def main():
	logging.basicConfig(filename=LOG_FILE, encoding="utf-8", level=logging.DEBUG)
	startTime = datetime.datetime.now()
	for f in os.listdir('data/'):
		data = clean(open(os.path.join(os.path.dirname(__file__), 'data', f),'r').read())
		for w in data:
			if w not in count:
				count[w] = 0
			count[w] += 1
	print((sorted(count.items(), key=lambda item: item[1],reverse=True)[:10]))
	endTime = datetime.datetime.now()
	print(endTime-startTime)
	logging.info(f"main finished {endTime-startTime}")
if __name__=="__main__":
    main()