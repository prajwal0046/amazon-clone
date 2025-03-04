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
    1: Product(1, "Smart Watch", 19999.99, "Advanced smartwatch with health tracking", "Electronics", 
               "https://images.unsplash.com/photo-1523275335684-37898b6baf30"),
    2: Product(2, "Headphones", 14999.99, "Premium wireless headphones", "Electronics",
               "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"),
    3: Product(3, "Camera", 59999.99, "Professional DSLR camera", "Electronics",
               "https://images.unsplash.com/photo-1596460107916-430662021049"),
    4: Product(4, "Smartphone", 69999.99, "Latest smartphone model", "Electronics",
               "https://images.unsplash.com/photo-1615615228002-890bb61cac6e"),
    5: Product(5, "Laptop", 99999.99, "High-performance laptop", "Electronics",
               "https://images.unsplash.com/photo-1616423641454-caa695af6a0f"),
}

# Categories with banner images
categories = {
    "Electronics": "https://images.unsplash.com/photo-1468495244123-6c6c332eeece",
    "Fashion": "https://images.unsplash.com/photo-1483985988355-763728e1935b",
    "Home": "https://images.unsplash.com/photo-1484154218962-a197022b5858",
    "Books": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f",
    "Sports": "https://images.unsplash.com/photo-1517649763962-0c623066013b"
}