#initializing a set
my_cities = {"Kampala","Kigali","Nairobi","Mombasa","Arusha",}
print (my_cities)
#printing the length of the sets
print(len(my_cities))

#printing the type of structure
print(type(my_cities))

#add items to set
my_cities.add("cape Town")

print(my_cities)

other_cities = {"Nakuru","Naivasha","Mwanza","Jiji","Busia"}

my_cities.update(other_cities)
print(my_cities)

super_cities ={"New york","Washington",{"California","Oakland","LA"}}
print(super_cities)