import os.path
import random
import yaml

class Entity:
    """Basic Game Entity. Allows for yaml defined attributes and properties, two properties can_talk
    and dialogue are required. Dynamic dialogue is provided by the load dialogue method. """

    def __init__(self, properties: dict):
        self.stats = {}
        self.name = properties.get("name", "Unknown")
        self.can_talk = properties.get("can_Talk", False)
        self.dialogue = properties.get("dialogue", None)
        for key, value in properties.items():
            if isinstance(value, str) and value.startswith("random:"):
                range_values = value[len("random:"):].strip("[]").split(",")
                min_value, max_value = map(int, range_values)
                random_value = random.randint(min_value, max_value)
                setattr(self, key, random_value)
            else:
                setattr(self, key, value)

    def load_dialogue(self, dialogue_key: str, context=None) -> str:
        """
        Loads dialogue from yaml files, allows for branching options.
        Takes a key string, and an optional context value
        """
        if not self.can_talk:
            return "It cannot speak!"

        if not os.path.exists(self.dialogue):
            return "It says nothing..."

        # Load dialogue
        with open(self.dialogue, 'r') as file:
            dialogues = yaml.safe_load(file)

        dialogue_entry = dialogues.get(dialogue_key, "This dialogue does not exist!")
        if isinstance(dialogue_entry, str) and dialogue_entry.startswith("!dynamic "):
            function_name = dialogue_entry.split("!dynamic ")[1]
            dialogue_function = getattr(self, function_name, None)
            if callable(dialogue_function):
                return dialogue_function(context)
            else:
                return "Dialogue function does not exist!"
        return dialogue_entry

    @classmethod
    def load_item_from_yaml(cls, yaml_file_location):
        """
        Loads yaml files
        """
        with open(yaml_file_location, 'r') as file:
            item_data = yaml.safe_load(file)
            return [Entity(properties=item) for item in item_data]
