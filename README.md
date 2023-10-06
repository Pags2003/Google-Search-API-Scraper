
# Google Search API Scraper

This Python script allows you to perform a Google search for a specific keyword and collect the titles of the top search results from a specified site (in this example, "quora.com"). It then sends an email containing the collected titles to a specified recipient.
## Prerequisites

Before using this script, make sure you have the following:

* Python installed on your system.
* The requests, pandas, and json libraries installed. You can install them using pip:

```bash
pip install requests pandas

```
## Setup

1. You need to obtain a Google Custom Search API Key and a Custom Search Engine (CX) ID. Replace the placeholders (&key= and &cx=) in the google_url variable with your API Key and CX ID.

```bash
  google_url = "https://customsearch.googleapis.com/customsearch/v1?key=YOUR_API_KEY&cx=YOUR_CX_ID"

```
2. Provide your Gmail sender address and password (or an app password if you have 2-factor authentication enabled) in the following lines:

```bash
sender_address = 'YOUR_EMAIL_ADDRESS'
sender_password = 'YOUR_SENDER_PASSWORD'

```
## Usage

1. Run the script.

```bash
  python app.py
```

2. Enter the keyword you want to search for when prompted.

3. Enter the recipient's email address when prompted.
## Notes

* The script performs a Google search for the specified keyword on the site "quora.com" by default. You can modify the site_list variable to search on different sites.

* The script collects the titles of the top search results and sends them in an HTML email to the specified recipient.

* Make sure you have allowed "Less secure apps" in your Gmail settings if you are using your Gmail account to send emails. It's recommended to use an app password if you have 2-factor authentication enabled.

* Ensure that your API Key and CX ID are kept confidential.

* This script is a basic example and can be extended or customized as per your specific requirements.
