from art import text2art

import random
random_number = random.randint(10000, 99999)

art = text2art("LIBRARY SYSTEM")
print(art)
# ************************** LIBRARY ************************
list_of_books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee",
        "year of publication": 1960, "isbn": "978-0061120084", "available": True},
    {"title": "1984", "author": "George Orwell", "year of publication": 1949,
        "isbn": "978-0451524935", "available": False},
    {"title": "Pride and Prejudice", "author": "Jane Austen",
        "year of publication": 1813, "isbn": "978-0141439518", "available": True},
    {"title": "Naija Agile", "author": "Arikeuyo Akeem",
        "year of publication": 2025, "isbn": "000-012345", "available": True}

]


def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    year_of_publish = int(input("Enter Year of Publication: "))
    isbn = input("Enter ISBN: ")
    is_available = bool(int(input('Availability 1. true 0. false: ')))
    new_book_data = {
        "title": title,
        "author": author,
        "year of publication": year_of_publish,
        "isbn": isbn,
        "available": is_available
    }

    list_of_books.append(new_book_data)
    print(f"{title} Added!")


def view_books():
    print("**************************************")
    print("Title\t\t\t|Author\t\t|Year of Publication\t|ISBN\t\t|Available")
    for list in list_of_books:
        print(f"{list['title']}\t\t\t|{list['author']}\t\t|{list['year of publication']}\t|{list['isbn']}\t\t|{list['available']}")


def update_book(isbn):
    for list in list_of_books:
        if list['isbn'] == your_isbn:
            title = input("Enter new title: ")
            author = input("Enter New Author Name: ")
            year_of_publish = int(input("Update The Publication Year: "))
            isbn = input("Enter New ISBN: ")
            is_available = bool(int(input('Availability 1. true 0. false: ')))
            list["title"] = title
            list["author"] = author
            list["year of publication"] = year_of_publish
            list["isbn"] = isbn
            list["available"] = is_available
            print("Update!!!")
            break
    else:
        print("Book not found! Kindly check ensure you type the correct ISBN")


def delete_book(isbn):
    for i in range(len(list_of_books)):
        if list_of_books[i]['isbn'] == your_isbn:
            del list_of_books[i]
            print("Book Deleted")
            return
    else:
        print("Book not found! Kindly check ensure you type the correct ISBN")


def search_book(title):
    print("**************************************")
    print("Title\t\t\t|Author\t\t|Year of Publication\t|ISBN\t\t|Available")
    for book in list_of_books:
        if title.lower() == book["title"].lower():
            print(
                f"{book['title']}\t\t\t|{book['author']}\t\t|{book['year of publication']}\t|{book['isbn']}\t\t|{book['available']}")
            break
    else:
        print("Book not found! Kindly check ensure you type the correct title")


def borrow_book(isbn):
    for books in list_of_books:
        if not books["available"]:
            print("Book is not available!!!")
            return
        borrow_opt = input(
            "book is available for borrow, Do you want to borrow now (Yes/No): ")
        if borrow_opt == "yes":
            books["available"] = False
            print(
                f"Book Borrowd Please show {random_number} at the front desk to collect your book")
            break
        elif borrow_opt == "no":
            print("Borrowed Cancled")
            break
        else:
            print('Invalid input. Please enter Yes or No')
            return

    else:
        print("Book not found! Kindly check ensure you type the correct title")


def return_book(isbn):
    for books in list_of_books:
        if books['isbn'] == your_isbn:
            if books["available"]:
                print("Book is already returned")
                return

            borrow_opt = input("Do you want to return book now (Yes/No): ")
            if borrow_opt == "yes":
                books["available"] = True
                print(f"Book Returned Thank you!")
                break
            elif borrow_opt == "no":
                print('Returned Cancelled')
                break
            else:
                print('invalid input. Please enter yes or no')
                break

        else:
            print("Book not found! Kindly check ensure you type the correct title")


def exit_program():
    print("Exiting the program...")
    exit()


while True:
    option = input("""
                    1. Add Book         2. View Book
                    3. Update Book      4. Delete Book
                    5. Search Book      6. Borrow Book
                    7. Return Book      8. Exit
                    """)
    if option == "1":
        add_book()
    elif option == "2":
        view_books()
    elif option == "3":
        your_isbn = input("Please enter ISBN :")
        update_book("your_isbn")
    elif option == "4":
        your_isbn = input("Please enter ISBN :")
        delete_book("isbn")
    elif option == "5":
        t_name = input("Please enter name :")
        search_book(t_name)
    elif option == "6":
        your_isbn = input("Please enter ISBN :")
        borrow_book("isbn")
    elif option == "7":
        your_isbn = input("Please enter ISBN you want to return :")
        return_book("isbn")
    elif option == "8":
        exit_program()
