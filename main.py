# 2 Gerekli kütüphaneleri ekledik.
import csv
import datetime

for word in 'Welcome to Pizzaland'.split():
    print(f'{word.capitalize():=^65}')
print("\n")
# 3 “Menu.txt” dosyasını oluşturduk.

menu = open("menu.txt", "w")
menu.write(""" ***Please choose your pizza:
  1- Classic Pizza > $10
  2- Margherita Pizza > $20
  3- FourFromages Pizza > $35
  4- Supreme Pizza > $13
  5- Pepperoni Pizza > $16
  6- Gennaro Pizza > $18
  7- Special Pizzaland > $20
  *** Select the materials you want to add:
  8- Olive > $0.25
  9- Mushroom > $0.4
  10- Cheese > $0.5
  11- Meat > $1.5
  12- Onion > $0.25
  13- Sweetcorn > $0.20
  14- Sausage > $0.5aaaa
  15- Peperoni > $0.39
  16- Pineapple > $0.5
  ***Thanks!!! \n""")


# 4 Üst sınıf oluşturduk. “pizza”

class pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost


# 5 Alt sınıf oluşturduk. “pizza”
class ClassicPizza(pizza):
    cost = 10.0

    def __init__(self):
        self.description = "Inside: Peperoni,Cheese,Tomato sos"
        print(self.description)


class MargheritaPizza(pizza):
    cost = 20.0

    def __init__(self):
        self.description = "Inside: Mozarella,Basil,Tomato sos"
        print(self.description)


class FourFromagesPizza(pizza):
    cost = 35.0

    def __init__(self):
        self.description = "Inside: Mozarella,Blue cheese,Parmesan,Cheese"
        print(self.description)


class SupremePizza(pizza):
    cost = 13.0

    def __init__(self):
        self.description = "Inside: Mozarella,Sausage,Green Peper,Onion"
        print(self.description)


class PeperoniPizza(pizza):
    cost = 16.0

    def __init__(self):
        self.description = "Inside: Peperoni,Sausage,Cheese,Tomato sos"
        print(self.description)


class GennaroPizza(pizza):
    cost = 18.0

    def __init__(self):
        self.description = "Inside: Mozarella,Peperoni,Mushroom,Sweetcorn"
        print(self.description)


class SpecialPizzaland(pizza):
    cost = 20.0

    def __init__(self):
        self.description = "Inside: Mozarella,Pineapple,Basil"
        print(self.description)

    # 6 Üst sınıf oluşturduk “Decorator”


class Decorator(pizza):
    def __init__(self, material):
        self.additional = material

    def get_cost(self):
        return self.additional.get_cost() + \
            pizza.get_cost(self)

    def get_description(self):
        return self.additional.get_description() + \
            ":" + pizza.get_description(self)


class Olive(Decorator):
    cost = 0.25

    def __init__(self, material):
        Decorator.__init__(self, material)


class Mushroom(Decorator):
    cost = 0.4

    def __init__(self, material):
        Decorator.__init__(self, material)


class Cheese(Decorator):
    cost = 0.5

    def __init__(self, material):
        Decorator.__init__(self, material)


class Meat(Decorator):
    cost = 1.5

    def __init__(self, material):
        Decorator.__init__(self, material)


class Onion(Decorator):
    cost = 0.25

    def __init__(self, material):
        Decorator.__init__(self, material)


class Sweetcorn(Decorator):
    cost = 0.20

    def __init__(self, material):
        Decorator.__init__(self, material)


class Sausage(Decorator):
    cost = 0.5

    def __init__(self, material):
        Decorator.__init__(self, material)


class Peperoni(Decorator):
    cost = 0.39

    def __init__(self, material):
        Decorator.__init__(self, material)


class Pineapple(Decorator):
    cost = 0.5

    def __init__(self, material):
        Decorator.__init__(self, material)


# Menu yazdırıldı.
with open("menu.txt") as menu:
    for l in menu:
        print(l, end="")


def main():
    class_dict = {
        1: ClassicPizza,
        2: MargheritaPizza,
        3: FourFromagesPizza,
        5: PeperoniPizza,
        6: GennaroPizza,
        7: SpecialPizzaland,
        8: Olive,
        9: Mushroom,
        10: Cheese,
        11: Meat,
        12: Onion,
        13: Sweetcorn,
        14: Sausage,
        15: Peperoni,
        16: Pineapple}
    code = input("Please choose your pizza : ")
    while code not in ["1", "2", "3", "4", "5", "6", "7"]:
        code = input("Error! Please try again: ")

    order = class_dict[int(code)]()

    while code != "ok":
        code = input("Please select the materials you want to add (Press 'ok' to Confirm Your Order): ")
        if code in ["8", "9", "10", "11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(code)](order)

    print("\n" + order.get_description().strip() +
          ": ₺" + str(order.get_cost()))
    print("\n")

    print("********Order Information********\n")
    name = input("Name: ")
    ID = input("ID: ")
    credit_card = input("Enter Your Credit Card Number: ")
    credit_password = input("Enter Your Credit Card Password: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')
        orders.writerow([name, ID, credit_card, credit_password, order.get_description(), time_of_order])
    print("Your Order Received.")


if __name__ == '__main__':
    main()