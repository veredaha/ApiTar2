
class User():
    def __init__(self,id : int, username:str,firstname:str,lastname:str,email:str,password:str,phone :str, userstatus:int) -> None:
        self._id = id	
        self._username = username
        self._firstName = firstname
        self._lastName	= lastname
        self._email	=email
        self._password	= password 
        self._phone	= phone
        self._userStatus = userstatus

    def toJson(self) -> str:
        result = {}
        for key, val  in self.__dict__.items():
            if val is not None:
                if key.startswith("_"):
                    result[key[1:]] = val
                else:
                    result[key] = val
        return result