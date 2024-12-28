from time import time


class test_result:
    """
    A class that represents the results of a test.

    Attributes:
        title (str): The title of the test.
        attacker_results (List[int]): The amount of kills the attacker scored, per turn.
        defender_results (List[int]): The amount of kills the defender scored, per turn.
        attacker_wins (List[int]): Whether or not the attacker won the combat (destroyed all batallions), per turn.
        defender_wins (List[int]): Whether or not the defender won the combat (did not get destroyed), per turn.
        time_taken (float): The amount of time taken for the test, in milliseconds.
    """

    
    def __init__(self, test_title: str):
        """
        Initialises the instance.

        Args:
            test_title (str): The title of the test.
        """
        self.title = f"{test_title[:65]:>65}" # Force to be 30 chars.
        self.attacker_results = []
        self.defender_results = []
        self.attacker_wins = []
        self.defender_wins = []
        self.time_taken = 0.0


    def start_execution_timer(self) -> None:
        """
        Starts the timer for the test if it has not been started.
        """
        if (self.time_taken == 0.0):
            self.time_taken = time()
    

    def end_execution_timer(self) -> None:
        """
        Ends the timer for the test if it has been started.
        """
        if (self.time_taken != 0.0):
            self.time_taken = int((time() - self.time_taken) * 1000)


    def add_winner(self, team: str) -> None:
        """
        Adds a winner pair based to the respective object's lists on the winning team.

        Args:
            team (str): The winning team.
        """
        if (team == "attacker"):
            self.attacker_wins.append(1)
            self.defender_wins.append(0)
        else:
            self.attacker_wins.append(0)
            self.defender_wins.append(1)


    def add_result(self, team: str, result: int) -> None:
        """
        Adds a result to the team's result list.

        Args:
            team (str): The team to add the result to.
            result (int): The result that the team achieved (kills).
        """
        if (team == "attacker"):
            self.attacker_results.append(result)
        else:
            self.defender_results.append(result)


    def get_average_results(self, team: str) -> float:
        """
        Returns the average (mean) results of the team to 3 decimal places.

        Args:
            team (str): The team to get the average for.
        """
        result_list = []
        if (team == "attacker"):
            result_list = self.attacker_results
        else:
            result_list = self.defender_results
        total = sum(result_list)
        avg = total / len(result_list)
        return int(avg * 1000) / 1000
    

    def get_average_wins(self, team: str) -> float:
        """
        Returns the average (mean) wins of the team to 3 decimal places.

        Args:
            team (str): The team to get the average for.
        """
        result_list = []
        if (team == "attacker"):
            result_list = self.attacker_wins
        else:
            result_list = self.defender_wins
        total = sum(result_list)
        avg = total / len(result_list)
        return int(avg * 1000) / 1000
    
    
    def average_winner(self) -> str:
        """
        Returns who got more wins, on average.
        """
        attacker_avg = self.get_average_wins("attacker")
        defender_avg = self.get_average_wins("defender")
        if (attacker_avg > defender_avg):
            return "attacker"
        elif (attacker_avg == defender_avg):
            return "draw"
        return "defender"
    
    
    def average_results(self) -> str:
        """
        Returns who got more results, on average.
        """
        attacker_avg = self.get_average_results("attacker")
        defender_avg = self.get_average_results("defender")
        if (attacker_avg > defender_avg):
            return "attacker"
        elif (attacker_avg == defender_avg):
            return "draw"
        return "defender"