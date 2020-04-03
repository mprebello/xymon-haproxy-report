#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, conf

class PublishToXymon(object):
    def __init__(self, message=None):
        local_environment = os.environ
        self.__bb = local_environment['BB']
        self.__bbdisp = local_environment['XYMONSERVERS']
        self.__machine = local_environment['CLIENTHOSTNAME']
        self.__time_to_try_again = '1h'
        self.__column = conf.xymon_column
        self.__message = message

    def publish(self, test=False):
        execute = None

        line_to_execute = '{} {} \'status+{} {}.{} {}\' '.format(self.__bb, self.__bbdisp,
                                                                 self.__time_to_try_again, self.__machine,
                                                                 self.__column, self.__message)
        if test:
            print('{}'.format(line_to_execute))
        else:                                                     
            execute = os.system(line_to_execute)
        
        return execute


if __name__ == '__main__':
    xymon_output = PublishToXymon(message='here').publish(test=True)
    xymon_output = PublishToXymon()
    print(xymon_output)


