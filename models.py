from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')
    total = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Initial product data (completed from original code)
initial_products = [
    {
        "name": "Smart Watch",
        "price": 19999.99,
        "description": "Advanced smartwatch with health tracking",
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        "name": "Headphones",
        "price": 14999.99,
        "description": "Premium wireless headphones",
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    },
    {
        "name": "Camera",
        "price": 59999.99,
        "description": "Professional DSLR camera",
        "category": "Electronics",
        "image_url": "https://images.unsplash.com/photo-1596460107916-430662021049"
    },
    {
        "name": "Designer Watch",
        "price": 24999.99,
        "description": "Luxury wristwatch with premium design",
        "category": "Fashion",
        "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30"
    },
    {
        "name": "Leather Bag",
        "price": 12999.99,
        "description": "Premium leather handbag",
        "category": "Fashion",
        "image_url": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa"
    },
    {
        "name": "Smart Speaker",
        "price": 9999.99,
        "description": "Voice-controlled home assistant",
        "category": "Home",
        "image_url": "https://images.unsplash.com/photo-1512223792601-592a9809eed4"
    },
    {
        "name": "Coffee Maker",
        "price": 7999.99,
        "description": "Premium coffee brewing system",
        "category": "Home",
        "image_url": "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5"
    },
    {
        "name": "Programming Guide",
        "price": 1499.99,
        "description": "Comprehensive coding handbook",
        "category": "Books",
        "image_url": "https://images.unsplash.com/photo-1532012197267-da84d127e765"
    },
    {
        "name": "Novel Collection",
        "price": 2999.99,
        "description": "Bestselling fiction series",
        "category": "Books",
        "image_url": "https://images.unsplash.com/photo-1481627834876-b7833e8f5570"
    },
    {
        "name": "Yoga Mat",
        "price": 1999.99,
        "description": "Professional exercise mat",
        "category": "Sports",
        "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f"
    },
    {
        "name": "Dumbbells Set",
        "price": 4999.99,
        "description": "Adjustable weight training set",
        "category": "Sports",
        "image_url": "https://images.unsplash.com/photo-1586401100295-7a8096fd0a64"
    }
]

# Categories data (from original code)
categories = {
    "Electronics": "https://images.unsplash.com/photo-1468495244123-6c6c332eeece",
    "Fashion": "https://images.unsplash.com/photo-1483985988355-763728e1935b",
    "Home": "https://images.unsplash.com/photo-1484154218962-a197022b5858",
    "Books": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
    "Sports": "https://images.unsplash.com/photo-1517649763962-0c623066013b"
}