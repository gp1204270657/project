# -*- coding=utf-8 -*-
from selenium import webdriver

class Find():
    # id定位
    def ID(drivers,id):
        t = drivers.find_element_by_id(id)
        return t

    # class_name定位
    def class_name(drivers,class_name):
        t = drivers.find_element_by_class_name(class_name)
        return t

    # link_text定位
    def link_text(drivers,link_text):
        t = drivers.find_element_by_link_text(link_text)
        return t

    # name定位
    def name(drivers,name):
        t = drivers.find_element_by_name(name)
        return t


    # xpath定位
    def xpath(drivers,xpath):
        t = drivers.find_element_by_xpath(xpath)
        return t










