inventary = []

def add_product():
    product = input("insert the product: ")
    price=float(input("insert the price: "))
    quantity=int(input("insert the quantity: "))
    
    product = {"price": price,
               "quantity":quantity}
     
    product.append(inventary)
    return 

add_product()
print(inventary)