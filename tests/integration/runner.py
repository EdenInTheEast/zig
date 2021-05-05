
import threading
import uuid
import logging


#logger = logging.getLogger(__name__)


class LiveFlaskServerThread(threading.Thread):
    # uses Flask Server to run tests

    def __init__(self, host, port=0):
        self.host = host
        self.port = port

        self.is_ready = threading.Event()
        super().__init__()


class LiveFlaskServer(object):

    def __init__(self):
        self.port = 8050

        self.stop_route = "/_stop-{}".format(uuid.uuid4().hex)
        self.thread = None
    
    def __call__(self, *args, **kwargs):
        return self.start(*args, **kwargs)
        
    def __enter__(self):
        # doesn't start automatically. need to call it
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop()


    @staticmethod
    def _stop_server():
        stopper = flask.request.environ.get("werkzeug.server.shutdown") 
        stopper()
        return "Flask Server is shutting down"
    

    def start(self, app, **kwargs):
        #add stop route
        app.container.app_instance.add_url_rule(self.stop_route, 
                                                self.stop_route, 
                                                self._stop_server)

        # add error handler
        def __handle_error():
            self._stop_server()

        app.container.app_instance.errorhandler(500)(__handle_error)

        # define run function
        def run():            
            app.run()

        # start thread
        self.thread = threading.Thread(target=run)
        self.thread.daemon = True

        try:
            self.thread.start()
        except RuntimeError: # multiple calls on same thread
            self.started = False 

        self.started = self.thread.is_alive()


    def stop(self):
        #requests.get("{}{}".format(self.url, self.stop_route))
        pass

         

class ClientFlask:
    def __init__(self, server, **kwargs):
        self.server = server

    def start_server(self, app, **kwargs):
        self.server(app, **kwargs)


    def __enter__(self):
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        return 









