# E-COMMERCE BACKEND API
## Project Documentation

### 1. Introduction

The E-Commerce Backend API is a Python-based application developed using the Flask framework. It provides backend functionality for an online shopping system, allowing users to register, log in, view products, manage shopping cart items, and place orders.

The application uses SQLite as its database and Flask-SQLAlchemy to interact with database tables. REST APIs allow clients to communicate with the backend by sending HTTP requests and receiving JSON responses.

This project demonstrates the practical implementation of backend development concepts, database management, CRUD operations, request handling, and API testing.

### 2. Project Objectives

The main objectives of this project are:

- To develop a backend system for an e-commerce application.
- To implement user registration and login functionality.
- To create APIs for adding, viewing, updating, and deleting products.
- To provide shopping cart management functionality.
- To calculate the total price of products added to the cart.
- To process customer orders and maintain order details.
- To store and retrieve application data using an SQLite database.
- To understand REST API development and testing using Thunder Client.

### 3. Project Scope

This project focuses on the backend operations required for a basic online shopping application. It manages users, products, shopping carts, and orders through dedicated API endpoints.

The application can be tested using Thunder Client in Visual Studio Code. Users can send HTTP requests with JSON data to perform different operations and view the responses returned by the server.

The current version focuses on backend functionality and does not include a graphical shopping website or an integrated payment gateway.

### 4. Technologies Used

**Python:** Used as the main programming language to implement application logic and backend operations.

**Flask:** A lightweight Python web framework used to create API routes and handle HTTP requests and responses.

**SQLite:** A file-based relational database used to store user, product, cart, and order information.

**Flask-SQLAlchemy:** An Object Relational Mapper (ORM) that allows the application to work with database tables through Python classes and objects.

**Werkzeug:** Used to generate password hashes during registration and verify passwords during login.

**Thunder Client:** A VS Code extension used to send API requests and test the responses.

**Visual Studio Code:** The development environment used to write, execute, and test the application.

### 5. System Modules

#### 5.1 User Registration and Login

The authentication module allows new users to register by providing their name, email address, and password. The application checks whether the required fields are provided and whether the email address is already registered.

Passwords are stored as hashes instead of plain text. During login, the application verifies the entered password against the stored hash and returns an appropriate response.

#### 5.2 Product Management

The product management module handles product-related operations. It allows products to be added with their name, price, and available quantity.

Users can retrieve the list of products, update existing product details, and delete products through the corresponding API endpoints. These operations demonstrate CRUD functionality: Create, Read, Update, and Delete.

#### 5.3 Shopping Cart Management

The cart module allows a user to add products to a shopping cart by specifying the user ID, product ID, and quantity.

The application checks whether the user and product exist and whether sufficient stock is available. Users can view their cart, update quantities, and remove items. The cart response also includes item totals and the overall cart amount.

#### 5.4 Order Processing

The order module processes orders based on the items in a user's shopping cart. It checks whether the cart contains items and whether the requested quantities are available.

The application calculates the order total, reduces the available product stock, creates an order with its status, and clears the cart after successful order processing. Users can retrieve their order history through the order API.

### 6. Database Design

The application uses SQLite with four database models.

**User Table**
- `id`: Unique identifier for each user.
- `name`: Name of the user.
- `email`: User's email address, which must be unique.
- `password`: Hashed user password.

**Product Table**
- `id`: Unique identifier for each product.
- `name`: Product name.
- `price`: Price of the product.
- `quantity`: Available stock.

**Cart Table**
- `id`: Unique identifier for each cart item.
- `user_id`: Identifier of the user who added the item.
- `product_id`: Identifier of the selected product.
- `quantity`: Number of units selected.

**Order Table**
- `id`: Unique identifier for each order.
- `user_id`: Identifier of the user placing the order.
- `total_amount`: Total order amount.
- `status`: Current order status, initially set to "Placed".

The database tables are defined using SQLAlchemy models. The `db.create_all()` method creates the required tables when the application initializes.

### 7. API Endpoints

| HTTP Method | Endpoint | Purpose |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Verify user login details |
| GET | `/products` | Retrieve all products |
| POST | `/products` | Add a new product |
| PUT | `/products/<product_id>` | Update product details |
| DELETE | `/products/<product_id>` | Delete a product |
| POST | `/cart` | Add an item to the cart |
| GET | `/cart/<user_id>` | Retrieve a user's cart |
| PUT | `/cart/<cart_id>` | Update cart quantity |
| DELETE | `/cart/<cart_id>` | Remove a cart item |
| POST | `/orders` | Create an order |
| GET | `/orders/<user_id>` | Retrieve a user's orders |

### 8. Application Workflow

The application follows this general workflow:

1. The Flask application starts and initializes the database tables.
2. A user registers using the registration API.
3. The user logs in using their email and password.
4. Products are added to the database and retrieved through the product APIs.
5. A user adds selected products to the shopping cart.
6. The cart API calculates the total amount based on product prices and quantities.
7. The order API validates stock, calculates the order total, creates the order, updates product stock, and clears the cart.
8. The user retrieves the order details using the order history API.

### 9. Installation and Execution

**Step 1: Install the required packages**

Open the VS Code terminal and execute:

`pip install flask flask-sqlalchemy`

**Step 2: Run the application**

If the Python file is named `E-Commerce Backend.py`, execute:

`python "E-Commerce Backend.py"`

**Step 3: Verify the server**

Open the following URL in a browser:

`http://127.0.0.1:5000`

A JSON message confirms that the backend API is running.

**Step 4: Test the APIs**

Open Thunder Client in VS Code. Select the required HTTP method, enter the endpoint URL, provide JSON data where necessary, and click Send to view the response.

### 10. Testing

The application can be tested using Thunder Client by sending requests to each endpoint.

The following test scenarios should be checked:

- Register a user with valid details.
- Attempt registration with an already registered email.
- Log in with correct and incorrect credentials.
- Add a product and retrieve the product list.
- Update and delete an existing product.
- Add a valid product to the cart.
- Test invalid user IDs, product IDs, and quantities.
- Verify cart totals for different quantities.
- Place an order when stock is available.
- Confirm that stock decreases and the cart is cleared after an order.
- Retrieve order history for a user.

The actual test results should be recorded after running each request in Thunder Client.

### 11. Limitations

- The application does not currently include a graphical frontend.
- Online payment processing is not implemented.
- Login does not issue an authentication token or establish an authenticated session.
- User-specific cart and order endpoints do not fully enforce authorization.
- The application uses a local SQLite database, making it more suitable for learning and demonstration than large-scale deployment.

### 12. Future Enhancements

The project can be improved by adding a responsive frontend, secure token-based authentication, role-based access control, product search and categories, payment gateway integration, order cancellation, and more detailed order tracking.

A production version should also include stronger input validation, improved error handling, database relationship constraints, and appropriate security controls.

### 13. Conclusion

The E-Commerce Backend API provides a practical introduction to building REST APIs using Python and Flask. It demonstrates user registration and login, product management, shopping cart operations, order processing, and database integration using SQLite and Flask-SQLAlchemy.

Through this project, fundamental backend development skills can be practiced, including HTTP methods, JSON communication, CRUD operations, password hashing, database handling, and API testing. The project can serve as a foundation for developing a more complete and secure e-commerce application in the future.
