'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect
from add_record import add_child, select_person
from person import Person

person1 = Person('Maciej', 'Kowalski')
person1.addDates("1989-01-07", None)

person2 = Person("Tadeusz", "Kowalski")
person2.addDates("01.01.1972",None)

person3 = Person("Katarzyna", "Kowalski")
person3.addDates("10.06.1974", None)


conn = connect()
cursor = conn.cursor()
add_child(person1, cursor)
conn.commit()
       
           
# def ancestors(
#         family,
#         person):
#     if person in family:
#         parents = family[person]
#         result = parents
#         for parent in parents:
#                 result = result + ancestors(family, parent)
#     return [] 
            
            

