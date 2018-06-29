import yaml
import os


class Settings(object):

    def __init__(self):
        self._data = self.yaml_reader("settings.yaml")

    def __getitem__(self, item):
        return self._data[item]

    @staticmethod
    def yaml_reader(file):
        data = None
        file_path = os.path.join(os.getcwd(), file)
        if not os.path.isfile(file_path):
            dir_path = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(dir_path, 'default_settings.yaml')
        with open(file_path, 'r') as stream:
            try:
                data = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

        return data


Machine_Settings = Settings()

