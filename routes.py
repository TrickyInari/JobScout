from flask import render_template, request, Blueprint, current_app
from app.scraper import scrape_jobs  # Import the scraping function
from app.models import db, JobListing  # Import the database models

# Initialize the Blueprint
main = Blueprint('main', __name__)

# Home page route, which also handles search functionality
@main.route('/', methods=['GET', 'POST'])
def index():
    current_app.logger.info("Index route accessed.")  # Log access to the index route
    
    if request.method == 'POST':
        job_title = request.form.get('job_title')
        current_app.logger.info(f'Search initiated for job title: {job_title}')

        if not job_title:
            current_app.logger.warning("No job title provided for search.")
            return render_template('index.html', job_listings=[], error="Please enter a job title.")

        try:
            # Call the scraper to get job listings
            job_listings = scrape_jobs(job_title)

            # Log the number of job listings found
            current_app.logger.info(f'Found {len(job_listings)} job listings for title: {job_title}')

            # Store job listings in the database
            for job in job_listings:
                new_job = JobListing(
                    site=job['site'],
                    listing_url=job['listing_url'],
                    title=job['title'],
                    company=job['company'],
                    location=job['location'],
                    salary=job['salary'],
                    posting_date=job['posting_date'],
                    experience_level=job['experience_level'],
                    industry=job['industry']
                )

                # Check if the job already exists in the database
                existing_job = JobListing.query.filter_by(site=new_job.site, title=new_job.title).first()
                if existing_job is None:
                    db.session.add(new_job)
                else:
                    current_app.logger.info(f'Job listing for {new_job.title} at {new_job.site} already exists. Skipping addition.')

            # Commit the transaction to save to the database
            db.session.commit()
            current_app.logger.info(f'Saved {len(job_listings)} job listings to the database.')

        except Exception as e:
            current_app.logger.error(f'Error occurred during job search or saving: {str(e)}')  # Log the error
            return render_template('index.html', job_listings=[], error="An error occurred during search.")

    # Default render for GET requests
    return render_template('index.html', job_listings=[])  # Render the index page with an empty job list
