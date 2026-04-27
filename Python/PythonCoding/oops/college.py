class College:
    def __init__(self, ccode, cname, ccity):
        self._collcode = ccode
        self._collname = cname
        self._collcity = ccity

    def welcome_message(self):
        print('Hello there !!!')

    def display_college_details(self):
        print(f'College Code: {self._collcode}\n College Name: {self._collname}\n City {self._collcity}' )