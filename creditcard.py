Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... import csv
... from bs4 import BeautifulSoup
... 
... # Send a GET request to the webpage
... url = "https://www.hdfcbank.com/personal/pay/cards/credit-cards"
... response = requests.get(url)
... 
... # Create BeautifulSoup object to parse the HTML content
... soup = BeautifulSoup(response.content, "html.parser")
... 
... # Find the container that holds the credit card details
... cards_container = soup.find("div", class_="product-listing-grid")
... 
... # Create a CSV file to store the scraped data
... csv_filename = "credit_cards_data.csv"
... csv_file = open(csv_filename, "w", newline="", encoding="utf-8")
... writer = csv.writer(csv_file)
... 
... # Write the header row in the CSV file
... header = ["Card Name", "Card Fee", "Reward Points/Percentage per 100 spent", "Lounge Access", "Milestone Benefit", "Card Fee Reversal Condition"]
... writer.writerow(header)
... 
... # Extract details for each credit card
... cards = cards_container.find_all("div", class_="list-item")
... for card in cards:
...     card_name = card.find("h3", class_="product-title").text.strip()
...     card_fee = card.find("span", class_="joining-fee").text.strip()
...     reward_points = card.find("span", class_="reward-points").text.strip()
...     lounge_access = card.find("span", class_="lounge-access").text.strip()
...     milestone_benefit = card.find("span", class_="milestone-benefit").text.strip()
...     fee_reversal_condition = card.find("span", class_="fee-reversal-condition").text.strip()
...     
...     # Write the card details into the CSV file
    writer.writerow([card_name, card_fee, reward_points, lounge_access, milestone_benefit, fee_reversal_condition])

# Close the CSV file
csv_file.close()

print("Data scraping and CSV export complete. Please check the file:", csv_filename
