import json

class JsonOutputter:
    def __init__(self, mapped_metadata):
        self.mapped_metadata = mapped_metadata

    def _create_nested_structure(self, keys, value, dictionary):
        if len(keys) == 1:
            dictionary[keys[0]] = value
        else:
            key = keys.pop(0)
            if key not in dictionary:
                dictionary[key] = {}
            self._create_nested_structure(keys, value, dictionary[key])

    def generate_nested_json(self):
        nested_dict = {}
        for key, value in self.mapped_metadata.items():
            keys_list = key.split('.')
            self._create_nested_structure(keys_list, value, nested_dict)
        return nested_dict

    def save_to_file(self, file_path):
        nested_json = self.generate_nested_json()
        with open(file_path, 'w') as f:
            json.dump(nested_json, f, indent=4)