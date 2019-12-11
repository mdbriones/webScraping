import requests
from bs4 import BeautifulSoup
import csv

csv_file = open('details.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['company Name', 'link', 'established', 'members', 'address'])

for i in range(10):
    res = requests.get('https://en-jp.wantedly.com/projects?type=mixed&page='+str(i))
    soup = BeautifulSoup(res.text, 'lxml')
    site = soup.select('h1>a', href=True)

    for i in site:
        res = requests.get('https://en-jp.wantedly.com/projects/' + i['href'][10:16])
        soup1 = BeautifulSoup(res.text, 'lxml')

        data = soup1.find('div', class_='company')
        company_name = (data.a.text).strip()
        
        data = soup1.find('div', class_='company-info-list')
        company_desc = data.find_all('div', class_='company-description')
        try:
            company_link = company_desc[0].text.strip()
        except Exception as e:
            company_link = "None"

        try:
            company_established = company_desc[1].text.strip()
        except Exception as identifier:
            company_established = "None"

        try:
            company_members = company_desc[2].text.strip()
        except Exception as identifier:
            company_members = "None"

        try:
            company_address = company_desc[4].text.strip()
        except Exception as identifier:
            company_address = "None"
        
        csv_writer.writerow([company_name, company_link, company_established, company_members, company_address])

csv_file.close()