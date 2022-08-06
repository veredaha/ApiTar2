import json
import requests
import pytest
import logging
from accountapi import accountApi
from models.bookmodel import AllBooksModal, BookModal,GetUserResult
from bookstoreapi import BookStoreApi
from models.tokenviewmodel import LoginViewModel,TokenViewModel
from models.userbooksresult import MessageModal,ReplaceIsbn,StringObject,BooksResult,UserBooksResult
from models.collectionofIsbn import AddListOfBooks,CollectionOfIsbn


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

@pytest.fixture
def bookapi() ->accountApi:
 url = "https://bookstore.toolsqa.com/BookStore/v1"
 headrs ={'accept': 'application/json'}
 api = BookStoreApi(url,headrs)
 return api

@pytest.fixture
def accounteapi() ->accountApi:
 url = "https://bookstore.toolsqa.com/Account/v1/"
 headrs ={'accept': 'application/json'}
 api = accountApi(url,headrs)
 return api

@pytest.fixture
def logview() -> LoginViewModel:
 logview = LoginViewModel('lion', '12345@Aa')  
 return logview

@pytest.fixture
def addlists() -> AddListOfBooks:
 Add = AddListOfBooks('9cfb6df4-74f5-4380-9653-7ffca8c156eb', CollectionOfIsbn("string"))  
 return Add

@pytest.fixture
def book() -> BookModal:
 book = BookModal('123', 'vvv','aaa',"ana", '13/12/2014', 'kk', 200, 'hhh', 'aaaaa')  
 return book

def test_post_account_authorize(accounteapi:accountApi,logview:TokenViewModel) :
    """ test post account and authorize
    :param: bookapi->accountApi
    :param:logview->TokenViewModel
     :returns: TokenViewModel
     """
    mylogger.info("test for posting account")
    account = accounteapi.post_account_authorize(logview)
    assert account == True


def test_post_account_generatetoken(accounteapi:accountApi,logview:TokenViewModel) ->None:
    """ 
    test post account and generate token
    :param: bookapi->accountApi
    :param:logview->TokenViewModel
    :returns: TokenViewModel
    """
    mylogger.info("test for posting account generate token")
    account = accounteapi.post_account_generatetoken(logview)
    assert account._result == 'User authorized successfully.'

def test_post_account_user(accounteapi:accountApi,logview:TokenViewModel):
    """ test post new account
    :param: bookapi->accountApi
    :param:logview->TokenViewModel
     :returns: TokenViewModel
     """
    #The test will fail because user already exists (406)
    mylogger.info("test for posting new  user")
    account = accounteapi.post_account_user(logview)
    assert account._username == 'addv'

def tests_delete_account_by_id(accounteapi:accountApi):
    """ test delete account
     :param: bookapi->accountApi
     :returns: MessageModal
     """
     #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for deleting account by id") 
    dele = accounteapi.delete_account_by_id('98a9f32e-8c82-48ba-ac5b-8c5ca86bc82e')
    assert dele._code == '1207'

def test_get_account_by_id(accounteapi:accountApi)->GetUserResult:
    """ test get account
    :param: bookapi->accountApi
     :returns: TokenViewModel
     """
      #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for getting account by id") 
    account =  accounteapi.get_account_by_id('98a9f32e-8c82-48ba-ac5b-8c5ca86bc82e') 
    assert account._id == '98a9f32e-8c82-48ba-ac5b-8c5ca86bc82e'

def test_get_books(bookapi:accountApi)->None:
    """ test get books
    :param: bookapi->accountApi
     :returns: TokenViewModel
     """
    mylogger.info("test for getting all books") 
    books =  bookapi.get_books() 
    assert books[0]._isbn == '9781449325862'

def test_post_book(bookapi:accountApi,book:BookModal):
    """ test post book
    :param: bookapi->accountApi
     :returns: TokenViewModel
     """
      #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for posting new book")
    book = bookapi.post_book(book)
    assert book._isbn == 'string'

def test_delete_book(bookapi:BookStoreApi):
    """ test delete book
     :returns: TokenViewModel
     """
      #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for deleting book") 
    dele = bookapi.delete_book('98a9f32e-8c82-48ba-ac5b-8c5ca86bc82e')
    assert dele._userId == '98a9f32e-8c82-48ba-ac5b-8c5ca86bc82e'
 
def test_get_book_by_isbn(bookapi:BookStoreApi):
    """ test get book
     :returns: TokenViewModel
     """
    mylogger.info("test for getting book by isbn") 
    account =  bookapi.get_book_by_isbn('9781449325862') 
    assert account._isbn == '9781449325862'

def test_delete_book_by_isbn(bookapi:BookStoreApi) :
    """ test delete book by isbn
     :returns: TokenViewModel
     """
      #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for deleting book by isbn") 
    string = StringObject('9781449325862','9cfb6df4-74f5-4380-9653-7ffca8c156eb')
    dele = bookapi.delete_book_by_isbn(string)
    assert dele._userId == '9cfb6df4-74f5-4380-9653-7ffca8c156eb' 

def test_put_book(bookapi:BookStoreApi,book:BookModal):
    """ test for replacing isbn
     :returns: TokenViewModel
     """
      #The test will fail because of a bug - it says the user is not authorize but it is
    mylogger.info("test for replacing isbn")
    data = r = ReplaceIsbn('9cfb6df4-74f5-4380-9653-7ffca8c156eb','9781449325862')
    account = bookapi.put_book('9781449325862',data)
    assert account._userId == '9cfb6df4-74f5-4380-9653-7ffca8c156eb'
