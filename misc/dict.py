'''
Created on Mar 19, 2012

@author: Rejith
'''
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

def get_http(page):
    try:
        server, port, url, method = re.compile('(.com.*)').sub('.com',re.compile('(http://)').sub( '', page)),80, page,'GET'
        h1 = httplib.HTTPConnection(server,port)
        h1.connect()
        h1.request(method,url)
        page = h1.getresponse(True).read(None)
        h1.close()
        return page
    except:
        return -1

def get_all_links(content):
    page_list=[]
    while(True):
        url, endpos = print_next_url(content)
        if endpos == 0:
            break
        if url:
            page_list.append(url)
            content = content[endpos:]
    return page_list

def add_to_index(index,keyword,url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]


def crawl_web(seed):
    crawled = []
    index = {}
    graph= {}
    links = []
    to_crawl = [seed]
    f = open('f:\\output.txt', 'w')
    while len(to_crawl) > 0:
        t = to_crawl.pop()
        if len(crawled) > 100:
            break

        content = get_http(t)
        for i in content.split():
            if i[0] != '<':
                add_to_index(index,i,t)
        if content == -1:
            crawled.append(t);
            continue
        for i in get_all_links(content):
            if i not in crawled and i not in to_crawl:
                to_crawl.append(i)
                links.append(i)
        crawled.append(t);
        graph[t] = links
        links = []
        f.write(t);
        f.write('\n')


    return crawled,index,graph  
    
        
#crawled = crawl_web('http://www.google.com')
crawled,index,graph = crawl_web('http://www.udacity.com/cs101x/urank/index.html')
print crawled
print index
print graph


