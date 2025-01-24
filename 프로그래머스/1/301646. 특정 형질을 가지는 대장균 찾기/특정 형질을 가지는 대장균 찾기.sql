select count(*) COUNT
from ECOLI_DATA
where (GENOTYPE & 5 >= 1) and (GENOTYPE & 2 = 0)
# where (SIZE_OF_COLONY | 9 >= 1) and (SIZE_OF_COLONY & 15 != 15)