import json
import requests
import pytest
import logging
from petapi import petApi 
from storeapi import storeApi
from models.pet import Pet
from models.pet import Category
from models.order import Order
from models.user import User
from userapi import userApi


logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


@pytest.fixture
def api() -> petApi:
 url = "https://petstore3.swagger.io/api/v3"
 api = petApi(url)
 return api

@pytest.fixture
def storeapi() -> storeApi:
 url = "https://petstore3.swagger.io/api/v3"
 api = storeApi(url)
 return api

@pytest.fixture
def orderapi() -> petApi:
 url = "https://petstore3.swagger.io/api/v3"
 api = userApi(url)
 return api

@pytest.fixture
def pet() -> Pet:
 pet = Pet(10, 'vv', None, None ,None,None)  
 return pet

@pytest.fixture
def order() -> Order:
 Ord = Order(10, 198772, 7, "2022-08-02T16:07:44.983Z" ,True,"approved")  
 return ord

@pytest.fixture
def user() -> User:
 use = User(10, 'vv', 'vered' ,'aha',"vered@gmail.com",'12345','0525332626',1)  
 return use

def test_update_pet(api,pet):
 mylogger.info("test for updating a pet")
 res = api.update_pet(pet)
 get = api.get_pet_by_id(10)
 assert get._name == 'vv'


def test_post_new_pet(api,pet):
 mylogger.info("test for posting a new pet")
 pet = api.post_new_pet(pet)
 get = api.get_pet_by_id(10)
 assert get._name == 'vv'
 
def test_get_by_status(api):
 mylogger.info("test for getting pets by status")
 pets =  api.get_pet_by_status("available")
 for pet in pets:
  assert   pet._status == "available"

def test_get_by_tags(api):
 mylogger.info("test for getting pets by tags")
 pets =  api.get_pet_by_tags(["name"])
 #for pet in pets:
  #assert pet._tags == "name"

def test_get_pet_by_id(api):
  mylogger.info("test for getting pet by id") 
  pet =  api.get_pet_by_id(10) 
  assert pet._id == 10

def test_update_with_form_data(api, pet):
    mylogger.info("test for updating with form data") 
    pet = api.update_with_form_data(pet,10, 'vv', 'available')
    assert pet._status == 'available'

def test_delete_pet(api):
    mylogger.info("test for deleting pet") 
    api.delete_pet(2)
    pet = api.get_pet_by_id(2)
    assert pet == None


def test_upload_image(api):
    mylogger.info("test for uploading image") 
    image = '/tmp/inflector7440998430605450804.tmp'
    pet = api.upload_image(image,1220)
    assert pet.photo_urls == ["string", "/tmp/inflector7440998430605450804.tmp"]



def test_get_inventory(storeapi):
    mylogger.info("test for getting inventory") 
    store = storeapi.get_inventory()
    assert store == ['approved', 'placed', 'delivered']


def test_place_order(storeapi,order):
    mylogger.info("test for placing new order") 
    order = storeapi.place_order(order)
    assert order["id"] == 10

def test_get_purchase_by_id(storeapi):
    mylogger.info("test for finding purchase by id") 
    order = storeapi.get_purchase_by_id(1)
    assert order._id == 1


def test_delete_order_by_id(storeapi):
    mylogger.info("test for deleting order") 
    storeapi.delete_order_by_id(2)
    pet = storeapi.get_purchase_by_id(2)
    assert pet == None


def test_create_user(userapi,user):
 mylogger.info("test for create  a user")
 user = userapi.create_user(user)
 get = api.get_user_by_id(10)
 assert get._name == 'vv'

def test_create_users_with_array(userapi):
 mylogger.info("test for creat a users with array")
 users=[User(2, 'gigi', 'dana' ,'aha',"gg@gmail.com",'12345','0525332626',1),User(4, 'tt', 'lior' ,'aha',"vered@gmail.com",'12345','0525332626',1) ]
 user = userapi.create_user(users)
 get = api.get_user_by_id(2)
 assert get._username == 'tt'


def test_login_user(userapi):
    mylogger.info("test for logging in")
    user = userapi.login_user('theUser','12345')
    assert user.status_code == 200

def test_log_out(userapi):
    mylogger.info("test for logging out")
    user = userapi.log_out()
    assert user.status_code == 200

def test_get_user_by_name(userapi):
    mylogger.info("test for getting user by name")
    user = userapi.get_user_by_name('vv')
    assert user._username == 'vv'

def test_update_user(userapi,user):
    mylogger.info("test for updating a user")
    res = userapi.update_user(user,'vv')
    get = api.get_user_by_name('vv')
    assert get._mail == 'vered@gmail.com'

def test_delete_user_by_name(userapi):
    mylogger.info("test for deleting user") 
    userapi.delete_user_by_name('theUser')
    user = userapi.get_user_by_name('theUser')
    assert user == None
"""
url = "https://petstore3.swagger.io/api/v3"
api4 = storeApi(url)
Ord = Order(10, 198772, 7, "2022-08-02T16:07:44.983Z" ,True,"approved")  
test_place_order(api4, Ord)"""