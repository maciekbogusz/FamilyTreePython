'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect
from add_record import *

class family_member:
    def __init__(self, name, surname, sex):
        self.name = name 
        self.surname = surname
        self.sex = sex
                   
    def addDates(self, birthDate, deathDate):
        self.birthDate = birthDate
        self.deathDate = deathDate        
    
    def getDict(self):
        return self.dict_family   
    
    def getNames(self):
        return self.name
    
    def getSex(self):
        return self.sex
    
    def getSurname(self):
        return self.surname    
    
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
            
person1 = family_member("Maciej", "Kowalski", "Man")
person1.addDates("1989-01-07", None)

person2 = family_member("Taduesz", "Kowalski", "Man")
person2.addDates("01.01.1972",None)

person3 = family_member("Katarzyna", "Kowalski", "Woman")
person3.addDates("10.06.1974", None)


dict_family = { person1.getNames(): [person2.getNames(), person3.getNames()] }
 
for key, value in dict_family.items():    
    ancestors(dict_family, key)
    
    
conn = connect()
cursor = conn.cursor()
#add_child(person1, cursor)
print select_person(person1.getNames(), cursor)
conn.commit()
