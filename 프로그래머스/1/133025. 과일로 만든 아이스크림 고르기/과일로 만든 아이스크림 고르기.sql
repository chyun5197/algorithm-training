-- 코드를 입력하세요
SELECT FIRST_HALF.flavor from FIRST_HALF inner join ICECREAM_INFO on FIRST_HALF.flavor = ICECREAM_INFO.flavor
where TOTAL_ORDER>3000 and INGREDIENT_TYPE = 'fruit_based' order by TOTAL_ORDER desc