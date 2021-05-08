
from runner2 import LiveServerThread
from browsers import ApiParser, SeleniumBrowser 


from zig import Zig



"""class ThreadComposite:

    def __init__(self, thread=None):
        # use a common 
        self.app = app
"""


class Controller(object):
    """ Able to plug in any type of server

    """
    def __init__(self, *arg, thread=None, **kwargs):
        self.started = None
        self.server_thread = thread if thread else LiveServerThread()

    def __call__(self, *args, **kwarg):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.started and self.server_thread:
            # close thread
            self.server_thread.close()

        else:
            raise Exception(exc_value)
        


    def start_server_thread(self, app: Zig):
        # assign zig app here
        self.server_thread.app = app

        try:
	        self.server_thread.start()
        except RuntimeError:
            raise

        self.started = self.server_thread.is_alive() 

        return self.server_thread


    def start_subprocess(self):
        # set this up with gunicorn
        # other options 
        # TODO: test compatibility with WSGI server
        pass


class ApiParserThread(Controller, ApiParser):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class SeleniumBrowserThread(Controller, SeleniumBrowser):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        SeleniumBrowser.__init__(self, *args, **kwargs) 



