

import threading
import uuid
import logging
import requests
import flask


from typing import Callable

from zig import Zig



class ServerThread:
    # interface
    def __init__(self):
        pass



class LiveServerThread(threading.Thread, ServerThread):
    """ Uses Flask/Django Server to run tests
    it should be agnostics
    """

    def __init__(self):
        # set app later
        self.app = None
        self.stop_route = "/_stop-{}".format(uuid.uuid4().hex)
        self.is_ready = threading.Event()
        super().__init__()

    @staticmethod
    def _stop_server():
        #TODO: should be container agnostic
        stopper = flask.request.environ.get("werkzeug.server.shutdown") 
        stopper()
        return "Flask Server is shutting down"


    def run(self):
        if not self.app: raise ValueError("Need to pass zig app to thread")

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

        # runs Flask/Django server
        self.app.run()

        #wait_for(requests.get(self.index_url), 1000)


    def close(self):
        #TODO container agnostic method
        #TODO need to get host and port from app 
        stop_url =  "".join([self.index_url, self.stop_route]) 

        requests.get(stop_url)


"""
def wait_for(condition: Callable, timeout, poll=1):
    res = condition()
    end_time = time.time() + time_out

    while not res:
        if time.time() > end_time:
            raise Exception("timeout")
            
        time.sleep(poll)
        # try again
        res=condition()
    return res




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



