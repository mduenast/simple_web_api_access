#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

from WeatherClient import WeatherClient

class WeatherClientPrinter(object):

    def printAlmanacXml(self,almanacResponse):
        pass

    def printAlmanacJson(self,almanacResponse):
        for (key,value) in almanacResponse.items():
            print key.strip()
            for (key2,value2) in almanacResponse[key].items():
                print "\t",key2.strip()," = ",value2.strip()

    def printForecastXml(self,forecastResponse):
        pass

    def printForecastJson(self,forecastResponse):
        for (key,value) in forecastResponse.items():
            print key.strip()
            for (key2,value2) in forecastResponse[key].items():
                print "\t",key2.strip()," = ",value2.strip()

    def printHourlyXml(self,hourlyResponse):
        pass

    def printHourlyJson(self,hourlyResponse):
        for (key,value) in hourlyResponse.items():
            print key.strip() + " h"
            for (key2,value2) in hourlyResponse[key].items():
                print "\t",key2.strip()," = ",value2.strip()

    def printConditionsXml(self,conditionsResponse):
        pass

    def printConditionsJson(self,conditionsResponse):
        for (key,value) in conditionsResponse.items():
                print "\t",key.strip()," = ",value.strip()