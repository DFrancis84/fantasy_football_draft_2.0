import csv
import sqlite3

def create_csv_from_draft_database(league_name):
    """Convert Database to CSV file"""
    conn = sqlite3.connect('{}.db'.format(league_name))
    cur = conn.cursor()
    cur.execute("SELECT * FROM {}".format(league_name))
    result = cur.fetchall()
    headers = ["pickNumber",
               "managerName",
               "playerFirstName",
               "playerLastName",
               "playerPosition",
               "teamAbbreviation"]
    with open("{}.csv".format(league_name), "w") as csvfile:
        filewriter = csv.writer(csvfile)
        filewriter.writerow(headers)
        for _r_ in result:
            filewriter.writerow(_r_)
