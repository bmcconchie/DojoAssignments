import random
class Patient(object):
	def __init__(self, name, allergies):
		self.id = ''.join( name[0] + random.choice('0123456789ABCDEF') for i in range(7))
		self.name = name
		self.allergies = allergies




class Hospital(object):
	def __init__(self, capacity):
		self.beds = {}
		self.capacity = capacity
		self.patientCount = 0
		for x in range(1, capacity+1):
			self.beds[str(x)] = None

	def admit(self, patient):
		if self.patientCount >= self.capacity:
			print 'Hospital is full.'
		else:
			for bed in self.beds:
				if self.beds[bed] == None:
					self.beds[bed] = patient
					self.patientCount +=1
					return
	def discharge(self, name):
		for bed in self.beds:
			if self.beds[bed] != None and self.beds[bed].name == name:
				self.beds[bed] = None
				self.patientCount -=1


ray = Patient('Ray', 'bees')
brit = Patient('Brit', 'bees')

amy = Patient('Amy', 'bees')


myCenter = Hospital(2)
myCenter.admit(ray)
myCenter.admit(brit)
myCenter.admit(amy)
myCenter.discharge('Ray')
myCenter.discharge('Brit')


print myCenter.beds
