
# class Shoe initialised with 5 parameters
# functions to get cost, quantity, product of the shoe
# __str__ to return all details of the shoe 
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity  = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
    
    def get_product(self):
        return self.product

    def __str__(self):
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")


# The list will be used to store a list of objects of shoes.
shoe_list = []

    
# This function will open the file inventory.txt
# and read the data from this file, then create a shoes object with this data
# and append this object into the shoes list. One line in this file represents
# data to create one object of shoes. 
def read_shoes_data():
    f = open("inventory.txt", "r+")
    next(f)
    try:
         for lines in f:
            line = lines.strip().split(",")
            shoe = Shoe(line[0], line[1], line[2], line[3], int(line[4]))
            shoe_list.append(shoe)
    except FileNotFoundError as error:
        print("This file does not exist")
    f.close()           
            

# This function will allow a user to capture data
# about a shoe and use this data to create a shoe object
# and append this object inside the shoe list
def capture_shoes():
    country, code, product, cost, quantity = input("Please enter the values in this format: Country, Code, Product, Cost, Quantity\n").split(",")
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)



# This function will iterate over the shoes list and
# print the details of the shoes returned from the __str__ function
def view_all():
    read_shoes_data()
    for shoe in shoe_list:
        print(shoe.__str__())
      

# This function will find the shoe object with the lowest quantity,
# which is the shoes that need to be re-stocked. Asks the user if they
# want to add this quantity of shoes and then updates it
def re_stock():
    read_shoes_data()
    shoe_quantity_list = []
    for shoe in shoe_list:
        shoe_quantity_list.append(shoe.get_quantity())
    lowest_quantity = min(shoe_quantity_list)
    lowest_quantity_shoe = next((obj for obj in shoe_list if obj.quantity == lowest_quantity))
    
    print(f"The details of the shoe with the lowest stock is: {lowest_quantity_shoe}")        
    
    restock = input("Would you like to increase the quantity of this shoe? Y or N ")
    
    if restock == "Y":
        quantity = input("How much quantity would you like to have? ")
        f = open("inventory.txt", "r+")
        next(f)
        for lines in f:
            line = lines.strip().split(",")
            if int(line[4]) == lowest_quantity_shoe.quantity:
                line.pop(4)
                line.append(quantity)
                new_quantity = ",".join(line)
                f.write(f"\n{new_quantity}")
        print("Your stock has now been updated")
        
        

# This function will search for a shoe from the list
# using the shoe code and return this object so that it will be printed.
def search_shoe():
    read_shoes_data()
    shoe_code = input("Please enter the shoe code: ")
    shoe = next((obj for obj in shoe_list if obj.code == shoe_code))
    print(f"The details for {shoe_code} are: {shoe}")


# This function will calculate the total value for each item
def value_per_item():
    read_shoes_data()
    for line in shoe_list:
        value = int(line.get_cost()) * int(line.get_quantity())
        print(f"{line.get_product()}\'s Total Stock Value: {value}")


# This function determines the product with the highest quantity and
# print this shoe as being for sale.
def highest_qty():
    read_shoes_data()
    shoe_quantity_list = []
    for shoe in shoe_list:
        shoe_quantity_list.append(shoe.get_quantity())
        
    highest_quantity = max(shoe_quantity_list)
    highest_shoe = next((obj for obj in shoe_list if obj.quantity == highest_quantity))
    print(f"The {highest_shoe.product}\'s is now on sale!")


#==========Main Menu=============
while True:

    try:
        menu = int(input('''\n
            Please select from the menu below:
            1. Capture Shoes
            2. View All
            3. Restock
            4. Search
            5. View Item Values
            6. View Sale Items
            \n'''))

        if menu == 1:
            capture_shoes()

        elif menu == 2:
            view_all()

        elif menu == 3:
            re_stock()

        elif menu == 4:
            search_shoe()

        elif menu == 5:
            value_per_item()

        elif menu == 6:
            highest_qty()

        elif menu > 6:
            print("\nYou have selected an invalid option. Please try again by choosing from the menu below.\n")

    except ValueError:
        print("\nYou have selected an invalid option. Please try again by entering a number.\n")