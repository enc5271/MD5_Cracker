import md5

def loadDict(self,filename='john.txt'):
	with open(filename,'rb') as csvfile:
		with open('precomputedHash.csv','r+') as outFile:
			qreader = csv.reader(csvfile)
			for row in qreader:
				#compute hash
				md5Hash = md5.new(row[0])
				#write md5 hash value and original to file
				outfile.write('{0},{1}\n'.format(row[0],md5Hash.hexdigest()))	#verify this returns the hex value matching db.txt
