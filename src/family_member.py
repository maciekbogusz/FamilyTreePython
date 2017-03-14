'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect


class family_member:
#checker is set to distinguish if person is a child or a parent
    def __init__(self, name, checker):
        self.name = name 
        self.checker = checker
        
                   
    def addDates(self, birthDate, deathDate):
        self.birthDate = birthDate
        self.deathDate = deathDate        
    
    def getDict(self):
        return self.dict_family   
    
    def getNames(self):
        return self.name
    
    def getCheck(self):
        return self.checker   
    
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
   
            
person1 = family_member("Maciej", True)
person1.addDates("07.01.1989", None)

person2 = family_member("Taduesz", False)
person2.addDates("01.01.1972",None)

person3 = family_member("Katarzyna", False)
person3.addDates("10.06.1974", None)


dict_family = { person1.getNames(): [person2.getNames(), person3.getNames()] }
 
for key, value in dict_family.items():    
    ancestors(dict_family, key)
    
    
