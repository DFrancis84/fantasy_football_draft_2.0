class Managers():
    def __init__(self):
        self.managers = []
        self.managers_draft_order = []
        self.managers_list = len(self.managers)

    def add_managers(self, number_teams):
        '''Add managers'''
        i = 1
        for i in range(number_teams+1):
            if i < number_teams:
                manager_name = input('Please enter Team #{} name: '.format(i+1))
                self.managers.append(manager_name)
                i += 1
            else:
                break

    def create_draft_order(self, rounds):
        '''Creates draft order based off of managers and number of rounds in draft'''
        i = 1
        self.managers_draft_order = self.managers.copy()
        for i in range(rounds+1):
            if i == 0:
                i += 1
                continue
            if i == 1:
                i += 1
                continue
            if i%2 == 0:
                self.managers_draft_order.extend(self.managers[::-1])
                i += 1
                continue
            if i%2 == 1:
                self.managers_draft_order.extend(self.managers)
                i += 1
                continue
            if i == rounds:
                break
        return self.managers_draft_order
