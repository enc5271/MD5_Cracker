import csv
import authenticator

'''i really want to thread this since cracking each user is an independent subproblem.
That probably has a lot to due with the fall of MD5. My GPU has 4 GB (GTX 770 1526 cores 1100MHZ) 
and could destroy 
the hash function using CUDA but I dont have time to mess with the libraries other than
the built in threading lib.
'''

class DictAttack:
	def __init__(self):
		self.hashList = []
		self.auth = authenticator.Authenticator()
		self.loadPrecomputedHash()

	def loadPrecomputedHash(self,filename='precomputedHash.csv'):
		with open(filename,'rb') as csvfile:
			qreader = csv.reader(csvfile)
			for row in qreader:
				self.hashList.append(row)

	def writePassword(self,username,password,filename='foundPasswords.csv'):
		with open(filename,'a') as csvfile:
			csvfile.write('{0},{1}\n'.format(username,password))


	#dummy test on first 5
	def crackAllUsers(self):
		for user in self.auth.userData:
			success = self.auth.authenticateList(user[2],self.hashList)
			if success == -1:
				print 'Dictionary attack failed'
			else:
				print 'User: {0} has password: {1}'.format(user[2],success)
				self.writePassword(user[2],success)


if __name__=='__main__':
	test = DictAttack()
	test.crackAllUsers()