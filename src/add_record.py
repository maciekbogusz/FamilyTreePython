
def add_child(
        person,
        cursor
        ):
    name = person.getNames()
    surname = person.getSurname()
    birthdate = person.getDates()
    query =  "INSERT INTO family_member (id, name, surname, birth_date) VALUES (nextval('primary_key_seq'),%s, %s, %s);"
    data = (name, surname, birthdate)
    cursor.execute(query, data)


def add_parents(
        person,
        cursor
        ):
    name = person.getNames()
    surname = person.getSurname()
    birthdate = person.getDates()
    query =  "INSERT INTO family_member (id, name, surname, birth_date, child_id) VALUES (nextval('primary_key_seq'),%s, %s, %s);"
    data = (name, surname, birthdate)
    cursor.execute(query, data)
