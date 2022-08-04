class UserBooksResult: 
 def __init__(self, userId:str, isbn:str, message:str) -> None:
    self._userId =userId	  
    self._isbn = isbn
    self._message = message

class MessageModal:
    def __init__(self,code:int, message:str) -> None:
       self._code = code
       self._message = message

class ReplaceIsbn:
    def __init__(self, userId:str, isbn:str) -> None:
       self._userId =userId	  
       self._isbn = isbn

class BooksResult:
    def __init__(self,userId:str, message:str) -> None:
       self._userId =userId	
       self._message = message


class StringObject:
    def __init__(self, isbn:str, userId:str) -> None:
       self._isbn = isbn
       self._userId =userId	 