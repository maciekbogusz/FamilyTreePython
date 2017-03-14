create table individuals(
	id serial primary key,
	first_name varchar(25),
	last_name varchar(40),
	date_of_birth date,
	date_of_death date
);

create table relationships_types(
	relationship_type_code serial primary key,
	relationship_type_description varchar(40)
);

create table roles(
	role_code serial primary key,
	role_description varchar(40)
);

create table relationships(
	relationship_id serial primary key,
	individual_id serial references individuals(id),
	releationship_type_code serial references relationships_types(relationship_type_code),
	individual_1_role_code serial references roles(role_code)
);


CREATE SEQUENCE primary_key_seq 
	start 1
	increment 1
	NO MAXVALUE
	CACHE 1;

