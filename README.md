<h1>Bookstore Management System</h1>


<h2>Overview:</h2>
<h3>
The Bookstore Management System API is a simple Flask-based web service. It supports operations such as adding, retrieving, updating, and deleting books.The API is secured using JSON Web Tokens (JWT) for user authentication.
</h3>


<h2>Table of Contents:</h2>

    1. Setup
    2. Authentication
    3. Endpoints
        (a)Login
        (b)Add Book
        (c)Delete Book
        (d)Get All Books
        (e)Get Book by ISBN
        (f)Update Book

<h2>Setup: </h2>

    Prerequisites:
        (a)Python 3.6 or later
        (b)PostgreSQL database
        (c)requirements.txt file for installing dependencies
        (d)Flask, Psycopg2, Flask-JWT-Extended, and Dotenv libraries
    
    Authentication:
        To access certain endpoints, you need to authenticate using JWT. 
        Obtain a token by sending a POST request to /api/login with valid credentials.

<h2>Endpoints:</h2>

    Login:
        Endpoint: /api/login
        Method: POST
            Description: Authenticates the user and provides a JWT for accessing protected endpoints.
        
    Add Book:
        Endpoint: /api/addBook
        Method: POST
        Authentication: Required
            Description: Adds a new book to the bookstore inventory.
        
    Delete Book:
        Endpoint: /api/deleteBook/<int:isbn>
        Method: DELETE
        Authentication: Required
          Description: Deletes a book from the bookstore inventory by ISBN.
        
    Get All Books:
        Endpoint: /api/getAllBooks
        Method: GET
        Authentication: Required
          Description: Retrieves details of all books in the bookstore inventory.
        
    Get Book by ISBN:
        Endpoint: /api/getBook/<int:isbn>
        Method: GET
        Authentication: Required
          Description: Retrieves details of a specific book by ISBN.
        
    Update Book:
      Endpoint: /api/updateBook/<int:isbn>
      Method: PUT
      Authentication: Required
        Description: Updates details of a book in the bookstore inventory by ISBN.
      
