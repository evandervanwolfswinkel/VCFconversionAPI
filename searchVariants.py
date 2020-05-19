import csv
import pickle


def main():
    input_csv_dict_list = readCSV('testinput.csv')
    searchVariant(input_csv_dict_list)

def openVarDict(filename):
    ## Open dictionary with variants of specific chromosome
    infile = open(filename, 'rb')
    var_dict = pickle.load(infile)
    infile.close()
    return var_dict

def readCSV(inputfile):
    ## Read CSV input file
    input_csv_dict_list = []
    with open(inputfile) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            csvdict = {}
            csvdict[str(list(line.values())[0])] = [str(list(line.values())[1]), str(list(line.values())[2])]
            input_csv_dict_list.append(csvdict)
    return(input_csv_dict_list)

def searchVariant(input):
    ## Search variants from input file and return values
    results = []
    for dict in input:
        for key, value in dict.items():
            pos = value[0]
            inputnucl = value[1]
            var_dict = openVarDict(key)
            values = var_dict.get(pos)
            result = [inputnucl, values]
            results.append(result)
    print(results)
    return results

if __name__ == '__main__':
    main()