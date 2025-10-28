import random
random_number = random.randint(10000, 99999)

list_of_books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
        "year of publication": 1960, "isbn": "978-0061120084", "available": True},
    {"title": "1984", "author": "George Orwell", "year of publication": 1949,
        "isbn": "978-0451524935", "available": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
        "year of publication": 1813, "isbn": "978-0141439518", "available": True}

]


def borrow_book(isbn):
    for books in list_of_books:
        your_isbn = input("Please enter ISBN :")
        if books['isbn'] == your_isbn:
            if books['available']:
                borrow_opt = input(
                    "book is available for borrow, Do you want to borrow now (Yes/No): ")
                if borrow_opt == "yes":
                    books["available"] = False
                    print(f"Book Borrowd Please show {random_number} at the front desk to collect your book")
                elif borrow_book == "no":
                    break
        else:
                print('Book is not available!!!')

            
    else:
        print("ensure u enter")


borrow_book("isbn")
# your_isbn = input("Please enter ISBN :")
