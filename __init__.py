from flask import Flask
from .models import db  # Import db

def create_app():
    app = Flask(__name__)
    
    # Configure the database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Use your desired database
    db.init_app(app)  # Initialize the SQLAlchemy object

    with app.app_context():
        db.create_all()  # Create tables if needed
        
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app