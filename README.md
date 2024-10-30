# Hyderabad GitHub Users and Repositories Analysis

- **Data Scraping**: The data was scraped using the GitHub API to fetch users from Hyderabad with over 50 followers and their recent repositories.
- **Interesting Observation**: A large percentage of users with many followers are actively contributing to open-source projects in Python and JavaScript.
- **Recommendation**: Hyderabad-based developers could focus on Python and JavaScript to increase visibility and collaboration opportunities.

## Project Description

This project collects data from GitHub on users located in Hyderabad who have more than 50 followers. It fetches information on each user's profile and repositories and saves the data to `users.csv` and `repositories.csv` files.

## How to Run the Script

1. Clone this repository.
2. Set up your virtual environment and install dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # or .\env\Scripts\activate on Windows
   pip install -r requirements.txt
