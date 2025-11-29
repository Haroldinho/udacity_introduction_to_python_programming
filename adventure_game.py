"""
Simple version of an old-fashioned text-based adventure game.

First assignment of the Udacity Introduction to Programming with Python I
 course.

Date: 2025-11-28
"""

# You can use this workspace to write and submit your adventure game project.
import random
import time
from typing import List

# Optional: set the seed for reproducible testing
random.seed(42)

# Base probabilities that are common across locations
BASE_PROBABILITIES = {"dragon": 0.1}

# Location-specific probability overrides
LOCATION_SPECIFIC_PROBABILITIES = {
    "castle": {"knight": 0.8, "troll": 0.1, "villain": 0.6, "fairy": 0.0},
    "cave": {"knight": 0.6, "troll": 0.1, "villain": 0.3, "fairy": 0.0},
    "village": {"knight": 0.6, "troll": 0.1, "villain": 0.4, "fairy": 0.1},
    "open_field": {"knight": 0.4, "troll": 0.3, "villain": 0.4, "fairy": 0.4},
    "ancient_fortress": {
        "knight": 0.5, "troll": 0.3, "villain": 0.1, "fairy": 0.2
    },
    "river": {
        "knight": 0.1, "troll": 0.8, "villain": 0.6, "fairy": 0.6
    },
    "ruins": {
        "knight": 0.1,
        "troll": 0.6,
        "villain": 0.3,
        "fairy": 0.9,
    },
    "woods": {"knight": 0.1, "troll": 0.6, "villain": 0.7, "fairy": 0.1},
}

# Build complete probability dictionary by merging base and location-specific


def build_villain_probabilities():
    """Build complete villain probability dictionary for each location."""
    result = {}
    for location, specific_probs in LOCATION_SPECIFIC_PROBABILITIES.items():
        result[location] = {**BASE_PROBABILITIES, **specific_probs}
    return result


config = {
    "player_options": ["knight", "troll", "villain"],
    "map": {
        "castle": [
            "cave", "village", "open_field", "ancient_fortress", "ruins"
        ],
        "cave": ["castle", "river", "woods"],
        "village": ["castle", "cave", "open_field", "ancient_fortress"],
        "river": ["cave", "woods"],
        "woods": ["cave", "river"],
        "open_field": ["castle", "cave", "village", "ancient_fortress"],
        "ancient_fortress": ["castle", "cave", "village", "open_field"],
        "ruins": [
            "castle", "cave", "village", "open_field", "ancient_fortress"
        ],
    },
    "chance_of_meeting_a_villain_by_location": build_villain_probabilities(),
    "risks_of_death_by_direct_conflict": {
        "knight": {
            "knight": 0.2, "troll": 0.5, "villain": 0.1, "dragon": 0.4,
            "fairy": 0.1
        },
        "troll": {
            "knight": 0.3, "troll": 0.5, "villain": 0.1, "dragon": 0.8,
            "fairy": 0.8
        },
        "villain": {
            "knight": 0.6, "troll": 0.5, "villain": 0.3, "dragon": 0.6,
            "fairy": 0.9
        },
    },
}


def print_starting_text(main_character: str):
    """Print the starting text for the game."""
    print(f"You are a {main_character}")
    time.sleep(0.1)
    print("You stand amidst the moss-covered ruins of an ancient fortress.")
    time.sleep(0.1)
    print(
        "The villagers say a dragon circled this place last night,"
        " drawn by something buried in the rubble."
    )
    time.sleep(0.1)
    print("Shadows shift between the fallen towers—too large to be wolves.")
    time.sleep(0.1)
    print("Trolls have been seen scavenging for relics.")
    time.sleep(0.1)
    print("An evil fairy is also said to be lurking in the ruins.\n\n")
    time.sleep(random.randint(2, 4))


def get_location_input(available_locations: List[str]):
    """Get location choice from player input."""
    print("You can go to the following locations: ")
    for i, location in enumerate(available_locations):
        time.sleep(0.05)
        print(f"\t{i}. {location}")
    time.sleep(0.2)
    # the player input a number for the next location
    try:
        selected_location_option = int(
            input("Enter the number of the next location: ")
        )
        if (
            selected_location_option < 0 or
            selected_location_option >= len(available_locations)
        ):
            print("Invalid location. Please try again.")
            time.sleep(0.4)
            return get_location_input(available_locations)
        selected_location = available_locations[selected_location_option]
        print(f"You chose to go to the {selected_location}")
        time.sleep(0.2)
        return selected_location
    except ValueError:
        print("Invalid input. Please enter a number.")
        time.sleep(0.4)
        return get_location_input(available_locations)


def get_next_location(selected_location: str):
    """Get the next location from the player."""
    if selected_location not in config["map"]:
        raise ValueError(f"Unknown location: {selected_location}")
    available_locations = config["map"][selected_location]
    return get_location_input(available_locations)


def select_enemy_by_probability(location: str) -> str:
    """Select an enemy based on weighted probabilities for the location."""
    if location not in config["chance_of_meeting_a_villain_by_location"]:
        raise ValueError(f"Unknown location: {location}")
    probabilities = config["chance_of_meeting_a_villain_by_location"][location]
    enemies = list(probabilities.keys())
    weights = list(probabilities.values())
    return random.choices(enemies, weights=weights, k=1)[0]


def play_turn_by_turn_game(
    selected_location: str, selected_player: str, turn_count: int = 0,
    max_turns: int = 20
):
    """Play the game turn by turn with a maximum turn limit."""
    if turn_count >= max_turns:
        print(f"You've survived {max_turns} turns! You win!")
        return

    print(f"You are now in the {selected_location}")
    time.sleep(0.2)
    # sample from chance_of_meeting_a_villain_by_location to see
    # who the player will meet in the current location
    selected_enemy = select_enemy_by_probability(selected_location)
    print(
        f"You just met a {selected_enemy}!"
        f"The {selected_enemy} wants to fight you!\n\n"
    )
    # draw the risk of death by direct conflict
    risk_of_death_dict = config["risks_of_death_by_direct_conflict"]
    if selected_player not in risk_of_death_dict:
        raise ValueError(f"Unknown player type: {selected_player}")
    if (
        selected_enemy
        not in risk_of_death_dict[selected_player]
    ):
        raise ValueError(
            f"Unknown enemy type: {selected_enemy} for player: "
            f"{selected_player}"
        )

    selected_risk_of_death = risk_of_death_dict[selected_player][
        selected_enemy
    ]

    # print(f"The risk of death is {selected_risk_of_death}")
    time.sleep(random.randint(2, 4))
    # sample a random number betweeen 0 and 1
    random_number = random.random()
    if random_number < selected_risk_of_death:
        print(f"The {selected_enemy} attacked you. You died!")
    else:
        print(
            f"You survived the attack of the {selected_enemy}!"
            " You can continue your journey.\n\n"
        )
        selected_location = get_next_location(selected_location)
        play_turn_by_turn_game(
            selected_location,
            selected_player,
            turn_count + 1,
            max_turns
        )
    return


def printing_story():
    selected_player = random.choice(config["player_options"])

    print_starting_text(selected_player)
    # the game always starts in the ancient fortress
    selected_location = "ancient_fortress"

    # Give the player options for the next locations
    available_locations = config["map"][selected_location]
    selected_location = get_location_input(available_locations)

    # play turn by turn game
    play_turn_by_turn_game(selected_location, selected_player)
    print("GAME OVER")
    time.sleep(1)
    print("Would you like to play again? (y/n)")
    play_again = input()
    if play_again == "y":
        printing_story()
    else:
        print("Thank you for playing! Goodbye!")
        time.sleep(1)
        exit()


if __name__ == "__main__":
    printing_story()
