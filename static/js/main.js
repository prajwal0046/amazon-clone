// Search functionality
function searchProducts() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = searchInput.value.toLowerCase();
    const products = document.getElementsByClassName('product-card');

    Array.from(products).forEach(product => {
        const title = product.querySelector('.card-title').textContent.toLowerCase();
        const description = product.querySelector('.card-text').textContent.toLowerCase();
        
        if (title.includes(searchTerm) || description.includes(searchTerm)) {
            product.style.display = '';
        } else {
            product.style.display = 'none';
        }
    });
}

// Loading states
function showLoading() {
    const loadingSpinner = document.createElement('div');
    loadingSpinner.className = 'spinner-border text-primary';
    loadingSpinner.setAttribute('role', 'status');
    document.body.appendChild(loadingSpinner);
}

function hideLoading() {
    const spinner = document.querySelector('.spinner-border');
    if (spinner) {
        spinner.remove();
    }
}

// Error handling
function showError(message) {
    const errorAlert = document.createElement('div');
    errorAlert.className = 'alert alert-danger alert-dismissible fade show';
    errorAlert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.insertBefore(errorAlert, document.body.firstChild);
}
