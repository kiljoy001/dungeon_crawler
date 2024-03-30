from src.Items.BaseItem import BaseItem


class BaseAttack(BaseItem):
    def __init__(self, properties: dict):
        super().__init__(properties)
        self.attack_type = properties.get("attack_type", "physical")
        self.attack_stats = properties.get("base_stats", [])
