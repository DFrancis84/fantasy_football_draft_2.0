def enter_league_definitions():
    """Enter league parameters"""
    league_name = input('Please enter league name: ')
    number_teams = input('How many teams are drafting? ')
    number_rounds = input('How many rounds in this draft? ')
    draft_type = input('Draft Type: Snake or Custom? ').upper()
    number_picks = int(number_teams)*int(number_rounds)
    print("This draft will contain {} picks.".format(number_picks))
    return league_name, number_teams, number_rounds, draft_type, number_picks
