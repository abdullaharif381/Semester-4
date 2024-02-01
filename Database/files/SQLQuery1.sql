create table std(
	name1 varchar(255),
	roll int not null unique,
	gpa float,
	age int
	constraint special unique (roll, name1)
);
alter table std
drop column age;
insert into std (name1,roll,gpa)values('sa',211,NULL);

select* from std;
alter table std
alter column   gpa int NOT NULL;
alter table std
alter column name1 int not null;



alter table std
drop constraint special;

