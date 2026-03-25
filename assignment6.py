class library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available
        
    def check_out(self):
        if self.available:
            self.available = False
            print(f'"{self.book_name} has been checked out."')
        else:
            print(f'" {self.book_name} is currently not availabe."')
            
    def return_book(self):
        self.available = True
        print(f' "{self.book_name}" has been returned and is now available.')
        
    def display_book(self):
        status = "Available." if self.available else "Not Available."
        print(f"Book Name: {self.book_name}, Author: {self.author}, status: {status}")

book1 = library("Python Programming", "Guido van Rossum")
book2 = library("Data structure", "Mark Allen Weiss")

book1.display_book()
book1.check_out()
book1.display_book()

book1.return_book()
book1.display_book()
