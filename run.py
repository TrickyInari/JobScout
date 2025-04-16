from app import create_app  # Importing the app factory function

# Create Flask application instance
app = create_app()

if __name__ == '__main__':
    # Running the application on the specified IP at port 443 (not secure without SSL)
    app.run(host='0.0.0.0', port=443, debug=True)  # For development (not secure)
