import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import check_password_hash


# Here I have created a database schema to store book details(ISBN, Title, Author, Price, Quantity) 
CREATE_BOOKS_TABLE=(
    "CREATE TABLE IF NOT EXISTS books (ISBN INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Price INTEGER, Quantity INTEGER);"
)


# Below are the SQL Query's that I have used to Insert, Retrieve(all or by ISBN), Update, Delete
INSERT_BOOKS_RETURN_ID= "INSERT INTO books (isbn, title, author, price, quantity) VALUES (%s, %s, %s, %s, %s) RETURNING isbn, title, author, price, quantity;"
RETRIEVE_ALL_BOOKS = "SELECT * FROM books;"
RETRIEVE_BOOK_BY_ISBN = "SELECT * FROM books WHERE isbn = %s;"
UPDATE_BOOK_BY_ISBN = "UPDATE books SET title = %s, author = %s, price = %s, quantity = %s WHERE isbn = %s RETURNING isbn, title, author, price, quantity;"
DELETE_BOOK_BY_ISBN = "DELETE FROM books WHERE isbn = %s RETURNING isbn, title, author, price, quantity;"


load_dotenv()


#Below I have configured the flask app
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "super-secret"
app.config["JWT_ALGORITHM"] = "HS256"
jwt = JWTManager(app)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


# Endpoint for user login 
@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Simplified username and password (for testing purposes only)
    if username == "test_user" and password == "test_password":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid username or password"}), 401


# Endpoint to add a new book
@app.post("/api/addBook")
@jwt_required()
def create_book():
    data = request.get_json()
    isbn=int(data["isbn"])
    title=data["title"]
    author=data["author"]
    price =int(data["price"])
    quantity=int(data["quantity"])

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_BOOKS_TABLE)
            cursor.execute(INSERT_BOOKS_RETURN_ID, (isbn, title, author, price, quantity))
            book_info = cursor.fetchone()
    return {
        "ISBN": book_info[0],
        "Title": book_info[1],
        "Author": book_info[2],
        "Price": book_info[3],
        "Quantity": book_info[4]
    }


# Endpoint to delete a book by ISBN
@app.delete("/api/deleteBook/<int:isbn>")
@jwt_required()
def delete_book(isbn):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_BOOK_BY_ISBN, (isbn,))
            deleted_book_info = cursor.fetchone()

    if not deleted_book_info:
        return jsonify({"error": "Book not found"}), 404


    return {
        "ISBN": deleted_book_info[0],
        "Title": deleted_book_info[1],
        "Author": deleted_book_info[2],
        "Price": deleted_book_info[3],
        "Quantity": deleted_book_info[4]
    }


# Endpoint to retrieve all books
@app.get("/api/getAllBooks")
@jwt_required()
def get_all_books():
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_BOOKS_TABLE)
            cursor.execute(RETRIEVE_ALL_BOOKS)
            all_books_info = cursor.fetchall()

    books_list = []
    for book_info in all_books_info:
        books_list.append({
            "ISBN": book_info[0],
            "Title": book_info[1],
            "Author": book_info[2],
            "Price": book_info[3],
            "Quantity": book_info[4]
        })

    return jsonify({"books": books_list})


# Endpoint to retrieve a book by its ISBN
@app.get("/api/getBook/<int:isbn>")
@jwt_required()
def get_book_by_isbn(isbn):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_BOOKS_TABLE)
            cursor.execute(RETRIEVE_BOOK_BY_ISBN, (isbn,))
            book_info = cursor.fetchone()

    if not book_info:
        return jsonify({"error": "Book not found"}), 404

    return {
        "ISBN": book_info[0],
        "Title": book_info[1],
        "Author": book_info[2],
        "Price": book_info[3],
        "Quantity": book_info[4]
    }


# Endpoint for updating a book using ISBN
@app.put("/api/updateBook/<int:isbn>")
@jwt_required()
def update_book(isbn):
    data = request.get_json()
    title = data["title"]
    author = data["author"]
    price = int(data["price"])
    quantity = int(data["quantity"])

    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_BOOKS_TABLE)
            cursor.execute(UPDATE_BOOK_BY_ISBN, (title, author, price, quantity, isbn))
            updated_book_info = cursor.fetchone()

    if not updated_book_info:
        return jsonify({"error": "Book not found"}), 404

    return {
        "ISBN": updated_book_info[0],
        "Title": updated_book_info[1],
        "Author": updated_book_info[2],
        "Price": updated_book_info[3],
        "Quantity": updated_book_info[4]
    }



if __name__ == "__main__":
    app.run(debug=True)