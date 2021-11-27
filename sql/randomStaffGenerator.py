import random
import string

position=['technician','mechanic','manager']


i=1
while(i<100):
    print('INSERT INTO `hvmpxx81gs6eza1p`.`staffs` (`name`, `position`, `branchNo`) VALUES ('+"'"+'staff'+str(i)+"'"+', '+"'"+position[random.randint(0,2)]+"'"+', '+"'"+str(random.randint(1,4))+"'"+');')
    i+=1