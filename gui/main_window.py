import wx
import app
import services

class MainWindow(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title=f"{app.name} {app.version}")
		self.init_ui()
		self.bind_events()
		self.populate_services()
	
	def init_ui(self):
		self.panel = wx.Panel(self)
		self.main_sizer = wx.BoxSizer(wx.VERTICAL)
		service_sizer = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(self.panel, label="Services")
		self.service_list = wx.ListBox(self.panel)
		service_sizer.Add(label, 0, wx.ALL, 5)
		service_sizer.Add(self.service_list, 0, wx.ALL, 5)
		query_sizer = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(self.panel, label="&Query")
		self.query = wx.TextCtrl(self.panel, style=wx.TE_PROCESS_ENTER)
		query_sizer.Add(label, 0, wx.ALL, 5)
		query_sizer.Add(self.query, 0, wx.ALL, 5)
		result_sizer = wx.BoxSizer(wx.HORIZONTAL)
		label = wx.StaticText(self.panel, label="&results")
		self.results = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_DONTWRAP)
		result_sizer.Add(label, 0, wx.ALL, 5)
		result_sizer.Add(self.results, 0, wx.ALL, 5)
		self.main_sizer.Add(service_sizer)
		self.main_sizer.Add(query_sizer)
		self.main_sizer.Add(result_sizer)
		self.panel.SetSizerAndFit(self.main_sizer)
		self.panel.Layout()
	
	def bind_events(self):
		self.Bind(wx.EVT_CLOSE, self.on_exit)
		self.query.Bind(wx.EVT_TEXT_ENTER, self.on_text_enter)
	
	def populate_services(self):
		if services.supported_services == []:
			return
		for i in services.supported_services:
			self.service_list.Insert(i.name, self.service_list.GetCount())
		self.service_list.SetSelection(0)
	
	def on_exit(self, event):
		app.quit()
	
	def on_text_enter(self, event):
		results = services.supported_services[self.service_list.GetSelection()].get_results(self.query.GetValue())
		self.results.SetValue(results)
		wx.CallAfter(self.results.SetFocus)
