from urllib.parse import urlparse

# URL Helper class handle all URL related functions
class url_helper:
    # Function return the domain name from URL
    def domin_finder(self, url):
        try:
            return urlparse(url).hostname
        except Exception as ex:
            return "Exception: " + str(ex)
