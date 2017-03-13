'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect

class Person:

    def __init__(self, name):
        self.name = name 
                   
    def addDates(self, birthDate, deathDate):
        self.birthDate = birthDate
        self.deathDate = deathDate        
    
    def getDict(self):
        return self.dict_family   
    
    def getNames(self):
        return self.name
    
    def getDates(self):
        if self.deathDate is None:
            return self.birthDate
        if self.deathDate is not None:
            return  self.birthDate, self.deathDate

def ancestors(
        family,
        person):
    if person in family:
        parents = family[person]
        result = parents
        for parent in parents:
                    result = result + ancestors(family, parent)
        print result
    return [] 
   
            
son = Person("Maciej")
son.addDates("07.01.1989", None)

father = Person("Taduesz")
father.addDates("01.01.1972",None)

mother = Person("Katarzyna")
mother.addDates("10.06.1974", None)


dict_family = { son.getNames(): [father.getNames(), mother.getNames()] }
 
for key, value in dict_family.items():
    ancestors(dict_family, key)

connect()
