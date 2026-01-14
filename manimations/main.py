from manim import * 

class SimpleScene(Scene):
    def construct(self):
       tx = Text("A person who thinks all the time has nothing")
       tx2 = Text("to think about except thoughts")
       sq = Square(10, stroke_color=GREEN, fill_color=BLUE, fill_opacity=0.5)
       self.play(Write(tx))
       self.play(Write(tx2.next_to(tx, DOWN)))
       self.play(Create(sq))
       self.wait(2)