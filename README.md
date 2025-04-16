# JobScout

JobScout is a web application that helps users find job opportunities from many popular job boards in one place. Users can enter the job title they want, and JobScout will gather and display listings from sites like Indeed, LinkedIn, Glassdoor, ZipRecruiter, and Monster. By bringing all the results together, JobScout saves users time and effort, making the job search faster and easier.

Disclaimer: This repository uses AI in some places, sorry I'm not that kind of wizard... ¯\_(ツ)_/¯

Your file layout should be as follows. 

jobscout/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── scraper.py
│   ├── models.py
│   ├── templates/
│   │   ├── index.html
│   │   └── layout.html
│   └── static/
│       ├── css/
│       │   └── styles.css  # Your CSS file should be here
│       └── js/              # Any JavaScript files (optional)
│
├── venv/                     # Your virtual environment
├── requirements.txt          # List of dependencies for the project
└── run.py                    # Entry point for running the application
