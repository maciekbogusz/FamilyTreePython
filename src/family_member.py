'''
Created on 07.03.2017

@author: mcbg
'''
import config
from connect import connect
from add_record import add_person, select_person_id, add_son
from person import Person
from django.contrib.admin.templatetags.admin_list import items_for_result

def display_list(elements): 
    idlist = [item[0] for item in elements]
    print idlist          

person1 = Person('Maciej', 'Kowalski')
person1.addDates("1989-01-07", None)

person2 = Person("Tadeusz", "Kowalski")
person2.addDates("1972-01-01",None)

person3 = Person("Katarzyna", "Kowalski")
person3.addDates("1974-06-10", None)

conn = connect()
cursor = conn.cursor()
#add_person(person3, cursor)
person1_id = select_person_id(person1, cursor)
person2_id = select_person_id(person2, cursor)
person3_id = select_person_id(person3, cursor)
add_son(person1_id, person2_id, person3_id, cursor)

#display_list(person2_id)
conn.commit()
