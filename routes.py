from flask import render_template, request
from .scraper import scrape_jobs  # Import the scraping function
from .models import db, JobListing  # Import the database models

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    job_title = request.form.get('job_title')
    job_listings = scrape_jobs(job_title)  # Call the scraper function
    
    # If you're storing into DB, you can uncomment and implement as needed:
    # for job in job_listings:
    #     new_job = JobListing(title=job['title'], company=job['company'], location=job['location'])
    #     db.session.add(new_job)
    # db.session.commit()
    
    return render_template('index.html', job_listings=job_listings)