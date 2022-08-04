from models.pet import Pet
from models.order import Order
from models.order import Status



import json
import requests



class storeApi():

    def __init__(self, url)-> None:
        self.url = url
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)


    def get_inventory(self)-> list:
        """ get inventory
     :returns: pet
         """
        res = self.session.get(url=f"{self.url}/store/inventory")
        inventoey = res.json()
        result = [] 
        if res.status_code == 200:
         for a in inventoey:
            result.append(a)
         return result 
        else:
            return None

    def place_order(self,order:Order):
        """ place order
        :returns: pet
          """
        order_data = order.toJson()
        res = self.session.post(url=f"{self.url}/pet", data=order_data)
        if res.status_code == 200:
            ord = res.json()
            return ord
        else:
            return None

    def get_purchase_by_id(self, order_id):
        res = self.session.get(url=f"{self.url}/order/{order_id}")
        if res.status_code == 200:
            order = res.json()
            my_pet = Pet(**order)
            return my_pet  
        else:
            return None

    def delete_order_by_id(self,order_id):
        res = self.session.delete(url=f"{self.url}/order/{order_id}")
        return res.status_code





