# Write a program that repeatedly asks the user to enter product names and prices. Store all 
# of these in a dictionary whose keys are the product names and whose values are the prices. 
# When the user is done entering products and prices, allow them to repeatedly enter a 
# product name and print the corresponding price or a message if the product is not in the dictionary. 

products ={}

while True :
    names = input("enter the product name : ")
    price = float(input("enter the price : "))
    products[names] = price
    product =input("if you want to enter more product then print yes otherwise no  : ")
    if product != 'yes':
        break

while True:
    name = input("enter the product name to get its price : ")

    if name in products:
        print(f"The price of {name} is {products[name]}")
    else:
        print(f"Product {name} not found")

    more = input("if you get the price of more product then print yes otherwise no :")
    
    if more != 'yes':
        print("you are successfully exit ")
        break



