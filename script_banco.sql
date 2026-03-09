CREATE DATABASE IF NOT EXISTS cadastro;
USE cadastro;

CREATE TABLE IF NOT EXISTS manifestos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_manifesto VARCHAR(50) NOT NULL,
    numero_cte VARCHAR(50) NOT NULL,
    data_registro DATE NOT NULL
