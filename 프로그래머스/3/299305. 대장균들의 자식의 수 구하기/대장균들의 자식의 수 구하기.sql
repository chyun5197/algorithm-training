-- 코드를 작성해주세요
select C.ID, COUNT(P.ID) CHILD_COUNT
from ECOLI_DATA C
left join ECOLI_DATA P
on C.ID = P.PARENT_ID
group by C.ID
order by C.ID