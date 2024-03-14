import random
import yaml


class BaseItem:
    """base item class, all items use this as base. Random values can be expressed as random: [min, max] in yaml file"""

    def __init__(self, properties: dict):
        self.stackable = False
        self.stack_count = 1
        for key, value in properties.items():
            if isinstance(value, str) and value.startswith("random:"):
                range_values = value[len("random:"):].strip("[]").split(",")
                min_value, max_value = map(int, range_values)
                random_value = random.randint(min_value, max_value)
                setattr(self, key, random_value)
            elif key == "stackable" and value:
                self.stackable = True
            else:
                setattr(self, key, value)

    @classmethod
    def load_item_from_yaml(cls, yaml_file_location):
        with open(yaml_file_location, 'r') as file:
            item_data = yaml.safe_load(file)
            return [BaseItem(properties=item) for item in item_data]
