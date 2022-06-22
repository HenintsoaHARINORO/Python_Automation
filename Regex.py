import re
phoneNumReg = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mess = phoneNumReg.search('My phone munber is 415-555-4242.')
print('Phone number found:' + mess.group(1))