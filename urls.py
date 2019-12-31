import importlib


class App(object):
    def __init__(self, path=None):
        self.path = path
        self.apps = ['login',
                  ]

    def urls(self):
        for app in self.apps:
            if self.path[0] == app:
                importlib.import_module(app)
                object(app).urls.urls(self.path[1,])
        return str(self.path)