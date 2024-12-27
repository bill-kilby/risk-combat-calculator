from time import time

class test_result:
    def __init__(self, test_title: str):
        self.title = f"{test_title[:65]:>65}" # Force to be 30 chars.
        self.attacker_results = []
        self.defender_results = []
        self.attacker_wins = []
        self.defender_wins = []
        self.time_taken = 0.0


    def start_execution_timer(self) -> None:
        if (self.time_taken == 0.0):
            self.time_taken = time()
    

    def end_execution_timer(self) -> None:
        if (self.time_taken != 0.0):
            self.time_taken = int((time() - self.time_taken) * 1000)

    def add_winner(self, team: str) -> None:
        if (team == "attacker"):
            self.attacker_wins.append(1)
            self.defender_wins.append(0)
        else:
            self.attacker_wins.append(0)
            self.defender_wins.append(1)


    def add_result(self, team: str, result: int) -> None:
        if (team == "attacker"):
            self.attacker_results.append(result)
        else:
            self.defender_results.append(result)


    # to 3 dp
    def get_average_results(self, team: str) -> float:
        result_list = []
        if (team == "attacker"):
            result_list = self.attacker_results
        else:
            result_list = self.defender_results
        total = sum(result_list)
        avg = total / len(result_list)
        return int(avg * 1000) / 1000
    

    # to 3 dp
    def get_average_wins(self, team: str) -> float:
        result_list = []
        if (team == "attacker"):
            result_list = self.attacker_wins
        else:
            result_list = self.defender_wins
        total = sum(result_list)
        avg = total / len(result_list)
        return int(avg * 1000) / 1000
   
    
    def average_winner(self) -> str:
        attacker_avg = self.get_average_wins("attacker")
        defender_avg = self.get_average_wins("defender")
        if (attacker_avg > defender_avg):
            return "attacker"
        elif (attacker_avg == defender_avg):
            return "draw"
        return "defender"
    
    
    
    def average_results(self) -> str:
        attacker_avg = self.get_average_results("attacker")
        defender_avg = self.get_average_results("defender")
        if (attacker_avg > defender_avg):
            return "attacker"
        elif (attacker_avg == defender_avg):
            return "draw"
        return "defender"
    
