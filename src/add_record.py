from Tkconstants import LAST
from person import Person
def add_child(
        person,
        cursor
        ):
    name = person.getName()
    surname = person.getSurname()
    birthdate = person.getDates()
    query =  "INSERT INTO individuals (id, first_name, last_name, date_of_birth) VALUES (nextval('primary_key_seq'),%s, %s, %s);"
    data = (name, surname, birthdate)
    cursor.execute(query, data)

def add_relationship(
        person,
        cursor      
        ):
    name = person.getNames()
    
def add_parents(
        child,
        parent,
        cursor
        ):
    name = parent.getNames()
    surname = parent.getSurname()
    birthdate = parent.getDates()
    query =  "INSERT INTO family_member (id, name, surname, birth_date, child_id) VALUES (nextval('primary_key_seq'),%s, %s, 2);"
    data = (name, surname, birthdate)
    cursor.execute(query, data)
    
def select_person_id(
        person, 
        cursor
        ):
    name = person.getName()
    cursor.execute("SELECT id FROM individuals WHERE first_name LIKE %s;", (name,))
    rows = cursor.fetchall()
    idlist = [item[0] for item in rows]
    return idlist