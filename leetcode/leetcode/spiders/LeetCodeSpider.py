import scrapy

from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector
import ConfigParser
import os.path
import logging


from ..items import Question, Submission


class LeetCodeSpider(InitSpider):
    name = 'leetcode'
    allowed_domains = ["leetcode.com"]

    config = ConfigParser.RawConfigParser()
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(curr_dir, '../../../settings.cfg')
    config.read(path)

    login_url = config.get('leetcode','login_url')
    start_urls = [config.get('leetcode','problems_url')]
    base_url = config.get('leetcode','base_url')
    USEREMAIL = config.get('leetcode','USEREMAIL')
    PASSWORD = config.get('leetcode','PASSWORD')

    logging.basicConfig(level=logging.INFO)

    question_dict = {} # question_link -> Question
    link_map = {} # submission_link -> question_link, only used internally
    code_map = {} # question_link -> [Submission List]

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_url, callback=self.login)
    

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'login': self.USEREMAIL, 'password': self.PASSWORD },
                    callback=self.check_login_response)


    def check_login_response(self, response):
        # check login succeed before going on
        logging.debug("checking login...")
        if "Sign out" in response.body:
            logging.info("\n\nLOGIN SUCCESS!!\n\n")
            return self.initialized()            
        else:
            logging.error("\n\nLOGINED FAIL\n\n")
            exit()

        
    def parse_ac_submission(self, response):
        """ the code page"""

        print "parse_ac_submission with %s" %(response.url,)
        if "Sign out" in response.body:
            logging.info("\n\nSUBMISSION GOOD!!\n\n")
            
            if "scope.code.java" in response.body:
                logging.debug("scope.code.java FOUND")
                startIndex1 = response.body.find("scope.code.java") + len("scope.code.java")
                endIndex1 = response.body.find("scope.$apply();")
                
                startIndex = response.body.find("public",startIndex1)
                endIndex = response.body.rfind("';",startIndex1,endIndex1)

                logging.debug("startIndex is %d and endIndex is %d" %(startIndex,endIndex) )
                code = response.body[startIndex:endIndex].decode('unicode-escape')
                # logging.debug(code)
                sub = Submission()
                sub['code'] = code
                sub['language'] = 'java'

                # logging.debug(response.url)
                # logging.debug(self.link_map[response.url])
                # logging.debug(self.question_dict[self.link_map[response.url]])
                
                if self.code_map.has_key(self.link_map[response.url]):
                    l = self.code_map[self.link_map[response.url]]
                    l.append(sub)
                    self.code_map[self.link_map[response.url]] = l
                else:
                    self.code_map[self.link_map[response.url]] = [sub]
                
                yield sub

    def parse_ac_problem(self, response):
        """  submissions list page and go to each ac code"""

        logging.debug("parse_ac_problem with %s" %(response.url,))
        if "Sign out" in response.body:
            sel = Selector(response)
            for a in sel.css(".status-accepted::attr('href')"):
                link = "https://oj.leetcode.com" + a.extract()
                logging.debug(link)
                self.link_map[link] = response.url
                yield Request(link,callback=self.parse_ac_submission)
        else:
            logging.error("parse_ac_problem() username not found")
        
        # logging.debug(self.link_map)

    def parse(self, response):
        """ the question list page and go to submissions directly"""

        links = []
        
        if "Sign out" in response.body:
            
            sel = Selector(response)

            for tr in sel.css("#problemList tbody tr"):
                ac = tr.css("td:nth-child(1) span::attr('class')").extract()[0]
                if ac == u'ac':
                    pTitle = tr.css("td:nth-child(2) a::text").extract()[0]
                    pLink = tr.css("td:nth-child(2) a::attr('href')").extract()[0]
                    pDate = tr.css("td:nth-child(3)::text").extract()[0]
                    pRate = tr.css("td:nth-child(4)::text").extract()[0]

                    question = Question()
                    question['title'] = pTitle
                    question['add_date'] = pDate
                    question['ac_rates'] = pRate
                    question['url'] = "https://oj.leetcode.com"+ pLink + "submissions/"
                    
                    links.append(question['url'])
                    self.question_dict[question['url']] = question

                    yield Request(question['url'],callback=self.parse_ac_problem)

                    # uncomment below if need to pipeline
                    # yield question
            # logging.debug(self.question_dict)
            # logging.debug(links)
            
            # for link in links[:5]:    
            #     yield Request(link,callback=self.parse_ac_problem)

        else:
            logging.error("parse() username not found")

    def closed(self,reason):
        logging.info("on closed with reason: "+reason)

        f = open('export.md','wb')

        for (question_link,subs) in self.code_map.iteritems():
            question = self.question_dict[question_link]
            
            f.write("## ")
            f.write(question['title'])
            f.write("\n\n")

            f.write("**")
            f.write(question['ac_rates'])
            f.write("**\n\n")

            f.write("*")
            f.write(question['add_date'])
            f.write("*\n\n")

            f.write("[url](")
            f.write(question['url'])
            f.write(")\n\n")

            for sub in subs:
                f.write("`")
                f.write(sub['language'])
                f.write("`\n\n")

                f.write("```\n\n")
                f.write(sub['code'])
                f.write("\n\n```\n\n")

                
            f.write("====")
            f.write("\r\n\r\n")

            logging.debug(question_link)
            logging.debug(question)
            logging.debug(subs)

        f.close()
            
        logging.debug(len(self.code_map))
        logging.debug(len(self.link_map))
        logging.debug(len(self.question_dict))




