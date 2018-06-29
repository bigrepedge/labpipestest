# from opcua import Server
from .opc_ua_structure import node_definitions, NAMESPACES, construct_node_structure, Server
from .machine_systems_simulation import system_builder, functions_definitions
import threading
import random
import time


class AMServer:

    def __init__(self):
        self.url = "opc.tcp://0.0.0.0:4840/"

        self.server = Server()
        self.server.set_endpoint(self.url)

        for namespace in NAMESPACES:
            self.server.register_namespace(namespace)

        self.nodes = node_definitions()
        node_structure_server = construct_node_structure(self.nodes, self.server)

        self.serving = False
        self._running = False
        self.process_thread = threading.Thread(target=self.proccess, args=(self,))

        self.machine_functions = system_builder(functions_definitions(), node_structure_server)

    def _start_process(self):
        self._running = True
        self.process_thread.start()

    def setup_nodes(self):
        pass

    def start(self):
        if self.serving:
            return
        self._start_process()
        self.server.start()
        self.serving = True

    def stop(self):
        if not self.serving:
            return
        self.server.stop()
        self._running = False
        self.serving = False

    def proccess(self, *args, **kwargs):
        while self._running:
            time.sleep(0.1)
            for system in self.machine_functions:
                self.machine_functions[system].process()


if __name__ == '__main__':
    Vivi = AMServer()
    try:
        Vivi.start()
        while True:
            pass
    finally:
        Vivi.stop()
