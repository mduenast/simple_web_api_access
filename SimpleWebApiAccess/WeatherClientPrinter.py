#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

from WeatherClient import WeatherClient

class WeatherClientPrinter(object):

    def printAlmanacXml(self,almanacResponse):
        """
        Imprimeix les dades de almanac resultants del recurs en xml.
        :param almanacResponse:
        :return:
        """
        pass

    def printAlmanacJson(self,almanacResponse):
        """
        Imprimeix les dades de almanac resultants del recurs en json.
        :param almanacResponse:
        :return:
        """
        for (key,value) in almanacResponse.items():
            print "*",key.strip()
            for (key2,value2) in almanacResponse[key].items():
                print "\t","*",key2.strip()," = ",value2.strip()

    def printForecastXml(self,forecastResponse):
        """
        Imprimeix les forecast de almanac resultants del recurs en xml.
        :param forecastResponse:
        :return:
        """
        pass

    def printForecastJson(self,forecastResponse):
        """
        Imprimeix les dades de forecast resultants del recurs en json.
        :param forecastResponse:
        :return:
        """
        for (key,value) in forecastResponse.items():
            print "*",key.strip()
            for (key2,value2) in forecastResponse[key].items():
                print "\t","*",key2.strip()," = ",value2.strip()

    def printHourlyXml(self,hourlyResponse):
        """
        Imprimeix les dades de hourly resultants del recurs en xml.
        :param hourlyResponse:
        :return:
        """
        pass

    def printHourlyJson(self,hourlyResponse):
        """
        Imprimeix les dades de hourly resultants del recurs en json.
        :param hourlyResponse:
        :return:
        """
        for (key,value) in hourlyResponse.items():
            print "*",key.strip() + " h"
            for (key2,value2) in hourlyResponse[key].items():
                print "\t","*",key2.strip()," = ",value2.strip()

    def printConditionsXml(self,conditionsResponse):
        """
        Imprimeix les conditions de almanac resultants del recurs en json.
        :param conditionsResponse:
        :return:
        """
        pass

    def printConditionsJson(self,conditionsResponse):
        """
        Imprimeix les dades de conditions resultants del recurs en json.
        :param conditionsResponse:
        :return:
        """
        for (key,value) in conditionsResponse.items():
            print "*",key.strip()," = ",value.strip()