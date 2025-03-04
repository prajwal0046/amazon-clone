from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
import logging
from app import app, login_manager, db
from models import User, Product, Order, OrderItem, categories

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    selected_category = request.args.get('category')
    logging.debug(f"Selected category: {selected_category}")

    if selected_category:
        filtered_products = Product.query.filter_by(category=selected_category).all()
        logging.debug(f"Found {len(filtered_products)} products in category {selected_category}")
    else:
        filtered_products = Product.query.all()
        logging.debug(f"Showing all {len(filtered_products)} products")

    logging.debug(f"Available categories: {list(categories.keys())}")
    return render_template('home.html', products=filtered_products, categories=categories)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    cart_data = session.get('cart', {})

    for product_id, quantity in cart_data.items():
        product = Product.query.get(int(product_id))
        if product:
            cart_items.append({
                'product': product,
                'quantity': quantity
            })
            total += product.price * quantity

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    if str(product_id) not in session.get('cart', {}):
        cart = session.get('cart', {})
        cart[str(product_id)] = 1
        session['cart'] = cart
        flash('Product added to cart!')
    return redirect(request.referrer or url_for('home'))

@app.route('/checkout')
@login_required
def checkout():
    cart_data = session.get('cart', {})
    total = 0
    for pid, qty in cart_data.items():
        product = Product.query.get(int(pid))
        if product:
            total += product.price * qty
    return render_template('checkout.html', total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Successfully logged in!')
            return redirect(url_for('home'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return render_template('register.html')

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Registration successful!')
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))