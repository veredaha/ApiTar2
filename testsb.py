import json
import requests
import pytest
import logging
from accountapi import accountApi
from bookstore.models.bookmodel import BookModal
from bookstoreapi import BookStoreApi
from models.tokenviewmodel import LoginViewModel
from models.tokenviewmodel import TokenViewModel


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

@pytest.fixture
def bookapi() ->accountApi:
 url = "https://bookstore.toolsqa.com/swagger/"
 headrs ={'accept': 'application/json'}
 api = accountApi(url,headrs)
 return api

@pytest.fixture
def storeapi() ->accountApi:
 url = "https://bookstore.toolsqa.com/swagger/"
 headrs ={'accept': 'application/json'}
 api = BookStoreApi(url,headrs)
 return api

@pytest.fixture
def logview() -> LoginViewModel:
 logview = LoginViewModel('vv', '12345')  
 return logview

@pytest.fixture
def tokenview() -> TokenViewModel:
 logview = TokenViewModel('vv', '20/9/2023','status',"result")  
 return logview

@pytest.fixture
def book() -> BookModal:
 book = BookModal('123', 'vvv','aaa',"ana", '13/12/2014', 'kk', 200, 'hhh', 'aaaaa')  
 return book

def test_post_account_authorize(bookapi:accountApi,logview:TokenViewModel) :
    """ test post account
     :returns: TokenViewModel
     """
    mylogger.info("test for posting account")
    account = bookapi.post_account_authorize(logview)
    assert account == True


def test_post_account_generatetoken(bookapi:accountApi,logview:TokenViewModel) :
    """ test post account
     :returns: TokenViewModel
     """
    mylogger.info("test for posting account generate token")
    account = bookapi.post_account_generatetoken(logview)
    assert account._token == 'string'

def test_post_account_user(bookapi:accountApi,logview:TokenViewModel):
    """ test post account
     :returns: TokenViewModel
     """
    mylogger.info("test for posting user")
    account = bookapi.post_account_user(tokenview)
    assert account == True

def tests_delete_account_by_id(bookapi:accountApi):
    """ test delete account
     :returns: TokenViewModel
     """
    mylogger.info("test for deleting account") 
    bookapi.delete_account_by_id('c9cca7dc-e9e0-4eed-8d09-d3a08759c544')
    account =  bookapi.get_account_by_id('c9cca7dc-e9e0-4eed-8d09-d3a08759c544') 
    assert account == None

def test_get_account_by_id(bookapi:accountApi):
    """ test get account
     :returns: TokenViewModel
     """
    mylogger.info("test for getting account by id") 
    account =  bookapi.get_account_by_id('c9cca7dc-e9e0-4eed-8d09-d3a08759c544') 
    assert account._id == 'c9cca7dc-e9e0-4eed-8d09-d3a08759c544'

def test_get_books(bookapi:accountApi):
    """ test get books
     :returns: TokenViewModel
     """
    mylogger.info("test for getting all books") 
    books =  bookapi.get_books() 
    assert books[0]._isbn == '9781449325862'

def test_post_book(bookapi:accountApi,book:BookModal):
    """ test post book
     :returns: TokenViewModel
     """
    mylogger.info("test for posting new book")
    book = bookapi.post_book(book)
    assert book._isbn == 'string'

def test_delete_book(self):
    """ test delete book
     :returns: TokenViewModel
     """
    mylogger.info("test for deleting book") 
    bookapi.delete_book('vv')
    account =  bookapi.get_book_by_isbn('vv') 
    assert account == None
 
def test_get_book_by_isbn(self,isbn:str):
    """ test get book
     :returns: TokenViewModel
     """
    mylogger.info("test for getting book by isbn") 
    account =  bookapi.get_book_by_isbn('vv') 
    assert account._isbn == 'vv'
  

def test_put_book(self,book:BookModal):
    """ test get book
     :returns: TokenViewModel
     """
    mylogger.info("test for putting book")
    book = bookapi.post_put_book(book)
    assert book._isbn == 'vv'