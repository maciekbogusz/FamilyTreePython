CREATE TABLE  family_member(
	id 	BIGSERIAL PRIMARY KEY,
	name 	varchar(30) not null,
	surname varchar(60) not null,
	birht_date date,
	death_date date
);

CREATE TABLE  parents(
	id 	BIGSERIAL PRIMARY KEY,
	name 	varchar(30) not null,
	surname varchar(60) not null,
	child_id BIGSERIAL references family_member(id),
	birht_date date,
	death_date date
);

CREATE SEQUENCE primary_key_seq 
	start 1
	increment 1
	NO MAXVALUE
	CACHE 1;



