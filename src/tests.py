"""
Tests a series of functions to determine that they are still working properly
"""
import mechanics


def check_exact(actual, expected) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (str): actual value
        expected (str): expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0


def check_range(actual, low, high) -> int:
    """checks for error, returns 1 if error exists, 0 if it doesn't

    Args:
        actual (str): actual value
        expected (str): expected value
    """
    if actual < low or actual > high:
        print(f"Actual: {actual} is not within range {low} and {high}")
        return 1
    return 0


def test_roll_dice() -> int:
    """
    Tests the function... test_roll_dice()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(len(mechanics.roll_dice(1, 4)), 1)
    failure_count += check_exact(len(mechanics.roll_dice(10, 4)), 10)
    failure_count += check_range((mechanics.roll_dice(1, 4))[0], 1, 4)
    return failure_count


def test_nat_one() -> int:
    """
    Tests the function... test_nat_one()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(mechanics.nat_one(1), True)
    failure_count += check_exact(mechanics.nat_one(10), False)
    failure_count += check_exact(mechanics.nat_one(-1), False)
    return failure_count


def test_nat_twenty() -> int:
    """
    Tests the function... test_nat_twenty()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(mechanics.nat_twenty(20), True)
    failure_count += check_exact(mechanics.nat_twenty(10), False)
    failure_count += check_exact(mechanics.nat_twenty(-1), False)
    return failure_count


def test_degree_of_success() -> int:
    """
    Tests the function... test_degree_of_success()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(mechanics.degree_of_success(28, 14), -1)
    failure_count += check_exact(mechanics.degree_of_success(28, 29), 1)
    failure_count += check_exact(mechanics.degree_of_success(28, 40), 2)
    failure_count += check_exact(mechanics.degree_of_success(30, 27), 0)
    failure_count += check_exact(mechanics.degree_of_success(28, 24, True), -1)
    failure_count += check_exact(mechanics.degree_of_success(28,
                                 24, nat_twenty=True), 1)
    failure_count += check_exact(mechanics.degree_of_success(28,
                                 28, nat_twenty=True), 2)
    return failure_count


def test_damage_dealt() -> int:
    """
    Tests the function... test_damage_dealt()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(
        mechanics.calculate_damage_dealt([3, 2, 5], 2), 12)
    failure_count += check_exact(
        mechanics.calculate_damage_dealt([3, 1, 5], 2), 11)
    return failure_count


def test_player_input_category() -> int:
    """
    Tests the function... test_player_input_category()
    Will return the total number of failures.

    Return:
        failure_count (int): The total number of failures
    """
    failure_count = 0
    failure_count += check_exact(
        mechanics.player_input_category("move"), "navigation")
    failure_count += check_exact(
        mechanics.player_input_category("start"), "play")
    failure_count += check_exact(
        mechanics.player_input_category("recall knowledge"), "recall knowledge")
    failure_count += check_exact(
        mechanics.player_input_category("cast cantrip spell"), "cast spell")
    failure_count += check_exact(
        mechanics.player_input_category("attack"), "attacking")
    failure_count += check_exact(
        mechanics.player_input_category("potato"), None)
    return failure_count


def main() -> None:
    """
    Runs test functions for the doc.
    """
    failure_count = 0
    failure_count += test_roll_dice()
    failure_count += test_nat_one()
    failure_count += test_nat_twenty()
    failure_count += test_damage_dealt()
    failure_count += test_player_input_category()
    failure_count += test_degree_of_success()

    print(f"Failed {failure_count} tests")


if __name__ == "__main__":
    main()
