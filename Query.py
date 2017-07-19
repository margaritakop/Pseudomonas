import requests, bs4, logging
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.debug('Start of program')

def get_domains_table(UniprotID):
    url = 'http://pfam.xfam.org/protein/' + str(UniprotID)
    res = requests.get(url)
    res.raise_for_status()
    noStarchSoup = bs4.BeautifulSoup(res.text)
    logging.debug('Website downloaded as %s ' % (type(noStarchSoup)))
    domains_table = noStarchSoup.select('.resultTable')
    return domains_table

#LasR_domains = get_domains('P25084')


LasR_domains_table = '''[<table class="resultTable details" id="imageKey" summary="Key for the Pfam domain image">
<thead>
<tr>
<th class="dh" rowspan="2">Source</th>
<th class="dh" rowspan="2">Domain</th>
<th class="dh" rowspan="2">Start</th>
<th class="dh" rowspan="2">End</th>
<th class="sh" colspan="2" style="display: none">Gathering threshold (bits)</th>
<th class="sh" colspan="2" style="display: none">Score (bits)</th>
<th class="sh" colspan="2" style="display: none">E-value</th>
</tr>
<tr>
<th class="sh" style="display: none">Sequence</th>
<th class="sh" style="display: none">Domain</th>
<th class="sh" style="display: none">Sequence</th>
<th class="sh" style="display: none">Domain</th>
<th class="sh" style="display: none">Sequence</th>
<th class="sh" style="display: none">Domain</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td class="pfama_PF03472">Pfam</td>
<td><a href="http://pfam.xfam.org/family/Autoind_bind">Autoind_bind</a></td>
<td>16</td>
<td>161</td>
<td class="sh" style="display: none">21.00</td>
<td class="sh" style="display: none">21.00</td>
<td class="sh" style="display: none">126.40</td>
<td class="sh" style="display: none">125.90</td>
<td class="sh" style="display: none">9.4e-34</td>
<td class="sh" style="display: none">1.3e-33</td>
</tr>
<tr class="odd">
<td class="pfama_PF00196">Pfam</td>
<td><a href="http://pfam.xfam.org/family/GerE">GerE</a></td>
<td>175</td>
<td>231</td>
<td class="sh" style="display: none">22.40</td>
<td class="sh" style="display: none">22.40</td>
<td class="sh" style="display: none">77.80</td>
<td class="sh" style="display: none">77.00</td>
<td class="sh" style="display: none">4.8e-19</td>
<td class="sh" style="display: none">9e-19</td>
</tr>
</tbody>
</table>]'''


def get_domains(domains_table):
    soup = BeautifulSoup(domains_table)
    table = soup.find("table")
    # The first tr contains the field names.
    headings = [th.get_text() for th in table.find("tr").find_all("th")]

    # Get the rows of the table, and find the domains as a nested list.
    rows = table.find_all('tr')
    domains = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            domains.append([ele for ele in cols if ele])

    return headings, domains

print(get_domains (LasR_domains_table))

