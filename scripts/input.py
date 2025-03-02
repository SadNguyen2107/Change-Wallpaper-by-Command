import argparse


def get_user_input():
    """
    Get user input
    :return: user mood
    """

    # Get user input
    parser = argparse.ArgumentParser(description="Process user mood.")
    parser.add_argument("mood", type=str, help="User mood")
    args = parser.parse_args()

    return args.mood
