"""Fantasy Football Draft Tool"""
import time
from internal.league import League
from internal.managers import Managers
from internal import generate, displays, style


def start_draft():
    """Starts the Draft"""
    # Print program banner
    displays.print_banner()
    # Set League Definitions
    league = League()
    league.set_league_settings()
    # Create Draft Database
    league.create_board()
    # Run draft based on designated draft type
    managers = Managers()
    managers.add_managers(league.number_teams)
    # Create list of teams
    managers_list = managers.create_draft_order(league.rounds)
    # Enter draft picks into database
    style.snake_draft(league.number_picks, league.number_teams, league.league_name, managers_list)
    # Print notification to let user know draft is complete
    print("Your draft is complete for {}!".format(league.league_name))
    # Small sleep timer for fluiditiy
    time.sleep(3)
    # # Display entire draft results
    displays.show_draft_results(league.league_name)
    # Create csv file from draftboard
    generate.create_csv_from_draft_database(league.league_name)

start_draft()
