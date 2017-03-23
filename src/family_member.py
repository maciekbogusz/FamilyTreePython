'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect
from add_record import add_child, select_person_id
from person import Person
from django.contrib.admin.templatetags.admin_list import items_for_result

def display_list(elements): 
    idlist = [item[0] for item in elements]
    print idlist          

person1 = Person('Maciej', 'Kowalski')
person1.addDates("1989-01-07", None)

person2 = Person("Tadeusz", "Kowalski")
person2.addDates("01.01.1972",None)

person3 = Person("Katarzyna", "Kowalski")
person3.addDates("10.06.1974", None)

conn = connect()
cursor = conn.cursor()
#add_child(person1, cursor)
person_id = select_person_id(person1, cursor)
display_list(person_id)
conn.commit()
