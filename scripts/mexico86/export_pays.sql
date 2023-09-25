COPY (SELECT array_to_json(array_agg(p))
FROM (
  SELECT nom, groupe
  FROM pays
) p) TO STDOUT WITH (FORMAT text, HEADER FALSE);
