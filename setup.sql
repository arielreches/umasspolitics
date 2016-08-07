-- Student table
CREATE TABLE Student (
	studentId SERIAL PRIMARY KEY,
	deviceId varchar(100),
	year integer,
	location varchar(20),
	housing varchar(20),
	building varchar(20),
	candidate varchar(20)
)