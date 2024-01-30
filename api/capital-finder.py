from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):
    """
    A simple HTTP request handler that responds to GET requests with information about countries and their capitals.
    
    Usage:
        - /?country=<country_name>: Returns the capital of the specified country.
        - /?capital=<capital_name>: Returns the country with the specified capital.
    """

    #  https://capital-finder-xind14.vercel.app/api/capital-finder?country=Japan
    def do_GET(self):
        url = self.path
        url_components = parse.urlsplit(url)
        query_string_list = parse.parse_qsl(url_components.query)
        dictionary = dict(query_string_list)

        dictionary_api_url = "https://restcountries.com/v3.1/all?fields=name,capital"

        if 'country' in dictionary:
            country_name = dictionary['country']
            response = requests.get(dictionary_api_url)
            data = response.json()

            for country_info in data:
                if 'name' in country_info and 'common' in country_info['name']: 
                    if country_info['name']['common'] == country_name:
                        capital_list = country_info.get('capital', [])
                        if capital_list:
                            capital = capital_list[0]
                            message = f"The capital of {country_name} is {capital}."
                            break
            else:
                message = f"Country {country_name} not found."

        elif 'capital' in dictionary:
            capital_name = dictionary['capital']
            response = requests.get(dictionary_api_url)
            data = response.json()

            for country_info in data:
                if 'capital' in country_info and capital_name in country_info['capital']:
                    country_name = country_info['name']['common']
                    message = f"{capital_name} is the capital of {country_name}."
                    break

        else:
            message = "Invalid. Please provide either 'country' or 'capital' search."

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(message.encode())
        return
