class test_case:
    """
    A class that represents a test case.

    Attributes:
        attackers (int): The amount of attackers.
        defenders (int): The amount of defenders.
        attacker_has_leader (bool): Whether or not the attacker has a leader (+1 to top dice if so).
        defender_has_leader (bool): Whether or not the defender has a leader (+1 to top dice if so).
        has_stronghold (bool): Whether or not there is a stronghold in the defender's tile (+1 to top dice if so).
    """


    def __init__(self, attackers: int, defenders: int, attacker_has_leader: bool, defender_has_leader: bool, has_stronghold: bool):
        """
        Initialises the instance.

        Args:
            attackers (int): The amount of attackers.
            defenders (int): The amount of defenders.
            attacker_has_leader (bool): Whether or not the attacker has a leader (+1 to top dice if so).
            defender_has_leader (bool): Whether or not the defender has a leader (+1 to top dice if so).
            has_stronghold (bool): Whether or not there is a stronghold in the defender's tile (+1 to top dice if so).
        """
        self.attackers = attackers
        self.defenders = defenders
        self.attacker_has_leader = attacker_has_leader
        self.defender_has_leader = defender_has_leader
        self.has_stronghold = has_stronghold


    def __str__(self):
        """
        Override of __str__ that formats the test case into a readable string.
        """
        return f"Atk: {self.attackers}, Def: {self.defenders}, AtkLead: {self.attacker_has_leader}, DefLead: {self.defender_has_leader}, Strhold: {self.has_stronghold}"
