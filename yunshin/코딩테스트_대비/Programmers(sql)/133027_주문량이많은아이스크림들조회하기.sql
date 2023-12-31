SELECT J.FLAVOR FLAVOR
    FROM (SELECT SUM(TOTAL_ORDER) TOTAL_ORDER, FLAVOR FROM FIRST_HALF GROUP BY FLAVOR) AS F  
        INNER JOIN (SELECT SUM(TOTAL_ORDER) TOTAL_ORDER, FLAVOR FROM JULY GROUP BY FLAVOR) AS J 
        ON J.FLAVOR = F.FLAVOR
    ORDER BY (F.TOTAL_ORDER + J.TOTAL_ORDER) DESC
    LIMIT 3