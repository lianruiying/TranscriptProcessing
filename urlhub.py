# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:20:57 2018

@author: lianr

This py is to make a list of usable url
"""
def refine(raw_urlhub):
    """
    ****This is for testing when I'm writing this***
    
    file = open("C:\\Users\\lianr\\Desktop\\url.txt")
    cont = file.read()
    #print(cont)
    
    """

    urlhub = []
    
    def test_if(url):
        if "http" in url:
            return False
        else:
            return True
    def getfullurl(url,urlhub):
        if "http" in url:
            url += "/transcript"
            urlhub.append(url)
        else:
            urlhub.append("http://www.ted.com"+url[1:]+"/transcript")
            #print(url)
            #print("http://www.ted.com"+url[1:])
            
    for line in raw_urlhub.split("\r"):
        
        #print(line)
        #print(line.split(":"))
        
        for url in line.split(":"):
            if "talks" in url:
                if "\n" in url:
                    refined = url.split("\"\n")
                    
                    for spl in refined:
                        if "talks" in spl:
                            if test_if(spl):
                                getfullurl(spl,urlhub)
                else:
                    if test_if(spl):
                        getfullurl(spl,urlhub)
                            
    return(urlhub)
