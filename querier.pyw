import app
from gui.main_window import MainWindow

def main():
	app.init()
	window = MainWindow(title=f"{app.name} {app.version}", top_level_window=True)
	window.display()
	app.app.MainLoop()

if __name__ == "__main__":
	main()
