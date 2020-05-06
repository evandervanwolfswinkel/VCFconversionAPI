import vcf

vcf_reader = vcf.Reader(open('/home/rick/Documents/Data-intergratie/data/gnomad.exomes.r2.1.1.sites.Y.vcf', 'r'))
id = []
freq = []
try:
    for record in vcf_reader:
        number = str(record.INFO['AF']).strip("[]").replace("e-", "")
        number = float(number)
        if float(number) >= float(0.01):
            print(number)
            id.append(str(record.ID))
            freq.append(str(record.INFO['AF']).strip("[]"))

except:
        pass
        print("faulty")
print(len(freq))