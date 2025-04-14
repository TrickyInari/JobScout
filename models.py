from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class JobListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(100))
    location = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'