import urllib
import socket
import http.cookiejar as cookielib
import urllib.request as urllib2

class Get():
    def __init__(self, url, headers=None, paramenters = None, data=None, file=None, timeout=30):
        self.url = url
        self.paramenters = paramenters
        self.headers = headers
        self.data = data
        self.file = file
        self.timeout = timeout

        self.requestUrl = None
        self.request = None
        self.response = None

        self.responseBody = None
        self.responseHeaders = None
        self.responseStatus = 200
    def generateUrl(self):
        if self.paramenters == None or len(self.paramenters) == 0:
            self.requestUrl = self.url
            return

        self.requestUrl = self.url + "?"
        for key in self.paramenters:
            self.requestUrl = self.requestUrl + key + "=" + self.paramenters[key] + "&"
        self.requestUrl = self.requestUrl[0:len(self.requestUrl)-1]
        print(self.requestUrl)

    def preprocess(self):
        self.generateUrl()
        if self.headers == None:
            self.headers = {}

    def run(self):
        self.preprocess()
        self.request = urllib2.Request(self.requestUrl, self.data, self.headers)
        try:
            self.response = urllib2.urlopen(self.request)
            self.responseBody = self.response.read()
            self.responseHeaders = self.response.headers
        except urllib.error.HTTPError as e:
            print(e)
            self.responseStatus = e.code

    def getHeaders(self):
        return self.responseHeaders.__str__()

    def getBody(self):
        return self.responseBody.decode("utf-8")