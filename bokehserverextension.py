from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    Popen(["bokeh", "server", "bokeh-app", "--allow-websocket-origin=*"])
