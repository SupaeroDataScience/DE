COPY (SELECT array_to_json(array_agg(matches))
FROM (
  SELECT paysl, paysv, butsl, butsv, type, date
  FROM match
) matches) TO STDOUT WITH (FORMAT text, HEADER FALSE);
