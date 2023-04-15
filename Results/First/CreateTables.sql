use our_organization;

create table departments(
id int primary key identity not null,
department VARCHAR(50) not null
);

create table pc (
pc_id nvarchar(255) primary key not null,
pc_serial NVARCHAR(25) not null,
pc_mac NVARCHAR(40) not null,
pc_ip nvarchar(100) not null
);

CREATE TABLE personal
(
    user_id uniqueidentifier primary key not null,
    first_name NVARCHAR(20) not null,
    last_name NVARCHAR(20) not null,
    birth_date date not null,
    login VARCHAR(30) not null,
	email VARCHAR(100) unique,
	department_id int not null,
	pc_id nvarchar(255) not null unique,
	FOREIGN KEY (department_id) REFERENCES departments (id) ON DELETE CASCADE,
	FOREIGN KEY (pc_id) REFERENCES pc (pc_id) ON DELETE CASCADE
);

create table login_dates (
user_id uniqueidentifier not null,
pc_id nvarchar(255) not null,
date_time datetime2 not null,
primary key (user_id, pc_id),
FOREIGN KEY (user_id) REFERENCES personal (user_id) ON DELETE no action,
FOREIGN KEY (pc_id) REFERENCES pc (pc_id) ON DELETE no action
);

create table contracts (
user_id uniqueidentifier primary key not null,
date_from date not null,
date_to date not null
FOREIGN KEY (user_id) REFERENCES personal (user_id) ON DELETE CASCADE
);

create table salary (
user_id uniqueidentifier primary key not null,
month int not null,
year int not null,
salary int not null,
FOREIGN KEY (user_id) REFERENCES personal (user_id) ON DELETE CASCADE
);

go