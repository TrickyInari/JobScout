import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate the database object
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load configuration from environment variables or default values
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///jobs.db')  # Update for production
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_default_secret_key')  # Ensure secure sessions

    # Initialize the database with the Flask app instance
    db.init_app(app)

    # Set up logging
    setup_logging(app)

    # Create all database tables within the app context
    with app.app_context():
        db.create_all()

    # Import and register your blueprints from routes.py
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

def setup_logging(app):
    """Sets up logging for the Flask application."""
    log_dir = 'app/logs'
    
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)  # Create the logs directory if it doesn't exist

    log_file = os.path.join(log_dir, 'app.log')  # Specify the log file path
    # Configure the RotatingFileHandler
    handler = RotatingFileHandler(log_file, maxBytes=1000000, backupCount=1)
    handler.setLevel(logging.INFO)  # Set the log level for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the file handler to the app's logger
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)  # Set the application's logger level to INFO

    # Optional: also log to standard output (useful for development and debugging)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    app.logger.addHandler(stream_handler)

# Optionally, you might define other package-level functions or classes here
