#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import sys
import urllib2
from bs4 import BeautifulSoup

api_key = None
class SampleWeatherClient(object):
    """
        docstring for WeatherClient
    """
    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac" : "/almanac/q/CA/"}
    def __init__(self,api_key):
        super(SampleWeatherClient,self).__init__()
        self.api_key = api_key

    def almanac(self,location):
        # baixar-se la pagina web
        #"http://api.wunderground.com/api/53f287832b555a2e/almanac/q/CA/Madrid.json"
        url = SampleWeatherClient.url_base + self.api_key + \
              SampleWeatherClient.url_service["almanac"] + location + ".xml"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()
        # llegir-la
        soup = BeautifulSoup(response,"lxml")
        maximes = soup.find("temp_high")
        normal= maximes.find("normal").find("c").text
        record = maximes.find("record").find("c").text

        minimes = soup.find("temp_low")
        normal2= minimes.find("normal").find("c").text
        record2 = minimes.find("record").find("c").text

        # retornar els resultats
        return {"maximes" : { "normal " :int(normal), "record" : int(record) }, \
        "minimes" : { "normal" : int(normal2), "record" : int(record2) } }

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Api Key must be in CLI option"
    wc = SampleWeatherClient(api_key)
    resultat = wc.almanac("Lleida")
    print resultat
