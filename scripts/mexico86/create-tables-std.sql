CREATE TABLE match (
    paysl character varying(20) NOT NULL,
    paysv character varying(20) NOT NULL,
    butsl integer,
    butsv integer,
    type character varying(6) NOT NULL,
    date date,
    CONSTRAINT match_butsl_check CHECK ((butsl >= 0)),
    CONSTRAINT match_butsv_check CHECK ((butsv >= 0))
);

CREATE TABLE pays (
    nom character varying(20) NOT NULL,
    groupe character(1)
);

CREATE TABLE typematch (
    type character varying(6) NOT NULL
);

INSERT INTO match VALUES
('Bulgarie','Italie','1','1','Poule','1986-05-31'),('Argentine','Corée','3','1','Poule','1986-06-02'),('Italie','Argentine','1','1','Poule','1986-06-05'),('Corée','Bulgarie','1','1','Poule','1986-06-05'),('Corée','Italie','2','3','Poule','1986-06-10'),('Argentine','Bulgarie','2','0','Poule','1986-06-10'),('Belgique','Mexique','1','2','Poule','1986-06-03'),('Paraguay','Irak','1','0','Poule','1986-06-04'),('Mexique','Paraguay','1','1','Poule','1986-06-07'),('Irak','Belgique','1','2','Poule','1986-06-08'),('Irak','Mexique','0','1','Poule','1986-06-11'),('Paraguay','Belgique','2','2','Poule','1986-06-11'),('Canada','France','0','1','Poule','1986-06-01'),('URSS','Hongrie','6','0','Poule','1986-06-02'),('France','URSS','1','1','Poule','1986-06-05'),('Hongrie','Canada','2','0','Poule','1986-06-06'),('URSS','Canada','2','0','Poule','1986-06-09'),('Hongrie','France','0','3','Poule','1986-06-09'),('Espagne','Brésil','0','1','Poule','1986-06-01'),('Algérie','Irlande du Nord','1','1','Poule','1986-06-03'),('Brésil','Algérie','1','0','Poule','1986-06-06'),('Irlande du Nord','Espagne','1','2','Poule','1986-06-07'),('Irlande du Nord','Brésil','0','2','Poule','1986-06-12'),('Algérie','Espagne','0','3','Poule','1986-06-12'),('Uruguay','RFA','1','1','Poule','1986-06-04'),('Écosse','Danemark','0','1','Poule','1986-06-04'),('Danemark','Uruguay','6','1','Poule','1986-06-08'),('RFA','Écosse','2','1','Poule','1986-06-08'),('Écosse','Uruguay','0','0','Poule','1986-06-13'),('Danemark','RFA','2','0','Poule','1986-06-13'),('Maroc','Pologne','0','0','Poule','1986-06-02'),('Portugal','Angleterre','1','0','Poule','1986-06-03'),('Angleterre','Maroc','0','0','Poule','1986-06-06'),('Pologne','Portugal','1','0','Poule','1986-06-07'),('Angleterre','Pologne','3','0','Poule','1986-06-11'),('Maroc','Portugal','3','1','Poule','1986-06-11'),('Brésil','Pologne','4','0','1/8','1986-06-16'),('France','Italie','2','0','1/8','1986-06-17'),('Maroc','RFA','0','1','1/8','1986-06-17'),('Mexique','Bulgarie','2','0','1/8','1986-06-15'),('Argentine','Uruguay','1','0','1/8','1986-06-16'),('Angleterre','Paraguay','3','0','1/8','1986-06-18'),('URSS','Belgique','3','4','1/8','1986-06-15'),('Espagne','Danemark','5','1','1/8','1986-06-18'),('Brésil','France','1','1','1/4','1986-06-21'),('RFA','Mexique','0','0','1/4','1986-06-21'),('Argentine','Angleterre','2','1','1/4','1986-06-22'),('Belgique','Espagne','1','1','1/4','1986-06-22'),('France','RFA','0','2','1/2','1986-06-25'),('Argentine','Belgique','2','0','1/2','1986-06-25'),('RFA','Argentine','2','3','Finale','1986-06-29');

INSERT INTO typematch VALUES
('Poule'),('1/8'),('1/4'),('1/2'),('Finale');

INSERT INTO pays VALUES
('Argentine','A'),('Italie','A'),('Bulgarie','A'),('Corée','A'),('Mexique','B'),('Paraguay','B'),('Belgique','B'),('Irak','B'),('URSS','C'),('Hongrie','C'),('France','C'),('Canada','C'),('Brésil','D'),('Espagne','D'),('Irlande du Nord','D'),('Algérie','D'),('Danemark','E'),('RFA','E'),('Uruguay','E'),('Écosse','E'),('Maroc','F'),('Angleterre','F'),('Pologne','F'),('Portugal','F');

ALTER TABLE ONLY match
    ADD CONSTRAINT match_pkey PRIMARY KEY (paysl, paysv, type);
ALTER TABLE ONLY pays
    ADD CONSTRAINT pays_pkey PRIMARY KEY (nom);
ALTER TABLE ONLY typematch
    ADD CONSTRAINT typematch_pkey PRIMARY KEY (type);
ALTER TABLE ONLY match
    ADD CONSTRAINT match_paysl_fkey FOREIGN KEY (paysl) REFERENCES pays(nom);
ALTER TABLE ONLY match
    ADD CONSTRAINT match_paysv_fkey FOREIGN KEY (paysv) REFERENCES pays(nom);
ALTER TABLE ONLY match
    ADD CONSTRAINT match_type_fkey FOREIGN KEY (type) REFERENCES typematch(type);

