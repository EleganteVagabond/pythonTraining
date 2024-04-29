girls = "Girls"
punc = "?"
print("Hello {}{}".format(girls,punc))
print(f"Hello {girls}, how are you{punc}")
print("\\n")
print("_-_"*30)
import string
from string import ascii_lowercase

message = "hello"
print(id(message))

message = "\nhello\n"
print(message.strip())
print(message.rstrip())

message = "world of hurt"
print(id(message))

print(message.find('orl'))
print(message.split("""
o
"""))
print("^_^".join(['1','2','3']))
print(string.ascii_lowercase)
print(ascii_lowercase)

print("Hello world")
print(5+6)

print('Hello world I\'m using single quotes')
print("Hello world I'm using \"quotes\"")
# """Multi
# line
# string"""
