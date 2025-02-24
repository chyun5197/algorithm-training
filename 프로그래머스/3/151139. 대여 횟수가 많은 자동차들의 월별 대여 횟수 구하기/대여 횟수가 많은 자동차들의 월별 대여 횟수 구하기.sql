-- 코드를 입력하세요
SELECT month(START_DATE) as MONTH,CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where DATE_FORMAT(START_DATE, "%Y-%m") between "2022-08" and "2022-10"
and car_id in (select car_id 
               from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
               where DATE_FORMAT(START_DATE, "%Y-%m") between "2022-08" and "2022-10"
               group by CAR_ID 
               having count(CAR_ID)>=5)
group by month, car_id
having RECORDS > 0 
order by month asc, CAR_ID desc