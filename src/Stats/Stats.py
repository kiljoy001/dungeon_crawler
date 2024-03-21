class Stats:
    def __init__(self, physical: int, agility: int, willpower: int, charisma: int, intelligence: int):
        self.physical = physical
        self.agility = agility
        self.willpower = willpower
        self.charisma = charisma
        self.intelligence = intelligence

    def modify_stat(self, stat_name, value):
        if hasattr(self, stat_name):
            current_value = getattr(self, stat_name)
            setattr(self, stat_name, current_value + value)

    def calculate_health(self) -> int:
        physical = max(1, self.physical)
        willpower = max(1, self.willpower)
        return round((physical / 5) * (willpower / 2))

    def calculater_magic(self) -> int:
        intelligence = max(1, self.intelligence)
        willpower = max(1, self.willpower)
        return round((willpower / 4) * (intelligence / 3))

    def calculate_psycho(self) -> int:
        """
        Calculates the Psycho power resource pool using willpower and charisma with charisma being favored
        :return: int
        """
        willpower = max(1, self.willpower)
        charisma = max(1, self.charisma)
        return round((willpower / 4) * (charisma / 2))

    def calculate_speed(self) -> int:
        """
        Calculates the speed stat, it is a super stat that takes physical, agility, willpower, and intelligence
        with weights favoring agility and willpower.
        :return: int
        """
        physical = max(1, self.physical)
        agility = max(1, self.agility)
        willpower = max(1, self.willpower)
        intelligence = max(1, self.intelligence)
        return round((agility / 2 + physical / 10) * (willpower / 3 + intelligence / 10))

    def calculate_guile(self) -> int:
        """
        Calculates the guile sub stat, it is a combination of charisma and intelligence. Charisma is
        favored over intelligence
        :return: int
        """
        charisma = max(1, self.charisma)
        intelligence = max(1, self.intelligence)
        calculation = charisma / 10 + intelligence / 100
        # normalize value
        probability = (calculation / 100) * 100
        probability = min(max(probability, 0), 100)
        return int(probability)

    def calculate_knowledge(self, stat_max) -> int:
        """
        Calculates probability that player will know something (for items identification or dialogue)
        :param stat_max: int - represents the maximum for that stat, in this case, intelligence
        :return: int
        """
        probability = (self.intelligence / stat_max) * 100
        probability = min(max(probability, 0), 100)
        return int(probability)