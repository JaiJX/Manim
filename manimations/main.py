from manim import * 

class SimpleScene(Scene):
    def construct(self):
       tx = Text("I hate Pyhsics")
       self.play(Write(tx))
       self.wait(2)