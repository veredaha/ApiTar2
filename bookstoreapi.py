import json
import requests
from models.tokenviewmodel import LoginViewModel
from models.tokenviewmodel import TokenViewModel
from models.bookmodel import BookModal
from models.bookmodel import GetUserResult


url = 'https://bookstore.toolsqa.com/Account/v1/GenerateToken'
def bearer_auth_session(url:str)-> requests:
     """ bearer authontication
     :param: url -> str
     :returns: session
     """
     User ={ "userName": "veredaharonov",
                "password": "12345@Aa"}
     hader = {'accept': 'application/json'}
     res = requests.post( url = f"{url}" ,data=User,headers=hader)
     my_token = res.json()["token"]
     session = requests.session()
     session.headers.update(hader)
     session.headers.update({'Authorization': f'Bearer {my_token}'})
     return session


class BookStoreApi():

 def __init__(self, url:str,headrs:str)-> None:
        """function creates class BookStoreApi
         :returns: None 
         """
        self.url = url
        self.headrs = headrs
        self.session = requests.session()
        self.session.headers.update(self.headrs)

 def get_books(self) -> BookModal:
    """ get books
     :param: url -> str
     :returns: session
     """
    res = self.session.get(url=f"{self.url}/BookStore/v1/Books")
    if res.status_code == 200:
            book = res.json()
            my_book = BookModal(**book)
            return my_book
    else:
            return None

 def post_book(self,book: BookModal) -> BookModal:
     """ post book
     :param: book -> str
     :returns: book
     """
     book_data = book.toJson()
     res = self.session.post(url=f"{self.url}/BookStore/v1/Books", data=book_data)
     book = res.json()
     if res.status_code == 200:
            my_book = BookModal(**book)
            return my_book
     else:
            return None

 def delete_book(self)-> BookModal:
     """ delete book
     :param: book -> str
     :returns: book
     """
     res = self.session.delete(url=f"{self.url}/BookStore/v1/Books")
     return res.status_code
 
 def get_book_by_isbn(self,isbn:str)-> BookModal:
  """ get book
     :param: isbn -> str
     :returns: book
     """
  res = self.session.get(url=f"{self.url}/BookStore/v1/Books")
  if res.status_code == 200:
            book = res.json()
            my_book = BookModal(**book)
            return my_book
  else:
            return None
  

def put_book(self,book:BookModal)-> BookModal:
     """ put book
     :param: book -> BookModal
     :returns: book
     """
     book_data = book.toJson()
     res = self.session.post(url=f"{self.url}/BookStore/v1/Books", data=book_data)
     book = res.json()
     if res.status_code == 200:
            my_book = BookModal(**book)
            return my_book
     else:
            return None