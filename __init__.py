import Get_Trans
import raw_url
import urlhub

file = open("scripts.txt",'a')
index = 0

url = "http://www.ted.com/"
raw_urlhub =raw_url.raw_url(url)
urlhub = urlhub.refine(raw_urlhub)

#print(urlhub)

for url in urlhub:
    
    try:
        script = Get_Trans.transcript(url)
        index += 1
        file.write(format(index))
        file.write(script)
    except:
        print("Some Kind of Error Occored.")

file.close()
