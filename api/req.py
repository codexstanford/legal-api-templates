import requests
from pprint import pprint

apiKey = 'YOUR_API_KEY'
requestURL = 'https://www.example.com'

getReq = requests.get(requestURL)
postReq = requests.post(requestURL)

pprint(getReq.text)

#delete(url, args)  ->  Sends a DELETE request to the specified url
#get(url, params, args)  ->  Sends a GET request to the specified url
#head(url, args)  ->  Sends a HEAD request to the specified url
#patch(url, data, args)  ->  Sends a PATCH request to the specified url
#post(url, data, json, args)  ->  Sends a POST request to the specified url
#put(url, data, args)  ->  Sends a PUT request to the specified url
#request(method, url, args)  ->  Sends a request of the specified method to the specified url

################

####
#Get Params
####

# params  ->  A dictionary, list of tuples or bytes to send as a query string.  |  Default: None
#allow_redirects  ->  A Boolean to enable/disable redirection.  |  Default: True (allowing redirects)
#auth  ->  A tuple to enable a certain HTTP authentication.  |  Default: None
#cert  ->  A String or Tuple specifying a cert file or key.  |  Default: None
#cookies  ->  A dictionary of cookies to send to the specified url.  |  Default: None
#headers  ->  A dictionary of HTTP headers to send to the specified url.  |  Default: None
#proxies  ->  A dictionary of the protocol to the proxy url.  |  Default: None
#stream  ->  A Boolean indication if the response should be immediately downloaded (False) or streamed (True).  |  Default: False
#timeout  ->  A number, or a tuple, indicating how many seconds to wait for the client to make a connection and/or send a response.  |  Default: None (request will continue until the connection is closed)
#verify  ->  A Boolean or a String indication to verify the servers TLS certificate or not.  |  Default: True
################
