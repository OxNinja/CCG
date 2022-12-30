drop database if exists `database`;
create database `database`;
use `database`;

drop table if exists `database`.`articles`;
create table `database`.`articles` (
	id int not null auto_increment,
	title text not null,
	content text not null,
	primary key (id)
);

insert into `database`.`articles` (title, content) values
	("My fist article","I love PHP & MySQL."),
	("My blog","I made this blog and I am very proud of it.");

drop table if exists `database`.`users`;
create table `database`.`users` (
	id int not null auto_increment,
	username text not null,
	password text not null,
	primary key (id)
);

insert into `database`.`users` (username, password) values
	("admin","$FLAG"),
	("john","password");
