
import logging
from typing import Union, List

from selenium import webdriver

logger = logging.getLogger(__name__)


class BaseBrowser:
    # Browser interface

    def __init__(self):
        pass

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError 

    def put(self):
        raise NotImplementedError



class SeleniumBrowser(BaseBrowser):
    """ Uses Selenium to parse and assert all integration tests

    """

    def __init__(self, url, browsers: Union[str, List[str]]=None, headless:bool=True):
        self.url = url

        #NOTE maybe we can use pool pattern to
        # keep the same browser objects?

        # a list of browsers to run tests in
        if browsers:
            self.browers = browers
        else:
            self.browsers = {"Firefox":"_firefox", "Chrome":"_chrome"}


        self.headless = headless 


        for b in self.browsers:
            self.initialize_web_drivers()
        

    def initialize_web_drivers(self, drivers: None):
        drivers = drivers if drivers else self


    def create_web_driver(self, driver):
        # uses lazy initialization pattern
        return getattr(self, self.drivers[driver])

    @property
    def _firefox(self):
        # only create and store if specified
        if not hasattr(self, "__firefox":
            self.__firefox = self._create_firefox_driver()
            return self.__firefox 
        else:
            return self.__firefox

    def _create_firefox_driver(self):
        return self.webdriver.FireFox() 
            

    """ 
    @_firefox.setter
    def _firefox(self, value):
        # value handling
        if value == "initialize":
            self.__firefox == self.webdriver.FireFox() 
            return self.__firefox 
    """

    
    @property
    def _chrome(self):
        pass

    @property
    def _ie(self):
        pass

    @property
    def _opera(self):
        pass

         



class SeleniumServer(BaseBrowser):
    """ Uses Selenium Server to parse and assert all integration tests
    """
        
    def __init__(self, url):
        pass
        

class SeleniumComposite(SeleniumBrowser, SeleniumServer):
    """ Main Selenium Class for testing
    able to switch between Browser or Server mode with main config
    Use SeleniumBrowser or SeleniumServer if need specific mode explicitly 
    """

    def __init__(self):
        pass


class FlatHTMLParser(BaseBrowser):
    """ Doesn't use/launch any browser
    Uses requests and BeautifulSoap to parse html response.
    Use this for checking templates' contents quickly.
    Doesn't check user-interaction, front-end rendering 
    or JS applications.
    """

    def __init__(self):
        pass


class ApiParser() 
    """Parser for JSON responses
    Use this to check api responses
    """

    def __init__(self)
        pass


    
