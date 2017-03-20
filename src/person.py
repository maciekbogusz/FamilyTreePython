class Person(object):   
    
    def __init__(self, name, surname):
        self.name = name 
        self.surname = surname
                           
    def addDates(self, birthDate, deathDate):
        self.birthDate = birthDate
        self.deathDate = deathDate        
    
    def getDict(self):
        return self.dict_family   
    
    def getName(self):
        return self.name
    
    def getSurname(self):
        return self.surname
        
    def getSex(self):
        return self.sex
    
    def getCheck(self):
        return self.checker   
    
    def getDates(self):
        if self.deathDate is None:
            return self.birthDate
        if self.deathDate is not None:
            return  self.birthDate, self.deathDate