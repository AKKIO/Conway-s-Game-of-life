import pyglet
from game_of_life import GameOfLife
#from game_of_life_mine import GameOfLife
#from game_of_life_mineV2 import GameOfLife
class Window(pyglet.window.Window):
	def __init__(self):
		super().__init__(800, 800)
		#pyglet.gl.glClearColor(0.1, 0.3, 0.3, 1.0)
		self.gameOfLife = GameOfLife(self.get_size()[0],
									 self.get_size()[1],
									 20,
									 0.3)
		pyglet.clock.schedule_interval(self.update, 1.0/24.0)

	def on_draw(self):
		self.clear()
		self.gameOfLife.draw()
		
	def update(self, dt):
		self.gameOfLife.run_rules()

if __name__ == '__main__':
	window = Window()
	pyglet.app.run()