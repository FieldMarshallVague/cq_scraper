import certifi
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
baseurl = "https://en.wikipedia.org/api/rest_v1/"

def get(url):
    print('getting :', url)
    req = http.request('GET', url, headers={
        'Api-User-Agent': 'tobyworth@hotmail.com'
    })

    return req.data

def main():
    print('running main')
    try:
        page = baseurl + 'page/html/Lists_of_radio_stations_in_the_United_States'
        source = get(page)
        #print(source)
        soup = BeautifulSoup(source, 'html.parser')

        statelinks = soup.select('h2#Stations_by_State + ul > li > a')
        #print(statelinks)
        for link in statelinks:
            print(link)
            abslink = link.get('href')
            print(abslink)
            get_stations(abslink)
            break

    except Exception as e:
        print(str(e))


def get_stations(link):
    source_link = baseurl + 'page/html/' + link[2:]
    #print(source_link)

    try:
        # retrieve page and parse html table into list of objects
        source = get(source_link)
        #print(source)
        soup = BeautifulSoup(source, 'html.parser')
        #print(soup.prettify())
        table = soup.find('table', class_="wikitable")
        #print(table)
        theaders = table.find_all('th')
        headers = [col.contents[0] for col in theaders]
        print(headers)
        
        body_rows = table.find_all('tr')
        slicer = slice(1, len(body_rows), 1)
        rows = body_rows[slicer]
        print(rows)

    except Exception as e:
        print(str(e))


main()
