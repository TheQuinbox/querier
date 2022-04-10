import wx
import sys

name = "Querier"
version = "Beta 1"
app = None

def init():
	global app
	app = wx.App()

def exit():
	app.ExitMainLoop()
	sys.exit()
