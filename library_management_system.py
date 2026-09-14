#library_management_system
import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

class Book:
    def __init__(self,title , author , year , status = True):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
class Library:
    def __init__(self):
        pass
    def addBook(self , book):
        query = "INSERT INTO books (title , author , year , status) VALUES (? , ? , ? , ?)"
        parametr = (book.title , book.author , book.year , book.status)
        cursor.execute(query , parametr)
        connection.commit()
        print("added")
    def showBooks(self):
        query = "SELECT * FROM books"
        cursor.execute(query)
        result = cursor.fetchall()
        if not result:
            print("there is not any book")
        else:
            for row in result:
                print(row)
        
    def search(self , title):
        query = "SELECT * FROM books WHERE title = ?"
        cursor.execute(query , (title,))
        result = cursor.fetchall()
        if not result:
            print("not found anything")
        else:
            for row in result:
                print(row)
    def edit(self):
        title = input("enter the title of the book you want to edit: ")
        author = input("enter the author of the book you want to edit: ")
        query = "SELECT * FROM books WHERE title = ? AND author = ?"
        cursor.execute(query, (title, author))
        result = cursor.fetchone()
        if not result:
            print("there is not this book")
            return

        new_title = input("enter the new title: ")
        new_author = input("enter the new author: ")
        new_year = input("enter the new year: ")

        update_query = "UPDATE books SET title = ?, author = ?, year = ? WHERE title = ? AND author = ?"
        parameters = (new_title, new_author, new_year, title, author)
        cursor.execute(update_query, parameters)
        connection.commit()
        print("book updated successfully")
        
    def delete(self , title , author):
        query = "DELETE FROM books WHERE title = ? AND author = ?"
        parametrs = (title , author)
        cursor.execute(query , parametrs)
        result = cursor.fetchone()
        if not result:
            print("there is not this book")
        else:
            connection.commit()
            print("deleted")
    def barrow(self, title, author):
        query = """
            UPDATE books
            SET status = ?
            WHERE title = ? AND author = ? AND status = ?
        """
        parameters = (False, title, author, True)
        cursor.execute(query, parameters)

        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT status FROM books WHERE title = ? AND author = ?",
                (title, author)
            )
            book = cursor.fetchone()

            if book is None:
                print("the book not found")
            else:
                print("the book is already borrowed")
        else:
            connection.commit()
            print("the book was successfully borrowed.")

    def Return(self, title, author):
        query = """
            UPDATE books
            SET status = ?
            WHERE title = ? AND author = ? AND status = ?
        """
        parameters = (True, title, author, False)
        cursor.execute(query, parameters)

        if cursor.rowcount == 0:
            cursor.execute(
                "SELECT status FROM books WHERE title = ? AND author = ?",
                (title, author)
            )
            book = cursor.fetchone()

            if book is None:
                print("the book not found")
            else:
                print("the book is already returned")
        else:
            connection.commit()
            print("the book was successfully returned")


cursor.close()
connection.close()       
