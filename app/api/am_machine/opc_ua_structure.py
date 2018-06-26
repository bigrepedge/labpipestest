from opcua import ua, Server, Client
import numpy as np
import logging
import yaml
import os

logger = logging.getLogger(__name__)

NAMESPACES = (
    'http://opcfoundation.org/UA/',
    'urn:IndraControl:OpcUa-Server',
    'http://www.boschrexroth.com/IndraLogic',
    '',
    'http://opcfoundation.org/UA/DI/',
    'http://PLCopen.org/OpcUa/IEC61131-3/',
    'http://sercos.org/UA/',
    'http://boschrexroth.com/OpcUa/Sercos/Objects/',
    '',
    '',
    'http://boschrexroth.com/OpcUa/Device/Objects/',
    '',
    '',
    '',
    '',
    'http://boschrexroth.com/OpcUa/DiagnosisLogbook/Types/',
    'http://boschrexroth.com/OpcUa/DiagnosisLogbook/Objects/',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    'http://boschrexroth.com/OpcUa/Filesystem/Types/',
    'http://boschrexroth.com/OpcUa/Filesystem/Objects/',
    'http://boschrexroth.com/OpcUa/CNC/Objects/',
    'http://boschrexroth.com/OpcUa/CNC/Types/',
    'http://boschrexroth.com/OpcUa/CNC/Motion/Types/',
)


class UABasic:
    def __init__(self, parent=None, idx=-1, bname='', opc_entity=None, *args, **kwargs):
        self.parent = parent

        if idx == -1 and parent is not None:
            idx = parent.idx
        self.namespace_idx = idx

        self.bname = bname
        self.children = dict()

        self.data_handler =None
        if 'data_handler' in kwargs:
            self.data_handler = kwargs['data_handler']

        self.object_ids = None
        if 'identifier' in kwargs:
            self.identifier = kwargs['identifier']

        self.opc_entity = opc_entity

        self.node = None
        if type(opc_entity) is Server and parent is None:
            self.node = opc_entity.get_objects_node()
        elif type(opc_entity) is Client or parent is not None:
            self.add_self_node()

    def add_self_node(self):
        raise NotImplementedError

    def add_child(self, **kwargs):
        child_type = kwargs['type']
        if ('opc_entity' not in kwargs or kwargs['opc_entity'] is None) and self.opc_entity is not None:
            kwargs['opc_entity'] = self.opc_entity
        if ('data_handler' not in kwargs or kwargs['data_handler'] is None) and self.data_handler is not None:
            kwargs['data_handler'] = self.data_handler

        child = None
        if child_type == 'object':
            child = UAObject(parent=self,  **kwargs)
        elif child_type == 'variable':
            child = UAVariable(parent=self, **kwargs)
        elif child_type == 'folder':
            child = UAFolder(parent=self, **kwargs)

        if child is not None:
            self.children[child.bname] = child

        return child

    @property
    def idx(self):
        return self.namespace_idx

    @property
    def get_path(self):
        if type(self) is UABasic:
            return ''

        path = ''
        if self.parent is not None:
            path = '{}.{}'.format(self.parent.get_path, self.identifier)

        return path

    @property
    def node_id(self):
        identifier = self.get_path
        if type(self.identifier) is int:
            identifier = self.identifier

        return ua.NodeId(identifier, self.namespace_idx)


class UAHost(UABasic):

    def __init__(self, *args, **kwargs):
        UABasic.__init__(self, *args, **kwargs)

    def get_node(self, key):
        keys = key.split('.')
        n = len(keys)
        d = self

        value = None
        for i in range(n):
            if len(keys[i]) > 0:
                if i < (n - 1):
                    d = d.children[keys[i]]
                else:
                    value = d.children[keys[i]].node

        return value


class UAVariable(UABasic):
    def __init__(self, parent=None, idx=-1, bname='', default_value=None, data_type=None, *args, **kwargs):
        self._data_type = data_type
        self.default_value = default_value

        UABasic.__init__(self, parent, idx, bname, *args, **kwargs)

    @property
    def data_type(self):
        if self._data_type is None:
            return None
        return ua.VariantType[self._data_type]

    def add_self_node(self):
        if self.parent is not None and self.parent.node is not None:
            parent_node = self.parent.node
            self.node = parent_node.add_variable(self.node_id, self.bname, self.default_value, self.data_type)
            self.node.set_writable()

        elif type(self.opc_entity) is Client:
            self.node = self.opc_entity.get_node(self.node_id)
            if self.data_handler is not None:
                self.data_handler[self.get_path] = self.node.get_value()
                self.data_handler[self.get_path + '.node'] = self.node
                handler = DataChangeHandler(self.data_handler, self.get_path)
                data_change = self.opc_entity.create_subscription(10, handler)
                data_change.subscribe_data_change(self.node)


class UAObject(UABasic):
    def __init__(self, *args, **kwargs):
        self.object_type = None
        if 'object_type' in kwargs:
            self.object_type = kwargs['object_type']
        UABasic.__init__(self, *args, **kwargs)

    def add_self_node(self):
        if self.parent is not None and self.parent.node is not None:
            parent_node = self.parent.node
            self.node = parent_node.add_object(self.node_id, self.bname, objecttype=self.object_type)

        elif type(self.opc_entity) is Client:
            pass


class UAFolder(UABasic):
    def __init__(self, parent=None, idx=-1, bname='', *args, **kwargs):
        UABasic.__init__(self, parent, idx, bname, *args, **kwargs)

    def add_self_node(self):
        if self.parent is not None and self.parent.node is not None:
            parent_node = self.parent.node
            self.node = parent_node.add_folder(self.node_id, self.bname)

        elif type(self.opc_entity) is Client:
            pass


def recursive_node_contructor(parent, children, opc_entity=None, data_handler=None):
    for child_name in children:
        child = children[child_name]
        ua_child = parent.add_child(**child, opc_entity=opc_entity, data_handler=data_handler)
        if 'children' in child:
            grand_children = child['children']
            recursive_node_contructor(ua_child, grand_children)


def construct_node_structure(node_info, opc_entity=None, data_handler=None):
    struct = UAHost(opc_entity=opc_entity, data_handler=data_handler)
    recursive_node_contructor(struct, node_info, opc_entity=opc_entity, data_handler=data_handler)
    return struct


class DataChangeHandler:
    def __init__(self, data_dict, key):
        self.data = data_dict
        self.key = key

    def datachange_notification(self, node, val, data):
        if type(val) is list:
            val = np.array(val)
        self.data[self.key] = val
        logger.info('{} -> {}'.format(self.key, val))


class UADataDict(dict):

    def __getitem__(self, key):
        keys = key.replace('/', '.').split('.')
        n = len(keys)
        d = self
        get_node = False
        if keys[-1] == 'node':
            keys.pop()
            get_node = True
        value = None
        for i in range(n):
            if len(keys[i]) > 0:
                if i < (n - 1):
                    if d == self:
                        d = dict.__getitem__(self, keys[i])
                    else:
                        d = d[keys[i]]
                else:
                    if d == self:
                        value = dict.__getitem__(self, keys[i])
                    else:
                        value = d[keys[i]]

        if type(value) is dict and 'val' in value.keys():
            if not get_node:
                value = value['val']
            else:
                value = value['node']

        return value

    def __setitem__(self, item, value):
        keys = item.split('.')
        if keys[-1] == 'node':
            keys.pop()
            value = dict(val=self['.'.join(keys)], node=value)

        n = len(keys)
        d = self
        for i in range(n):
            if len(keys[i]) > 0:
                if i < (n - 1):
                    if keys[i] not in d:
                        if d == self:
                            dict.__setitem__(self, keys[i], dict())
                        else:
                            d[keys[i]] = dict()
                    d = d[keys[i]]
                else:
                    if d == self:
                        dict.__setitem__(self, keys[i], value)
                    else:
                        d[keys[i]] = value


def node_definitions():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'node_structure.yaml')
    data = None
    with open(file_path, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return data


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # from opcua import Server, Client

    print('setup server')
    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/")

    node_structure_server = construct_node_structure(node_definitions(), server)

    server.start()

    #print('setup client')
    #client = Client("opc.tcp://0.0.0.0:4840/")
    #data = UADataDict()
    #client.connect()  # NOTE: need to connect before making subscription

    #node_structure_client = construct_node_structure(node_definitions(), opc_entity=client, data_handler=data)

    try:
        while True:
            pass

    finally:
        #client.disconnect()
        server.stop()

