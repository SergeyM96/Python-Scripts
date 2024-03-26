import requests
import re

def extract_links_and_emails(url):
    """
    Extracts links and email addresses from a webpage.

    Args:
    url (str): The URL of the webpage.

    Returns:
    list: A tuple containing a list of links and a list of email addresses found on the webpage.
    """
    try:
        # Connect to the URL and get the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for any HTTP errors
        html = response.text

        # Use regular expressions to find links and email addresses in the HTML content
        links = re.findall(r'"((http|ftp)s?://.*?)"', html)
        emails = re.findall(r'([\w\.,]+@[\w\.,]+\.\w+)', html)

        return links, emails

    except requests.RequestException as e:
        print("Error connecting to the URL:", e)
        return [], []

if __name__ == "__main__":
    # Prompt the user to enter a URL
    url = input('Enter a URL (include `http://`): ')

    # Extract links and email addresses from the webpage
    links, emails = extract_links_and_emails(url)

    # Print the results
    print("\nFound {} links".format(len(links)))
    for link in links:
        print(link)

    print("\nFound {} email addresses:".format(len(emails)))
    for email in emails:
        print(email)
