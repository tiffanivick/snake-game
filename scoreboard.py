from turtle import Turtle
ALIGNMENT = "center"
FRONT = ("Courier", 24, "normal")

# score needs to be in the center at the top of the screen
# score needs to be tracked inside the scoreboard class
# score needs to increase by one every time the snake eats a piece of food
# snake needs to increase by one every time it eats a piece of food
# clear writing every time you update the score


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FRONT)

    def reset(self):
        # if the score is greater than high score
        if self.score > self.high_score:
            # set score as new high score
            self.high_score = self.score
            # open txt file in write mode
            with open("data.txt", mode="w") as data:
                # write the new high score to the file
                data.write(f"{self.high_score}")
        # reset score to zero
        self.score = 0
        # update scoreboard to show new high score and the reset value of zero
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



