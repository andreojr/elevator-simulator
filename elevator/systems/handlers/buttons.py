class ButtonsHandler:
    def __init__(self):
        pass

    def update(self, buttons, leds):
        if buttons['st_button']:
            leds['st_button_led']['status'] = True
        if buttons['nd_button']:
            leds['nd_button_led']['status'] = True
        if buttons['rd_button']:
            leds['rd_button_led']['status'] = True
        if buttons['keep_door_open_button']:
            leds['keep_door_open_button_led']['status'] = True

        return leds
