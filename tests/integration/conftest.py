import pytest


from runner2 import ClientFlask, LiveFlaskServer 
from composite import ApiParserThread, SeleniumBrowserThread

@pytest.fixture
def api_parser():
    # json parser
    try:
        with ApiParserThread() as parser:
            yield parser
    except Exception as e:
        raise Exception("unable to create thread")


@pytest.fixture
def selenium_browser():
    # selenium browser: all browsers
    with SeleniumBrowserThread() as browser:
        yield browser 


@pytest.fixture
def chrome_browser():
    # selenium browser: just chrome
    with SeleniumBrowserThread(browser="chrome") as browser:
        yield browser 


@pytest.fixture
def thread_server():
    with LiveFlaskServer() as starter:
        yield starter

@pytest.fixture
def server(thread_server):
    with ClientFlask(thread_server) as cf:
        yield cf

@pytest.fixture
def browser():
    with SeleniumBrowser() as b:
        yield b








