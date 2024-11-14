#declaring a dictionary
my_phone={
    "Brand" : "Iphone",
    "Make"  : "Apple" ,
    "Version" : "XS Max",
    "YOM" : "2020",
    "Origin" : "United States of America"
}
#print the entire dictionary
print(my_phone)

#Access a value by its key
print(f'My phone make is :{my_phone ["Make"]} and the Brand is  : {my_phone["Brand"]}')


#A nested dictionary

my_phone = {
    "phone_one": {
        "Brand": "Samsung",
        "Make": "Galaxy",
        "Version": "S21",
        "YoM": 2021,
        "Orign": "South Korea"
    },

    "phone_two": {
        "Brand": "Apple",
        "Make": "iPhone",
        "Version": "13",
        "YoM": 2021,
        "Orign": "USA"
    }
}

print(my_phone["phone_one"])
print(my_phone["phone_two"])



