SELECT     COUNT(*) FROM
sme.opportunities AS o INNER JOIN sme.accounts_opportunities ao ON
o.id = ao.opportunity_id WHERE     o.deleted = 0
AND ao.deleted = 1
AND o.id NOT IN( SELECT  ao1.opportunity_id  FROM   sme.accounts_opportunities ao1  WHERE ao1.deleted = 0 )
AND ao.DATE_MODIFIED >= '2017-11-01' WITH UR;