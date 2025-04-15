import requests
from bs4 import BeautifulSoup

def scrape_jobs(job_title):
    base_url = "https://www.examplejobsite.com"  # Replace with the actual job site
    search_url = f"{base_url}/search?q={job_title.replace(' ', '+')}"
    
    response = requests.get(search_url)
    
    # Check for any errors in the request
    if response.status_code != 200:
        print("Failed to retrieve results")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Adjust this selector based on the actual HTML structure
    job_cards = soup.find_all('div', class_='job-card')  # Modify as necessary

    job_listings = []
    
    for card in job_cards:
        # Extracting elements based on the known HTML structure
        title_elem = card.find('h2', class_='job-title')  # Adjust the class name
        company_elem = card.find('span', class_='company')  # Adjust as necessary
        location_elem = card.find('span', class_='location')  # Adjust as necessary
        salary_elem = card.find('span', class_='salary')  # Adjust for salary if available
        posting_date_elem = card.find('span', class_='posting-date')  # Adjust as necessary
        experience_level_elem = card.find('span', class_='experience-level')  # Adjust for experience level
        industry_elem = card.find('span', class_='industry')  # Adjust for industry
        
        # Extracting the URL (usually from an anchor tag within the job card)
        url_elem = card.find('a', class_='job-link')  # Adjust as necessary for the job link

        if title_elem and url_elem:  # Ensuring we found both title and link
            job_listing = {
                'site': base_url,  # The site from which we're scraping
                'listing_url': base_url + url_elem['href'],  # Construct full URL
                'title': title_elem.get_text(strip=True),  # Job title
                'company': company_elem.get_text(strip=True) if company_elem else "N/A",  # Company name
                'location': location_elem.get_text(strip=True) if location_elem else "N/A",  # Job location
                'salary': salary_elem.get_text(strip=True) if salary_elem else "N/A",  # Salary info
                'posting_date': posting_date_elem.get_text(strip=True) if posting_date_elem else "N/A",  # Posting date
                'experience_level': experience_level_elem.get_text(strip=True) if experience_level_elem else "N/A",  # Experience level
                'industry': industry_elem.get_text(strip=True) if industry_elem else "N/A",  # Industry
            }
            job_listings.append(job_listing)  # Add the job listing to the list

    return job_listings

# Example usage of the function
if __name__ == "__main__":
    job_title = "Software Engineer"  # Change to desired job title
    listings = scrape_jobs(job_title)
    for listing in listings:
        print(listing)
