
# # ########## to set or ge the value of the private memebers of the class then we need to declare setter and getters for them

# # ### the decorators of @ things are used in the class when i do not want someone to change the value sof the properties in class and i want to make them only read only as a variable even if its a function



# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.__model = model
    
#     def get_fullname(self):
#         return f"The full name of car is {self.__brand} {self.__model}"
    
#     def get_brandname(self):
#         return f"The name of the brand is {self.__brand}"
    
#     def set_brandname(self,value):
#         self.__brand = value
    
#     def fuel_type(self):
#         return "Petrol or Diesel"
    
#     @property
#     def modelname(self):
#         return self.__model



# class ElectricCar(Car):
#     def __init__(self,brand,model,batterySize):
#         super().__init__(brand,model)
#         self.batterySize = batterySize
    

#     def fuel_type(self):
#         return "electric Charge"


# # my_car = Car("Honda","City Z")
# # print(my_car.get_fullname())
# # print(my_car.get_brandname())

# # my_elecCar = ElectricCar("Tata","Punch EV","100kWH")
# # print(my_elecCar.get_fullname())

# # my_elecCar.set_brandname("Curvv")
# # print(my_elecCar.get_fullname())
# # # print(my_elecCar.batterySize)

# # print(my_elecCar.fuel_type())

# my_newCar = ElectricCar("Tata","Nexon","100kwh")
# print(my_newCar.modelname)




# #### concept of decorators

# #### decorators are nothing but a function (like a toll gate) where all the other functions (like the vehicles) are obligated to be passed from it

# ## for example i have a decorator function which calculates time of execution of every single function

# # import time

# # def timer(func):
# #     def executer(*args,**kwargs):
# #         start_time = time.time()
# #         result = func(*args,**kwargs)
# #         end_time = time.time()
# #         print(f"{func.__name__}is the function executed in {end_time - start_time}")
# #         print(result)
# #         return result
# #     return executer

# # @timer
# # def func_one(n):
# #      time.sleep(n)

# # func_one(3)

# ## example 2 calculate the number of args a function passes and also print its name using decorator

# # def func_decorator(func):
# #     def executer(*args,**kwargs):
# #         args_value = ', '.join(str(arg) for arg in args)
# #         kwargs_value = ', '.join(str(kwarg) for kwarg in kwargs)
# #         print(f"the function name is {func.__name__} and the count opf paramters are {args_value}, {kwargs_value}")
# #     return executer


# # @func_decorator
# # def hello():
# #     print("Hemlo World!")


# # @func_decorator
# # def greeting(name, greet="Hemlo"):
# #     print(f"{greet}, {name}")

# # greeting("dhurv", "namaste")
# # hello()




# ### using a decorator function you have to return the cached values of a fucntion if it is called for more than one time and if not add those values in cached values as a memory reference

# import time

# def cache_decorator(func):
#     def executer(*args):
#         cache_value = {}
#         print(cache_value)
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] = result
#         print(result)
#         return result
#     return executer


# @cache_decorator
# def func_one( a , b):
#     time.sleep(3)
#     return a + b



# func_one(5,5)
# func_one(5,5)
# func_one(5,4)
