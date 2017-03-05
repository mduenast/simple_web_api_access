#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import sys
import urllib2
import json
from bs4 import BeautifulSoup

api_key = None
resource = None
location = None

class WeatherClient(object):
    """
        docstring for WeatherClient
    """
    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac" : "/almanac/q/CA/", "forecast" : "/forecast/q/CA/" \
        ,"conditions" : "/conditions/q/CA/"}
    def __init__(self,api_key):
        super(WeatherClient,self).__init__()
        self.api_key = api_key

    def almanacXml(self,location):
        """
        Retorna les temperatures maximes (normal i record) i les minimes (normal i record)
        :param location:
        :return:
        """
        # baixar-se la pagina web
        url = WeatherClient.url_base + self.api_key + \
              WeatherClient.url_service["almanac"] + location + ".xml"
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

    def almanacJson(self,location):
        """
        Retorna les temperatures maximes (normal i record) i les minimes (normal i record)
        :param location:
        :return:
        """
        # baixar-se la pagina web
        url = WeatherClient.url_base + self.api_key + \
              WeatherClient.url_service["almanac"] + location + ".json"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()

        decoded = json.loads(response)
        maximes = decoded["almanac"]["temp_high"]
        normal = maximes["normal"]["C"]
        record = maximes["record"]["C"]

        minimes = decoded["almanac"]["temp_low"]
        normal2 = minimes["normal"]["C"]
        record2 = minimes["record"]["C"]

        # retornar els resultats
        return {"maximes": {"normal ": int(normal), "record": int(record)}, \
                "minimes": {"normal": int(normal2), "record": int(record2)}}

    def forecastXml(self,location):
        pass

    def forecastJson(self,location):
        pass

    def conditionsXml(self,location):
        pass

    def conditionsJson(self,location):
        pass

if __name__ == "__main__":
    if not api_key:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "Api Key must be in CLI option"
            sys.exit(-1)
    if not resource:
        try:
            resource = sys.argv[2]
        except IndexError:
            print "Resource must be specified"
            sys.exit(-1)
    if not location:
        try:
            location = sys.argv[3]
        except IndexError:
            print "Location argument must be specified"
            sys.exit(-1)
    wc = WeatherClient(api_key)
    if resource == "almanac":
        print wc.almanacJson(location)