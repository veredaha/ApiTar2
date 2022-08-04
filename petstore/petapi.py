
from models.pet import Pet
from models.pet import Status



import json
import requests



class petApi():

    def __init__(self, url:str, headers:str)-> None:
        self.url = url
        self.headrs = headers
        self.session = requests.session()
        self.session.headers.update(self.headrs)

    def update_pet(self,pet:Pet):
        """ update pet
     :returns: pet
     """
        my_pet = pet.toJson()
        res = requests.put(url=f"{self.url}/pet", json=my_pet)
        if res.status_code == 200:
            return my_pet
        else:
            return None
        
    def post_new_pet(self,pet )->Pet:
        """ get new pet
     :returns: pet
     """
        pet_data = pet.toJson()
        res = self.session.post(url=f"{self.url}/pet", data=pet_data)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

    def get_pet_by_status(self, status) -> list:
        """ get pet by status
     :returns: pet
     """
        res = self.session.get(url=f"{self.url}/pet/findByStatus?status={Status[status].value}")
        pets = res.json()
        result = [] 
        if res.status_code == 200:
         for a in pets:
            pet = res.json()
            pet = Pet(**a)
            result.append(pet)
         return result 
        else:
            return None
    
    def get_pet_by_tags(self, tags) -> list:
        """ get pet by tags
     :returns: pet
     """
        res = self.session.get(url=f"{self.url}/pet/findByTags?tags={tags}")
        pets = res.json()
        result = [] 
        if res.status_code == 200:
         for a in pets:
            pet = Pet(**a)
            result.append(pet)
         return result 
        else:
            return None

    def get_pet_by_id(self,pet_id : int)->Pet:
        """ get pet
     :returns: pet
     """
        res = self.session.get(url=f"{self.url}/pet/{pet_id}")
        if res.status_code == 200:
            pet = res.json()
            my_pet = Pet(**pet)
            return my_pet  
        else:
            return None


    def update_with_form_data(self ,pet:Pet,petid:int, petname:str, petstatus:str)->Pet:
        """ update pet
     :returns: pet
     """
        pet_data = pet.toJson()
        res = self.session.post(url=f"{self.url}/pet/{petid}?name={petname}&status={petstatus}", data=pet_data)
        if res.status_code == 200:
            pet = res.json()
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

    def delete_pet(self,petid:int)->Pet:
        """ delete pet
     :returns: pet
     """
        res = self.session.delete(url=f"{self.url}/pet/{petid}")
        return res.status_code
            
    def upload_image(self,image:str,petid:int):
        """ upload image
     :returns: pet
     """
        res = self.session.post(url=f"{self.url}/pet/{petid}/uploadImage", data=image)
        pet = res.json()
        if res.status_code == 200:
            my_pet = Pet(**pet)
            return my_pet
        else:
            return None

"""
url = "https://petstore3.swagger.io/api/v3"
api7 = petApi(url)
pet = Pet(10, 'vv', None, None ,None,None)  
image = '/tmp/inflector7440998430605450804.tmp'
r = api7.upload_image(image,10)
print(r)"""
