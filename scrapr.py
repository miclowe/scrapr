from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url = "http://egolferz.com/html/leaderboard.htm"

page = urlopen(my_url)
html = page.read()
page.close()

page_soup = soup(html, "html.parser")

table = page_soup.find('table')
table_header = table.find('thead')
table_body = table.find('tbody')

# Get list of tournaments
headings = table_header.findAll('th', {'scope' : 'col'})
tournaments = []
for i, h in enumerate(headings):
    if i > 0 and i < len(headings) - 1:
        tournaments.append(h.text)

filename = "leaderboard.csv"
f = open(filename, "w")
headers = ", ".join(["Name"] + tournaments) + "\n"
f.write(headers)

# Get each member stats
rows = table_body.findAll('tr')
scores = []

for r in rows:
    member = []
    name = r.a.text if r.a else r.th.text
    member.append(name)
    # Exclude ranking and total points
    cols = r.findAll('td', {'class' : None})
    member += [ele.text for ele in cols]
    f.write(", ".join(member) + "\n")
    # scores.append(member)

f.close()
