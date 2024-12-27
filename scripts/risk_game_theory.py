from colorama import just_fix_windows_console, Fore, Back, Style
from sys import argv
from random import randrange
from test_result import test_result
from test_case import test_case
from uuid import uuid4
import re


# Maybe a bit too verbose... but useful for testing.
test_cases = [
    test_case(attackers=1, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=2, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=3, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=1, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=2, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=3, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=1, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=2, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=3, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=1, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=2, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=3, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=False),
    test_case(attackers=1, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=2, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=3, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=1, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=2, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=3, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=1, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=2, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=3, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=1, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=2, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=3, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=False),
    test_case(attackers=1, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=2, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=3, defenders=1, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=1, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=2, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=3, defenders=2, attacker_has_leader=True, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=1, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=2, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=3, defenders=1, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=1, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=2, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=3, defenders=2, attacker_has_leader=False, defender_has_leader=True, has_stronghold=True),
    test_case(attackers=1, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=2, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=3, defenders=1, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=1, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=2, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=3, defenders=2, attacker_has_leader=True, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=1, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=2, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=3, defenders=1, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=1, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=2, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True),
    test_case(attackers=3, defenders=2, attacker_has_leader=False, defender_has_leader=False, has_stronghold=True)
]


#
# So we have done:
# Calculating the amount of average losses.
# But we should also do -> if we win, as a full stop.
# Because this is just as important!


# TODO: Add absolute wins. We might lose troops. But do we win the territory?
# 1. Add this to test_result
# 2. Log this in run_test_case so that it logs who wins in the test_reuslt
# 3. Change the output so that it returns who actually won the most territory.
# 4. Add the two columns. They'll add up to one.
# 5. Change the colours on the average kills.


def format_team_output(team: str, result: test_result) -> str:
    output_str = ""
    average_result = result.average_results()
    if (average_result == team):
        output_str += Fore.GREEN
    elif (average_result == "draw"):
        output_str += Fore.LIGHTYELLOW_EX
    else:
        output_str += Fore.RED
    output_str += str(result.get_average_results(team))
    output_str += Style.RESET_ALL
    output_str += " | "
    average_result = result.average_winner()
    if (average_result == team):
        output_str += Fore.GREEN
    elif (average_result == "draw"):
        output_str += Fore.LIGHTYELLOW_EX
    else:
        output_str += Fore.RED
    output_str += str(result.get_average_wins(team))
    output_str += Style.RESET_ALL
    return output_str


def output_test_result(result: test_result, result_file) -> None:
    attacker_str = format_team_output("attacker", result)
    defender_str = format_team_output("defender", result)
    output_str = f"{result.title} | {attacker_str} | {defender_str} | {result.time_taken}ms"
    print(output_str)
    output_str = re.sub(r'\x1b\[[0-9;]*[mK]', '', output_str)
    output_str = output_str.split("|", 1)[1].strip()
    title_params = result.title.split(",")
    formatted_title = f"{title_params[0].split(":")[1].strip()}"
    formatted_title += f",{title_params[1].split(":")[1].strip()}"
    formatted_title += f",{title_params[2].split(":")[1].strip()}"
    formatted_title += f",{title_params[3].split(":")[1].strip()}"
    formatted_title += f",{title_params[4].split(":")[1].strip()},"
    output_str = formatted_title + output_str
    output_str = output_str.replace(" | ",",")
    output_str = output_str.strip()
    result_file.write(f"{output_str}\n")


def output_test_header():
    print("some header")


"""
Starts the pipeline to run all of the results all of the tests to the console and writes to csv.
"""
def output_all_test_results(test_results: list[test_result]) -> None:
    result_file = open(f"./{uuid4()}.csv", "w")
    print("                                                        TEST NAME | Akils | AWins | DKill | DWins | TIME TAKEN")
    result_file.write("Attackers,Defenders,Attacker Leader, Defender Leader,Stronghold,Average Attacker Kills,Average Attacker Wins,Average Defender Kills,Average Defender Wins,Test Run Time\n")
    for result in test_results:
        output_test_result(result, result_file)


"""
Gets rolls depending on the amount of batallions and any modifiers.

Args:
    rolls (int): The amount of rolls.
    has_leader (bool): Whether or not the batallion has a leader (+1 to highest if so).
    has_stronghold (bool): Whether or not the batallion has a stronghold (+1 to highest if so).

Returns:
    list[int]: The rolls (1-6 inclusive) for each batallion, sorted by highest first.
"""
def get_rolls(rolls: int, has_leader: bool, has_stronghold: bool) -> list[int]:
    roll_results = []
    for _ in range(0, rolls):
        roll = randrange(1, 7) # As inclusive->exclusive.
        roll_results.append(roll)
    roll_results.sort(reverse=True)
    if (has_leader):
        roll_results[0] += 1
    if (has_stronghold):
        roll_results[0] += 1
    return roll_results


"""
Returns the results of a singular test case.

Args:
    test (test_case): The test case to run.

Returns:
    list[int]: The results, formatted as [Attacker Kills, Defender Kills]
"""
def get_test_case_results(test: test_case) -> list[int]:
    # Get rolls.
    attacker_rolls = get_rolls(test.attackers, test.attacker_has_leader, False)
    defender_rolls = get_rolls(test.defenders, test.defender_has_leader, test.has_stronghold)
    attacker_kills, defender_kills = 0,0
    # Compare first always - there'll always be one defending and one attacking.
    if (attacker_rolls[0] > defender_rolls[0]):
        attacker_kills += 1
    else:
        defender_kills += 1
    # Compare second if there is a second defender - this is not always the case.
    if (test.attackers >= 2 and test.defenders >= 2):
        if (attacker_rolls[1] > defender_rolls[1]):
            attacker_kills += 1
        else:
            defender_kills += 1
    # Output and return the results of the test.
    print(f"A rolls {attacker_rolls}, and D rolls {defender_rolls} causing A to get {attacker_kills} kills and D to get {defender_kills} kills.")
    return [attacker_kills, defender_kills]


"""
Handles the test case results, adding these to the respective properties in the test_result object.

Args:
    result (test_result): The result object to adjust/handle.
    results (list[int]): The results from the single test run.
    defenders (int): The amount of defenders, to calculate the winner.
"""
def handle_test_case_results(result: test_result, results: list[int], defenders: int) -> None:
    result.add_result("attacker", results[0])
    result.add_result("defender", results[1])
    if (results[0] == defenders):
        result.add_winner("attacker")
    else:
        result.add_winner("defender")


"""
Handles running a single test case x amount of times (where x is test_runs). It collects these results
and returns them in a test_result object.

Args:
    test (test_case): The test case definition object.
    test_runs (int): The amount of tests to be ran for this test case.

Returns:
    test_result: A test result object containing data on the test run(s) results.
"""
def handle_test_case_execution(test: test_case, test_runs: int) -> test_result:
    print(f"\nRunning test case: {test}")
    result = test_result(f"{test}")
    result.start_execution_timer()
    for _ in range(0, test_runs):
        results = get_test_case_results(test)
        handle_test_case_results(result, results, test.defenders)
    result.end_execution_timer()
    return result


"""
Handles running all test cases and collecting the results.

Args:
    test_runs (int): The amount of test runs to execute per test case.

Returns:
    list[test_result]: A list of the test case results.
"""
def run_tests(test_runs: int) -> list[test_result]:
    test_results = []
    for test in test_cases:
        test_results.append(handle_test_case_execution(test, test_runs))
    return test_results


"""
Starts the pipeline for running and outputting the program.

Args:
    test_runs (int): The amount of test runs to execute per test case.
"""
def execute(test_runs: int) -> None:
    test_results = run_tests(test_runs)
    output_all_test_results(test_results)
    exit()



if __name__ == "__main__":
    just_fix_windows_console()
    if len(argv) == 2:
        if argv[1].isdigit():
            test_runs = int(argv[1])
            execute(test_runs)
    print("Please provide amount of test runs!")
    print("For example: 'python risk_game_theory.py 500' for 500 runs per test.")