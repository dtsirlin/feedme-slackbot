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

        # print(dictWithoutKeys)
        # print(dictWithKeys)

        for key in dictWithoutKeys:
            # print(id)
            # print(key)
            dictWithKeys[id] = key
            id += 1
        
        # print("\n")
        # print(dictWithKeys)
        # print("\n")

        return dictWithKeys


    def cleanRecord(self, record):
        record['name'] = record['name'].replace('"','').strip()
        record['address'] = record['address'].replace('"','').strip()
        record['menuLink'] = record['menuLink'].replace('"','').strip().lower()
        record['instagram'] = record['instagram'].replace('"','').strip().lower()
        record['contactEmail'] = record['contactEmail'].replace('"','').strip().lower()
        record['contactNumber'] = record['contactNumber'].replace('"','').strip().lower()
        record['category'] = record['category'].replace('"','').strip().lower()

        return record

        
