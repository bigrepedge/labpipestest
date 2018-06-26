import logging

logger = logging.getLogger(__name__)


class BasicSystem:
    dt = 0.1
    logger = logger

    def __init__(self, data_handler, inputs=None, outputs=None):
        self.data_handler = data_handler
        self.inputs = inputs
        self.outputs = outputs

    def process(self):
        raise NotImplementedError