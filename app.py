import wx
import sys

name = "Querier"
version = "Beta 1"
app = None

def init():
	global app
	app = wx.App()

def quit():
	app.ExitMainLoop()
	sys.exit()
