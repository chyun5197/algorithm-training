-- 코드를 작성해주세요
select A.ID,
case when A.PERCENTILE<=0.25 then "CRITICAL"
when A.PERCENTILE<=0.5 then "HIGH"
when A.PERCENTILE<=0.75 then "MEDIUM"
ELSE "LOW"
END COLONY_NAME
from 
(select ID, 
 PERCENT_RANK() over (order by SIZE_OF_COLONY desc) PERCENTILE
from ECOLI_DATA) A
order by A.ID