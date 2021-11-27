import string
import random

name=['Keith Corrigan','Arran Hancock','Rebekka Henson','Samia Sloan','Huda Harris','Mischa Gardner','Tanner Jeffery','Beverley Oconnor','Jon-Paul Good','Kimberly Guest','Polly Portillo','Malakai Robertson','Davina Solis','Yvette Swift',
        'Thelma Larsen','Lewie Rigby','Bertha Jaramillo','Cherie Duarte','Raja Stevenson','Kasim Bailey','Pola Hatfield','Federico Schultz','Bobbi Wilkinson','Charlotte Crosby','Sandra Mohamed','Che Mcgregor','Yasin Sears','Floyd Busby',
        'Cathal Estes','Opal Devlin','Ehsan Bourne','Derren Fountain','Indigo Serrano','Macauly Mcgee','Alysha Villegas','Maiya Oneill','Curtis Finch','Jorden Stanley','Hamza Mendez','Cem Hurley','Zachariah Alston','Keiren Clements',
        'Matthew Pham','Keisha Macleod','Phebe Waller','Samual Anthony','Franklin York','Brennan Fritz','Sumaiya Cox','Kaya Kirby','Javan Morrison','Safa Farrow','Faiza Schofield','Keiron Berry','Emmie Hook','Georga Knapp']

number=['0','1','2','3','4','5','6','7','8','9']


def clientNameGenerator():
    return(name[random.randint(0,55)])


def addressGenerator():
    address=random.choice(string.ascii_uppercase) + number[random.randint(0,9)] + random.choice(string.ascii_uppercase) +" "+ number[random.randint(0,9)] + random.choice(string.ascii_uppercase) + number[random.randint(0,9)]
    return address

def phoneGenerator():
    pnumber=number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)] + number[random.randint(0,9)]
    return pnumber

i=0

while(i<200):
    namen=clientNameGenerator()
    addressn=addressGenerator()
    phonen=phoneGenerator()

    print('INSERT INTO `hvmpxx81gs6eza1p`.`client` (`name`, `address`, `phone`) VALUES ('+"'"+namen+"'"+', '+"'"+addressn+"'"+', '+"'"+phonen+"'"+');')
    i=i+1