'''
Central file for the running of Roze
'''

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(arcade.Sprite) :
    def update(self) :

        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Game(arcade.Window) :

    def __init__(self, width, height, title) :

        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.COOL_BLACK)

        self.player_sprite = None
        self.player_list = None
        self.coin_list = None

    def setup(self) :
        self.coin_list = arcade.SpriteList()

        self.player_sprite = Player("soldier.png", .5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 500

        for i in range(20) :
            coin = arcade.Sprite("coin.png")
            coin.center_x = random.random() * 800
            coin.center_y = random.random() * 600
            self.coin_list.append(coin)
    
    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_sprite.draw()

    def update(self, delta_time: float):
        self.player_sprite.update()

        coins_hit = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coins_hit :
            coin.remove_from_sprite_lists()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W :
            self.player_sprite.change_y += 3
        if symbol == arcade.key.A :
            self.player_sprite.change_x += -3
        if symbol == arcade.key.S :
            self.player_sprite.change_y += -3
        if symbol == arcade.key.D :
            self.player_sprite.change_x += 3

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W :
            self.player_sprite.change_y += -3
        if symbol == arcade.key.A :
            self.player_sprite.change_x += 3
        if symbol == arcade.key.S :
            self.player_sprite.change_y += 3
        if symbol == arcade.key.D :
            self.player_sprite.change_x += -3

    
def main() :
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, 'Roze')
    window.setup()
    arcade.run()

main()