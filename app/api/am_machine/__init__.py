from .opc_ua_handler import AMHandler
from .opc_ua_machine import AMServer

Bossy = AMHandler()


class OPCUAMachine:

    def __init__(self, url):
        self.Bossy = Bossy
        self.Vivi = None
        self.url = url

    def start(self, virtual=False):
        if virtual:
            self.Vivi = AMServer()
            self.Vivi.start()
            self.url = self.Vivi.url

        self.Bossy.start(self.url)

    def stop(self):
        if self.Bossy is not None:
            self.Bossy.disconnect()

        if self.Vivi is not None:
            self.Vivi.stop()
