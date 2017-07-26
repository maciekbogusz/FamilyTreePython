from Tkconstants import LAST
from person import Person
def add_person(
        person,
        cursor
        ):
    name = person.getName()
    surname = person.getSurname()
    birthdate = person.getDates()
    query =  "INSERT INTO individuals (id, first_name, last_name, date_of_birth) VALUES (nextval('primary_key_seq'),%s, %s, %s);"
    data = (name, surname, birthdate)
    cursor.execute(query, data)

def add_son(
        child,
        parent1,
        parent2, 
        cursor
        ):
    # role_id = 1
    child = child
    father = parent1
    mother = parent2
    query = "INSERT INTO relationships (relationship_id, individual_id, relationship_type_code, individual_1_role_code) VALUES (nextval('primary_key_seq'),%s, %s, %s);"
    print parent1
    
def select_person_id(
        person, 
        cursor
        ):
    name = person.getName()
    cursor.execute("SELECT id FROM individuals WHERE first_name LIKE %s;", (name,))
    rows = cursor.fetchall()
    return rows