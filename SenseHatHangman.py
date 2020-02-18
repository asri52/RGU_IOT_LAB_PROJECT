from sense_hat import SenseHat
import time

# Module for drawing Hangman drawings using the Sense HAT LED matrix
class SenseHatHangman:

    X = [135, 64, 8]  # Brown
    O = [255, 255, 255]  # White
    B = [0, 0, 255] # Blue
    G = [0, 255, 0] # Green


    # lights/display for each step
    step_O = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O 
    ]

    step_1 = [
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_2 = [
    X, X, X, X, X, X, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_3 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, O, O, O,
    X, O, X, O, O, O, O, O,
    X, X, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_4 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_5 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_6 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, O, O, B, O, O,
    X, O, O, O, O, B, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_7 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, O, O, B, B, G,
    X, O, O, O, O, B, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_8 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, G, B, B, B, G,
    X, O, O, O, O, B, O, O,
    X, O, O, O, O, O, O, O,
    X, O, O, O, O, O, O, O 
    ]

    step_9 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, G, B, B, B, G,
    X, O, O, O, O, B, O, O,
    X, O, O, O, O, O, B, O,
    X, O, O, O, O, O, O, G 
    ]

    step_10 = [
    X, X, X, X, X, X, O, O,
    X, O, O, X, O, X, O, O,
    X, O, X, O, O, X, O, O,
    X, X, O, O, O, G, O, O,
    X, O, O, G, B, B, B, G,
    X, O, O, O, O, B, O, O,
    X, O, O, O, B, O, B, O,
    X, O, O, G, O, O, O, G 
    ]

    # all of the steps in order
    steps = [step_O, step_1, step_2, step_3, step_4, step_5, step_6, step_7, step_8, step_9, step_10]

    def __init__(self):
        self.sense = SenseHat()
        self.index = 0
        
    def start(self):
        self.sense.set_pixels(self.step_O)
        self.index = 0
        
    def wrongGuess(self):
        if self.index < 10:
            self.index += 1
            self.sense.set_pixels(self.steps[self.index])
       
    
    def gameOver(self):
        self.sense.show_message("Game Over")
        
    def winner(self, w):
        self.sense.show_message("Congratulations, you guessed %s"%w)

