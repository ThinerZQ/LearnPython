import urllib.request as request
import urllib.parse as parse
import string
import re
import os
import urllib.error as error

baseUrl = "http://tieba.baidu.com"

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html

def getPostLink(html):
    reg = r'a href="/p/\d*" title="\S*" target="_blank" class="j_th_tit "'
    postReg = re.compile(reg)
    postLink = re.findall(postReg,html)
    return postLink

def getMemberList(html):
    # print(html)
    # reg = r'a class="manager_btn" title="[\u4e00-\u9fa5]+" target="_blank" href="\S*"'
    reg = r'class="manager_btn" title="[\S*]+"'
    memberReg = re.compile(reg)
    memberLink = re.findall(memberReg,html)
    print(memberLink)












if __name__ == '__main__':
    html = getHtml(baseUrl+"/f?kw=%E6%83%B3%E5%90%AC%E4%BB%80%E4%B9%88baby")
    html = html.decode("utf-8")
    # print(html)
    postLink = getPostLink(html)

    for a in postLink:
        print(a)
    getMemberList(html)