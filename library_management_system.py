#library_management_system
import sqlite3

connection = sqlite3.connect("books.db")
cursor = connection.cursor()

class Book:
    def __init__(self,title , author , year , status = bool):
        self.title = title
        self.author = author
        self.year = year
        self.status = status
class Library:
    def __init__(self):
        pass
    def addBook(self , book):
        quary = "INSERT INTO books (title , author , year , status) VALUES (? , ? , ? , ?)"
        parametr = (book.title , book.author , book.year , book.status)
        cursor.execute(quary , parametr)
        connection.commit()


    
        
        

