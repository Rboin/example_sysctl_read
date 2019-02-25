import json


class JsonSerializable:

    def __init__(self):
        pass

    def to_json(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.to_json()


class ServiceInfo(JsonSerializable):

    def __init__(self, key, value):
        JsonSerializable.__init__(self)
        self.key = key
        self.value = value


