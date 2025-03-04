from flask import render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from app import app, login_manager
from models import User, users, products, categories

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html', products=products.values(), categories=categories)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = products.get(product_id)
    if product:
        return render_template('product.html', product=product)
    flash('Product not found')
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    cart_data = session.get('cart', {})

    for product_id, quantity in cart_data.items():
        product = products.get(int(product_id))
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
    total = sum(products[int(pid)].price * qty for pid, qty in cart_data.items())
    return render_template('checkout.html', total=total)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = next((u for u in users.values() if u.email == email), None)
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
        if not any(u.email == email for u in users.values()):
            user_id = len(users) + 1
            users[user_id] = User(user_id, username, email, password)
            login_user(users[user_id])
            flash('Registration successful!')
            return redirect(url_for('home'))
        flash('Email already registered')
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))