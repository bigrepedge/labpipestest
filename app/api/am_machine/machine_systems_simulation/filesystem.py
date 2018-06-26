import os
from opcua import ua


from .base import BasicSystem


class FileSystem(BasicSystem):
    ua_dir_type = 13353
    ua_file_type = 11575

    def __init__(self, data_handler, inputs=None, outputs=None, **kwargs):
        BasicSystem.__init__(self, data_handler, inputs, outputs)

        options = dict()
        if 'options' in kwargs:
            options = kwargs['options']

        if 'dir' in options:
            self.mnt_dir = os.path.abspath(options['dir'])
        else:
            self.mnt_dir = os.path.abspath('./mnt')

        base_node = self.data_handler.get_node('Filesystem')

        if not os.path.isdir(self.mnt_dir):
            os.mkdir(self.mnt_dir)

        self.mnt_node = base_node.add_object(ua.NodeId('/mnt', 26), 'mnt', objecttype=self.ua_dir_type)
        self.recursive_file_list(self.mnt_dir, self.mnt_node)

    def recursive_file_list(self, parent_path, parent_node):
        for ent in os.listdir(parent_path):
            ent_path = os.path.join(self.mnt_dir, ent)
            print(ent_path)
            rel_path = '/{}'.format(os.path.relpath(ent_path, os.path.abspath('.')))
            if os.path.isfile(ent_path):
                parent_node.add_object(ua.NodeId(rel_path, 26), ent, objecttype=self.ua_file_type)
            elif os.path.isdir(ent_path):
                ent_node = parent_node.add_object(ua.NodeId(rel_path, 26), ent, objecttype=self.ua_dir_type)
                self.recursive_file_list(ent_path, ent_node)

    def process(self):

        pass
