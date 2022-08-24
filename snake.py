
import turtle, random


class Game:
    '''
Purpose: The purpose of this class is to initialize the game, and begin the game loop.
Instance variables: It setups the board for the playing the game, it is the game function to set up the game for playing, it sets up the player and the foodpellet, allowing the keyboard keys to be associated with up,down, right, and left, and a speedtimer that speeds up the game.
Methods: There is gameloop, the began a gameloop that continues until the player ends the game.
    '''
    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)
     

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.tracer(0,0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        self.player=Snake(315, 315,'green')
        self.ball=Food(90,90,'red')
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        self.player.move(self.ball)
        if self.player.collison() == True:
            turtle.penup()
            turtle.setpos(315, 315)
            turtle.write ('Game Over', align= 'center', font= 'Times 40 normal')
        else:
            turtle.ontimer(self.gameloop, 200)
        turtle.update()
        

        

class Snake:
    '''
Purpose: It inializes the player's snake and the functions of the player's snake
Instance variables: it sets up the velocity of the snake, the length, the color, and grow function that allows the snake to grow when eating the food pellet.
Methods: there's grow that allows the snake to grow when eating a food pellet, there is move method that allows the snake to move with the touch keys function, there is collision; it allows for when the snake hits a border the game is over. and there is a go down, go up, go right and left and it allows for when the player hits a keyboard key it moves it with the corresponding key.
    '''

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.segments = []
        self.grow()
        self.vx = 30
        self.vy = 0
        self.go_down()
       
    def grow(self):
        snake = turtle.Turtle()
        snake.speed(0)
        snake.fillcolor(self.color)
        snake.shape('square')
        snake.shapesize(1.5, 1.5)
        snake.penup()
        snake.setpos(self.x, self.y)
        self.segments.append(snake)
    def move(self, ball):
        self.x +=self.vx
        self.y +=self.vy
        if self.x == ball.foodx and self.y == ball.foody:
            self.grow()
            ball.movefood()
        else:
            for i in range(len(self.segments[:-1])):
                new_posx = self.segments[i+1].xcor()
                new_posy = self.segments[i+1].ycor()
                self.segments[i].setpos((new_posx, new_posy))
            self.segments[-1].setpos((self.x, self.y))  
    def collison(self):
        count = 0
        head = self.segments[-1]
        collide = False
        if head.xcor() > 600 or head.xcor() < 0 or  head.ycor()  > 600 or head.ycor() <0 :
            collide = True
        for cor in self.segments[:-1]:
            if cor.pos() == head.pos():
                print(cor.pos() , head.pos(), count)
                collide = True
            count+=1
        return collide          
    def go_down(self):
        self.vx =0
        self.vy = -30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_up(self):
        self.vx = 0
        self.vy = 30
    def go_left(self):
        self.vx = -30
        self.vy = 0
   

class Food:
    '''
Purpose: The food ball, it randomize the pellet so the ball can be around theboard.
Instance variables: There is color, make food; that makes the ball, and there is move food that moves the food around the board.
Methods: It has make food that sets up the foodpellet as a snake object, and there is move food that randomizes where the food pellet is arpund the board.
    '''

    def __init__(self, x, y, color):
        self.foodx = x
        self.foody = y
        self.color = color
        self.make_food()
        self.movefood()
       
    def make_food(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.fillcolor(self.color)
        self.ball.shape('circle')
        self.ball.shapesize(1.5, 1.5)
        self.ball.penup()

    def movefood(self):
        self.foodx =15 + 30*random.randint(0,19)
        self.foody =15 + 30*random.randint(0,19)
        self.ball.setpos(self.foodx,self.foody)



     
    
   
   

    



Game()
