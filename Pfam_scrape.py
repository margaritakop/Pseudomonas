import requests, bs4, logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def get_domains_table(UniprotID):
    url = 'http://pfam.xfam.org/protein/' + str(UniprotID)
    res = requests.get(url)
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text, "lxml")
    logging.debug('Website downloaded as %s ' % (type(noStarchSoup)))
    domains_table = noStarchSoup.select('.resultTable')
    return domains_table

def get_domains(domains_table):
    soup = BeautifulSoup(str(domains_table), "lxml")
    table = soup.find("table")
    # The first tr contains the field names, uncomment this if you need the headings.
    #headings = [th.get_text() for th in table.find("tr").find_all("th")]

    # Get the rows of the table, and find the domains.
    rows = table.find_all('tr')
    domains = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            domains.append([ele for ele in cols if ele])
    logging.debug('%s Domains found' % len(domains))
    return domains

