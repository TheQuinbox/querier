from gui_builder import fields, forms
import app
import services
import threading

class MainWindow(forms.Frame):
	service_list = fields.ListBox(label="&Services")
	query = fields.Text(label="&Query", process_enter=True)
	results = fields.Text(label="&Results", multiline=True, read_only=True)
	
	def render(self, *args, **kwargs):
		super().render(*args, **kwargs)
		if services.supported_services == []:
			return
		service_list = []
		for service in services.supported_services:
			service_list.append(service.name)
		self.service_list.set_value(service_list)
		self.service_list.set_index(0)
	
	@query.add_callback
	def do_query(self, event):
		threading.Thread(target=self.run_service).start()
	
	def run_service(self):
		results = services.supported_services[self.service_list.GetSelection()].get_results(self.query.GetValue())
		self.results.SetValue(results)
		wx.CallAfter(self.results.SetFocus)
	
	extra_callbacks = (
		("close", app.exit),
	)
