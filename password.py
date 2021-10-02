import random
import string
print("Would you like a password?")
a= input("Type yes or no: ")
if a == 'yes':
    b = random.randint(0 , 9)
    c = random.choice(string.ascii_letters)
    print(b,c)
else:
    print("bye fuck off")