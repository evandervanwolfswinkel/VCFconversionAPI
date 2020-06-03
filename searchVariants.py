import csv
import pickle
import os
from settings import APP_STATIC
import loadDB

def main(inputcsv):
    input_csv_dict_list = readCSV(inputcsv)
    result = searchVariant(input_csv_dict_list)
    return result

def openVarDict(filename):
    ## Open dictionary with variants of specific chromosome
    var_dict = loadDB.main(filename)
    print(var_dict)
    return var_dict

def readCSV(inputfile):
    ## Read CSV input file
    input_csv_dict_list = []
    for list in inputfile:
        csvdict = {}
        csvdict[list[0]] = [list[1], list[2]]
        input_csv_dict_list.append(csvdict)
    return(input_csv_dict_list)


def searchVariant(input):
    ## Search variants from input file and return values
    results = []
    for dict in input:
        for key, value in dict.items():
            pos = value[0]
            inputnucl = value[1]
            try:
                var_dict = openVarDict(str(key))
                print(var_dict)
                values = var_dict.get(pos)
                result = [inputnucl, values]
                results.append(result)
            except FileNotFoundError:
                print("Error: File not found")
    return results

if __name__ == '__main__':
    main()