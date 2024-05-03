def get_name():
    global name
    name = input("Please enter your name: ")
    return name

def get_tshirt(brand_name):

    available_brands = [ "Nike","Puma", "Adidas", "Reebok"]
    
    

    if brand in available_brands :
        print("Hi ", name, " the brand you are looking for is available in our store.")

        if brand=='Nike':
            avai_size=['s','m','l']
            if size in avai_size:
               print("Hi ", name , " ,",size,"size in the brand you are looking for is available in our store.")

            if brand=='Puma':
                    avai_size=['s','m','l']
                    if size in avai_size:
                       print("Hi ", name , " ,",size,"size in the brand you are looking for is available in our store.")


            if brand=='Adidas':
                    avai_size=['s','m','l']
                    if size in avai_size:
                       print("Hi ", name , " ,",size," size in the brand you are looking for is available in our store.")


            if brand=='Reebok':
                    avai_size=['s','m','l']
                    if size in avai_size:
                       print("Hi ", name , " ,",size,"size in the brand you are looking for is available in our store.")


    else:
        print("Hi", name, "Unfortunately the brand you are looking for is not available in our store.")

# Example usage
brand = input("Enter the T-shirt brand you are looking for: ")
size = input("Enter the size (optional): ")

get_name()
get_tshirt(brand)
