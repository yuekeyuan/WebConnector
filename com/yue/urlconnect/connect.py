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

    def generateUrl(self):
        if self.paramenters == None:
            self.requestUrl = self.url
            return
        self.requestUrl = self.url + "?"
        for key,value in self.paramenters:
            self.requestUrl + key + "=" + value + "&"
        self.requestUrl = self.requestUrl[0:len(self.requestUrl)-2]

    def preprocess(self):
        self.generateUrl()
        if self.headers == None:
            self.headers = {}

    def run(self):
        self.preprocess()
        self.request = urllib2.Request(self.requestUrl, self.data, self.headers)
        self.response = urllib2.urlopen(self.request)
        self.responseBody = self.response.read()
        self.responseHeaders = self.response.headers

    def getHeaders(self):
        return self.responseHeaders.__str__()

    def getBody(self):
        return self.responseBody.decode("utf-8")