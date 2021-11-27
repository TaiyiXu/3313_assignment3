import random
import string


location=['wonderland road 101','western road 100','northwest street 201','saniar201']

def randomPCGenerator():
    random.choice(string.ascii_uppercase)
    str(random.randint(0,9))
    postolCode=(random.choice(string.ascii_uppercase)+str(random.randint(0,9))+random.choice(string.ascii_uppercase)+" "+str(random.randint(0,9))+random.choice(string.ascii_uppercase)+str(random.randint(0,9)))
    return postolCode

def randomLocationGenerator():
    location=(random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters))
    return location
i=1
while(i<5):
    posC=randomPCGenerator()
    location=randomLocationGenerator()
    print('INSERT INTO `hvmpxx81gs6eza1p`.`branches` (`branchNo`, `location`, `postalcode`) VALUES ('+"'"+str(i)+"'"+', '+"'"+location+"'"+', '+"'"+posC+"'"+');')
    i+=1
    