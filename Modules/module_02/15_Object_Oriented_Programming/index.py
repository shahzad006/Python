# ----------------------------------- Class ---------------------------------- #

class Car:

    # ------------------------------ Class variable ------------------------------ #
    total_car = 0



    # -------------------------------- Constructor ------------------------------- #
    def __init__(self , brand , model):

        # ********** Attributes *********
        # ********** __ private Encapsulate **********
        self.__brand = brand
        self.__model = model
        Car.total_car +=1

    # ------------------------------- Getter method ------------------------------ #
    def get_brand(self):
        return self.__brand + "!"


    # --------------------------- Class method and self -------------------------- #
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    


    def fuel_type(self):
        return "Petrol and Diesel"
    

    # ------------------------------- Static method ------------------------------ #
    @staticmethod
    def gernal_descripation():
        return "Cars are mean of transport"
    
    # ---------------------------- Property Decorators --------------------------- #
    @property
    def model(self):
        return self.__model



# -------------------------------- Inheritance ------------------------------- #
class ElectricCar(Car):
    def __init__(self , brand , model , battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size




    def fuel_type(self):
        return "Electric Charge"
    


print(Car.gernal_descripation())





# ---------------------------------- Object ---------------------------------- #
my_car_1 = Car("Toyota" , "Corolla")
my_car_1.model = "City"
print(my_car_1.model)
# print(my_car_1.brand) Private
print(my_car_1.model)
print(my_car_1.full_name())
print(my_car_1.fuel_type())


# ---------------------------------- Object ---------------------------------- #
my_car_2 = ElectricCar("Tesla" , "Model" , "85KWH")


# ---------------- Class inheritance and isinstance() Function --------------- #
print(isinstance(my_car_2 , Car))
print(isinstance(my_car_2 , ElectricCar))
print(my_car_2.battery_size)
print(my_car_2.get_brand())
print(my_car_2.fuel_type())


print(Car.total_car)




# --------------------------- Multiple Inheritance --------------------------- #

class Battery:
    
    def battery_info(self):
        return "This is Battery"

class Engine:

    def engine_info(self):
        return "This is Engine"


class ElectricCar_Two(Battery , Engine , Car):
    pass



my_new_car = ElectricCar_Two("Tesla" , "Model S")
print(my_new_car.battery_info())
print(my_new_car.engine_info())