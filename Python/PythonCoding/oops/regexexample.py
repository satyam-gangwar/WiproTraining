"""import re

txt = input('Enter a text ')
bpat = input('Enter beginning pattern ')
epat = input('Enter ending pattern ')
bpat = '^' + bpat
epat = epat + '$'

if re.search(pattern=bpat, string=txt):
    print('Beginning pattern available')
else:
    print('Beginning pattern not available')

if re.search(pattern=epat, string=txt):
    print('Ending pattern available')
else:
    print('Ending pattern not available')
"""


'''import re
from _ast import pattern'''

'''import re

mbno = input('Enter a text ')
pat = r"[0-9]"

if re.fullmatch(pattern=pat, string=mbno):
    print('Only digits')
else:
    print('Other char available')
'''

#username
import re

'''un = input('Enter username ')
pat = r"^[a-z_]{8,}$"

if re.match(pattern=pat, string=un):
    print('Valid')
else:
    print('Invalid')'''

#email

'''emailadd = input('Email ')
pat = r"^[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"

if re.match(pattern=pat, string=emailadd):
    print('Valid')
else:
    print('Invalid')
'''

#pwd
'''pwdtxt = input('pwd : ')
pat = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@_-]).{8,}$"

if re.match(pattern=pat, string=pwdtxt):
    print('Valid')
else:
    print('Invalid')'''

txt = input('Text ')
pat = r"\s+"

#print(re.sub(pattern=pat, string=txt,repl='*fi'))
print(re.split(pattern=pat, string=txt))

