from flask_sqlalchemy import SQLAlchemy

# Instantiate the database object
db = SQLAlchemy()

class JobListing(db.Model):
    __tablename__ = 'job_listings'  # The name of the table in the database

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each job listing
    site = db.Column(db.String(255), nullable=False)  # Name of the job site (e.g., Indeed, LinkedIn)
    listing_url = db.Column(db.String(255), nullable=False)  # URL for the job listing
    title = db.Column(db.String(255), nullable=False)  # Job title
    company = db.Column(db.String(100), nullable=False)  # Company name
    location = db.Column(db.String(100), nullable=True)  # Job location (optional)
    salary = db.Column(db.String(50), nullable=True)  # Salary information (optional)
    posting_date = db.Column(db.String(50), nullable=True)  # Posting date (optional)
    experience_level = db.Column(db.String(50), nullable=True)  # Experience level (optional)
    industry = db.Column(db.String(100), nullable=True)  # Industry (optional)

    # Adding a unique constraint on the combination of site and title
    __table_args__ = (db.UniqueConstraint('site', 'title', name='uq_site_title'),)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'
