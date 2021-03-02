import requests
import json
from datetime import datetime

base_url = 'https://order-pizza-api.herokuapp.com/api/'
access_token = ""

def get_auth():
    global access_token
    body = {
        'username':'test',
        'password':'test'
    }
    url = base_url + 'auth'
    req = requests.post(url, json=body)

    content = json.loads(req.content)
    access_token = content['access_token']

get_auth()
def create_pizza_order(crust="Pan", flavor="Pepperoni", order_id=0, size="Small", table_no=0, timestamp=datetime.now()):
    global access_token
    if access_token != "":
        body = {
            "Crust":crust,
            "Flavor":flavor,
            "Order_ID":order_id,
            "Size":size,
            "Table_No":table_no,
            "Timestamp":str(timestamp)
        }

        headers = {
            "Authorization":f"Bearer {access_token}"
        }

        url = base_url + "orders"
        req = requests.post(url, headers=headers, json=body)

        # print(req.status_code)
        # print(req.content)
    else:
        print("No auth to be found.")

def get_pizza_orders():
    url = base_url + "orders"
    req = requests.get(url)

    # print(req.status_code)
    # print(json.loads(req.content))
    
    return json.loads(req.content)
    

def delete_pizza_order(order_id):
    # global access_token
    # if access_token != None:
        # headers = {
        #     "Authorization":f"Bearer {access_token}"
        # }
    url = base_url + f"orders/{order_id}"
    print(url)

    req = requests.delete(url)

    print(req.status_code)
    print(req.content)

    

if __name__ == '__main__':
    get_auth()
    create_pizza_order("NORMAL", "CHICKEN-FAJITA", 3, "L", 3, "2019-12-03T18:21:08.710006")
    # get_pizza_orders()
    # print('-' * 50)
    # delete_pizza_order(4)
    # get_pizza_orders()