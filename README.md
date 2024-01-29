# vercel dev

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        url_components = parse.urlsplit(url)
        # print (f"the url components are{url_components}")
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        dictionary_api_url = "https://restcountries.com/v3.1/name/"

        # print(dictionary)

        if 'country' in dictionary and 'capital' in dictionary:
            country_name = dictionary['country']
            capital_name = dictionary['capital']
            response = requests.get(dictionary_api_url + country_name)
            data = response. json()

            if response.status_code == 200 and 'capital' in data[0] and capital_name in data[0]['capital']:
                message = f"The query was a correct match for {country_name} and {capital_name}."
            else:
                message = f"The query was not a match."

        elif 'country' in dictionary:

            response = requests.get(dictionary_api_url + dictionary["country"])
            data = response.json()
            capital_list = ", ".join(data[0]['capital'])
            message = f"The capital(s) of {dictionary['country']} is/are {capital_list}"

        elif 'capital' in dictionary:

            dictionary_api_url ="https://restcountries.com/v3.1/capital/"
            response = requests.get(dictionary_api_url + dictionary["capital"])
            data = response.json()
            country = data[0]['name']['common']
            message = f"The country of {dictionary['capital']} is {country}"

        else:
            message = "Invalid request, please try another request"

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(message.encode())

        return

