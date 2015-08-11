import urllib
import urllib.parse
import socket
import http.cookiejar as cookielib
import urllib.request as urllib2
import json


class commonInterface():
    def __init__(self):
        self.config = None
        self.readConfig()

    def readConfig(self):
        f = open("properties.json")
        self.config = json.load(f)
        f.close()

class Get(commonInterface):
    def __init__(self, url, headers=None, paramenters = None, data=None, file=None, timeout=30):
        super(Get, self).__init__()
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
        print(self.config["isProxy"])

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
        if self.config["isProxy"]:
            proxy_handler = urllib.request.ProxyHandler({'http':'http://proxy.statestreet.com:80'})
            #proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
            #proxy_auth_handler.add_password('realm', '123.123.2123.123', 'user', 'password')
            urllib2.build_opener(urllib.request.HTTPHandler, proxy_handler)
        self.request = urllib2.Request(self.requestUrl, self.data, self.headers)
        try:
            self.response = urllib2.urlopen(self.request)
            self.responseBody = self.response.read()
            self.responseHeaders = self.response.headers

            #if self.responseHeaders["Content-Type"] == "csv":
            if True:
                #csv file
                #fileName = self.responseHeaders["Content-disposition"];
                #fileName = fileName.split("\"").reverse()[1];
                #print("fileName ", fileName)
                f = open("a.file", "wb")
                f.write(self.responseBody)
                f.close()

        except urllib.error.HTTPError as e:
            print(e)
            self.responseStatus = e.code

    def getHeaders(self):
        return self.responseHeaders.__str__()

    def getBody(self):
        return self.responseBody.decode("utf-8");

class Post(commonInterface):
    def __init__(self, url, headers=None, paramenters = None, data=None, type = None, file=None, timeout=30):
        super(Post, self).__init__()
        self.url = url
        self.paramenters = paramenters
        self.headers = headers
        self.data = data
        self.timeout = timeout
        self.type = type

        self.requestUrl = None
        self.request = None
        self.response = None

        self.responseBody = None
        self.responseHeaders = None
        self.responseStatus = 200
        print(self.config["isProxy"])

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
        if self.config["isProxy"]:
            proxy_handler = urllib.request.ProxyHandler({'http':'http://proxy.statestreet.com:80'})
            #proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
            #proxy_auth_handler.add_password('realm', '123.123.2123.123', 'user', 'password')
            urllib2.build_opener(urllib.request.HTTPHandler, proxy_handler)
        #self.newData = urllib.parse.urlencode(self.data)
        self.newData = self.data
        self.headers["Content-Type"] = self.type
        print("new data", self.newData.encode())
        print("req", self.headers)
        self.request = urllib2.Request(url=self.requestUrl, data=self.newData.encode(), headers=self.headers, method="POST")
        try:
            self.response = urllib2.urlopen(self.request)
            self.responseBody = self.response.read()
            self.responseHeaders = self.response.headers
            #save files of xls and csv
            contentType = self.responseHeaders["Content-Type"];

            #if self.responseHeaders["Content-Type"] == "csv":
            if True:
                f = open("./a.file", "wb")
                f.write(self.responseBody)
                f.close()

        except urllib.error.HTTPError as e:
            print(e)
            self.responseStatus = e.code

    def getHeaders(self):
        return self.responseHeaders.__str__()

    def getBody(self):
        return self.responseBody.decode("utf-8");
