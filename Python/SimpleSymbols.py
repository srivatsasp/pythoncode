import re
exists = 0
text = '=d+==+s+'
pattern = re.compile(r'[+=]\w[+=]')
matches = pattern.finditer(text)
for match in matches:
    exists = True
    print(match)
if exists:
    print('We got it')
else:
    print('Something is wrong with the pattern')
