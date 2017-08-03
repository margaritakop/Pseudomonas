import logging
import Pfam_scrape as scrape
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')


#The Uniprot Accession of LasR is 'P25084'. For multiple queries, loop through a list of Uniprot Accession numbers!
#Accessions: ['P298437', 'P20984', 'P2984']
#for Accesion in Accesions:
#    domains = scrape.get_domains(
#        scrape.get_domains_table(Accession))


Uniprot_Accession = 'P25084'


LasR_domains = scrape.get_domains(
                scrape.get_domains_table(Uniprot_Accession))

for domain in LasR_domains:
    print('%s domain from %s to %s' % (domain[1], domain[2], domain[3]))

print(LasR_domains)