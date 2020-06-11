# Author: Rick Schoenmaker & Evander Van Wolfswinkel
# Class: BIN3A



# import dependencies.
import vcf
import pickle

# Import vcf reader to open vcf files.
vcf_reader = vcf.Reader(open('gnomad.exomes.r2.1.1.sites.Y.vcf', 'r'))

# create a dictionary
dicts = {}


try:
    # A for loop to looping through all records in the vcf file.
    for record in vcf_reader:
        # Retrieves the allele frequenties in a string and removes [ ] and e-.
        number = str(record.INFO['AF']).strip("[]").replace("e-", "")
        # Turns string number into float.
        number = float(number)
        # Filters the allele frequenties to select only the the ones that appear less than 0.01%
        if float(number) <= float(0.01):
            # Create a dictionary
            dict = {}
            # Fills a dictionary with position, reference nucleotide(s), alternative nucleotide(s), allele frequentie and ID
            dict[str(record.POS)] = [str(record.REF), str(record.ALT),
                                     str(record.INFO['AF']).strip("[]"),
                                     str(record.ID)]
            dicts.update(dict)


except:
        pass

# Create a pickle from the dictionary and save it in the static folder.
outfile = open('static/X', 'wb')
pickle.dump(dicts, outfile)
outfile.close()