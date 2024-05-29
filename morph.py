import requests
from bs4 import BeautifulSoup
import json

def fetch_morph_details(morfword, params: dict):
    try:
        # Send a GET request to the URL with the provided parameters
        response = requests.get(url, params=params)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the HTML response
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing the morphological details
        table = soup.find('table', {'bordercolor': 'brown'})
        
        # Extract the required output
        output = []
        if table:
            # Find all rows in the table
            rows = table.find_all('tr')
            for row in rows:
                # Get the text from each row and strip leading/trailing whitespace
                text = row.get_text().strip()
                # Append the extracted text to the output list
                output.append(text)
        
        return output
        
    except requests.exceptions.HTTPError as http_err:
        return [{"error": f"HTTP error occurred: {http_err}"}]
    except Exception as err:
        return [{"error": f"An error occurred: {err}"}]

# URL for the morphological analysis tool
url = "https://sanskrit.uohyd.ac.in/cgi-bin/scl/MT/prog/morph/morph.cgi"

# Prompt the user to enter the word to be analyzed
morfword = input("Enter the word: ")

# Set the parameters
params = {
    "morfword": morfword,
    "encoding": "IAST",
    "outencoding": "IAST"
}

# Fetch the morphological analysis
result = fetch_morph_details(morfword, params)

# Create a dictionary to store the input word and the morphological analysis output
morphological_data = {
    "morph_word": morfword,
    "morphology": result
}

# Convert the dictionary to JSON with ensure_ascii=False to remove Unicode escape sequences
json_output = json.dumps(morphological_data, indent=4, ensure_ascii=False)

# Print the JSON output
print(json_output)
