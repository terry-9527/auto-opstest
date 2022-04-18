from pywinauto.application import Application
class WinAuto:

	def __init__(self,class_name,title_re):
		# 连接到指定应用程序，此处为连接到指定窗口
		self.app = Application().connect(class_name = class_name, title_re = title_re)

	# 定位窗口方法
	def get_window(self,window_object,class_name = "",title_re = ""):
		return window_object.window(class_name = class_name, title_re = title_re)

	# 向编辑框输入指定信息
	def file_input(self,file_path):
		# 定位到标题名为“打开”对话框
		window = self.get_window(self.app, "#32770", "打开")
		# 定位到编辑框
		window = self.get_window(window, class_name ="Edit")
		# 向编辑框中输入信息
		window.type_keys(file_path)

	# 点击【打开】按钮
	def open_button_click(self):
		# 定位到标题名为“打开”对话框
		window = self.get_window(self.app, "#32770", "打开")
		# 定位到【打开】按钮
		button = self.get_window(window, class_name = "Button", title_re = "打开")
		# 点击【打开】按钮
		button.click()

if __name__ == '__main__':
	window = WinAuto("#32770","打开")
	window.file_input("ttttt_test")
	window.open_button_click()
