#define a function 
def toppings(): 
    #user input for tooping
    print("tooping add is sprinkles, hot fudge, whipped cream, crushed nuts ")
    topping=input("Enter the name of topping") 
    return topping 
#define a another function
def scoop_size(): 
    #user input for+ scoop size
    scoop_size=int(input("Enter the scoop size ")) 
    return scoop_size
    #define a another functio
def make_shake(): 
    #user input for shake
    print("choice of shake nuts or fruits")
    choice=input("Enter your choice of shake") 
    return choice 

#import a ice_cream 
from ice_cream import * 
size=scoop_size() 
topping=toppings() 
choice=make_shake() 
print("The size of your scoop is:",size,)
print("Your added topping is:",topping) 
print("Your choice of shake is:",choice,"shake") 
