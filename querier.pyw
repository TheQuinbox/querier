import app
from gui.main_window import MainWindow

def main():
	app.init()
	window = MainWindow()
	window.Show()
	app.app.MainLoop()

if __name__ == "__main__":
	main()
