SELECT MEMBER_ID, MEMBER_NAME, GENDER, date_format(date_of_birth, '%Y-%m-%d') DATE_OF_BIRTH 
from MEMBER_PROFILE 
where month(date_of_birth) = '03' and tlno != '' and gender='W' 
order by member_id asc