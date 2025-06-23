
#1
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return round(pow(self.radius, 2)*pi, 2)
    def perimeter(self):
        return round(2*pi*self.radius, 2)
small_circle = Circle(5)
medium_circle = Circle(10)
large_circle = Circle(50)
print('The area of the cirle is:',  small_circle.area())
print('The perimeter of the cirle is:',  small_circle.perimeter())

print('The area of the cirle is:',  medium_circle.area())
print('The perimeter of the cirle is:',  medium_circle.perimeter())

print('The area of the cirle is:',  large_circle.area())
print('The perimeter of the cirle is:',  large_circle.perimeter())
#2
from datetime import date, datetime

class Person:

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def get_age(self):
        today = date.today()
        dob = datetime.strptime(self.date_of_birth,"%Y-%m-%d").date()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        
        return age


client = Person('Nice', 'Uzbekistan', '2007-05-30')
print(client.get_age())
#3
class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        try:
            result = self.a / self.b
            return result
        except ZeroDivisionError:
            print("Divizor CAN'T be zero")

nums = Calculator(5, 0)
print(nums.div())
#4
class Shape:
    pass

                    
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return round(pow(self.radius, 2)*3.14, 2)

    def get_perimeter(self):
        return round(2*3.14*self.radius, 2)

class Square(Shape):
    def __init__(self, size):
        self.size = size

    def get_area(self):
        return self.size**2

    def get_perimeter(self):
        return self.size*4

    def get_diagonal(self):
        return self.size*pow(2,0.5)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.sides = f'{a = }, {b = }, {c = }'

    def get_area(self, height, base):
        return height*base * 0.5

    def get_perimeter(self):
        return self.a + self.b + self.c

cyrcle = Circle(3.14)
print(cyrcle.get_perimeter())

sqware = Square(10)
print(sqware.get_diagonal())

threeangle = Triangle(4, 5, 7)
print(threeangle.get_area(6, 10))
print(threeangle.get_perimeter())
print(threeangle.sides)
#5
class Tree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Tree(val)
    if root.key == val:
        return root
    if root.key > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key > key:
        return search(root.left, key)
    
    return search(root.right, key)


root = Tree(50)
root.left = Tree(30)
root.right = Tree(70)
root.left.left = Tree(20)
root.left.right = Tree(40)
root.right.left = Tree(60)
root.right.right = Tree(80)

# Searching for keys in the BST
print("Found" if search(root, 19) else "Not Found")
print("Found" if search(root, 80) else "Not Found")
#6
class Stack:
    elements_list = []
    def __init__(self):
        pass


    def push(self, val):
        self.elements_list.append(val)


    def pop(self):
        self.elements_list.pop()


    def peek(self):
        '''Returns the top elements of the stack'''
        return self.elements_list[-1]


    def isEmpty(self):
        if not self.elements_list:
            return True
        else:
            return False
    def size(self):
        return len(self.elements_list)
#7
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def InsAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def InsAtIndex(self, data, index):
        if index == 0:
            self.InsAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        while current_node is not None and position + 1 != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Invalid index')
        
    
    def InsAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node


    def UpdateNode(self, value, index):
        current_node = self.head
        position = 0
        
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next
        if current_node is not None:
            current_node.data = value
        else:
            print('Index not present')

    def remove_first_node(self):
        if self.head is None:
            return
        
        self.head = self.head.next

    def remove_last_node(self):
        if self.head is None:
            return

        current_node = self.head
        while current_node.next is not None and current_node.next.next is not None:
            current_node = current_node.next
        
        current_node.next = None

    def remove_at_index(self, index):
        if self.head is None:
            return
            
        current_node = self.head
        position = 0

        if index == 0:
            self.remove_first_node()
        else:
            while current_node.next is not None and position + 1 != index:
                position += 1
                current_node = current_node.next

            if current_node is None or current_node.next is None:
                print("Index not present")
            else:
                current_node.next = current_node.next.next
        
    def remove_node(self, data):
        current_node = self.head
        
        if current_node.data == data:
            self.remove_first_node()
            return
        
        while current_node is not None and current_node.next.next.data != data:
            current_node = current_node.next

        if current_node is None:
            print('The data does not present')
        else:
            current_node.next = current_node.next.next

    def printLL(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def sizeOfLL(self):
        size = 0
        if self.head is None:
            return 0
        current_node = self.head
        while current_node is not None:
            size += 1
            current_node = current_node.next 
        return size 

#8
class Cart:
    items = dict()
    def __init__(self):
        pass

    def add_item(self, product: str, price: float):
        if product in self.items:
            print(f'You already have {product} in your cart!')
        self.items[product] = price
    
    def remove_item(self, product):
        if product in self.items:
            self.items.pop(product)
        else:
            print('You do not have this product in your cart!')

    def my_items(self):
        if self.items:
            print('Items in your cart:')
            n = 1
            for item in self.items.keys():
                print(f'{n}. ' + item)
                n += 1
        else:
            print("You don't have anytihing in your cart, yet")

    def total_price(self):
        return sum(self.items.values())
    
    def clear_cart(self):
        return self.items.clear()
#9
class Stack:
    elements_list = []
    def __init__(self):
        pass


    def push(self, val):
        self.elements_list.append(val)


    def pop_element(self):
        self.elements_list.pop()


    def peek(self):
        '''Returns the top elements of the stack'''
        return self.elements_list[-1]


    def isEmpty(self):
        if not self.elements_list:
            return True
        else:
            return False

    def size(self):
        return len(self.elements_list)

    def display(self):
        for i in self.elements_list:
            print(i)
#10
class Queue:
    queue = []
    def __init__(self):
        pass
    
    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        self.queue.pop(0)

    def display(self):
        print(self.queue)
#11
class Bank:
    def __init__(self, user: str, balance = 0, in_debt = 0) -> None:
        self.user = user
        self.balance = balance
        self.in_debt = in_debt
    
    def __str__(self):
        return f"User: {self.user}, Balance: {self.balance}, In Debt: {self.in_debt}"

    def deposit(self, amount: float):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print('You have insufficient amount of money to make the withdrawal!')
            
    def take_loan(self, amount):
        self.in_debt += amount*1.1 #interest rate
        self.balance += amount
    
    def return_loan(self, amount):
        if self.balance >= amount:
            if amount > self.in_debt:
                self.balance - self.in_debt
                self.in_debt = 0
            else:
                self.balance -= amount
                self.in_debt -= amount
        else:
            print('You have insufficient funds to return the loan')
            
    
    

class Customers:
    def __init__(self):
        self.users_list = []
    
    def add_user(self, user, balance=0, in_debt=0):
        new_user = Bank(user, balance, in_debt)
        self.users_list.append(new_user)

    def transfer(self, from_user_name: str, to_user_name: str, amount: float):
        from_user = next((account for account in self.users_list if account.user == from_user_name), None)
        to_user = next((account for account in self.users_list if account.user == to_user_name), None)

        if from_user is None:
            print(f"Sender '{from_user_name}' not found.")
            return

        if to_user is None:
            print(f"Receiver '{to_user_name}' not found.")
            return

        if from_user.balance >= amount:
            from_user.balance -= amount
            to_user.balance += amount
            print(f"Transferred {amount} from {from_user_name} to {to_user_name}.")
        else:
            print(f"{from_user_name} has insufficient funds to transfer {amount}.")

    
