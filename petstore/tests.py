import json
import requests
import pytest
import logging
from petapi import petApi 
from storeapi import storeApi
from models.pet import Pet,Category
from models.order import Order
from models.user import User
from userapi import userApi


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def api() -> petApi:
 url = "https://petstore3.swagger.io/api/v3"
 headrs ={'accept': 'application/json'}
 api = petApi(url,headrs)
 return api

@pytest.fixture
def storeapi() -> storeApi:
 url = "https://petstore3.swagger.io/api/v3"
 headrs ={'accept': 'application/json'}
 api = storeApi(url,headrs)
 return api

@pytest.fixture
def userapi() -> petApi:
 url = "https://petstore3.swagger.io/api/v3"
 headrs ={'accept': 'application/json'}
 api = userApi(url,headrs)
 return api

@pytest.fixture
def pet() -> Pet:
 pet = Pet(10, 'vv', None, None ,None,None)  
 return pet

@pytest.fixture
def order() -> Order:
 Ord = Order(10, 198772, 7, "2022-08-02T16:07:44.983Z" ,"approved",True)  
 return Ord

@pytest.fixture
def user() -> User:
 use = User(10, 'vv', 'vered' ,'aha',"vered@gmail.com",'12345@uU','0525332626',1)  
 return use

def test_update_pet(api:petApi,pet:Pet)->None: 
 """
 test for updating a pet
 :param" api->petApi
 :param:pet->Pet
 :returns:None
 """
 mylogger.info("test for updating a pet")
 res = api.update_pet(pet)
 assert res._name == 'vv'


def test_post_new_pet(api:petApi,pet:Pet)->None:
 """
 test for posting a new pet
 :param" api->petApi
 :param:pet->Pet
 :returns:None
 """
 mylogger.info("test for posting a new pet")
 pet = api.post_new_pet(pet)
 assert pet._name == 'vv'
 
def test_get_by_status(api:petApi)->None:
 """
 test for getting pets by status
 :param" api->petApi
 :returns:None
 """
 mylogger.info("test for getting pets by status")
 pets =  api.get_pet_by_status("available")
 assert   pets[0]['status'] == "available"

def test_get_by_tags(api:petApi)->None:
 """
 test for getting pets by status
 :param" api->petApi
 :returns:None
 """
 mylogger.info("test for getting pets by tags")
 pets =  api.get_pet_by_tags(1)
 for pet in pets:
   assert pet._tags == 1

def test_get_pet_by_id(api:petApi)->None:
  """
 test for getting pet by id
 :param" api->petApi
 :returns:None
 """
  mylogger.info("test for getting pet by id") 
  pet =  api.get_pet_by_id(10) 
  assert pet._id == 10

def test_update_with_form_data(api:petApi,pet:Pet)->None:
    """
 test for updating with form data
 :param" api->petApi
 :param:pet->Pet
 :returns:None
 """
    mylogger.info("test for updating with form data") 
    pet = api.update_with_form_data(pet,10, 'vv', 'available')
    assert pet._status == 'available'

def test_delete_pet(api:petApi)->None:
    """
 test for deleting pet
 :param" api->petApi
 :returns:None
 """
    mylogger.info("test for deleting pet") 
    dele =api.delete_pet(2)
    assert dele.status_code == 200


def test_upload_image(api:petApi)->None:
    """
 test for uploading image
 :param" api->petApi
 :returns:None
 """
    mylogger.info("test for uploading image") 
    image = '@87fc90b8adc99582eb71d99a6b0c33b46935.jpg'
    pet = api.upload_image(image,10)
    assert pet.photo_urls == ["string", "/tmp/inflector7440998430605450804.tmp"]


def test_get_inventory(storeapi:storeApi)->None:
    """
 test for getting inventory
 :param" storeapi->storeApi,
 :returns:None
 """
    mylogger.info("test for getting inventory") 
    store = storeapi.get_inventory()
    assert store['delivered'] == 50


def test_place_order(storeapi:storeApi,order:Order)->None:
    """
test for placing new order
 :param: storeapi->storeApi
 :param: order->Order
 :returns:None
 """
    mylogger.info("test for placing new order") 
    order = storeapi.place_order(order)
    assert order._id == 10

def test_get_purchase_by_id(storeapi:storeApi)->None:
    """
 test for finding purchase by id
 :param" storeapi->storeApi
 :returns:None
 """
    mylogger.info("test for finding purchase by id") 
    order = storeapi.get_purchase_by_id(10)
    assert order._id == 10


def test_delete_order_by_id(storeapi:storeApi)->None:
    """
 test for deleting order
 :param" storeapi->storeApi
 :returns:None
 """
    mylogger.info("test for deleting order") 
    order = storeapi.delete_order_by_id(2)
    assert order.status_code == 200


def test_create_user(userapi:userApi,user:User)->None:
 """
 test for create  a usertest for deleting order
 :param" userapi->userApi
 :param" user->User
 :returns:None
 """
 mylogger.info("test for create  a user")
 user = userapi.create_user(user)
 assert user._username == 'vv'

def test_create_users_with_list(userapi:userApi)->None:
 """
 test for creat a users with array
 :param" userapi->userApi
 :returns:None
 """
 mylogger.info("test for creat a users with array")
 users ='[{ "id": 10, "username": "theUser", "firstName": "John", "lastName": "James", "email": "john@email.com", "password": "12345", "phone": "12345",  "userStatus": 1 }, .\
{ "id": 20, "username": "theUser", "firstName": "John", "lastName": "James", "email": "john@email.com", "password": "12345", "phone": "12345",  "userStatus": 1 }]'

 users = userapi.create_users_with_list(users)
 assert users[0]['id'] == 10


def test_login_user(userapi:userApi)->None:
    """
 test for logging in
 :param" userapi->userApi
 :returns:None
 """
    mylogger.info("test for logging in")
    user = userapi.login_user('vv','12345@uU')
    assert user.status_code == 200

def test_log_out(userapi:userApi)->None:
    """
 test for logging out
 :param: userapi->userApi
 :returns:None
 """
    mylogger.info("test for logging out")
    user = userapi.log_out()
    assert user.status_code == 200

def test_get_user_by_name(userapi:userApi)->None:
    """
 test for getting user by name
 :param: userapi->userApi
 :returns:None
 """
    mylogger.info("test for getting user by name")
    user = userapi.get_user_by_name('vv')
    assert user._username == 'vv'

def test_update_user(userapi:userApi,user:User)->None:
    """
 test for updating a user
 :param: userapi->userApi
 :param:user->User
 :returns:None
 """
    mylogger.info("test for updating a user")
    user = userapi.update_user(user,'vv')
    assert user._username == 'vv'

def test_delete_order_by_name(userapi:userApi)->None:
    """
 test for deleting user
 :param: userapi->userApi
 :returns:None
 """
    mylogger.info("test for deleting user by name") 
    res =userapi.delete_order_by_name('vv')
    assert res.status_code== 200
