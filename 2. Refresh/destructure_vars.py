class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
    def __str__(self):
        return 'Whassup'
    
    def __repr__(self):
        return f'Person{self.name}, {self.age}'

    @classmethod
    def class_method(cls):
        print(f'called class method of {cls}')
        
me = Person('Tad', 30
)
print(me)

Person.class_method()

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'Book {self.name}, {self.book_type}, weighing {self.weight}'

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

book = Book('Harry Potter', 'Fantasy', '4')

print(book)
newbook = Book.hardcover('Harry Potter', 2000)
print(newbook)