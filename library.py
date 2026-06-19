from database import get_connection
from logger import write_log
# Add New Book
def add_book():
    conn = None
    try:
        title = input("Enter Book Title: ")
        author = input("Enter Author: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO books(title, author, status)
            VALUES(%s,%s,%s)
            """,
            (title, author, "Available")
        )
        conn.commit()
        write_log(f"Added book: {title}")

        print("Book Added Successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()

def remove_book():
    conn = None
    try:
        book_id = input("Enter Book ID: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM books WHERE id=%s",
            (book_id,)
        )

        conn.commit()

        write_log(f"Removed book id: {book_id}")

        print("Book Removed Successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()




def update_book():
    conn = None
    try:
        book_id = input("Enter Book ID: ")
        title = input("New Title: ")
        author = input("New Author: ")
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE books
            SET title=%s, author=%s
            WHERE id=%s
            """,
            (title, author, book_id)
        )

        conn.commit()

        write_log(f"Updated book id: {book_id}")

        print("Book Updated Successfully")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()


# Issue and Return Book Feature

def search_book():
    conn = None
    try:
        keyword = input("Enter title or author: ")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM books
            WHERE title LIKE %s
            OR author LIKE %s
            """,
            (
                "%" + keyword + "%",
                "%" + keyword + "%"
            )
        )

        books = cursor.fetchall()

        if books:
            for book in books:
                print(book)
        else:
            print("No Book Found")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            conn.close()




def issue_book():
    conn = None
    try:
        book_id = input("Enter Book ID: ")
        user_id = input("Enter User ID: ")

        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO issued_books
            (book_id,user_id,issue_date)
            VALUES(%s,%s,CURDATE())
            """,
            (book_id,user_id)
        )


        cursor.execute(
            """
            UPDATE books
            SET status='Issued'
            WHERE id=%s
            """,
            (book_id,)
        )


        conn.commit()

        write_log(
            f"Book {book_id} issued to user {user_id}"
        )

        print("Book Issued Successfully")


    except Exception as e:
        print("Error:", e)


    finally:
        if conn:
            conn.close()




def return_book():
    conn = None

    try:
        book_id = input("Enter Book ID: ")

        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
            """
            UPDATE books
            SET status='Available'
            WHERE id=%s
            """,
            (book_id,)
        )


        conn.commit()

        write_log(
            f"Book returned: {book_id}"
        )

        print("Book Returned Successfully")


    except Exception as e:
        print("Error:", e)


    finally:
        if conn:
            conn.close()



# View All Books
def view_books():

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM books"
        )


        books = cursor.fetchall()


        for book in books:
            print(book)


    except Exception as e:
        print("Error:", e)


    finally:
        if conn:
            conn.close()




def view_issued_books():

    conn = None

    try:

        conn = get_connection()
        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT
            books.title,
            books.author,
            users.name,
            issued_books.issue_date

            FROM issued_books

            JOIN books
            ON issued_books.book_id = books.id

            JOIN users
            ON issued_books.user_id = users.user_id
            """
        )


        records = cursor.fetchall()


        if records:
            for row in records:
                print(row)
        else:
            print("No Issued Books")


    except Exception as e:
        print("Error:", e)


    finally:
        if conn:
            conn.close()