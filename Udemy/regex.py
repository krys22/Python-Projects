import re

string = "I AM NOT YELLING', she said, while yelling."
new = re.sub('[a-z]', '', string)
print(new)