#defining a function to get tshirt
def get_tshirt(x):
    #Brand available in store
    shirt=["python_tshirt","c_tshirt","java_tshirt"]
    #tshirt size alailable in store
    l=["m","l","x","xl","xxl"]
    #calling the name function 
    user=get_name()
    for i in (shirt):
        #if using for the brand available or not
        if(i==x):
            print("Hi" ,{user},"Brand you looking for is available in our store")
            n=input("enter the size you wont:")
            for j in (l):
                #if using for the size available or not
                if(j==n):
                    print("your size is available ")
                    break
            else:
                print("your brand was available but size not available")
        break
    else:
        print("Hi" ,{user},"Unfortunately Brand you looking for is not available in our store")

#defining another function to get name
def get_name():
    name=input("enter the name : ")
    return name
    
#user input of brand 
a=input("enter the brand:")
#calling the first function 
get_tshirt(a)
