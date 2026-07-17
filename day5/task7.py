class Library:
    def __init__(self):
        self.__books=[]
    def add_book(self,b):
        self.__books.append(b)
    def remove_book(self,b):
        if b in self.__books:
            self.__books.remove(b)
    def show_books(self):
        for b in self.__books:
            print(b)
lib=Library()
lib.add_book('Python')
lib.add_book('Java')
lib.add_book('C++')
lib.show_books()
lib.remove_book('Java')
print('After Removing:')
lib.show_books()
