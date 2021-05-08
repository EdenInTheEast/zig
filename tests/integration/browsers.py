
import logging
import requests

# typing
from requests import Response 
from typing import Union, List, Type

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 



logger = logging.getLogger(__name__)

class BaseParser:
    # Browser interface

    def __init__(self):
        pass

    def get(self):
        raise NotImplementedError

    def post(self):
        raise NotImplementedError 

    def put(self):
        raise NotImplementedError



class SeleniumBrowser(BaseParser):
    """ Uses Selenium to parse and assert all integration tests

    """

    def __init__(self, url:str=None, 
                 browser: Union[str, List[str]]=None, 
                 headless:bool=True):

        self.url = url

        #NOTE maybe we can use pool pattern to
        # keep the same browser objects?

        self._default_browsers = ["chrome"] 

        # a list of browsers to run tests in
        if isinstance(browser, list):
            self.browsers = browser
        elif isinstance(browser, str) and browser.lower() in self._default_browsers:
            self.browsers = [browser]
        else:
            self.browsers = self._default_browsers 

        self.headless = headless 
        
        
    def get(self, url=None):
        url = url if url else self.url
        self.webdrivers = self._initialize_web_drivers(self.browsers)

        if url is None: raise ValueError("No valid url is given")

        for b in self.webdrivers.values():
            b.get(url)
        
            """try:
                element = WebDriverWait(b, 10).until(EC.presence_of_element((By.ID, "123")))
            """

            b.close() 
            


        #TODO: how to know when ajax is loaded?


    def post(self):
        raise Exception("Use json parser instead. Or test on angular code instead.")
    
    def put(self):
        raise Exception("Use json parser instead. Or test on angular code instead")

    def _initialize_web_drivers(self, browsers):
        drivers = dict()

        for b in self.browsers:
            try:
                drivers[b] = getattr(self, f"{b.lower()}")
            except Exception:
                raise
        return drivers

    @property
    def firefox(self):        
        if not hasattr(self, "__firefox"):
            self.__firefox = self._create_firefox_driver() 
        return self.__firefox 

    def _create_firefox_driver(self):
        return webdriver.FireFox()

    @property
    def chrome(self):        
        if not hasattr(self, "__chrome"):            
            self.__chrome = self._create_chrome_driver() 
        return self.__chrome 

    def _create_chrome_driver(self):
        return webdriver.Chrome()


    def __enter__(self):
        return self
    

    def __exit__(self):
        for b in self.webdrivers.values():
            b.close()



class SeleniumServer(BaseParser):
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


class FlatHTMLParser(BaseParser):
    """ Doesn't use/launch any browser
    Uses requests and BeautifulSoap to parse html response.
    Use this for checking templates' contents quickly.
    Doesn't check user-interaction, front-end rendering 
    or JS applications.
    """

    def __init__(self):
        pass


class ApiParser(BaseParser): 
    """Parser for JSON responses
    Use this to check api responses
    """

    def __init__(self):
        self.url = None
        self.response = None

    def get(self, url):
        try:
            self.response = requests.get(url) 
            return self.response 
        except:
            raise ValueError(f"Invalid url: {url}, unable to process get request")

    def post(self):
        pass

    def put(self):
        pass

    def is_json(self, response: Type[Response]=None):
        # return False if it is not json type
        response = response if response else self.response

        if response.status_code == 200:
            if response.headers['content-type'] == 'application/json':
                return True
        return False

    def get_json(self, response: Type[Response]=None):
        response = response if response else self.response 
        
        if self.is_json(response):
            #implicit is_json assertion
            return response.json()
        else:
            raise Exception("Response is not a JSON response")
        








    
