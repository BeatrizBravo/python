# Define a Class named "Book"

'''
class Book:
    pass
'''
class Book:
    # Define an init method which will be called when an object of this class is created
    # inicializador  __ini__::
    #manda a llamar automaticamente cuando estamos instanciado un objeto
    def __init__(self, title, author, year):
        # EL PARAMETRO SELF
        # Set the properties of the book object
        self.title = title
        self.author = author
        self.year = year

    # Define methods to get and print the properties of the book object
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def print_book(self):
        print('Title:', self.title)
        print('Author:', self.author)
        print('Year:', self.year)


# Create an instance of the Book class
book = Book('Python for Beginners', 'John Smith', 2021)

# Call the print_book() method to print the properties of the book object
book.print_book()
