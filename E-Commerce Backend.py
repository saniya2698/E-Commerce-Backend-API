from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce_backend.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# =========================
# DATABASE MODELS
# =========================

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Placed")


# =========================
# CREATE DATABASE
# =========================

with app.app_context():
    db.create_all()


# =========================
# AUTHENTICATION
# =========================

@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already registered"
        }), 400

    hashed_password = generate_password_hash(password)

    user = User(
        name=name,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully",
        "user_id": user.id
    }), 201


@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    if not check_password_hash(user.password, password):
        return jsonify({
            "message": "Invalid email or password"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user.id,
        "name": user.name
    })


# =========================
# PRODUCT MANAGEMENT
# =========================

@app.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()

    product_list = []

    for product in products:
        product_list.append({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        })

    return jsonify(product_list)


@app.route("/products", methods=["POST"])
def add_product():

    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    if not name or price is None or quantity is None:
        return jsonify({
            "message": "All fields are required"
        }), 400

    product = Product(
        name=name,
        price=price,
        quantity=quantity
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully",
        "product_id": product.id
    }), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.get_json()

    if "name" in data:
        product.name = data["name"]

    if "price" in data:
        product.price = data["price"]

    if "quantity" in data:
        product.quantity = data["quantity"]

    db.session.commit()

    return jsonify({
        "message": "Product updated successfully"
    })


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"
    })


# =========================
# CART MANAGEMENT
# =========================

@app.route("/cart", methods=["POST"])
def add_to_cart():

    data = request.get_json()

    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not user_id or not product_id or not quantity:
        return jsonify({
            "message": "All fields are required"
        }), 400

    user = User.query.get(user_id)
    product = Product.query.get(product_id)

    if not user:
        return jsonify({
            "message": "User not found"
        }), 404

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    if quantity > product.quantity:
        return jsonify({
            "message": "Not enough product stock"
        }), 400

    cart_item = Cart.query.filter_by(
        user_id=user_id,
        product_id=product_id
    ).first()

    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(
            user_id=user_id,
            product_id=product_id,
            quantity=quantity
        )

        db.session.add(cart_item)

    db.session.commit()

    return jsonify({
        "message": "Product added to cart"
    })


@app.route("/cart/<int:user_id>", methods=["GET"])
def get_cart(user_id):

    cart_items = Cart.query.filter_by(user_id=user_id).all()

    cart = []
    total = 0

    for item in cart_items:

        product = Product.query.get(item.product_id)

        if product:
            item_total = product.price * item.quantity
            total += item_total

            cart.append({
                "cart_id": item.id,
                "product_id": product.id,
                "product_name": product.name,
                "price": product.price,
                "quantity": item.quantity,
                "item_total": item_total
            })

    return jsonify({
        "items": cart,
        "total_amount": total
    })


@app.route("/cart/<int:cart_id>", methods=["PUT"])
def update_cart(cart_id):

    cart_item = Cart.query.get(cart_id)

    if not cart_item:
        return jsonify({
            "message": "Cart item not found"
        }), 404

    data = request.get_json()
    quantity = data.get("quantity")

    if not quantity or quantity <= 0:
        return jsonify({
            "message": "Invalid quantity"
        }), 400

    product = Product.query.get(cart_item.product_id)

    if quantity > product.quantity:
        return jsonify({
            "message": "Not enough product stock"
        }), 400

    cart_item.quantity = quantity

    db.session.commit()

    return jsonify({
        "message": "Cart updated successfully"
    })


@app.route("/cart/<int:cart_id>", methods=["DELETE"])
def remove_from_cart(cart_id):

    cart_item = Cart.query.get(cart_id)

    if not cart_item:
        return jsonify({
            "message": "Cart item not found"
        }), 404

    db.session.delete(cart_item)
    db.session.commit()

    return jsonify({
        "message": "Product removed from cart"
    })


# =========================
# ORDER PROCESSING
# =========================

@app.route("/orders", methods=["POST"])
def create_order():

    data = request.get_json()

    user_id = data.get("user_id")

    if not user_id:
        return jsonify({
            "message": "User ID is required"
        }), 400

    cart_items = Cart.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return jsonify({
            "message": "Cart is empty"
        }), 400

    total_amount = 0

    for item in cart_items:

        product = Product.query.get(item.product_id)

        if not product:
            return jsonify({
                "message": "Product not found"
            }), 404

        if item.quantity > product.quantity:
            return jsonify({
                "message": f"Not enough stock for {product.name}"
            }), 400

        total_amount += product.price * item.quantity

    # Reduce product stock
    for item in cart_items:

        product = Product.query.get(item.product_id)

        product.quantity -= item.quantity

    # Create order
    order = Order(
        user_id=user_id,
        total_amount=total_amount,
        status="Placed"
    )

    db.session.add(order)

    # Clear cart
    for item in cart_items:
        db.session.delete(item)

    db.session.commit()

    return jsonify({
        "message": "Order placed successfully",
        "order_id": order.id,
        "total_amount": total_amount,
        "status": order.status
    }), 201


@app.route("/orders/<int:user_id>", methods=["GET"])
def get_orders(user_id):

    orders = Order.query.filter_by(user_id=user_id).all()

    order_list = []

    for order in orders:

        order_list.append({
            "order_id": order.id,
            "total_amount": order.total_amount,
            "status": order.status
        })

    return jsonify(order_list)


# =========================
# HOME
# =========================

@app.route("/")
def home():

    return jsonify({
        "message": "E-Commerce Backend API is running"
    })


# =========================
# RUN APPLICATION
# =========================

if __name__ == "__main__":
    app.run(debug=True)