# -*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from itertools import chain
from jqzx_data  import jqzx as tickets_repo
import pdb
import gitlab
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

def submit_gitlab_issue(url,token,user,project,issues):
    gl = gitlab.Gitlab(url,private_token=token)
    gl.auth()
    projects = gl.projects.list()
    dl_prj = gl.projects.get('{}/{}'.format(user,projects))
    #dl_prj = gl.projects.get('victor/DeepLearning')
    #issues = dl_prj.issues.list()
    ##<class 'gitlab.v4.objects.ProjectIssue'> => {u'due_date': None, 
    # u'description': u'https://github.com/Microsoft/pai\nhttp://www.kejilie.com/leiphone/article/yMNv2u.html\n* [ ]  \u5982\u4f55\u89e3\u51b3DevOp\u4e0eAI\u7684\u7ed3\u5408\u7684\u95ee\u9898\n* [ ] pai \u73b0\u5728\u5904\u4e8e\u4e00\u4e2a\u4ec0\u4e48\u6c34\u5e73\uff0c\u662f\u5426\u53ef\u7528\u3002',
    # u'confidential': False, 
    # u'downvotes': 0, 
    # u'labels': [], 
    # u'updated_at': u'2018-05-28T05:09:26.109Z', 
    # u'iid': 1, u'assignee': None, 
    # u'web_url': u'http://121.199.2.29:18080/victor/DeepLearning/issues/1',
    # u'milestone': None, 
    # u'discussion_locked': None, 
    # u'closed_at': None, 
    # u'assignees': [],
    #  u'id': 5, 
    # u'title': u'OpenPAI  MSRA\u8054\u624b\u56fd\u5185\u56db\u5927\u9876\u7ea7\u9ad8\u6821\u5171\u5efa\u65b0\u4e00\u4ee3\u4eba\u5de5\u667a\u80fd\u5f00\u653e\u79d1\u7814\u6559\u80b2\u5e73\u53f0', 
    # u'created_at': u'2018-05-28T05:09:26.109Z', 
    # u'author': {u'username': u'victor', u'web_url': u'http://121.199.2.29:18080/victor', u'name': u'victorli', u'state': u'active', u'avatar_url': u'https://www.gravatar.com/avatar/591d5066a13a937a28ebd0f196d75781?s=80&d=identicon', u'id': 2}, u'closed_by': None, u'time_stats': {u'time_estimate': 0, u'human_total_time_spent': None, u'human_time_estimate': None, u'total_time_spent': 0}, u'state': u'opened', u'user_notes_count': 0, u'upvotes': 0, u'project_id': 11}
    #
    for i in issues:
        dl_prj.issues.create(i)
        issue.save()


def update_from_file():

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
if __name__ == "__main__":
   submit_gitlab_issue()
   #main()
