import os
import logging
from flask import Flask
from flask_login import LoginManager

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

# Initialize Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import routes after app initialization
from routes import *

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)