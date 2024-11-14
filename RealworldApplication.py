class Plane:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        # [] can create duplicates
        #[]arranges data in a sequential structure
        
        def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"Passenger {name} has been successfully booked."
        else:
            return "Sorry the plane is full.Bookung is Unsuccessful for {name}"
     

          #method to list passengers
def list_passengers(self):
    return self.passengers ##gives current list of a plane


plane_cesnar=Plane(4) #value of the capacity of that instance
print(plane_cesnar.add_passenger("John"))

#output "Passenger john has been succesfully booked"
print(plane_cesnar.add_passsenger("Mark"))
print(plane_cesnar.add_passsenger("Lily"))
print(plane_cesnar.add_passsenger("Mary"))

#Listing passengers
print(plane.list_passengers())#output: ['Alice' ,'Bob' , 'charlie']



