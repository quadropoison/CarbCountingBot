import urllib
import urllib.parse


class UrlBuilder:

    @staticmethod
    def build(base_url, *resources, **params):
        url = base_url
        for resource in resources:
            url = '{}/{}'.format(url, resource)
            if params:
                url = '{}?{}'.format(url, urllib.parse.urlencode(params))
                return url
