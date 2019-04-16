import certifi
import urllib3
from bs4 import BeautifulSoup
from radiostation import RadioStationColumns, RadioStation

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
baseurl = "https://en.wikipedia.org/api/rest_v1/"

def get(url):
    print('getting :', url)
    retval = {}

    req = http.request('GET', url, headers={
        'Api-User-Agent': 'tobyworth@hotmail.com'
    })

    if req.status == 200:
        retval = req.data

    return retval

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
            # break

    except Exception as e:
        print(str(e))

def sanitize(dirtyObj):
    return (str(dirtyObj)).strip().replace(' ','_').lower()

def get_stations(link):
    source_link = baseurl + 'page/html/' + link[2:]
    #print(source_link)

    try:
        source = get(source_link)
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find('table', class_="wikitable")
        theaders = table.find_all('th')
        
        #headers = [(str(col.contents[0])).strip().replace(' ','_').lower() for col in theaders]
        headers = [sanitize(col.contents[0]) for col in theaders]
        #print(headers)
        
        body_rows = table.find_all('tr')
        slicer = slice(1, len(body_rows), 1)
        rows = body_rows[slicer]
        #print(rows)

        stations = []

        for row in rows:
            cells = row.find_all('td')
            #print(cells)
            values = []
            for col in cells:
                if len(col.contents) == 1:
                    values.append(str(col.contents[0]))
                else:
                    values.append(None)
            #print(values)
            stations.append(dict(zip(headers, values)))
            break

        map_radio_station(stations)

    except Exception as e:
        print(str(e))

def map_radio_station(stations):
    try:    
        for station in stations:
                radio = RadioStationColumns(station)
                print(radio)
                break
    except Exception as e:
        print(str(e))


main()
