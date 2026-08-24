create database sangar;
use sangar;

create table goku(sno int, name varchar(20),age int, mobile varchar(10));

select * from goku;

insert into goku values(2,'arun',30,1123456789);

insert into goku values(3,'anandh',25,1123956789),(4,'rahul',23,8766879843);

select name,age,mobile from goku;