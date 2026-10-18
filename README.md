# E-Commerce Backend API

A RESTful E-Commerce Backend API built using Python, Flask, and SQLite to manage users, products, shopping carts, and orders. This project demonstrates backend development concepts, database integration, CRUD operations, and API testing.

## Overview

The E-Commerce Backend API provides the core functionality required for an online shopping application. It allows users to register and log in, manage products, add items to a shopping cart, calculate cart totals, and place orders.

The application uses Flask to handle HTTP requests, Flask-SQLAlchemy for database operations, SQLite for data storage, and Werkzeug for password hashing.

## Features

- **User Management:** Register users and verify login credentials.
- **Product Management:** Create, retrieve, update, and delete products.
- **Shopping Cart:** Add products, view cart items, update quantities, and remove items.
- **Order Processing:** Place orders, calculate order totals, and maintain order history.
- **Stock Validation:** Check product availability before adding items to the cart or placing an order.
- **Database Integration:** Store application data using SQLite and SQLAlchemy.
- **Password Security:** Store hashed passwords instead of plain-text passwords.
- **REST API Testing:** Test endpoints using Thunder Client.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | REST API development |
| SQLite | Database storage |
| Flask-SQLAlchemy | Database ORM |
| Werkzeug | Password hashing and verification |
| Thunder Client | API testing |
| Visual Studio Code | Development environment |

## Project Structure

```text
E-Commerce-Backend/
│
├── E-Commerce Backend.py
├── requirements.txt
├── README.md
└── instance/
    └── ecommerce_backend.db
```

*Note: The database file is created when the application initializes, and its exact location depends on the SQLite configuration. The `instance/` folder is shown as an example.*

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd E-Commerce-Backend
```

Replace `<your-repository-url>` with your GitHub repository URL.

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is not available, install the main dependencies:

```bash
pip install flask flask-sqlalchemy
```

### 4. Run the Application

```bash
python "E-Commerce Backend.py"
```

The local development server will be available at:

`http://127.0.0.1:5000`

Open the URL in a browser to verify that the API is running.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Verify login credentials |

### Product Management

| Method | Endpoint | Description |
|---|---|---|
| GET | `/products` | Retrieve all products |
| POST | `/products` | Add a product |
| PUT | `/products/<product_id>` | Update product details |
| DELETE | `/products/<product_id>` | Delete a product |

### Shopping Cart

| Method | Endpoint | Description |
|---|---|---|
| POST | `/cart` | Add a product to the cart |
| GET | `/cart/<user_id>` | View a user's cart |
| PUT | `/cart/<cart_id>` | Update cart quantity |
| DELETE | `/cart/<cart_id>` | Remove a cart item |

### Orders

| Method | Endpoint | Description |
|---|---|---|
| POST | `/orders` | Place an order |
| GET | `/orders/<user_id>` | Retrieve a user's orders |

## Example API Requests

### Register a User

**POST** `/register`

```json
{
  "name": "Test User",
  "email": "testuser@example.com",
  "password": "your-password"
}
```

### Add a Product

**POST** `/products`

```json
{
  "name": "Laptop",
  "price": 55000,
  "quantity": 10
}
```

### Add a Product to the Cart

**POST** `/cart`

```json
{
  "user_id": 1,
  "product_id": 1,
  "quantity": 2
}
```

Use the actual user and product IDs returned by your API.

### Place an Order

**POST** `/orders`

```json
{
  "user_id": 1
}
```

The order is created from the user's cart, provided the cart contains valid items and sufficient stock is available.

## Database Models

The application uses four SQLAlchemy models:

- **User:** Stores user details and hashed passwords.
- **Product:** Stores product names, prices, and available stock.
- **Cart:** Stores selected products and quantities for each user.
- **Order:** Stores order totals and order status.

## Testing

The API endpoints can be tested using Thunder Client in Visual Studio Code.

Recommended test cases include:

- Registering a new user and testing duplicate email registration.
- Testing valid and invalid login credentials.
- Adding, retrieving, updating, and deleting products.
- Adding products to the cart and checking total amounts.
- Testing invalid product IDs and insufficient stock.
- Placing orders and verifying stock updates.
- Retrieving order history.

## Limitations

- No frontend interface is included.
- Payment gateway integration is not implemented.
- Token-based authentication and complete authorization are not implemented.
- The application is designed as a learning project and requires additional security controls before production use.

## Learning Outcomes

This project provides practical experience with Python backend development, REST APIs, HTTP methods, JSON requests and responses, database operations, CRUD functionality, password hashing, and API testing.

## Author

**Python Backend Development Project**

Developed as a practical project to explore Flask, SQLite, and RESTful API development.

---

*If you find this project useful for learning, feel free to explore the code and extend its functionality.*
