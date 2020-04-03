#!/usr/bin/python
# -*- coding: utf-8 -*-

class ConvertToDictionary(object):
    def __init__(self, answer):
        self.__answer = answer

    def convert(self):
        header = self.__capture_headers()
        converted_to_dictonary= self.__group_by_svc(header)
        return converted_to_dictonary

    def __capture_headers(self):
        list = []
        for line in self.__answer:
            value = line['# pxname']
            if value not in list:
                list.append(value)
        
        return list

    def __group_by_svc(self, header):
        dict = {}
        status_global = 'NEW'
        for key in header:
            dict.update({key: { 'Status': 'NEW', 'Color' : 'green', 'Details' : []}})
            for line in self.__answer:
                if line['# pxname'] == key:
                    current_key = dict[key]
                    current_list = current_key['Details']
                    old_status = current_key['Status']
                    current_status = self.__convert_status(line['status'])
                    result_status = self.__verify_status(old_status, current_status)
                    color = self.__define_color(current_status)
                    color_service = self.__define_color(result_status)
                    current_list.append({'Service': line['svname'], 'Color': color, 'Status': line['status']})
                    dict.update(
                        {key: {'Status': result_status, 'Color': color_service, 'Details':  current_list}})

            result_global_status = self.__verify_status(old_status=status_global, current_status=result_status, alarm=True)
            status_global = result_global_status
            color_global = self.__define_color(status_global)

        #all_data = {'Status': status_global, }
        data_result = {'Status': status_global,'Color': color_global, 'Details': dict}
        return data_result

    def __convert_status(self, status):
        if status == 'OPEN':
            return 'UP'
        else:
            return status


    def __verify_status(self, old_status, current_status, alarm=False):
        if old_status == 'NEW':
            return current_status

        if alarm:
            if current_status == 'DOWN' or old_status == 'DOWN':
                return 'DOWN'

        if current_status == old_status:
            return current_status
        
        if current_status != old_status:
            return 'Parcial'

    def __define_color(self, status):
        if status == 'UP':
            return 'green'
        elif status == 'Parcial':
            return 'yellow'
        else:
            return 'red'

