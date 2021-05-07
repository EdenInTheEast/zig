

import threading
import uuid
import logging
import requests
import flask

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

        # runs Flask/Django server
        self.app.run()


    def close(self):
        #TODO container agnostic method
        #TODO need to get host and port from app
        if self.port:
            stop_url = "".join(["http://", self.host, ":", str(self.port), self.stop_route])
        else: 
            stop_url =  "".join(["http://", self.host, self.stop_route]) 

        requests.get(stop_url)


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



