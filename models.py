from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Since we're using in-memory storage, we'll create simple class-based models
class User(UserMixin):
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Product:
    def __init__(self, id, name, price, description, category, image_url):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.category = category
        self.image_url = image_url

# In-memory storage
users = {}
products = {
    # Electronics
    1: Product(1, "Smart Watch", 19999.99, "Advanced smartwatch with health tracking", "Electronics", 
               "https://images.unsplash.com/photo-1523275335684-37898b6baf30"),
    2: Product(2, "Headphones", 14999.99, "Premium wireless headphones", "Electronics",
               "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"),
    3: Product(3, "Camera", 59999.99, "Professional DSLR camera", "Electronics",
               "https://images.unsplash.com/photo-1596460107916-430662021049"),

    # Fashion
    4: Product(4, "Designer Watch", 24999.99, "Luxury wristwatch with premium design", "Fashion",
               "https://images.unsplash.com/photo-1523275335684-37898b6baf30"),
    5: Product(5, "Leather Bag", 12999.99, "Premium leather handbag", "Fashion",
               "https://images.unsplash.com/photo-1548036328-c9fa89d128fa"),

    # Home
    6: Product(6, "Smart Speaker", 9999.99, "Voice-controlled home assistant", "Home",
               "https://images.unsplash.com/photo-1512223792601-592a9809eed4"),
    7: Product(7, "Coffee Maker", 7999.99, "Premium coffee brewing system", "Home",
               "https://images.unsplash.com/photo-1517701550927-30cf4ba1dba5"),

    # Books
    8: Product(8, "Programming Guide", 1499.99, "Comprehensive coding handbook", "Books",
               "https://images.unsplash.com/photo-1532012197267-da84d127e765"),
    9: Product(9, "Novel Collection", 2999.99, "Bestselling fiction series", "Books",
               "https://images.unsplash.com/photo-1481627834876-b7833e8f5570"),

    # Sports
    10: Product(10, "Yoga Mat", 1999.99, "Professional exercise mat", "Sports",
                "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f"),
    11: Product(11, "Dumbbells Set", 4999.99, "Adjustable weight training set", "Sports",
                "https://images.unsplash.com/photo-1586401100295-7a8096fd0a64")
}

# Categories with banner images
categories = {
    "Electronics": "https://images.unsplash.com/photo-1468495244123-6c6c332eeece",
    "Fashion": "https://images.unsplash.com/photo-1483985988355-763728e1935b",
    "Home": "https://images.unsplash.com/photo-1484154218962-a197022b5858",
    "Books": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
    "Sports": "https://images.unsplash.com/photo-1517649763962-0c623066013b"
}