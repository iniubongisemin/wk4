class Shop:
    # defining the class attribute 
    commodity_tax = 12.00
    product_list = ['milk', 'milo', 'sugar', 'cornflakes']

    # defining the constructor
    def __init__(self, *args):
        # instance attribute
        self.args = args
        # self.goods = goods

    # defining the instance method
    def your_order(self, *args):
        for args in args:
            if args in Shop.product_list:
                print(args)
            else:
                print(f'we\'re sorry {args} is out of stock')

    # defining another instance method 
    def pricing_list(self, price):
        self.price = price 
        product_price = price + Shop.commodity_tax
        print('here is your receipt have a lovely')
        return f'\u20a6{product_price}'
    
# calling the Shop class and assigning arguments
place_my_order = Shop('milk', 'milo', 'sugar', 'cornflakes')
print(place_my_order.your_order('milk', 'milo', 'golden mourn', 'biscuit'))
# print(place_my_order.your_order('milo', 'sugar'))
your_bill = Shop(12.09)
print(your_bill.pricing_list(500))

