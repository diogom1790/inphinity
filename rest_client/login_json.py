import json

class LoginJson(object):

    def __init__(self, jsonValue = ""):

        self.jsonData = jsonValue
        assert self.is_json(jsonValue) == True

    def is_json(self, jsonData):
        try:
            jsonData = json.dumps(jsonData)
            json_object = json.loads(jsonData)
        except ValueError as error:
            print("invalid json: %s" % error)
            return False
        self.jsonData = json.loads(jsonData)
        return True

    def lodingData(self):
        if 'error' in self.jsonData:
            print(self.jsonData['error'])
            return None
        else:
            return self.jsonData['name'], self.jsonData['token']