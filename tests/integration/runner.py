import threading
import multiprocessing

import uuid
import logging
import requests
import flask
import time



from typing import Callable

from zig import Zig




logger = logging.getLogger(__name__)


class ServerThread:
    # common interface that can be used by Thread or Process
    # without coupling Thread/Process library to code

    def __init__(self):
        pass

    def start(self):
        raise NotImplementedError

    def run(self):
        super().run() 

    def close(self):
        raise NotImplementedError

    def is_alive(self):
        raise NotImplementedError

    def join(self):
        raise NotImplementedError


class ServerOperations:
    # Operation object that can be instantiate and run by thread/process 
    # NOTE: QUESTIONS
    # Should this be inherited or use as an object(bridge)?
    # Inherit: share the same state, don't need to pass variables around
    # Inherit: can change inheritance in the future too
    # Object: decouple, can swap in another implementation in the future

    def __init__(self):
        self.app = None
        self.stop_route = "/_stop-{}".format(uuid.uuid4().hex)

    @staticmethod
    def _stop_server():
        #TODO: should be container agnostic
        stopper = flask.request.environ.get("werkzeug.server.shutdown") 
        stopper()
        return "Flask Server is shutting down"

    def prepare_app(self, app):
        container = self.app.container.app_instance
        self.app.container.add_url_route(container, 
                                         self.stop_route,
                                         self.stop_route,
                                         self._stop_server
                                        )

        self.host = self.app.container_config.host
        self.port = self.app.container_config.port

        #TODO: need to add container-specific method to get index
        if self.port:
            self.index_url = "".join(["http://", self.host, ":", str(self.port)])
        else: 
            self.index_url =  "".join(["http://", self.host])

    def run(self):
        if not self.app: raise ValueError("Need to pass zig app to thread")

        try:
            self.prepare_app(self.app)
        except:
            raise Exception("Failure to prepare app")

        # runs Flask/Django server
        try:
            self.app.run()
        except:
            # close thread if exception
            raise
        finally:
            logger.info("Server thread is running")

         #wait_for(requests.get(self.index_url), 1000)

    def close(self):
        #TODO container agnostic method
        #TODO need to get host and port from app 
        stop_url =  "".join([self.index_url, self.stop_route]) 

        if self.is_alive():
            try:
                requests.get(stop_url)
            except:
                raise Exception("Cannot reach stop url, or server wasn't started")


class LiveServerThread(ServerThread, ServerOperations):
    """ Uses Flask/Django Server to run tests
    it should be agnostics
    """

    def __init__(self):
        # set app later
        self.thread = threading.Thread(target=self.run) 
        ServerOperations.__init__(self)

    def start(self):
        self.thread.start()

    def is_alive(self):
        return self.thread.is_alive()

    def join(self):
        self.thread.join()

    def close(self):
        ServerOperations.close(self) 


class LiveServerProcess(ServerThread, ServerOperations):
   
    def __init__(self):
        self.process = multiprocessing.Process(target=self.run)

    def start(self):
        self.process.start()

    def close(self):
        if self.is_alive():
            try:
                self.process.close()        
            except ValueError:
                logging.debug("process wass still running. It will be forced killed")
                self.process.kill()
                
    def is_alive(self):
        self.process.is_alive()

    def join(self):
        self.process.join()

    def run(self):
        ServerOperations.run(self)
        


def wait_for(condition: Callable, time_out, expected_output=True, poll=0.1):
    res = condition()
    end_time = time.time() + time_out

    while res != expected_output:
        if time.time() > end_time:
            raise Exception("timeout")
            
        time.sleep(poll)
        # try again
        res=condition()

    return res


"""

class ThreadController(object):
    # Able to plug in any type of server

    def __init__(self, app):
        self.app = app
        self.server_thread = None

    def __call__(self, *args, **kwarg):
        self.start_thread(*args, **kwarg)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return

    def start_thread(self, app: Zig, thread_class: ServerThread=None):
        
        thread_class = thread_class if thread_class else LiveFlaskServerThread 

        self.server_thread = thread_class(app)

        try:
	        self.server_thread.start()
        except RuntimeError:
            raise

        self.started = self.server_thread.is_alive() 

        return self.server_thread


def thread(app):
    self.server_thread = LiveFlaskServerThread(app)

    try:
	    self.server_thread.start()
    except RuntimeError:
        raise

    self.started = self.thread.is_alive()

"""



