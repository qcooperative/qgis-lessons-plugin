
import glob
import os

class LessonsCollection:

	def __init__(self, iface):
		try:
			from lessons import addLessonModule
		except:
			return

		folder = os.path.join(os.path.dirname(__file__), "_lessons")
		def isPackage(d):
			d = os.path.join(folder, d)
			return os.path.isdir(d) and glob.glob(os.path.join(d, '__init__.py*'))
		packages = filter(isPackage, os.listdir(folder))
		for p in packages:
			m = __import__(__name__.split(".")[0] + "._lessons." + p, fromlist="dummy")
			addLessonModule(m)

	def unload(self):
		pass

	def initGui(self):
		pass






