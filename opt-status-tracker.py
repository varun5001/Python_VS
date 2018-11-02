
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

import requests
from bs4 import BeautifulSoup

url = 'https://egov.uscis.gov/casestatus/mycasestatus.do?appReceiptNum=<case-number>'
page = requests.get(url)
status = page.status_code
print(page.status_code)
soup = BeautifulSoup(page.text, 'html.parser')
soup.find_all('div', class_='rows text-center')
heading = soup.find('div', class_='rows text-center').h1.text
status_text = soup.find('div', class_='rows text-center').p.text
print(heading)
print(status_text)

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}


# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = <sid>
auth_token = <token>
from_ = <from_twilio_number>
to = <to_number>
body = <body_message>
client = Client(account_sid, auth_token, http_client=proxy_client)

message = client.messages.create(
    to,
    body=str(status) + " " + heading + " " + status_text,
    from_=from_

)
print(message.sid)
