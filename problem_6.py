#defineing a function
def ROI():  
    #user input 
    annual_rate=int(input("enter the annual site profit: "))  
    improve_rate=int(input("enter the improved conversion rate: ")) 
    current_rate=int(input("enter the current conversion rate: ")) 
    project_life=int(input("enter the expected project life: ")) 
    cost=int(input("enter the improvemenet Cost: ")) 
    # i value
    i=0.05
    # a=variable 
    #formula 
    a=annual_rate*(improve_rate/current_rate)-annual_rate*((1+i)**project_life-1) / ((i-cost)*(1+i)**project_life) 
    #formula 
    #return parameter 
    return a
    
#defining the main function     
def FGI():
    #calling the function 
    a=ROI() 
    #printing the output 
    print("The future gain from improvement is:",a) 
FGI() 
