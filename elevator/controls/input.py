class Input():
    def __init__(self):
        self.buttons = self.buttons_template()
        self.flips = self.flips_template()

    def buttons_template(self):
        return {
            'st_button': False,
            'nd_button': False,
            'rd_button': False,
            'keep_door_open_button': False,
        }

    def flips_template(self):
        return {
            'emergency_flip': False,
            'increase_people_flip': False,
            'decrease_people_flip': False,
        }

    def action(self, act):
        if 0 <= act <= 3:
            self.buttons[list(self.buttons.keys())[act]] = True
        elif 4 <= act <= 6:
            self.flips[list(self.flips.keys())[act-4]] = True

    def display(self):
        return {
            'buttons': self.buttons,
            'flips': self.flips,
        }
