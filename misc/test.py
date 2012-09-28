'''
Created on Mar 15, 2012

@author: Rejith
'''
import httplib
import re
def print_next_url(page):
    start_link = page.find('href=')
    if start_link == -1:
        return None, 0
    if page[start_link + 6:start_link + 10] != 'http':
        return None, start_link + 7
    start_quote = start_link + 5;
    end_quote = page.find('"',start_quote + 1)
    return page[start_quote + 1: end_quote], end_quote + 1

def get_http(server, port, url, method):
    h1 = httplib.HTTPConnection(server,port)
    h1.connect()
    h1.request(method,url)
    page = h1.getresponse(True).read(None)
    h1.close()
    return page

def crawl_web(seed):
    crawled = []
    to_crawl = [seed]
    f = open('f:\\output.txt', 'w')
    while len(to_crawl) > 0:
        t = to_crawl[len(to_crawl)-1]
        print t;
        if len(crawled) > 100:
            break
        if t in crawled:
            to_crawl.remove(t); 
            continue
        try:
 
            page = get_http(re.compile('(.com.*)').sub('.com',re.compile('(http://)').sub( '', t)),80,
                        t,'GET')
        except:
            crawled.append(t);
            to_crawl.remove(t); 
            continue
        while(True):
            url, endpos = print_next_url(page)
            if endpos == 0:
                break
            if url:
                if url not in crawled and url not in to_crawl:
                    to_crawl.append(url)
            page = page[endpos:]
        crawled.append(t);
        to_crawl.remove(t); 
        f.write(t);
        f.write('\n')


    return crawled  
    
        
crawled = crawl_web('http://www.google.com')
#crawled = crawl_web('http://www.udacity.com/cs101x/index.html')
print crawled


