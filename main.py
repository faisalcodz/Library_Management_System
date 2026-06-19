from library import *


while True:

    print("""
==== Library Management System ====

1. Add Book
2. Remove Book
3. Update Book
4. Search Book
5. Issue Book
6. Return Book
7. View All Books
8. View Issued Books
9. Exit

""")

    choice = input("Enter Choice: ")


    if choice == "1":
        add_book()

    elif choice == "2":
        remove_book()

    elif choice == "3":
        update_book()

    elif choice == "4":
        search_book()

    elif choice == "5":
        issue_book()

    elif choice == "6":
        return_book()

    elif choice == "7":
        view_books()

    elif choice == "8":
        view_issued_books()

    elif choice == "9":
        break

    else:
        print("Invalid Choice")