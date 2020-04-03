#!/usr/bin/python
# -*- coding: utf-8 -*-

from CaptureInformation import CaptureInformation
from ConvertToDictionary import ConvertToDictionary
from ConvertToXymon import ConvertToXymon
from PublishToXymon import PublishToXymon
import conf

information = CaptureInformation(url=conf.url, auth_user=conf.auth_user, auth_password=conf.auth_password).capture()
dictonary_format = ConvertToDictionary(information).convert()
converted_to_xymon_format = ConvertToXymon(dictonary_format).convert()
publish = PublishToXymon(converted_to_xymon_format).publish()
print(publish)
