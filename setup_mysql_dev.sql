-- A database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- A new user hbnb_dev (in localhost)

CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges on the database hbnb_dev_db

GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- SELECT privilege on the database performance_schema (and only this database)

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';