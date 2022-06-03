import csv
import os
import json
import pandas as pd

class SeedData():

    def __init__(self, csvFilepath):
        self.filepath = csvFilepath

    def csvToJsonString(self):
        jsonArray = []

        with open(self.filepath, encoding='utf-8') as csvf: 
            csvReader = csv.DictReader(csvf)

            for row in csvReader:
                row['address'] = row['address'].replace("|",",")

                jsonArray.append(row)

        return json.dumps(jsonArray, indent=4)

    def jsonStringToDict(self, jsonString):
        return json.loads(jsonString)

    def createDictWithKeysFromDict(self, dictWithoutKeys):
        dictWithKeys = dict()
        id = 0

        for key in dictWithoutKeys:
            dictWithKeys[id] = key
            id += 1

        return dictWithKeys


    def formatValues(self, dict):
        for value in dict.values():
            value['name'] = value['name'].replace('"','').strip()
            value['address'] = value['address'].replace('"','').strip()
            value['menuLink'] = value['menuLink'].replace('"','').strip().lower()
            value['instagram'] = value['instagram'].replace('"','').strip().lower()
            value['contactEmail'] = value['contactEmail'].replace('"','').strip().lower()
            value['contactNumber'] = value['contactNumber'].replace('"','').strip().lower()
            value['category'] = value['category'].replace('"','').strip().lower()

        return dict

        
