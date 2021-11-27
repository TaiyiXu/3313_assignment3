import random
import string

item=['Soap','Engine Oil','Brack Pads','Discs/Drums','Pumper','Electric Drill','Leveler','BrakeFluid/ClutchFlue','Battery','Electronic Device','Tools'
      ,'Gear','Air Filter','Cabin','Fuel Filter','Oil Filter','Spark Plugs','Car compnent','tires']

price=['122',
'146',
'110',
'56',
'193',
'141',
'76',
'54',
'56',
'184',
'142',
'122',
'171',
'58',
'104',
'137',
'191',
'147',
'126',
'131',]

serviceType=['carWash', 'ChangeEngineOil', 'CheckBrakePads', 'BrakeDiscs/Drums', 'CheckCondition(tires)', 'CheckCoolantHoses', 'CheckLevel', 'RefillBrakeFluid/ClutchFlu', 'CheckBattery', 'CheckChargingSystems', 'Inspection', 'Maintenance', 'ReplaceAirFilter', 'ReplaceCabin', 'ReplaceFuelFilter', 'ReplaceOilFilter', 'ReplaceSparkPlugs', 'Replacement', 'tire change']


def priceGenerator():
    return(str(random.randint(50,200)))

def inventoryGenerator():
    return(str(random.randint(1,50)))

def serviceTypeGenerator():
    return(serviceType)

def serviceTypeFormator():
    serviceList= serviceType.split()
    return serviceList

#print(serviceTypeFormator())

    


i=0
while(i<19):
    price=priceGenerator()
    inventory=inventoryGenerator()

    print('INSERT INTO `hvmpxx81gs6eza1p`.`accessories` (`item`, `price`, `inventory`, `serviceType`) VALUES ('+"'"+item[i]+"'"+', '+"'"+price+"'"+', '+"'"+inventory+"'"+', '+"'"+serviceType[i]+"'"+');')
    i=i+1

