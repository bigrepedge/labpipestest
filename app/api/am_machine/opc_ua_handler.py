# from opcua import Client, ua
from .opc_ua_structure import node_definitions, construct_node_structure, UADataDict, Client, ua
import numpy as np


class AMHandler:

    def __init__(self):
        self.client = None
        self.connected = False

        self.nodes = node_definitions()
        self.data = UADataDict()

    def start(self, url):
        self.client = Client(url)

    @property
    def root(self):
        return self.client.get_root_node()

    @property
    def objects(self):
        return self.client.get_objects_node()

    def connect(self):
        if self.connected:
            return
        self.client.connect()
        construct_node_structure(self.nodes, opc_entity=self.client, data_handler=self.data)
        self.connected = True

    def disconnect(self):
        if not self.connected:
            return
        self.client.disconnect()
        self.connected = False

    def process_nodes(self, nodes, parent_node=None):
        node_id = None
        if 'base_id' in nodes.keys():
            if parent_node is not None:
                node_id = '{}.{}'.format(parent_node, nodes['base_id'])
            else:
                node_id = nodes['base_id']

        if len(nodes.keys()) > 1:
            for node_key in nodes:
                if node_key is 'base_id':
                    continue
                node = nodes[node_key]
                self.process_nodes(node, parent_node=node_id)

        elif parent_node:
            nodes['node'] = self.client.get_node(node_id)

    def get_act_temp(self, heater, *args, **kwargs):
        """

        possible heating elements:
        Extruder
        Bed
        Chamber

        :param heater: string with heater name, ex: 'Extruder
        :param args:
        :param kwargs:
        :return:
        """
        key_to_value = 'stTempAct.{}'
        if heater == 'Extruder':
            heater = 'arExtruder'
        elif heater == 'Bed':
            heater = 'arBed'
        elif heater == 'Chamber':
            heater = 'arChamber'

        value = self.data[key_to_value.format(heater)]

        if heater == 'arExtruder' and 'extruder' in kwargs.keys():
            extruder = kwargs['extruder'] - 1
            value = value[extruder, :]

        if 'sensor' in kwargs.keys():
            sensor = kwargs['sensor'] - 1
            if len(value.shape) > 1:
                value = value[:, sensor]
            else:
                value = value[sensor]

        if type(value) is np.array:
            value = value.tolist()

        return value

    def get_tar_temp(self, heater, *args, **kwargs):
        """

        possible heating elements:
        Extruder
        Bed
        Chamber

        :param heater: string with heater name, ex: 'Extruder
        :param args:
        :param kwargs:
        :return:
        """
        key_to_value = 'stTempSet.{}'
        if heater == 'Extruder':
            heater = 'arExtruder'
        elif heater == 'Bed':
            heater = 'rBed'
        elif heater == 'Chamber':
            heater = 'rChamber'

        value = self.data[key_to_value.format(heater)]

        if 'extruder' in kwargs.keys():
            extruder = kwargs['extruder'] - 1
            value = value[extruder]

        return value


