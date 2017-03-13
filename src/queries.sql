select * from family_member;
select * from parents;

insert into family_member (id, name, surname) values (nextval('primary_key_seq'), 'Krzysztof', 'Kowalski');


insert into parents (id,name, surname, child_id) values(nextval('primary_key_seq'),'Katarzyna','Kowalski', 2);



CREATE TABLE  family_member(
	id 	BIGSERIAL PRIMARY KEY,
	name 	varchar(30) not null,
	surname varchar(60) not null
	--parents_id BIGSERIAL references parents(id)
);

CREATE TABLE  parents(
	id 	BIGSERIAL PRIMARY KEY,
	name 	varchar(30) not null,
	surname varchar(60) not null,
	child_id BIGSERIAL references family_member(id)
);


drop table parents

CREATE SEQUENCE primary_key_seq 
	start 1
	increment 1
	NO MAXVALUE
	CACHE 1;

select * from family_member;

