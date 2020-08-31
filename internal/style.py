import time
from .displays import create_table_per_round
from .picks import insert_draft_pick, insert_draft_pick_for_snake_draft

def custom_draft(number_picks, number_teams, league_name, managers_list):
    """The Entire Draft Process"""
    _r_ = 0
    for _ in range(number_picks):
        insert_draft_pick(league_name, managers_list)
        _r_ += 1
        if _r_%int(number_teams) == 0:
            create_table_per_round(league_name, number_teams)
        time.sleep(1)

def snake_draft(number_picks, number_teams, league_name, managers_list):
    """The Entire Draft Process"""
    print(managers_list)
    _p_ = 0
    i = 0
    for _ in range(number_picks):
        insert_draft_pick_for_snake_draft(league_name, managers_list[i])
        _p_ += 1
        i += 1
        if _p_%int(number_teams) == 0:
            create_table_per_round(league_name, number_teams)
        time.sleep(1)
