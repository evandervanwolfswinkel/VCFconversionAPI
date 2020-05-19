import vcf
import pickle

vcf_reader = vcf.Reader(open('gnomad.exomes.r2.1.1.sites.Y.vcf', 'r'))

dicts = {}
try:
    for record in vcf_reader:
        number = str(record.INFO['AF']).strip("[]").replace("e-", "")
        number = float(number)
        if float(number) <= float(0.01):
            #print(number)
            dict = {}
            dict[str(record.POS)] = [str(record.REF),str(record.ALT),
                                     str(record.INFO['AF']).strip("[]"),
                                     str(record.ID)]
            dicts.update(dict)


except:
        pass
        print("faulty")

print(dicts)
outfile = open('Y', 'wb')
pickle.dump(dicts,outfile)
outfile.close()