import requests

class MakeRequest:
    def __init__(self, url: str, method: str = "GET"):
        self.url = url
        self.method = method
    
    def make_request(self):
        url = self.url
        method = self.method.lower()
        
        response = requests.request(method, url)
        return response