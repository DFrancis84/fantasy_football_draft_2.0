import time
from .displays import create_table_per_round, show_draft_picks_by_manager
from .picks import Pick


def snake_draft(number_picks, number_teams, league_name, managers_list):
    """The Entire Draft Process"""
    print(managers_list)
    _p_ = 0
    i = 0
    for _ in range(number_picks):
        print("{} is on the clock....".format(managers_list[i]))
        show_draft_picks_by_manager(league_name, managers_list[i])
        player_first_name = input("Please enter players first name: ").upper()
        player_last_name = input("Please enter players last name: ").upper()
        player_position = input("Please enter players position: ").upper()
        player_team = input("Please enter players team: ").upper()
        pick = Pick()
        pick.create_pick(player_first_name,
                         player_last_name,
                         player_position,
                         player_team)
        pick.add_pick(league_name, managers_list[i])
        _p_ += 1
        i += 1
        if _p_%int(number_teams) == 0:
            create_table_per_round(league_name, number_teams)
        time.sleep(1)
