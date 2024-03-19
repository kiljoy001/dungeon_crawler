from src.NPC_Entites.Entity import Entity


class BaseEnemy(Entity):
    def __init__(self, properties: dict):
        super().__init__(properties)
        self.health = properties.get("health", 1000)
        self.attack = properties.get("attack", {})
        self.abilities = properties.get("abilities", [])

