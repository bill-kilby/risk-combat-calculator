from colorama import Fore, Style
from typing import List, TextIO
from uuid import uuid4
import re
from test_result import test_result


def format_team_results(team:str, result: test_result) -> str:
    """
    Formats the team results, colouring them on win/lose/draw.

    Args:
        team (str): The team to format the output for.
        result (test_result): The result of the test run.

    Returns:
        str: The formatted team results output.
    """
    result_str = ""
    average_result = result.average_results()
    if (average_result == team):
        result_str += Fore.GREEN
    elif (average_result == "draw"):
        result_str += Fore.LIGHTYELLOW_EX
    else:
        result_str += Fore.RED
    result_str += str(result.get_average_results(team))
    result_str += Style.RESET_ALL
    return f"{result_str:<14}"


def format_team_wins(team: str, result: test_result) -> str:
    """
    Formats the team's wins, colouring them on win/lose/draw.

    Args:
        team (str): The team to format the output for.
        result (test_result): The result of the test run.

    Returns:
        str: The formatted team wins output.
    """
    result_str = ""
    average_result = result.average_winner()
    if (average_result == team):
        result_str += Fore.GREEN
    elif (average_result == "draw"):
        result_str += Fore.LIGHTYELLOW_EX
    else:
        result_str += Fore.RED
    result_str += str(result.get_average_wins(team))
    result_str += Style.RESET_ALL
    return f"{result_str:<14}"


def format_team_output(team: str, result: test_result) -> str:
    """
    Formats the team output to be displayed to the console.

    Args:
        team (str): The team to format the output for.
        result (test_result): The result of the test run.

    Returns:
        str: The formatted team output.
    """
    output_str = format_team_results(team, result)
    output_str += " | "
    output_str += format_team_wins(team, result)
    return output_str


def handle_title_params(title_str: str) -> str:
    """
    Handles the title parameters and formats them into a readable string.

    Args:
        title_str (str): The title string to format.

    Returns:
        str: The formatted title params.
    """
    title_params = title_str.split(",")
    title = ""
    for param in title_params:
        title += f"{param.split(':')[1].strip()},"
    return title


def remove_ansi_escape(test_str: str) -> str:
    """
    Removes ANSI escape sequences from a string.

    Args:
        test_str (str): The string to remove ANSI escape sequences from.

    Returns:
        str: The string with ANSI escape sequences removed.
    """
    return re.sub(r'\x1b\[[0-9;]*[mK]', '', test_str)


def get_writable_test_result(test_str: str) -> str:
    """
    Gets the test result string to be written to the csv.

    Args:
        test_str (str): The output string that was output to the console.

    Returns:
        str: The result string to be written to the csv.
    """
    test_str = remove_ansi_escape(test_str)
    return test_str.split("|", 1)[1].strip()


def get_writable_team_output(result_str: str, title: str) -> str:
    """
    Formats the team output to be written to the csv.

    Args:
        result_str (str): The result string to be formatted into csv format.
        title (str): The title of the test case.

    Returns:
        str: The writable csv version of the team console output.
    """
    output_str = title + result_str
    output_str = output_str.replace(" | ",",")
    output_str = output_str.strip()
    return output_str


def write_test_result(test_str: str, result: test_result, result_file: TextIO) -> None:
    """
    Handles writing of the test result to the csv.

    Args:
        test_str (str): The output string that was output to the console.
        result (test_result): The result of the test run.
        result_file (TextIO): The file to write the result to.
    """
    test_result_str = get_writable_test_result(test_str)
    formatted_title = handle_title_params(result.title)
    output_str = get_writable_team_output(test_result_str, formatted_title)
    result_file.write(f"{output_str}\n")


def output_test_result(result: test_result, result_file: TextIO) -> None:
    """
    Handles output and writing of the test result to the console and csv, respectively.

    Args:
        result (test_result): The result of the test run.
        result_file(TextIO): The file to write the result to.
    """
    attacker_str = format_team_output("attacker", result)
    defender_str = format_team_output("defender", result)
    output_str = f"{result.title} | {attacker_str} | {defender_str} | {result.time_taken}ms"
    print(output_str)
    write_test_result(output_str, result, result_file)


def output_test_header(result_file: TextIO) -> None:
    """
    Handles output and writing of the header to the console and csv, respectively.

    Args:
        result_file (TextIO): The file to write the header to.
    """
    print(f"{'TEST NAME':>65} | {'AKils':<5} | {'AWins':<5} | {'DKils':<5} | {'DWins':<5} | {'TIME TAKEN':<10}")
    result_file.write(
        "Attackers,Defenders,Attacker Leader,Defender Leader,Stronghold,"
        "Average Attacker Kills,Average Attacker Wins,Average Defender Kills,"
        "Average Defender Wins,Test Run Time\n"
    )


def output_all_test_results(test_results: List[test_result]) -> None:
    """
    Starts the pipeline to run all of the results all of the tests to the console and writes to csv.

    Args:
        test_results (List[test_result]): The results of the test runs.
    """
    result_file = open(f"./{uuid4()}.csv", "w")
    output_test_header(result_file)
    for result in test_results:
        output_test_result(result, result_file)
