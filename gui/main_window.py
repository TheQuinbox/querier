from gui_builder import fields, forms
import app
import services
import threading
import wx

class MainWindow(forms.Frame):
	service_list = fields.ListBox(label="&Services")
	query = fields.Text(label="&Query", process_enter=True, default_focus=True)
	results = fields.Text(label="&Results", multiline=True, read_only=True)
	
	def __init__(self, *args, **kwargs):
		super().__init__(size=(800, 600), *args, **kwargs)
	
	def render(self, *args, **kwargs):
		super().render(*args, **kwargs)
		if services.supported_services == []:
			return
		service_list = []
		for service in services.supported_services:
			service_list.append(service.name)
		self.service_list.set_value(service_list)
		self.service_list.set_index(0)
	
	@query.add_callback("text_enter")
	def do_query(self):
		threading.Thread(target=self.run_service).start()
	
	def run_service(self):
		results = services.supported_services[self.service_list.get_index()].get_results(self.query.get_value())
		self.results.set_value(results)
		wx.CallAfter(self.results.set_focus)
	
	extra_callbacks = (
		("close", app.exit),
	)
