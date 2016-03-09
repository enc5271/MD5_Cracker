import md5
import csv

def loadDict(filename='john.txt'):
	with open(filename,'rb') as csvfile:
		with open('precomputedHash.csv','w+') as outFile:
			qreader = csv.reader(csvfile)
			for row in qreader:
				print row
				#compute hash
				md5Hash = md5.new(row[0])
				#write md5 hash value and original to file
				outFile.write('{0},{1}\n'.format(row[0],md5Hash.hexdigest()))	#verify this returns the hex value matching db.txt

if __name__ == "__main__":
	loadDict()