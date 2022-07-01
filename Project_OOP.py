#https://www.youtube.com/watch?v=Ej_02ICOIgs
import csv
class Item:
    pay_rate = 0.8 # the pay rate after 20% of discount
    all=[]
    def __init__(self, name:str, price: float, quantity=0):
        #Run validations to the received arguments
        assert price >=0 , f'Price {price} is not greater than or equal to zero!'
        assert quantity >=0, f' Quantity {quantity} is not greater or equal than zero!'
        #Assign to self object
        self.name = name
        self.price=price
        self.quantity=quantity
        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price*self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('Name.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.quantity})'

Item.instantiate_from_csv()

''''item1 = Item('Phone',100, 1)
item2 = Item('laptop', 1000, 3)
item3 = Item('Mouse', 50, 3)
item4 = Item('Keyboard', 75, 3)
item5 = Item('Cable', 75, 3)
item5 = Item('book', 7, 10)'''



print(Item.all)








