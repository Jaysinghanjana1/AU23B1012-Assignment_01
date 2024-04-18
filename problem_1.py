#defining a function to get tshirt
def get_tshirt(x):
    #Brand available in store
    shirt=["python_tshirt","c_tshirt","java_tshirt"]
    #calling the name function 
    user=get_name()
    #if using for the brand available or not
    for i in (shirt):
        if(i==x):
            print("Hi" ,{user},"Brand you looking for is available in our store")
            break
    else:
        print("Hi" ,{user},"Unfortunately Brand you looking for is not available in our store")

#defining another function to get name
def get_name():
    name=input("enter the name")
    return name

#user input of brand 
a=input("enter the brand")
#calling the first function 
get_tshirt(a)
