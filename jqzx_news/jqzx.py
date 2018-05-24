# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import chain
from jqzx_data  import jqzx as tickets_repo
import pdb

def print_log(mesgs):
    for mesg in mesgs:
        print(u"* [ ] {} {}".format(mesg[0],mesg[1]))
def get_cover(driver):
    print('cover')
    posts  = driver.find_elements_by_class_name("post__cover")
    return [ (ele.get_attribute('alt'),ele.get_attribute('href')) for ele in posts]


def get_latest(driver):
    print('latest_articles')
    articles  = driver.find_elements_by_class_name("article-item__right")

    def extract(article):
         ahref = article.find_element_by_tag_name('a')
         summary = ahref.text + article.find_element_by_tag_name('p').text 
         return (summary,ahref.get_attribute('href'))
          
    return map(extract,articles)
def get_hot_articles(driver):
    print('hot_articles')
    
    articles  = driver.find_elements_by_class_name("hot-item__title")
    def extract(article):
         summary = article.text
         return (summary,article.get_attribute('href'))
    return map(extract,articles)


def save_to_file(data_file,tickets_list):

    def myunicode(text):
        try:
           new_text = unicode(text,'utf-8')
        except TypeError:
            return text
        return new_text 
    with open(data_file,'w') as of:
        of.write("# -*- coding=utf-8 -*- \n")
        of.write("jqzx = [\n")
        for ticket in tickets_list:
            print(ticket[0])
            print(ticket[1])
            of.write("   ")
            of.write("(")
            of.write("\"")
            of.write(myunicode(ticket[0]).encode('utf8'))
            of.write("\"")
            of.write(",")
            of.write("\"")
            of.write(unicode(ticket[1]).encode('utf8'))
            of.write("\"")
            of.write("),\n")
            #print(u"   (\"{}\",\"{}\"), \n".format(ticket[0].decode('utf-8').encode('utf-8'),ticket[1].decode('utf-8').encode('utf-8')))
            #of.write(u"""   ("{}","{}"), \n""".format(ticket[0],ticket[1]))
        of.write("]\n")

def test2():
    save_to_file('jqzx_data.py',tickets_repo)

def test3():
    driver = webdriver.Firefox()
    driver.get("https://www.jiqizhixin.com/")
    
    new_tickets=[chain(get_cover(driver),
                    get_latest(driver),
                    get_hot_articles(driver))]
    diffs = [set(new_tickets)-set(tickets_repo)]
    #diffs = set(tickets_repo) -set(new_tickets)
    for ticket in diffs:
        tickets_repo.append(ticket)

    save_to_file('jqzx_data.py',tickets_repo)
    driver.close()
def main():
    driver = webdriver.Firefox()
    driver.get("https://www.jiqizhixin.com/")
    
    new_tickets=chain(get_cover(driver),
                    get_latest(driver),
                    get_hot_articles(driver))
    # due to internal encoding difference, which causes diff get a wrong results
    # write to disk as old_tickets and readback to make sure encoding consistant
    save_to_file('new_tickets.py',new_tickets)
    import new_tickets
    diffs = set(new_tickets.jqzx)-set(tickets_repo)
    #diffs = set(tickets_repo) -set(new_tickets)
    for ticket in diffs:
        print(ticket)
        tickets_repo.append(ticket)

    save_to_file('jqzx_data.py',tickets_repo)
    driver.close()

def test4():
    driver = webdriver.Firefox()
    driver.get("https://www.jiqizhixin.com/")
    
    new_tickets=list(chain(get_cover(driver),
                    get_latest(driver),
                    get_hot_articles(driver)))
    diffs = set(new_tickets)-set(tickets_repo)
    #diffs = set(tickets_repo) -set(new_tickets)
    pdb.set_trace()
    print("diff")
    save_to_file('diff.py',diffs)
    save_to_file('new_tickes.py',new_tickets)
    save_to_file('old_tickes.py',tickets_repo)
    for ticket in diffs:
        print(ticket)
        tickets_repo.append(ticket)

    save_to_file('final.py',tickets_repo)
    driver.close()

def test5():
    import new_tickets
    import old_tickets
    diffs = set(new_tickets.jqzx)-set(old_tickets.jqzx)
    for ticket in diffs:
        print(ticket)
        old_tickets.jqzx.append(ticket)

    save_to_file('test_5final.py',old_tickets.jqzx)
def test1():
    driver = webdriver.Firefox()
    driver.get("https://www.jiqizhixin.com/")

    
    print_log(chain(get_cover(driver),
                    get_latest(driver),
                    get_hot_articles(driver)))
    driver.close()

if __name__ == "__main__":
   main()
