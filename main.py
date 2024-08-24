import os, platform

# elevator_data = {
#     'open_when': None,
#     'next_floor': None,
# }

interface = {
    'input': {
        'st_button': False,
        'nd_button': False,
        'rd_button': False,
        'keep_door_open_button': False,
        'emergency_flip': False,
        'increase_people_flip': False,
        'decrease_people_flip': False,
    },
    'output': {
        'st_button_led': False,
        'nd_button_led': False,
        'rd_button_led': False,
        'st_floor_led': False,
        'nd_floor_led': False,
        'rd_floor_led': False,
        'moving_led': False,
        'auth_move_led': False,
        'emergency_led': False,
        'door_status_led': False,
        'up_led': False,
        'down_led': False,

    },
}

UP = "\x1B[99A"
CLR = "\x1B[0K"

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

n = int(input("Quantas ações quer executar? "))
for _ in range(n):
    clear()
    txt_input = "Acionar:\n"
    for i, key in enumerate(interface.keys()):
        txt_input += f"[{i+1}] {key}\n"
    act = int(input(txt_input))
