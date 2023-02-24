# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:23:15 2023

@author: Christian Akomeah Sarpong

"""

cars = {'Picanto 17 model': 125600, 'Honda civic 18 model': 134850, 'Benz 4matic 22 model': 23374568, 'Land cruiser Prado': 4393450, 'Hyundai 17 model': 53456600, 'ferrari 23 model': 568000,
        'Tesla 22 model': 6773000, 'Vibe pontiac 23 model': 78978000, 'bmw 17 model': 2344000, 'Opel Astra 15 model': 65000, 'lamborghini elvador 22 model': 5900203, 'matiz Toyota 23 model': 50000, 'buggati aventador 23 model': 590000,
        'Ford 22 model': 7700500, 'Kia Rio 23 model': 550050, 'Chevrolet turbo23 model': 6857000, 'Scion model 22': 9566000, 'Audi fortix 21 model': 650000, 'culvert 23 model': 78400,'falcon 23 model': 234000,
        'porsche 23 model': 5556000, ' Escalade 22 model': 5766440000, 'bentley 18 model': 52340000, 'Renault 23 model': 786868600, 'suzuki okai 22 model': 90344000, 'lexus v12 22 model': 36466000,
        'Land rover sport 22 model': 67780000, 'birkin 23 model': 13560000, 'Dodge charger 22 model': 5123450000, 'Toyota Tundra 22 model': 1233323, 'Range rover Discovery 23 model':3233999}

prompt = input('Which type of car model do you want to buy please? ')
if prompt in cars:
        print('Yes, we do have ' + prompt.upper() + ' obtainable.')
        price = cars[prompt]
        print(prompt.upper() + ' the price of the car goes for Euros' + str(price))


else:
        print("We dont have that type of car model in our garrage,sorry customer" + prompt + ' inaccessible. These are the cars we have here in our garrage:')
        a = cars.keys()
        print(a)
#https://github.com/cAkomeah