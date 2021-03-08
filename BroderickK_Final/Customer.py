
class customer():
    def __init__(self):
        self.name = 'Customer'
        self.order = {
            "Crust":"THIN",
            "Flavor":"CHEESE",
            "Order_ID":4,
            "Size":"S",
            "Table_No":1,
            "Timestamp":"2021-01-01T18:21:08.708470"
        }
        self.order_patience = 30000 # 30 seconds
        self.eat_time = 12000 #2minutes #1200000# 20 minutes # How long it takes to eat and then they are hungry again
        self.is_hungry = False

    def place_order(self):
        return self.order