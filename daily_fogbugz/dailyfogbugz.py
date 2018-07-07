#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
Created on Fri Jul 05 13:59:08 2013

@author: vili
"""
from fogbugz import FogBugz
import re
import argparse
import datetime
import time
import random
import logging
logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
import json
import ast
import os
GOOGLER='/usr/local/bin/googler'

def googler(question):
    time.sleep(random.randint(5,20))
    cmd = [GOOGLER,"-c hk", "-n 10", "--np --json" ,question.encode('utf-8')]
    logger.info(cmd)
    cmdstring = " ".join(cmd)
    logger.info(cmdstring)
    out= os.popen(cmdstring).read()
    logger.info(out)
    answers = ast.literal_eval(out)
    return answers



def update_tickets(args):
    cols = ["ixBug","sStatus","sTitle",'sTags',"ixPersonOpenedBy","dtOpened","sProject",'plugin_customfields',"latestEvent"]
    fb = FogBugz('https://daily.manuscript.com/')
    fb.logon(args.email,args.password)
    query = {
        "status": "Active",
        "AssignedTo": "Unassigned"
    }
    querystring = " ".join(["{}:{}".format(k,v) for k,v in query.items()])
    resp = fb.search(q=querystring,cols=",".join(cols))
    for casexml in resp.cases.childGenerator():
        #logger.info("case:##{}".format(casexml))
        logger.debug(casexml['ixBug'])
        id = casexml['ixBug']
        question = casexml.sTitle.getText()
        latest_event = casexml.events
        event_id = latest_event.ixBugEvent.getText()
        message_body = latest_event.s.getText()
        
        answers_string = ""
        pdb.set_trace()
        if message_body =="":
            answers = googler(question)
            for ele in answers:
                answers_string += "\n".join([ele['title'],ele['url'],ele['abstract']])
                answers_string += '\n\n' 
            fb.edit(ixBug=id,sEvent=answers_string,ixPersonAssignedTo=casexml.ixPersonOpenedBy.getText())
        else:
            for line in [ i for i in message_body.split('\n') if i !='']:
                answers_string = ""
                if line.startswith("##"):
                    answers_string += '**' + line[3:].encode('utf-8')
                    answers_string += '\n' 
                    answers = googler(line[3:])
                    for ele in answers:
                        answers_string += "\n".join([ele['title'],ele['url'],ele['abstract']])
                        answers_string += '\n\n' 
                    fb.edit(ixBug=id,ixPersonAssignedTo=casexml.ixPersonOpenedBy.getText(),sEvent=answers_string)
                    #fb.edit(ixBug=id,ixBugEvent=event_id,sEvent=answers_string,ixPersonAssignedT=casexml.ixPersonOpenedBy.getText())
                else:
                  break

def main(args):
    while True:
       time.sleep(random.randint(5*60,6*60))
       update_tickets(args)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="fogbugz search")
    parser.add_argument('--email',help='your email', type=str,default='')
    parser.add_argument('--password',type=str,default='')
    args = parser.parse_args()
    main(args)
        
