class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")
            

book1 = Book("Diary of a wimpy kid", "John doe")
book2 = Book("1984", "George Orwell")
book3 = Book("Amulet", "Harper Lee")

book1.borrow()
book1.return_book()

book2.borrow()
book2.return_book()

book3.borrow()
book3.return_book()
