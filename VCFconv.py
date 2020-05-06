import vcf

vcf_reader = vcf.Reader(open('gnomad.exomes.r2.1.1.sites.Y.vcf', 'r'))
for record in vcf_reader:
    print(record.INFO)
