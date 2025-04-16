# JobScout

JobScout is a web application that helps users find job opportunities from many popular job boards in one place. Users can enter the job title they want, and JobScout will gather and display listings from sites like Indeed, LinkedIn, Glassdoor, ZipRecruiter, and Monster. By bringing all the results together, JobScout saves users time and effort, making the job search faster and easier.

Disclaimer: This repository uses AI in some places, sorry I'm not that kind of wizard... ¯\_(ツ)_/¯

Your file layout should be as follows. 

**Example "C:/Desktop/Job Scout"**

![image](https://github.com/user-attachments/assets/98c4b17c-b083-4e2a-99d9-36ea06634e16)

jobscout/
├── app/
│   ├── __init__.py           # Flask app factory and configuration
│   ├── routes.py             # All view/routes logic
│   ├── scraper.py            # Web scraping logic for job sites
│   ├── models.py             # SQLAlchemy database models
│   ├── templates/
│   │   ├── layout.html       # Base template
│   │   └── index.html        # Main/search results page
│   └── static/
│       ├── css/
│       │   └── styles.css    # Your CSS styles
│       └── js/
│           └── scripts.js    # Any JavaScript (optional)
├── app/logs/
│   └── app.log               # Logging output (created at runtime)
├── migrations/               # (If using Flask-Migrate/DB migrations)
├── venv/                     # Python virtual environment (not tracked in git)
├── requirements.txt          # All project dependencies
├── run.py                    # Entry point (calls create_app)
└── README.md                 # Project overview and setup instructions
