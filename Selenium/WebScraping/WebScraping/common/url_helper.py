from urllib.parse import urlparse

class URLHelper():
    def domin_finder(self, url):
        try:
            return urlparse(url).hostname
        except Exception as ex:
            return "Exception: "+str(ex)
