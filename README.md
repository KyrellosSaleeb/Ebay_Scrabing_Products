# Ebay_Scrabing_Products

A Python script to scrape laptop product data from eBay, including product names, prices, shipping information, and subtitles across multiple pages.

## Features

- **Multi-page Scraping**: Automatically follows pagination to collect data from all available pages.
- **Data Collection**: Extracts product names, prices, shipping details, and subtitles.
- **Anti-Detection Measures**: Uses randomized user agents and session management to mimic real browser behavior.
- **Data Export**: Saves collected data into a structured CSV file (`ebay_Data.csv`).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ebay-scraper.git
   cd ebay-scraper
   ```
2. **Install Dependencies:**
   ``` bash
   pip install requests beautifulsoup4 fake-useragent pandas numpy
   ```
## Usage

1. **Run the Script:**
    ```bash
    python scraper.py
    ```
2. **Output:**
      * Data is saved to ebay_Data.csv with the following columns:

        * Product Name: Name of the laptop product.

        * Price: Product price (e.g., "$1,299.99").

        * Shipping Info: Shipping cost or status (e.g., "Free shipping").

        * Subtitle: Additional product details (e.g., condition or specifications).
  ## Dependencies

   * requests: Handles HTTP requests to eBay.

   * beautifulsoup4: Parses HTML content to extract data.

   * fake-useragent: Generates random user agents to avoid detection.

   * pandas & numpy: Manage and export data to CSV.


## Notes

   * Cookies & Headers: The script includes hardcoded cookies and headers. These may need periodic updates if eBay changes its anti-scraping mechanisms.

   * Rate Limiting: Avoid aggressive scraping. Add delays between requests to prevent IP bans.

   * Legal Compliance: Check eBay's robots.txt and terms of service before scraping. Use this script responsibly and for educational purposes only.


## Disclaimer

This script is intended for educational use only. Web scraping may violate eBay's terms of service. The developers are not responsible for misuse or any legal consequences arising from this code. Always obtain permission before scraping a website.
