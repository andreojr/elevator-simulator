from elevator.render import Render
from elevator.controls.input import Input
from elevator.controls.output import Output
from elevator.systems.handlers.buttons import ButtonsHandler

class Elevator():
    def __init__(self):
        self.render = Render()
        self.input = Input()
        self.output = Output()
        self.queue = []

    def run(self):
        while True:
            self.render.clear()
            self.render.preview(self.output.display())

            if len(self.queue):
                pass
            else:
                act = self.render.action(self.input.display())
                if not act:
                    break
                self.input.action(act-1)
                ButtonsHandler().update(self.input.buttons, self.output.buttons)
                
