from app import app, db
from models import Product, User, initial_products

def init_db():
    with app.app_context():
        # Create all tables
        db.create_all()
        
        # Check if we already have products
        if not Product.query.first():
            # Add initial products
            for product_data in initial_products:
                product = Product(**product_data)
                db.session.add(product)
            
            # Create a test user
            if not User.query.filter_by(email='test@example.com').first():
                test_user = User(username='test_user', email='test@example.com')
                test_user.set_password('password123')
                db.session.add(test_user)
            
            db.session.commit()
            print("Database initialized with sample data!")
        else:
            print("Database already contains data!")

if __name__ == "__main__":
    init_db()
