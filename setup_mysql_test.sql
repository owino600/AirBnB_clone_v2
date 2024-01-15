-- A database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- A new user hbnb_test (in localhost)

CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges on the database hbnb_test_db

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- SELECT privilege on the database performance_schema (and only this database)

GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';