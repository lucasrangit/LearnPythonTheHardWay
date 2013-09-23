from sys import exit
from random import randint

class Scene(object):

	def enter(self):
		print "This is the function executed when entering a new room. Subsclasses should override it."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n--------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

	def enter(self):
		print "This is when the player dies and should be something funny."
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "This is the starting point and has a Gothon already standing there they have to defeat with a joke before continuing."
		while True:
			something = raw_input('Do what? ')
			if something == "next":
				return 'laser_weapon_armory'

class LaserWeaponArmory(Scene):

	def enter(self):
		print "This is where the hero gets a neutron bomb to blow up the ship before getting to the escape pod. It has a keypad he has to guess the number for."
		attempts = 0
		while True:
			guess = int(raw_input('Guess a number: '))
			if guess == randint(1,10):
				return 'the_bridge'
			else:
				attempts++
			if attempts == 3:
				print "Too many attempts"
				return 'death'

class TheBridge(Scene):

	def enter(self):
		print "Another battle scene with a Gothon where the hero places the bomb."	
		return 'escape_pod'

class EscapePod(Scene):

	def enter(self):
		print "Where the hero escapes but only after guessing the right escape pod."	
		exit(0)

class Map(object):

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		if scene_name == 'laser_weapon_armory':
			return LaserWeaponArmory()
		elif scene_name == 'the_bridge':
			return TheBridge()
		elif scene_name == 'escape_pod':
			return EscapePod()
		else scene_name == 'death':
			return Death()
		else:
			print "Unknown scene:", scene_name
			exit(1)

	def opening_scene(self):
		if self.start_scene == 'central_corridor':
			return CentralCorridor()

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
