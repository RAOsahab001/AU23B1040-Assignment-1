def get_name():
    name = input("Please enter your name: ")
    return name

def get_tshirt(brand):
    
    available_brands = [ "Nike","Puma", "Adidas","Under Armour", "Reebok"]
   


    if brand in available_brands :
        print("Hi ", get_name(), " the brand you are looking for is available in our store.")
    else:
        print("Hi", get_name(), "Unfortunately the brand you are looking for is not available in our store.")
    

brand = input("Enter the T-shirt brand you are looking for: ")

get_tshirt(brand)
