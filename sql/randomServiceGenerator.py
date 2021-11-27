import string
import random

oldserviceType=['Change the engine oil','Replace the oil filter','Replace the air filter','Replace the fuel filter','Replace the cabin or a/c filter',
'Replace the spark plugs','Check level and refill brake fluid/clutch fluid',
'Check Brake pads/Liners, Brake discs/Drums, and replace if worn out',
'Check Coolant Hoses',
'Check the charging systems','Check the battery','Check condition of the tires']

serviceType=['carWash', 'ChangeEngineOil', 'CheckBrakePads', 'BrakeDiscs/Drums', 'CheckCondition(tires)', 'CheckCoolantHoses', 'CheckLevel', 'RefillBrakeFluid/ClutchFlu', 'CheckBattery', 'CheckChargingSystems', 'Inspection', 'Maintenance', 'ReplaceAirFilter', 'ReplaceCabin', 'ReplaceFuelFilter', 'ReplaceOilFilter', 'ReplaceSparkPlugs', 'Replacement', 'tire change']

serviceDescription=['KJMVCNHLRL','RPDRYLNRUV','HUHMWILUYD','RKDUHWMXPP',
                    'IQCYAONMQQ','DLOFIVTDSJ','INBTVDKZJL','NDWWMRURAB',
                    'TUQHJRCOVQ','PIVROVJSVA','FLYTPZSRGD','UVYTNMHCLI'
                    'PSIGPKENEI','LBSIXEWEOC','MUEIKPZHVN','JKAKSTRKYG',
                    'CLPIBWEGCP','BIBGPFIPOI','GKVRKJYPZE',]

price= ['146','142','165','194',
        '186','79','135','132',
        '159','197','129','200',
        '132','141','123','201',
        '32','313','203']


i=0



def descriptionGenertor():
    return(random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_uppercase))

def priceGenerator():
    return(str(random.randint(50,200)))


while(i<18):
    #print("'"+descriptionGenertor()+"',")   
    #print("'"+priceGenerator()+"'"+',')
    #print('UPDATE `hvmpxx81gs6eza1p`.`services` SET `serviceType` = '+"'"+serviceType[i]+"'"+', `serviceDescription` = '+"'"+serviceType[i]+"'"+', `price` = '+"'"+serviceType[i]+"'"+' WHERE (`serviceType` = '+"'"+oldserviceType[i]+"'"+');')
    #print('INSERT INTO `hvmpxx81gs6eza1p`.`services` (`serviceType`, `serviceDescription`, `price`) VALUES ("'+serviceType[i]+'", "'+serviceDescription[i]+'", "'+price[i]+'");')
    i=i+1


