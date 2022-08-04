import json
import requests
import pytest  
from models.tokenviewmodel import LoginViewModel
from models.tokenviewmodel import TokenViewModel
from models.bookmodel import BookModal
from models.bookmodel import GetUserResult



def bearer_auth_session()->requests:
     """ bearer authontication
     :param: url -> str
     :returns: session
     """
     User ={ "userName": "veredaharonov",
                "password": "12345@Aa"}
     hader = {'accept': 'application/json'}
     res = requests.post( 'https://bookstore.toolsqa.com/Account/v1/GenerateToken' ,data=User,headers=hader)
     my_token = res.json()["token"]
     session = requests.session()
     session.headers.update(hader)
     session.headers.update({'Authorization': f'Bearer {my_token}'})
     return session
    

class accountApi():

    def __init__(self, url : str,headrs:str)-> None:
        """function creates class accountApi
         :returns: None 
         """
        self.url = url
        self.headrs = headrs
        self.session = requests.session()
        self.session.headers.update(self.headrs)
   
    def post_account_authorize(self, account:LoginViewModel)->None:
        """ post account
     :returns: LoginViewModel
     """
        account_data = account.toJson()
        res = self.session.post(url=f"{self.url}/account/v1/AuthOrized", data=account_data, header=self.headers)
        if res.status_code == 200:
            account = res.json()
            my_account = LoginViewModel(**account)
            return my_account
        else:
            return None 

    def post_account_generatetoken(self, account:TokenViewModel):
        """ post account
     :returns: TokenViewModel
     """
        account_data = account.toJson()
        res = self.session.post(url=f"{self.url}/account/v1/GenerateToken", data=account_data)
        if res.status_code == 200:
            account = res.json()
            my_account = TokenViewModel(**account)
            return my_account
        else:
            return None 

    def post_account_user(self, account:TokenViewModel):
        """ post account
     :returns: TokenViewModel
     """
        account_data = account.toJson()
        res = self.session.post(url=f"{self.url}/account/v1/user", data=account_data)
        if res.status_code == 200:
            account = res.json()
            my_account = TokenViewModel(**account)
            return my_account
        else:
            return None 
    
    def delete_account_by_id(self,id:str):
        """ delete account
     :returns: status_code
     """
        res = self.session.delete(url=f"{self.url}/account/v1/user/{id}")
        return res.status_code
            

    def get_account_by_id(self,id:str):
        """ get account
     :returns: status_code
        """
        res = self.session.get(url=f"{self.url}/account/v1/User/{id}")
        if res.status_code == 200:
            user = res.json()
            my_user = GetUserResult(**user)
            return my_user 
        else:
            return None

def main():

 session = bearer_auth_session()
 response = session.get('https://bookstore.toolsqa.com/Account/v1/User/c9cca7dc-e9e0-4eed-8d09-d3a08759c544')
 print(response)
 url = "https://bookstore.toolsqa.com/swagger/"


if __name__ == "__main__":
    main()

