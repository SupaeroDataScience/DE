CREATE TABLE Frequente (
       buveur  VARCHAR(20),
       bar     VARCHAR(20),
       PRIMARY KEY (buveur, bar)
);



CREATE TABLE Sert (
       bar     VARCHAR(20),
       biere   VARCHAR(20),
       PRIMARY KEY (bar, biere)
);



CREATE TABLE Aime (
       buveur  VARCHAR(20),
       biere   VARCHAR(20),
       PRIMARY KEY (buveur, biere)
);


