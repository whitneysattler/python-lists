from tkinter import * # Import all definitions from tkinter
from random import randint

# Return a random color string in the form ##RRGGBB
def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15)) # Add a random digit
    return color

# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord("0"))
    else:
        return chr(hexValue - 10 + ord("A"))

# Define a Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x # starting center position
        self.y = y
        if randint(0,1) == 1:
            self.dx = 2
        else:
            self.dx = -2
        if randint(0,1) == 1:
            self.dy = 2
        else:
            self.dy = -2
        self.radius = 3 # The radius is fixed
        self.color = getRandomColor() # Get random color

class BounceBalls:
    def __init__(self):
        self.ballList = [] # Create a list for balls

        window = Tk() # Create a window
        window.title("Bouncing Balls") # Set a title

        self.width = 350 # Width of the self.canvas
        self.height = 150 # Height of the self.canvas
        self.canvas = Canvas(window, bg = "white", width = self.width, height = self.height)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()
        btStop = Button(frame, text = "Stop", command = self.stop)
        btStop.pack(side = LEFT)
        btResume = Button(frame, text = "Resume", command = self.resume)
        btResume.pack(side = LEFT)
        btAdd = Button(frame, text = "+", command = self.add)
        btAdd.pack(side = LEFT)
        btRemove = Button(frame, text = "-", command = self.remove)
        btRemove.pack(side = LEFT)

        self.sleepTime = 100 # Set a sleep time
        self.isStopped = False
        self.animate()

        window.mainloop() # Create an event loop

    def stop(self): # Stop animation
        self.isStopped = True

    def resume(self): # Resume animation
        self.isStopped = False
        self.animate()

    def add(self): # Add a new ball
        self.ballList.append(Ball(randint(0, self.width), randint(0, self.height)))

    def remove(self): # Remove the last ball
        self.ballList.pop()

    def animate(self): # Animate ball movements
        while not self.isStopped:
            self.canvas.after(self.sleepTime) # Sleep
            self.canvas.update() # Update self.canvas
            self.canvas.delete("ball")

            for ball in self.ballList:
                self.redisplayBall(ball)

    def redisplayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, ball.y - ball.radius, ball.x + ball.radius, ball.y + ball.radius, fill = ball.color, tags = "ball")

BounceBalls() # Create GUI
