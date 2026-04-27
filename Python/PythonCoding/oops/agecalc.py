from oops.myexception import AgeException


class AgeCalculation():
    def voting_age_check(self, age):
        if age < 18:
            raise AgeException('Not eligble to vote')
        else:
            return True

    def pension_age_check(selfself, age):
        if age < 60:
            raise AgeException('Not eligble for pension')
