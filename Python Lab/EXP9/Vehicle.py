"""Write a Python program to create a class Vehicle having methods vehicle_info() and
mode_transport() and derive two subclasses Bike and Train from it. Override the superclass methods
inside the two subclasses."""


class Vehicle:
    def vehicle_info(self):
        print("This is a vehicle")

    def mode_transport(self):
        print("This is a mode of transport")


class Bike(Vehicle):
    def vehicle_info(self):
        print("This is a bike")

    def mode_transport(self):
        print("This is a mode of road transport")

class Train(Vehicle):
    def vehicle_info(self):
        print("This is a train")

    def mode_transport(self):
        print("This is a mode of road transport")


bike = Bike()
train = Train()

print("\nBike:")
bike.vehicle_info()
bike.mode_transport()

print("\nTrain:")
train.vehicle_info()
train.mode_transport()
