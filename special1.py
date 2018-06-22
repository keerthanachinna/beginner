import re
x = "hello world.123"
new = re.sub('[\w]+' ,'', x)
print(new)
