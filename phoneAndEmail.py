import re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)
emailRegex = re.compile(r''' (
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
)''',re.VERBOSE)
mess = phoneRegex.findall('Hello +2h 34 bye 122 +125 7yy 545-121-4521')
mess1 = emailRegex.findall('hi I weedf@fjhks.com')
matches = []
for groups in mess:
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in mess1:
    matches.append(groups[0])
print(mess)
print(matches)
print(mess1)