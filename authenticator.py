import md5
import csv

class Authenticator:

	def __init__(self):
		self.userData  = []
		self.loadTable()

	def loadTable(self,filename='db.txt'):
		with open(filename,'rb') as csvfile:
			salt_counter = 0
			qreader = csv.reader(csvfile)
			for row in qreader:
				#Last name
				row[0] = row[0]
				#first name
				row[1] = row[1]
				#user name
				row[2] = row[2]
				#UIN lol
				row[3] = int(row[3])
				#Salt only 24 users have salt 6 of them do not have salt included... 
				if(row[4]==''):
					row[4] = row[4]
				else:
					salt_counter += 1
					row[4] = int(row[4])
				#read hex values as string
				#Note this is ok because md5.hexdigest() returns a string of length 32.
				row[5] = row[5]
				
				self.userData.append(row)
		print "Salt Counter: {0}".format(salt_counter)

	def lookupByUsername(self,username):
		for user in self.userData:
			if user[2]==username:
				return user
		print 'Error: User not found.'
		return None

	def authenticate(self, userName,password,salt=''):
		user = self.lookupByUsername(userName)
		#default hash is empty. God, I love python!
		md5Hash = md5.new(password+salt)
		accessMsg = 'ACCESS DENIED'
		if user[5]==md5Hash.hexdigest():
			accessMsg = 'ACCESS GRANTED, YOU STUD!'
		print 'username: {0}'.format(user[2])
		print 'password: {0}'.format(password+salt)
		print accessMsg

	def authenticateList(self,userName,passwords):
		user = self.lookupByUsername(userName)
		for pair in passwords:
			(real, hashVal)= pair
			if user[5]==hashVal:
				return real
		return -1

################################################################################################
# Main
if __name__ == "__main__":
	test = Authenticator()
	test.authenticate('esullivan','hotdog')