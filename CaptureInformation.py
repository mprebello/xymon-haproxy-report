#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv, requests
import conf

class CaptureInformation(object):
    def __init__(self, url, auth_user=None, auth_password=None):
        self.__connection = url
        self.__auth_user = auth_user
        self.__auth_password = auth_password

    def __capture_http(self):
        session = requests.Session()
        session.auth = (self.__auth_user, self.__auth_password)
        response = session.get(self.__connection)
        answer = response.content
        answer_treated = answer.split('\n')
        answer_converted = self.__convert_to_dictionary(answer_treated)
        return answer_converted

    def __convert_to_dictionary(self, content):
        convert_content_to_dict = csv.DictReader(content)
        dict_list = []
        for line in convert_content_to_dict:
            dict_list.append(line)

        return dict_list

    def capture(self):
        information = self.__capture_http()
        return information


if __name__ == '__main__':
    information = CaptureInformation(url=conf.url, auth_user=conf.auth_user, auth_password=conf.auth_password).capture()
    print(information)

    
