-- @BLOCK create user table
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    age INT NOT NULL,
    color VARCHAR(256) NOT NULL
)