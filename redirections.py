#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import random
import sys

hostname = "localhost"
port = 1234

class myApp(webapp.webApp):
    def process(self, parsedRequest):
        rand_num = random.randint(0, 1000000000)

        return ("302 Found", "<html><head><meta http-equiv='Refresh' content='0; " +
                "url=http://" + str(hostname) + ":" + str(port) + "/" + str(rand_num) + 
                "'></head>"+ 
                "<body>" + str(rand_num) + "</body></html>\r\n")

if __name__ == "__main__":
    try:
        testWebApp = myApp(hostname, port)
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
        sys.exit()
