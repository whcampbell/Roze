'''
Central file for the running of Roze
'''

import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Ball:
    def __init__(self, x, y, change_x, change_y, radius, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self) :
        arcade.draw_circle_filled(self.x, self.y, self.radius, self.color)

    def update(self) :
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.radius :
            self.change_x *= -1

        if self.x > SCREEN_WIDTH - self.radius :
            self.change_x *= -1

        if self.y < self.radius :
            self.change_y *= -1

        if self.y > SCREEN_HEIGHT - self.radius :
            self.change_y *= -1

class Game(arcade.Window) :


    def __init__(self, width, height, title) :

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.COOL_BLACK)
        self.ball = Ball(50, 50, 1, 1, 20, arcade.color.AUBURN)


        self.player_sprite = None
        self.player_list = None
        self.coin_list = None

    def setup(self) :
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
    
    def on_draw(self):
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time: float):
        self.ball.update()

    

def main() :
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roze')
    arcade.run()

main()