import re
from requests_html import HTMLSession

def transcript(url):
    session = HTMLSession()
    
    #url = "http://www.ted.com/talks/stephen_cave_the_4_stories_we_tell_ourselves_about_death/transcript"

    r = session.get(url)
    cont = r.html.text

    script = ""
    varibal = False
    for line in cont.split("\n"):
        #print(line)
        #print("---------------------------------------------------------")
        
        if line.startswith("q(\"talkPage.init"):
            varibal = False
            print("Abstracting Finished")
            break
        
        if varibal:
            print("writing.....")
            script += line
            script += "\n"
        
        if line == "Details About the talk":
            #print(line)
            print("Position Located")
            varibal = True
            
    return(script)
