from oops.agecalc import AgeCalculation
from oops.myexception import AgeException

age = int(input('Age '))
aobj = AgeCalculation()
try:

    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
    print('Eligble to vote...')
except  AgeException as ae:
     print(ae)
else:
    print('Eligble ')

