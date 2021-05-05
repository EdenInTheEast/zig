

import threading
import uuid
import logging


class LiveFlaskServerThread(threading.Thread):
    # uses Flask Server to run tests

    def __init__(self, app):
        self.app = app
        self.stop_route = "/_stop-{}".format(uuid.uuid4().hex)


        self.is_ready = threading.Event()
        super().__init__()


    @staticmethod
    def _stop_server():
        stopper = flask.request.environ.get("werkzeug.server.shutdown") 
        stopper()
        return "Flask Server is shutting down"


    def run(self):
        container = self.app.container.app_instance
        self.app.container.add_url_route(container, 
                                         self.stop_route,
                                         self.stop_route,
                                         self._stop_server
                                        )

        # runs Flask/Django server
        self.app.run()



class FlaskThread(object):

    def __init__(self, app):
        self.app = app
        self.server_thread = None


    def __enter__(self):
        return self.start_thread(self.app)


    def __exit__(self, exc_type, exc_value, exc_traceback):
        return


    def start_thread(self, app):
        self.server_thread = LiveFlaskServerThread(app)

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





