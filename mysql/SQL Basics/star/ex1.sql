CREATE DATABASE bootcamp;
USE bootcamp;
CREATE TABLE students(
student_id INT,
first_name VARCHAR(30),
last_name VARCHAR(30),
been_dismissed BOOLEAN,
cohort INT
);

INSERT INTO students
   VALUES(1, "gilad", "baa", false,12);