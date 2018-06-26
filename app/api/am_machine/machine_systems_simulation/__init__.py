import logging
import os
import yaml

from .filesystem import FileSystem
from .temperature_simulation import ExtruderTemperature


SYSTEM_FUNCTIONS = {
    'ExtruderTemperature': ExtruderTemperature,
    'FileSystem': FileSystem,
}


def recursive_system_constructor(parent_name, children, system, data):
    for child_name in children:
        child = children[child_name]
        name = '{}.{}'.format(parent_name, child_name)

        if 'function' in child:
            func = child['function']
            if func['name'] not in system:
                system[func['name']] = SYSTEM_FUNCTIONS[func['type']](data)
            # TODO: add self to part of function

        if 'children' in child:
            grand_children = child['children']
            recursive_system_constructor(name, grand_children, system, data)


def system_builder(functions, machine):
    systems = dict()
    for func_name in functions:
        this_func = functions[func_name]
        systems[func_name] = SYSTEM_FUNCTIONS[this_func['type']](machine, **this_func)

    return systems


def functions_definitions():
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'systems.yaml')
    data = None
    with open(file_path, 'r') as stream:
        try:
            data = yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    return data


if __name__ == '__main__':
    from opc_ua_structure import node_definitions, construct_node_structure, Server

    nodes = node_definitions()

    server = Server()
    server.set_endpoint("opc.tcp://0.0.0.0:4840/")

    node_structure_server = construct_node_structure(node_definitions(), server)

    s = system_builder(functions_definitions(), node_structure_server)

    try:
        server.start()

        while True:
            for system in s:
                s[system].process()
                # print(node_structure_server.get_node('stTempSet.arExtruder').get_value())
                # print(node_structure_server.get_node('stTempAct.arExtruder').get_value())
    finally:
        server.stop()





