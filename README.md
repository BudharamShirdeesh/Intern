Import necessary Libraries: 
**import requests**:used to send HTTP request 
**from bs4 import BeautifulSoup**:used for parsing HTML and XML documents, allowing you to extract data from them.
**import json**: for encoding and decoding JSON data.

**fetch_morph_details** function  fetches morphological details for a given word from a specified URL("https://sanskrit.uohyd.ac.in/cgi-bin/scl/MT/prog/morph/morph.cgi")
It takes two arguments:
**morfword**: The word to be analyzed morphologically.
**params**: Dictionary of parameters to be sent with the GET request.

Inside the function:
It sends a GET request to the specified URL with the provided parameters using requests.get.
If the request is successful, it parses the HTML response using BeautifulSoup.
It finds the table containing the morphological details based on its attributes.
It extracts the text content of each row in the table and appends it to the output list.
Finally, it returns the output list containing the morphological details.
It handles HTTP errors and other exceptions gracefully, returning an error message in case of failure.

URL and Input:
**url**: This variable stores the URL for the morphological analysis tool.
**morfword**: This variable stores the word inputted by the user.
**params**: This dictionary stores the parameters to be sent with the GET request, including the input word, encoding, and output encoding.

Fetching and Processing:
The **fetch_morph_details** function is called with the input word and parameters, and the result is stored in the result variable.

Create JSON Output:
A dictionary named** morphological_data** is created to store the input word and the morphological analysis output.
The dictionary is converted to JSON format using json.dumps, specifying ensure_ascii=False to ensure that Unicode escape sequences are removed and indent=4 for pretty formatting.

Print JSON output.
