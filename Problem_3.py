def get_orders(quantity):
    orders = []
    for i in range(quantity):
        print("Name of order", i+1, ":", end='')
        name_order = input('')
        orders.append(name_order)
    return orders

def prepare_and_dispatch_orders(orders, quantity):
    prepared_orders = list(reversed(orders))
    dispatched_orders = list(prepared_orders)
    
    print("Preparing orders:")
    for i in range(quantity):
        print("Preparing order", i+1 ,":" , prepared_orders.pop())
    
    print("Following orders are being dispatched:")
    for i in range(quantity):
        print("Order ",i+1, ":" ,dispatched_orders.pop())

def main():
    quantity = int(input("How many orders: "))
    orders = get_orders(quantity)
    prepare_and_dispatch_orders(orders, quantity)

if __name__ == "__main__":
    main()
