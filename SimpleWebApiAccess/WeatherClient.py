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
        ,"conditions" : "/conditions/q/CA/", "hourly" : "/hourly/q/CA/"}

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
        """
        Retorna les prediccions dels proxims 3 dies
        :param location:
        :return:
        """
        # baixar-se la pagina web
        url = WeatherClient.url_base + self.api_key + \
              WeatherClient.url_service["forecast"] + location + ".json"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()

        decoded = json.loads(response)
        forecast = {}
        for forecastday in decoded["forecast"]["txt_forecast"]["forecastday"]:
            partial = {}
            partial["title"] = str(forecastday["title"])
            partial["fcttext"] = str(forecastday["fcttext"])
            partial["fcttext_metric"] = str(forecastday["fcttext_metric"])
            forecast[str(partial["title"])] = str(partial)
        return forecast

    def conditionsXml(self,location):
        pass

    def conditionsJson(self,location):
        # baixar-se la pagina web
        url = WeatherClient.url_base + self.api_key + \
              WeatherClient.url_service["conditions"] + location + ".json"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()

        decoded = json.loads(response)
        conditions ={}
        conditions["weather"] = str(decoded["current_observation"]["weather"])
        conditions["temperature_String"] =  str(decoded["current_observation"]["temperature_string"])
        conditions["relative_humidity"] =  str(decoded["current_observation"]["relative_humidity"])
        conditions["wind_string"] =  str(decoded["current_observation"]["wind_string"])
        conditions["dewpoint_string"] =  str(decoded["current_observation"]["dewpoint_string"])
        conditions["heat_index_string"] =  str(decoded["current_observation"]["heat_index_string"])
        conditions["feelslike_string"] =  str(decoded["current_observation"]["feelslike_string"])
        conditions["precip_1hr_string"] = str(decoded["current_observation"]["precip_1hr_string"])
        conditions["precip_today_string"] = str(decoded["current_observation"]["precip_today_string"])
        return conditions

    def hourlyXml(self,location):
        pass

    def hourlyJson(self,location):
        # baixar-se la pagina web
        url = WeatherClient.url_base + self.api_key + \
              WeatherClient.url_service["hourly"] + location + ".json"
        f = urllib2.urlopen(url)
        response = f.read()
        f.close()

        decoded = json.loads(response)
        return decoded

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
    elif resource == "forecast":
        print wc.forecastJson(location)
    elif resource == "conditions":
        print wc.conditionsJson(location)
    elif resource == "hourly":
        print wc.hourlyJson(location)
    else:
        print "Recurs desconegut"
        sys.exit(-1)