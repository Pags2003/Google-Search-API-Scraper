import requests
import pandas as pd
import json
from datetime import date, timedelta

title_list = []

keyword_input = input("Enter Keyword: ")
site_list = ["quora.com"]
for site in site_list:
  keyword = keyword_input + " site:" + site
  google_url = "https://customsearch.googleapis.com/customsearch/v1?key=&cx=" #Enter API Key and CX Value
  google_url = google_url + "&q=" + keyword

  response = requests.get(google_url)

  json_response = json.loads(response.text)
  total_results = json_response["searchInformation"]["totalResults"]

  next_index = json_response["queries"]["nextPage"][0]["startIndex"]

  total_pages = round(int(total_results) / 10)
  print(total_pages)
  try:
    for item in json_response["items"]:
      title = item["title"]
      title_list.append(title)
  except Exception as e:
    print("Exception",e)

print("Collected Titles")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

lists = ""
for ttl in title_list:
  string = "<li>" + ttl +"</li>"
  lists += string
email_content = "<ol>" + lists + "</ol>"
sender_address = 'chennaipratham2003@gmail.com'
sender_password = '' #Enter appPassword
receiver_address = input("Enter Receiver mail :")
message = MIMEMultipart()
message["FROM"] = "Pratham Golhani <chennaipratham2003@gmail.com>"
message["TO"] = receiver_address
message["Subject"] = "List of top 10 search result in quora related to " + keyword_input
message.attach(MIMEText(email_content,"html"))

session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login(sender_address, sender_password)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print("Mail sent to "+receiver_address)

print("Process Complete")
