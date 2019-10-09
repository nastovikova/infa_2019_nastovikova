
def what_can_i_buy(products, money):
    # Prints wich of 'products' you can buy for your 'money'. 
    available = []
    for key in products:
        if products[key] <= money:
            available.append(key)
    print(available)


vegetables = {'tomato': 15, 'potato': 5, 'apple': 10, 'onion': 12, 'cucumber': 6}
what_can_i_buy(vegetables, 10)
