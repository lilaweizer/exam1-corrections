#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 08:50:56 2024

@author: lilaw
"""
# Redo of Problem 3, Exam 1
MONTH_DICT = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 
             'October': '10', 'November': '11', 'December': '12'}
def format_helper(string):
    formatted = string.split(" ")
    formatted[1] = formatted[1].strip(",")
    if len(formatted[1]) < 2:
        formatted[1] = "0" + formatted[1]
    formatted[0] = MONTH_DICT[formatted[0]]
    
    return formatted

def dates_to_iso8601(dates):
    iso_form = []
    for d in dates:
        components = format_helper(d)
        iso = components[2] + "-" + components[0] + "-" + components[1]
        iso_form.append(iso)
    return iso_form

def sort_dates(dates):
    iso_list = dates_to_iso8601(dates)
    date_dict = {}
    for normal, iso in zip(dates, iso_list):
        date_dict[iso] = normal
    sort1 = sorted(iso_list)
    sort2 = []
    for day in sort1:
        val = date_dict[str(day)]
        sort2.append(val)
    return sort2


