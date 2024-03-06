class LineItem:
    # Constructor method to initialize the instance attributes
    def __init__(self, stock_code, product_description, unit_price, quantity, date):
        self.stock_code = stock_code
        self.product_description = product_description
        self.unit_price = unit_price
        self.quantity = quantity
        self.date = date

    # Method to print the car's details
    def print_details(self):
        print("Stock Code:", self.stock_code)
        print("Product Description:", self.product_description)
        print("Unit Price:", self.unit_price)
        print("Quantity:", self.quantity)
        print("Date:", self.date)


# Creating object instances of the Car class
line_item1 = LineItem(stock_code="82095", product_description="HEART BUTTONS JEWELLERY BOX",
                      unit_price=4.96, quantity=1, date="2015/04/06")
line_item2 = LineItem(stock_code="21070", product_description="VINTAGE BILLBOARD MUG",
                      unit_price=2.46, quantity=1, date="2015/10/15")


line_item2.unit_price = 2.50


# Printing the details of the car instances
#line_item1.print_details()
#print("\n")
#line_item2.print_details()

print(line_item2.stock_code)

