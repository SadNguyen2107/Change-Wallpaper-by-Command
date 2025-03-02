import argparse


def get_user_input():
    """
    Get user input
    :param args: user input
    :return: user input
    """

    # Get user input
    parser = argparse.ArgumentParser(description="Process user input.")
    parser.add_argument("mood", type=str, help="User mood")
    args = parser.parse_args()

    return args.mood
