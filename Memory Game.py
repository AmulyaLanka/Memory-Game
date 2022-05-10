############################################
# Amulya Lanka
# CIS 2531
# Final Project : Memory Game
############################################

# imports
from graphics import *
import random
import time

# class
class Memory():

    # initializations
    def __init__(self, point, lenny):

        # attributes
        self.__location = point
        self.__face = lenny
        self.__point1 = Point((self.__location.getX() - 25), (self.__location.getY() - 25))
        self.__point2 = Point((self.__location.getX() + 25), (self.__location.getY() + 25))
        self.__button = Rectangle(self.__point1, self.__point2)

    # getter
    def getface(self):
        return self.__face

    # method to hide the rectangle and show lenny face
    def showFace(self, win):
        textBox = Text(self.__location, self.__face)
        textBox.draw(win)
        time.sleep(.5)
        textBox.undraw()

    # customizing button aka rectangle
    def drawButton(self, win):
        self.__button.setFill('gray')
        self.__button.draw(win)

    # check if the cursor is clicking around the button areas
    def clickTheButton(self, win, click):
        clickX = click.getX()
        clickY = click.getY()

        if clickX >= self.__point1.getX() and clickX <= self.__point2.getX() and clickY >= self.__point1.getY() and clickY <= self.__point2.getY():
            self.__button.undraw()
            self.showFace(win)
            return True
        else:
            return False

# main
def main():
    win = GraphWin("Memory Game", 500, 200)
    win.setBackground(color_rgb(242, 247, 244))

    # time
    start = time.time()

    # list of lenny faces
    data = ["( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)","ಠ_ಠ",
            "( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "ಠ_ಠ"]

    # list of points where the lenny faces can be places, under the rectangles
    listOfPoints = [Point(50,50), Point(150, 50), Point(250, 50), Point(350, 50), Point(450, 50),
                    Point(50, 150), Point(150, 150), Point(250, 150), Point(350, 150), Point(450, 150)]

    #shuffle either listofpoints or data
    random.shuffle(data)
    cards = []
    for i in range(10):
        cards.append(Memory(listOfPoints[i], data[i]))

    for card in cards:
        card.drawButton(win)

    matchesCount = 0
    while matchesCount != 5:
        click = win.getMouse()
        card1 = 0
        card2 = 0

        for card in cards:
            if card.clickTheButton(win, click):
                break
            else:
                card1 += 1
        click = win.getMouse()

        for card in cards:
            if card.clickTheButton(win, click):
                break
            else:
                card2 += 1

        if cards[card1].getface() == cards[card2].getface():
            if card1 < card2:
                cards.pop(card2)
                cards.pop(card1)
            else:
                cards.pop(card1)
                cards.pop(card2)
            matchesCount += 1
        else:
            cards[card1].drawButton(win)
            cards[card2].drawButton(win)

    time.sleep(.1)

    # prints time the user spent on the game
    end = time.time()
    timeSpent = end - start
    print("You've spent about", timeSpent, "seconds")


if __name__ == '__main__':
    main()





