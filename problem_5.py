def call():
    x = 2 
    x = 5 - x / 2 #x=2 hence oveall x=5-2/2= 4
    #call() is always 4 as output
    print(x)
def caller():
    # x initiate from here
    x = 1 
    while x < 20 :
        print ("x="+ str(x) ) 
        #call function is called by caller
        call() 
        #x will change as caller value
        x =x * 2 
        print("x = " + str(x))
print(caller())

