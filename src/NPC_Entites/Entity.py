import os.path
import yaml


class Entity:
    """Basic Game Entity"""

    def __init__(self, destructible: bool, movable: bool, talks: bool, animation_location: str, dialogue_location: str):
        self.is_Destructable = destructible
        self.is_Moveable = movable
        self.can_Talk = talks
        self.animation = animation_location
        self.dialogue = dialogue_location

    def load_dialogue(self, dialogue_key: str) -> str:
        if not self.can_Talk:
            return "It cannot speak!"

        if not os.path.exists(self.dialogue):
            return "It says nothing..."

        # Load dialogue
        with open(self.dialogue, 'r') as file:
            dialogues = yaml.safe_load(file)
            return dialogues.get(dialogue_key, "This dialogue does not exist!")
