class test_case:
    def __init__(self, attackers: int, defenders: int, attacker_has_leader: bool, defender_has_leader: bool, has_stronghold: bool):
        self.attackers = attackers
        self.defenders = defenders
        self.attacker_has_leader = attacker_has_leader
        self.defender_has_leader = defender_has_leader
        self.has_stronghold = has_stronghold

    def __str__(self):
        return f"Atk: {self.attackers}, Def: {self.defenders}, AtkLead: {self.attacker_has_leader}, DefLead: {self.defender_has_leader}, Strhold: {self.has_stronghold}"
