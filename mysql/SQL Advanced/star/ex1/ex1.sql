create database programs;

CREATE TABLE participant (
    id int NOT NULL,
    FirstName varchar(255),
    LastName varchar(255),
	Country varchar(255),
    Gender varchar(255), 
    levelOfEnglish int,
    DoesHaveIsraelPassport boolean,
    PRIMARY KEY (id)
    );

create table payments (
id int NOT NULL,
participant_id int,
sum_ int,
the_date varchar(255),
PaymentMethod ENUM('PayPal','Cash','Wire') NOT NULL default 'PayPal',
authoriztionCode text(100),
FOREIGN KEY (participant_id) REFERENCES participant(id),
PRIMARY KEY (id)
);