import random
import time


def generate_rolls(attack_dice: int, defense_dice: int) -> tuple[list[int], list[int]]:
    """
    Generates rolls; returns attack rolls and defense rolls.
    """

    rolls_attack_army = [random.randint(1, 6) for _ in range(attack_dice)]
    rolls_attack_army.sort(reverse=True)

    rolls_defense_army = [random.randint(1, 6) for _ in range(defense_dice)]
    rolls_defense_army.sort(reverse=True)

    return rolls_attack_army, rolls_defense_army


def check_results(rolls_attack_army: list[int], rolls_defense_army: list[int], least_dice: int) -> int:
    """
    Checks who won the turn; returns 0 if attack won, 1 if defense won, 2 if draw.
    """

    attack_wins = 0
    defense_wins = 0
    for i in range(least_dice):
        if rolls_attack_army[i] > rolls_defense_army[i]:
            attack_wins += 1
        else:
            defense_wins += 1

    if attack_wins > defense_wins:
        turn_win = 0
    elif defense_wins > attack_wins:
        turn_win = 1
    else:
        turn_win = 2

    return turn_win


def simulate(N_SIMULATIONS: int, attack_dice: int, defense_dice: int, least_dice: int) -> tuple[int, int, int]:
    """
    Simulates N_SIMULATIONS turns; returns number of attack wins, defense wins and draws.
    """

    attack_wins = 0
    defense_wins = 0
    draws = 0
    for _ in range(N_SIMULATIONS):
        rolls_attack_army, rolls_defense_army = generate_rolls(
            attack_dice=attack_dice, defense_dice=defense_dice)
        turn_win = check_results(
            rolls_attack_army=rolls_attack_army, rolls_defense_army=rolls_defense_army, least_dice=least_dice)
        if turn_win == 0:
            attack_wins += 1
        elif turn_win == 1:
            defense_wins += 1
        else:
            draws += 1

    return attack_wins, defense_wins, draws


def print_results(attack_wins, defense_wins, draws, execution_time, attack_dice, defense_dice, n_simulations) -> None:
    """
    Print results to console; returns None.
    """

    total_turns = attack_wins + defense_wins + draws
    attack_wins_percentage = attack_wins * 100 / total_turns
    defense_wins_percentage = defense_wins * 100 / total_turns
    draws_percentage = draws * 100 / total_turns

    print("*" * 50)
    print(
        f"Execution time: {execution_time} s\nNumber of simulations: {n_simulations:,}")
    print("-" * 5)
    print(f"Attack dice = {attack_dice}\nDefense dice = {defense_dice}")
    print("-" * 3)
    print(
        f"Attack turn wins = {attack_wins}\nDefense turn wins = {defense_wins}\nDraws = {draws}")
    print("-" * 3)
    print(
        f"Attack turn wins percentage = {attack_wins_percentage}\nDefense turn wins percentage = {defense_wins_percentage}\nDraws percentage = {draws_percentage}")
    print("*" * 50)


def main() -> None:
    """
    Run the script, contains editable values.
    """

    # editable values
    N_SIMULATIONS = 1_000_000  # higher = more accuracy
    attack_dice = 3  # number of dice used by attack
    defense_dice = 3  # number of dice used by defense
    # end editable values

    m = attack_dice if attack_dice < defense_dice else defense_dice

    start = time.perf_counter()

    attack_wins, defense_wins, draws = simulate(
        N_SIMULATIONS=N_SIMULATIONS, attack_dice=attack_dice, defense_dice=defense_dice, least_dice=m)

    end = time.perf_counter()
    execution_time = end - start

    print_results(attack_wins=attack_wins, defense_wins=defense_wins, draws=draws,
                  execution_time=execution_time, attack_dice=attack_dice, defense_dice=defense_dice, n_simulations=N_SIMULATIONS)


if __name__ == "__main__":
    main()
