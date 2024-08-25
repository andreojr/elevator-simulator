import os, platform

class Render():
    def __init__(self):
        pass

    def clear(self):
        os.system("cls" if platform.system() == "Windows" else "clear")

    def action(self, inputs):
        print('[0] Sair')
        i = 0
        for group in inputs.values():
            for key in group.keys():
                print(f"[{i+1}] {key}")
                i += 1
        return int(input('Acionar '))

    def preview(self, outputs):
        for key, group in outputs.items():
            print(key)
            output = ""
            for value in group.values():
                output += value["icon"] if value["status"] else "⬛"
            print(output, end="\n\n")
