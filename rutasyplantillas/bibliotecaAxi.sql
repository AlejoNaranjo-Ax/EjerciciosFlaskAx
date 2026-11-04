CREATE DATABASE IF NOT EXISTS bibliotecaAxi;
USE bibliotecaAxi;

CREATE TABLE IF NOT EXISTS libros (
    Id        INT PRIMARY KEY,
    Titulo    VARCHAR(150) NOT NULL,
    Autor     VARCHAR(100) NOT NULL,
    Edicion   VARCHAR(50),
    Anho      VARCHAR(10),
    Editorial VARCHAR(100),
    NoPaginas INT
);
