// Cart functionality
function updateCart() {
    const cartCount = document.getElementById('cart-count');
    const cartItems = JSON.parse(sessionStorage.getItem('cart')) || {};
    const itemCount = Object.values(cartItems).reduce((a, b) => a + b, 0);
    cartCount.textContent = itemCount;
}

function toggleCart() {
    const cartOverlay = document.getElementById('cart-overlay');
    cartOverlay.style.display = cartOverlay.style.display === 'none' ? 'block' : 'none';
}

function addToCart(productId) {
    let cart = JSON.parse(sessionStorage.getItem('cart')) || {};
    cart[productId] = (cart[productId] || 0) + 1;
    sessionStorage.setItem('cart', JSON.stringify(cart));
    updateCart();
    
    // Show confirmation message
    const toast = document.createElement('div');
    toast.className = 'alert alert-success position-fixed bottom-0 end-0 m-3';
    toast.textContent = 'Product added to cart!';
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 2000);
}

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', updateCart);
