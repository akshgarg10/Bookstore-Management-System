<h1>Bookstore API Documentation</h1>
<section>
        <h2>Overview</h2>
        <ul>
            <li>The Bookstore Management System API is a simple Flask-based web service.</li>
            <li>It supports operations such as adding, retrieving, updating, and deleting books.</li>
            <li>The API is secured using JSON Web Tokens (JWT) for user authentication.</li>
        </ul>
    </section>
<section>
        <h2>Table of Contents</h2>
        <ol>
            <li><a href="#setup">Setup</a></li>
            <li><a href="#authentication">Authentication</a></li>
            <li><a href="#endpoints">Endpoints</a>
                <ol>
                    <li><a href="#login">Login</a></li>
                    <li><a href="#add-book">Add Book</a></li>
                    <li><a href="#delete-book">Delete Book</a></li>
                    <li><a href="#get-all-books">Get All Books</a></li>
                    <li><a href="#get-book-by-isbn">Get Book by ISBN</a></li>
                    <li><a href="#update-book">Update Book</a></li>
                </ol>
            </li>
        </ol>
    </section>

    <section>
        <h2 id="setup">Setup</h2>
        <ul>
            <li><strong>Prerequisites:</strong></li>
            <ul>
                <li>Python 3.6 or later</li>
                <li>PostgreSQL database</li>
                <li><code>requirements.txt</code> file for installing dependencies</li>
                <li>Flask, Psycopg2, Flask-JWT-Extended, and Dotenv libraries</li>
            </ul>
        </ul>
    </section>

    <section>
        <h2 id="authentication">Authentication</h2>
        <p>To access certain endpoints, you need to authenticate using JWT. Obtain a token by sending a POST
            request to <code>/api/login</code> with valid credentials.</p>
    </section>
