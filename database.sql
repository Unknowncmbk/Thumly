CREATE TABLE users (
	email VARCHAR(40) NOT NULL,
	password VARCHAR(40) NOT NULL,
	PRIMARY KEY (email)
);
 
CREATE TABLE restaurants (
	rid VARBINARY(255) NOT NULL,
	name VARCHAR(50) NOT NULL,
	address VARCHAR(50) NOT NULL,
	city VARCHAR(30) NOT NULL,
	state VARCHAR(10) NOT NULL,
	zip VARCHAR(10) NOT NULL,
	phone VARCHAR(15) NOT NULL DEFAULT "",
	url VARCHAR(512) NOT NULL DEFAULT "",
	twitter VARCHAR(16) NOT NULL DEFAULT "",
	latitude DECIMAL(9,6) NOT NULL,
	longitude DECIMAL(9,6) NOT NULL,
	PRIMARY KEY (rid)
);

CREATE TABLE transactions (
	uid VARCHAR(40) NOT NULL,
	rid VARBINARY(255) NOT NULL,
	vote INT NOT NULL,
	creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (uid) REFERENCES users(email),
	FOREIGN KEY (rid) REFERENCES restaurants(rid),
	PRIMARY KEY (uid, rid)
);