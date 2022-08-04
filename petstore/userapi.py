from models.user import User
from models.order import Order
from models.order import Status



import json
import requests



class userApi():

    def __init__(self, url)-> None:
        self.url = url
        self.headrs = {'accept': 'application/json'}
        self.session = requests.session()
        self.session.headers.update(self.headrs)



    def create_user(self,user):
        user_data = user.toJson()
        res = self.session.post(url=f"{self.url}/user", data=user_data)
        user = res.json()
        if res.status_code == 200:
            my_user = User(**user)
            return my_user
        else:
            return None

    def create_users_with_array(self,users):
        users_data = users.toJson()
        res = self.session.post(url=f"{self.url}/user/createWithList", data=users_data)
        user = res.json()
        if res.status_code == 200:
            my_user = User(**user)
            return my_user
        else:
            return None

    def login_user(self,username,password):
        res = self.session.get(url=f"{self.url}/user/login?{username}=theUser&password={password}")
        return res.status_code
        

    def log_out(self):
     res = self.session.get(url=f"{self.url}/user/logout")
     return res.status_code

    def get_user_by_name(self,username):
     res = self.session.get(url=f"{self.url}/user/{username}")
     if res.status_code == 200:
            user = res.json()
            my_user = User(**user)
            return my_user 
     else:
            return None


    def update_user(self,user,username):
        my_user = user.toJson()
        res = requests.put(url=f"{self.url}/user/{username}", json=my_user)
        if res.status_code == 200:
            return my_user
        else:
            return None
           
           
    def delete_order_by_name(self,name):
        res = self.session.delete(url=f"{self.url}/user/{name}")
        return res.status_code