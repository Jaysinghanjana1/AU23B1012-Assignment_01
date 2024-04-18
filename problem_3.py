 #define a function 
def get_order(x):
    order=[]
    for i in range(x):
         #user input order
        l=input("enter your order: ")
        order.append(l)
    #reberse of order
    order.reverse()
        #popping of order
    print("Preparing your order",order.pop())
    print("Preparing your order",order.pop())
    print("Preparing your order",order.pop())
    print("The following order have been despatched")   
    for i in (order):
        print(i)
#user input how many order 
a=int(input("how many order you want:"))
#function call
get_order(a)
