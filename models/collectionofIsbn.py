class CollectionOfIsbn:
    def __init__(self,isbn:str) -> None:
        """function creates class CollectionOfIsbn
         :returns: None 
         """
        self._isbn = isbn

class AddListOfBooks(CollectionOfIsbn):
    def __init__(self,userId:str,collectionOfIsbns:CollectionOfIsbn) -> None:
        """function creates class AddListOfBooks
         :returns: None 
         """
        self._userId=userId
        self._collectionOfIsbns =collectionOfIsbns

