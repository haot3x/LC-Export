import scrapy

from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import Rule
from scrapy.selector import Selector


class LeetCodeSpider(InitSpider):
    name = 'leetcode'
    allowed_domains = ["leetcode.com"]
    login_urls = 'https://oj.leetcode.com/accounts/login/'
    start_urls = ['http://oj.leetcode.com/problems/']
    # _extractor = SgmlLinkExtractor()
    # _extractor = LinkExtractor()
    # rules = (    
    #     Rule(_extractor,callback='parse_ac_problem',follow=True) 
    #     )

    USEREMAIL = 'foo'
    PASSWORD = 'bar'

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_urls, callback=self.login)
    
    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'login': self.USEREMAIL, 'password': self.PASSWORD },
                    callback=self.check_login_response)

    def check_login_response(self, response):
        # check login succeed before going on
        print "checking login"
        if self.USEREMAIL in response.body:
            print "\n\nLOGIN SUCCESS!!\n\n"
            return self.initialized()            
        else:
            print "\n\nLOGINED FAIL\n\n"

        
    def parse_ac_submission(self, response):
        print "parse_ac_submission with %s" %(response.url,)
        if self.USEREMAIL in response.body:
            print "\n\nSUBMISSION GOOD!!\n\n"
            if "scope.code.java" in response.body:
                print "scope.code.java FOUND"
                startIndex = response.body.find("scope.code.java")
                endIndex = response.body.find("scope.$apply();")

                print "startIndex is %d and endIndex is %d" %(startIndex,endIndex)
                print response.body[startIndex:endIndex]
        
    def parse_ac_problem(self, response):
        print "parse_ac_problem with %s" %(response.url,)
        if self.USEREMAIL in response.body:
            print "\n\nGOOD!!\n\n"
            sel = Selector(response)
            for a in sel.css(".status-accepted::attr('href')"):
                link = "https://oj.leetcode.com" + a.extract()
                print link
                yield Request(link,callback=self.parse_ac_submission)

    def parse(self, response):

        print "=========== one come with %s" %(response.url,)

        links = []
        if self.USEREMAIL in response.body:
            print "%s is in the page, all good" % (self.USEREMAIL,)
            sel = Selector(response)

            for tr in sel.css("#problemList tbody tr"):
                ac = tr.css("td:nth-child(1) span::attr('class')").extract()[0]
                if ac == u'ac':
                    print "!!!!!!!! yea ac"
                    pTitle = tr.css("td:nth-child(2) a::text").extract()[0]
                    pLink = tr.css("td:nth-child(2) a::attr('href')").extract()[0]
                    pDate = tr.css("td:nth-child(3)::text").extract()[0]
                    pRate = tr.css("td:nth-child(4)::text").extract()[0]
                    print pTitle
                    print pLink
                    print pDate
                    print pRate
                    links.append(pLink)

            for link in links[:1]:
                link = "https://oj.leetcode.com"+link + "/submissions/"
                yield Request(link,callback=self.parse_ac_problem)
