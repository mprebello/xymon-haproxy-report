#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

class ConvertToXymon(object):
    def __init__(self, dictionary):
        self.__dictionary = dictionary
        self.__global_status = dictionary['Status']
        self.__global_color = dictionary['Color']
        self.__global_details = dictionary['Details']
        self.__html = ''

    def convert(self):
        self.__convert_html()
        return self.__html

    def __convert_html(self):
        current_date = datetime.datetime.now()
        Title = conf.xymon_title
        self.__html += '{} {} <br>'.format(self.__global_color, current_date)
        self.__html += '<H1 align = "center" >'
        self.__html += '{} Status &{} {}'.format(Title, self.__global_color, self.__global_status)
        self.__html += '</H1>'
        self.__html += '<table border = 1 align = "center">'
        body = self.__generate_table()
        self.__html += body
        self.__html += '</table>'

    def __generate_table(self):
        result = ''
        for head in self.__global_details:
            current_head  = head
            current_content = self.__dictionary['Details'][head]['Details']
            current_status = self.__dictionary['Details'][head]['Status']
            current_color = self.__dictionary['Details'][head]['Color']
            result += '<tr>'
            result += '<td>'
            result += '<b>{} - &{} {}</b>'.format(
                current_head, current_color, current_status)
            result += '</td>'
            result += '<td>'
            result += '<table border=1 width="100%">'

    
            for line in current_content:
                current_line_service = line['Service']
                current_line_color = line['Color']
                current_line_status = line['Status']
                result += '<tr>'
                result += '<td>'
                result += '{}'.format(current_line_service)
                result += '</td>'
                result += '<td>'
                result += '&{} {}'.format(current_line_color, current_line_status)
                result += '</td>'
                result += '</tr>'
           
            result += '</tr></td></table>'


        return result


