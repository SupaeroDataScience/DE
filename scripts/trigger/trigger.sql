CREATE OR REPLACE FUNCTION verifier_moyenne()
                  RETURNS trigger AS $verifier_moyenne$
    DECLARE
      moyenne FLOAT;
      nb      INTEGER;
    BEGIN
        moyenne := AVG(valeur) FROM rel;
        nb := COUNT(*) FROM rel;

        IF ((nb * moyenne + NEW.valeur) / (nb + 1)) < moyenne THEN
            RAISE EXCEPTION 'problem with insertion: valeur average is decreasing!';
        END IF;

        RETURN NEW;
    END;
$verifier_moyenne$ LANGUAGE plpgsql;

CREATE TRIGGER VerificationMoyenne
BEFORE INSERT ON rel
FOR EACH ROW
EXECUTE PROCEDURE verifier_moyenne();

INSERT INTO rel VALUES ('Fab', 15);

SELECT * FROM rel;

INSERT INTO rel VALUES ('Guy', 2);
