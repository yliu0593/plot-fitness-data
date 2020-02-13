# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 19:28:41 2020

@author: liu1935
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('db-fitness-vis.json', scope)
client = gspread.authorize(creds)

sheet = client.open("Youlin's fitness journey").sheet1

data = sheet.get_all_records()
data_fitness = pandas.DataFrame(data)
data_fitness.set_index('Date',inplace=True)


cols_plot = [ 'Weight','Calories', 'Protein (g)','Carbohydrates (g)','Fat (g)']
axes = data_fitness[cols_plot].plot(marker='o', linestyle='-',linewidth=1, figsize=(11, 9), subplots=True)
