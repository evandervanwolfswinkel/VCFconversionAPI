import csv
import pickle
import os
from settings import APP_STATIC
import loadDB

# Author: Evander van Wolfswinkel & Rick Schoenmaker
# Script for searching allel variants in human exome chromosomes

def main(inputcsv):
    ## Main workflow of searchvariants script
    input_csv_dict_list = readCSV(inputcsv)
    result = searchVariant(input_csv_dict_list)
    return result   # Return results JSON

def openVarDict(filename):
    ## Open dictionary with variants of specific chromosome
    var_dict = loadDB.main(filename) # LoadDB column based on filename=chromosome
    return var_dict     # Return dictionary containing variations

def readCSV(inputfile):
    ## Read CSV input file
    input_csv_dict_list = []
    for list in inputfile:
        csvdict = {}
        csvdict[list[0]] = [list[1], list[2]]
        input_csv_dict_list.append(csvdict)
    return(input_csv_dict_list)  # Return Dictionary of CSV content


def searchVariant(input):
    ## Search variants from input file and return values
    results = []
    for dict in input:
        for key, value in dict.items():
            pos = value[0] # Position
            inputnucl = value[1] # Input nucleotide
            try:
                print(str(key))
                var_dict = openVarDict(str(key)) # Open variations dictionary using the key as filename
                values = var_dict.get(pos)
                result = [inputnucl, values]
                results.append(result)
            except FileNotFoundError:
                print("Error: File not found")
            except Exception:
                continue
    return results

if __name__ == '__main__':
    main()