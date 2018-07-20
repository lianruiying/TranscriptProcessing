import re
from requests_html import HTMLSession

#url = 'https://www.ted.com/'

def raw_url(url):
    urlstring = ""
    session = HTMLSession()
    r = session.get(url)
    #print(r.html.text)
    data = r.html.text
    raw_url = re.findall("\"url\":\".+/talks/.+\"",data)
    #"url":"/talks/will_marshall_the_mission_to_create_a_searchable_database_of_earth_s_surface"
    #print(raw_url)

    for i in raw_url:
        for a in i.split(','):
             if "url" in a:
                 urlstring += a
                 urlstring += "\n"
    return(urlstring)

#raw_url('https://www.ted.com/')
