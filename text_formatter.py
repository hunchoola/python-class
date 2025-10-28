text = "    olamIdE is jEre     "
strip_txt = text.strip()
formated_txt = strip_txt.capitalize()
print(f"{formated_txt}.")


book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
book_info_list = book_info.split(' ; ')

name, book_title, year, isbn, price, total_page = book_info_list

book_title.strip()
price = float(price)
print(price)

formatted_book_info = (
    f"The {book_title} was written by {name.title()} and published in {year} It has {total_page}  pages and {isbn.replace("ISN", "ISBN")} and costs {price}.")

print(formatted_book_info)



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill= 15
elif size == "M":
    bill= 20
elif size == "L":
    bill= 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y":
    bill += 2
    
extra_cheese = input("Do you want extra cheese? Y or N: ")

