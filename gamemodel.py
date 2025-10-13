from math import sin, cos, radians
import random

""" This is the model of the game"""
class Game:
    """ Create a game with a given size of cannon (length of sides) and projectiles (radius) """
    def __init__(self, cannonSize, ballSize):
        self.cannon_size = cannonSize
        self.ball_size = ballSize

        # Skapa två spelare: vänster (blå) och höger (röd)
        self.Players = [
            Player(self, False, -90, "blue"),
            Player(self, True, 90, "red")
        ]

        self.current_player_index = 0

        # Slumpa startvind
        self.wind = random.random() * 20 - 10

    """ A list containing both players """
    def getPlayers(self):
         return self.Players 

    """ The height/width of the cannon """
    def getCannonSize(self):
        return self.cannon_size 
   
    """ The radius of cannon balls """
    def getBallSize(self):
        return self.ball_size 

    """ The current player, i.e. the player whose turn it is """
    def getCurrentPlayer(self):
        return self.Players[self.current_player_index] 

    """ The opponent of the current player """
    def getOtherPlayer(self):
        return self.Players[1 - self.current_player_index] 
    
    """ The number (0 or 1) of the current player. This should be the position of the current player in getPlayers(). """
    def getCurrentPlayerNumber(self):
        return self.current_player_index 
    
    """ Switch active player """
    def nextPlayer(self):
        self.current_player_index = 1 - self.current_player_index
       
    """ Set the current wind speed, only used for testing """
    def setCurrentWind(self, wind):
        self.wind = wind
        
    def getCurrentWind(self):
        return self.wind

    """ Start a new round with a random wind value (-10 to +10) """
    def newRound(self):
        self.wind = random.random() * 20 - 10
        

""" Models a player """
class Player:
    def __init__(self, game, isReversed, x, color):
        self._game = game
        self._isReversed = isReversed
        self._x = x
        self._color = color
        self._score = 0
        self._last_angle = 45
        self._last_velocity = 40

    """ Create and return a projectile starting at the centre of this players cannon. Replaces any previous projectile for this player. """
    def fire(self, angle, velocity):
        self._last_angle = angle
        self._last_velocity = velocity

        # Om spelaren skjuter åt andra hållet
        actual_angle = 180 - angle if self._isReversed else angle

        # Startposition: x = spelarens x, y = halva kanonstorleken
        xPos = self._x
        yPos = self._game.getCannonSize() / 2

        # Vind
        wind = self._game.getCurrentWind()

        # Hårdkodade gränser
        xLower = -110
        xUpper = 110

        return Projectile(actual_angle, velocity, wind, xPos, yPos, xLower, xUpper)

    """ Gives the x-distance from this players cannon to a projectile """
    def projectileDistance(self, proj):
        cannon_half = self._game.getCannonSize() / 2
        ball_radius = self._game.getBallSize()
        distance = proj.getX() - self._x
        if distance > 0:
            distance -= cannon_half + ball_radius
        else:
            distance += cannon_half + ball_radius
        return distance

    """ The current score of this player """
    def getScore(self):
        return self._score

    """ Increase the score of this player by 1."""
    def increaseScore(self):
        self._score += 1

    """ Returns the color of this player (a string)"""
    def getColor(self):
        return self._color

    """ The x-position of the centre of this players cannon """
    def getX(self):
        return self._x

    """ The angle and velocity of the last projectile this player fired, initially (45, 40) """
    def getAim(self):
        return (self._last_angle, self._last_velocity)


""" Models a projectile (a cannonball, but could be used more generally) """
class Projectile:
    def __init__(self, angle, velocity, wind, xPos, yPos, xLower, xUpper):
        self.yPos = yPos
        self.xPos = xPos
        self.xLower = xLower
        self.xUpper = xUpper
        theta = radians(angle)
        self.xvel = velocity*cos(theta)
        self.yvel = velocity*sin(theta)
        self.wind = wind

    def update(self, time):
        yvel1 = self.yvel - 9.8*time
        xvel1 = self.xvel + self.wind*time
        self.xPos = self.xPos + time * (self.xvel + xvel1) / 2.0
        self.yPos = self.yPos + time * (self.yvel + yvel1) / 2.0
        self.yPos = max(self.yPos, 0)
        self.xPos = max(self.xPos, self.xLower)
        self.xPos = min(self.xPos, self.xUpper)
        self.yvel = yvel1
        self.xvel = xvel1

    def isMoving(self):
        return 0 < self.getY() and self.xLower < self.getX() < self.xUpper

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos
