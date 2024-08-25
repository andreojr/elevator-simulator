class Output:
    def __init__(self):
        self.buttons = self.buttons_template()
        self.position = self.position_template()
        self.monitoring = self.monitoring_template()

    def buttons_template(self):
        return {
            'st_button_led': {
                'icon': '🟩',
                'status': False,
            },
            'nd_button_led': {
                'icon': '🟩',
                'status': False,
            },
            'rd_button_led': {
                'icon': '🟩',
                'status': False,
            },
            'keep_door_open_button_led': {
                'icon': '↔️',
                'status': False,
            },
        }

    def position_template(self):
        return {
            'st_floor_led': {
                'icon': '🟩',
                'status': True,
            },
            'nd_floor_led': {
                'icon': '🟩',
                'status': False,
            },
            'rd_floor_led': {
                'icon': '🟩',
                'status': False,
            },
        }
    
    def monitoring_template(self):
        return {
            'moving_led': {
                'icon': '🔃',
                'status': False,
            },
            'auth_move_led': {
                'icon': '✅',
                'status': True,
            },
            'door_status_led': {
                'icon': '🔒',
                'status': True, # True = closed, False = open
            },
            'up_led': {
                'icon': '🔼',
                'status': False,
            },
            'down_led': {
                'icon': '🔽',
                'status': False,
            },
            'emergency_led': {
                'icon': '🚨',
                'status': False,
            },
        }
    
    def display(self):
        return {
            'buttons': self.buttons,
            'position': self.position,
            'monitoring': self.monitoring,
        }
