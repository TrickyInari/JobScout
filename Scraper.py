import requests
from bs4 import BeautifulSoup
import time
import random
from flask import current_app

def scrape_jobs(job_title):
    job_listings = []

    # Define search URLs for each job site
    sources = {
        "Indeed": f"https://www.indeed.com/jobs?q={job_title.replace(' ', '+')}",
        "LinkedIn": f"https://www.linkedin.com/jobs/search?keywords={job_title.replace(' ', '%20')}",
        "Glassdoor": f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={job_title.replace(' ', '%20')}",
        "ZipRecruiter": f"https://www.ziprecruiter.com/candidate/jobs/search?search={job_title.replace(' ', '%20')}",
        "Monster": f"https://www.monster.com/jobs/search?q={job_title.replace(' ', '+')}"
    }

    # List of User-Agents to rotate
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/605.1.15",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0",
        "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Mobile Safari/537.36"
    ]

    # Loop through each source to scrape job listings
    for site_name, search_url in sources.items():
        headers = {
            "User-Agent": random.choice(user_agents)  # Use a random User-Agent for each request
        }

        # Use requests.Session to maintain state across requests
        session = requests.Session()
        session.headers.update(headers)

        try:
            response = session.get(search_url)
            
            # Check the response status
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Scraping logic for Indeed
                if site_name == "Indeed":
                    job_cards = soup.find_all('div', class_='job_seen_beacon')  # Adjust this selector based on Indeed's HTML structure
                    for card in job_cards:
                        title_elem = card.find('h2', class_='jobTitle')
                        company_elem = card.find('span', class_='companyName')
                        location_elem = card.find('div', class_='companyLocation')
                        link_elem = title_elem.find('a') if title_elem else None
                        
                        if title_elem and link_elem:
                            job_listing = {
                                'site': site_name,
                                'listing_url': "https://www.indeed.com" + link_elem['href'],
                                'title': title_elem.get_text(strip=True),
                                'company': company_elem.get_text(strip=True) if company_elem else "N/A",
                                'location': location_elem.get_text(strip=True) if location_elem else "N/A",
                                'salary': "N/A",  # Placeholder for salary
                                'posting_date': "N/A",  # Placeholder for posting date
                                'experience_level': "N/A",  # Placeholder
                                'industry': "N/A"  # Placeholder
                            }
                            job_listings.append(job_listing)

                # Scraping logic for LinkedIn
                elif site_name == "LinkedIn":
                    job_cards = soup.find_all('li', class_='result-card')  # Adjust this selector based on LinkedIn's HTML structure
                    for card in job_cards:
                        title_elem = card.find('h3', class_='result-card__title')
                        company_elem = card.find('h4', class_='result-card__subtitle')
                        location_elem = card.find('span', class_='job-result-card__location')

                        if title_elem:
                            job_listing = {
                                'site': site_name,
                                'listing_url': card.find('a')['href'],
                                'title': title_elem.get_text(strip=True),
                                'company': company_elem.get_text(strip=True) if company_elem else "N/A",
                                'location': location_elem.get_text(strip=True) if location_elem else "N/A",
                                'salary': "N/A",
                                'posting_date': "N/A",
                                'experience_level': "N/A",
                                'industry': "N/A"
                            }
                            job_listings.append(job_listing)

                # Scraping logic for Glassdoor
                elif site_name == "Glassdoor":
                    job_cards = soup.find_all('li', class_='react-job-listing')  # Adjust this selector based on Glassdoor's HTML
                    for card in job_cards:
                        title_elem = card.find('div', class_='jobHeader')
                        company_elem = card.find('div', class_='companyName')
                        location_elem = card.find('span', class_='loc')

                        if title_elem:
                            job_listing = {
                                'site': site_name,
                                'listing_url': card.find('a')['href'],
                                'title': title_elem.get_text(strip=True),
                                'company': company_elem.get_text(strip=True) if company_elem else "N/A",
                                'location': location_elem.get_text(strip=True) if location_elem else "N/A",
                                'salary': "N/A",
                                'posting_date': "N/A",
                                'experience_level': "N/A",
                                'industry': "N/A"
                            }
                            job_listings.append(job_listing)

                # Scraping logic for ZipRecruiter
                elif site_name == "ZipRecruiter":
                    job_cards = soup.find_all('div', class_='job_details')  # Adjust as per ZipRecruiter's actual structure
                    for card in job_cards:
                        title_elem = card.find('a', class_='job_link')
                        company_elem = card.find('div', class_='job_company')
                        location_elem = card.find('div', class_='job_location')

                        if title_elem:
                            job_listing = {
                                'site': site_name,
                                'listing_url': title_elem['href'],
                                'title': title_elem.get_text(strip=True),
                                'company': company_elem.get_text(strip=True) if company_elem else "N/A",
                                'location': location_elem.get_text(strip=True) if location_elem else "N/A",
                                'salary': "N/A",
                                'posting_date': "N/A",
                                'experience_level': "N/A",
                                'industry': "N/A"
                            }
                            job_listings.append(job_listing)

                # Scraping logic for Monster
                elif site_name == "Monster":
                    job_cards = soup.find_all('section', class_='card-content')  # Adjust according to Monster's HTML structure
                    for card in job_cards:
                        title_elem = card.find('h2', class_='title')
                        company_elem = card.find('div', class_='company')
                        location_elem = card.find('div', class_='location')

                        if title_elem:
                            job_listing = {
                                'site': site_name,
                                'listing_url': card.find('a')['href'],  # Assuming the URL is in the anchor tag
                                'title': title_elem.get_text(strip=True),
                                'company': company_elem.get_text(strip=True) if company_elem else "N/A",
                                'location': location_elem.get_text(strip=True) if location_elem else "N/A",
                                'salary': "N/A",
                                'posting_date': "N/A",
                                'experience_level': "N/A",
                                'industry': "N/A"
                            }
                            job_listings.append(job_listing)
            else:
                current_app.logger.error(f"Failed to retrieve results from {site_name}. Status code: {response.status_code}")

            time.sleep(15)  # Introduce a 15-second delay between requests to avoid being blocked
        except Exception as e:
            current_app.logger.error(f"Error occurred while scraping {site_name}: {str(e)}")  # Log the scraping error

    return job_listings
