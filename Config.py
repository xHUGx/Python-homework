
import pathlib
import json
import toml
import configparser
import os

class Config:

    allowed_types = ('json', 'toml', 'ini', 'env')

    def __init__(self):
        self.file_path = 'settings.json'
        self.type = 'json'

    def __init__(self, path : str):
        self.file_path = path
        self.type = pathlib.Path(path).suffix.replace('.','')
        if type not in self.allowed_types:
            raise Exception(f'Unsupported type {self.type}')

    def __init__(self, use_env : bool):
        if use_env == True:
            self.type = 'env'
        else:
            Config.__init__(self)

    def load(self):
        if self.type == 'env':
            for key, value in enumerate(os.environ):
                setattr(self, key, value)
        elif (self.type == 'ini'):
            config = configparser.ConfigParser()
            config.read(self.file_path)
            data = {s: dict(config.items(s)) for s in config.sections()}
            for key, value in enumerate(data):
                setattr(self, key, value)
        else:
            with open(self.file_path, "r") as f:
                if (self.type == 'json'):
                    data = json.load(f)
                    for key, value in enumerate(data):
                        setattr(self, key, value)

                elif (self.type == 'toml'):
                    data = toml.load(f)
                    for key, value in enumerate(data):
                        setattr(self, key, value)

    def reload(self):
        if self.type == 'env':
            for key, value in enumerate(os.environ):
                delattr(self, key)
        elif (self.type == 'ini'):
            config = configparser.ConfigParser()
            config.read(self.file_path)
            data = {s: dict(config.items(s)) for s in config.sections()}
            for key, value in enumerate(data):
                delattr(self, key)
        else:
            with open(self.file_path, "r") as f:
                if (self.type == 'json'):
                    data = json.load(f)
                    for key, value in enumerate(data):
                        delattr(self, key)

                elif (self.type == 'toml'):
                    data = toml.load(f)
                    for key, value in enumerate(data):
                        delattr(self, key)


    def reload_attr(self, name : str):
        if self.type == 'env':
            setattr(self, name, os.environ[name])

        elif (self.type == 'ini'):
            config = configparser.ConfigParser()
            config.read(self.file_path)
            data = {s: dict(config.items(s)) for s in config.sections()}
            setattr(self, name, data[name])
        else:
            with open(self.file_path, "r") as f:
                if (self.type == 'json'):
                    data = json.load(f)
                    setattr(self, name, data[name])

                elif (self.type == 'toml'):
                    data = toml.load(f)
                    setattr(self, name, data[name])