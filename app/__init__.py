from flask import Flask

app = Flask(__name__)

# Import routes after creating the app instance to avoid circular import
from app import routes
