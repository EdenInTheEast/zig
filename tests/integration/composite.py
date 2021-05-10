
import logging

from runner import LiveServerThread, LiveServerProcess
from browsers import ApiParser, SeleniumBrowser 

from zig import Zig


"""class ThreadComposite:

    def __init__(self, thread=None):
        # use a common 
        self.app = app
"""

logger = logging.getLogger(__name__)


class Controller(object):
    """ Able to plug in any type of server
    """
    #NOTE: Question, should thread and process both be managed by the same object?
    # what problems might it cause?
    # NOTE PRO: test code can decide on its own either to use thread or subprocess
    # from the same interface

    def __init__(self, *arg, thread=None, process=None, **kwargs):
        self.thread_started = None
        self.process_started = None  

        self.server_thread = thread if thread else LiveServerThread()
        self.server_process = process if process else LiveServerProcess() 
        

    def __call__(self, *args, **kwarg):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.server_thread and self.thread_started:
            # close thread
            try:
                self.server_thread.close()
            except Exception:
                #TODO: need a better way to handle this
                raise
            finally:
                self.server_thread.join()
                logger.info("thread exit")

        if self.process_started and self.server_process:
            try: 
                self.server_process.close()
            finally:
                self.server_process.join()

            logger.info("Subprocess exit")

    def start_server_thread(self, app: Zig):
        # assign zig app here
        self.server_thread.app = app

        try:
	        self.server_thread.start()
        except RuntimeError:
            raise

        self.thread_started = self.server_thread.is_alive() 
        return self.server_thread
    
    def start_subprocess(self, app: Zig):
        # set this up with gunicorn
        # other options 
        # TODO: test compatibility with WSGI server
        self.server_process.app = app
            
        try:
            self.server_process.start()
        except RuntimeError:
            raise

        self.process_started = self.server_process.is_alive()
        return self.server_process
    


class ApiParserThread(Controller, ApiParser):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class SeleniumBrowserThread(Controller, SeleniumBrowser):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        SeleniumBrowser.__init__(self, *args, **kwargs) 


