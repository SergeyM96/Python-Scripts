import requests
from bs4 import BeautifulSoup

"""
 Function to scrape S&P 500 company tickers from Wikipedia
"""
def get_stock_tickers():
    # Make an HTTP request to the Wikipedia page
    url = 'http://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing the company data
    table = soup.find('table', {'class': 'wikitable sortable'})

    # Initialize an empty list to store tickers
    tickers = []

    # Iterate over each row in the table, skipping the header row
    for row in table.findAll('tr')[1:]:
        # Extract columns from the row
        col = row.findAll('td')

        # Check if there are columns present
        if len(col) > 0:
            # Extract the ticker symbol from the first column
            ticker = col[0].text.strip()

            # If there's a hyperlink, extract the ticker from it
            if col[0].find('a'):
                ticker = col[0].find('a').text.strip()

            # Add the ticker to the list
            tickers.append(ticker)

    # Sort the tickers alphabetically
    tickers.sort()

    # Print the number of tickers found
    print("Number of tickers found:", len(tickers))

    # Return the list of tickers
    return tickers


# Function to fetch stock prices for a list of tickers from Alpha Vantage API
def get_stock_prices(tickers):
    # Iterate over each ticker in the list
    for ticker in tickers:
        try:
            # URL for fetching stock prices data from Alpha Vantage API -
            #          Replace YOUR_API_KEY with your actual KEY!!
            url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker}&apikey=YOUR_API_KEY"

            # Make an HTTP GET request to the API
            response = requests.get(url)

            # Parse the JSON response
            data = response.json()

            # Check if price data is available in the response
            if 'Global Quote' in data:
                # Extract the price from the response data
                price = data['Global Quote']['05. price']

                # Print the ticker symbol and its corresponding price
                print(f"{ticker}: {price}")
            else:
                # Print a message if price data is not found
                print(f"Failed to fetch data for {ticker}: Price data not found")
        except Exception as e:
            # Print an error message if fetching data fails
            print(f"Failed to fetch data for {ticker}: {e}")


# Main function to orchestrate the execution flow
def main():
    # Get the list of all S&P 500 tickers
    all_tickers = get_stock_tickers()

    # Fetch and print the stock prices for all tickers
    get_stock_prices(all_tickers)


# Entry point of the script
if __name__ == "__main__":
    # Call the main function to start the execution
    main()
