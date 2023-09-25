COPY (SELECT array_to_json(array_agg(matches))
FROM (
  SELECT butsl, butsv, type, date,
    (
      SELECT array_to_json(array_agg(l))
      FROM (
        SELECT nom, groupe FROM pays WHERE pays.nom like concat('%',match.paysl,'%')
      ) l 
    ) AS paysl,
    (
      SELECT array_to_json(array_agg(v))
      FROM (
        SELECT nom, groupe FROM pays WHERE pays.nom like concat('%',match.paysv,'%')
      ) v 
    ) AS paysv
  FROM match
) matches) TO STDOUT WITH (FORMAT text, HEADER FALSE);
