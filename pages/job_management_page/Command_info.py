from common.keywords import KeyWords
from PIL import ImageGrab

class CustemorPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    colony1 = ('xpath','//label[@title="目标集群"]/../../div[2]/div/div/div')
    hostinfo =('xpath','//span[text()="+ 选择主机"]')
    confirm =('xpath','//span[text()="确 认"]')
    template =('xpath','//span[text()="+ 选择模板"]')
    cancel =('xpath','//span[text()="取 消"]')



    def new_commandinfo(self,colony=None,host=None,template=None,states=False,start=False,section=True):
        self.click_navigation_bar("作业管理")
        self.wait()
        self.click_navigation_bar(" 命令执行")
        self.wait()
        if colony:
            self.div_selector(self.colony1,name=colony)
        self.input_host(self.hostinfo, host=host)
        if colony:
            self.click_span_button("确 认")
            self.wait()
        if states:
            self.input_host(self.template, name=template)
            self.click_elements(*self.confirm, list_number=1)
        if start:
            self.click_span_button("开始执行")
            self.wait(24)
        if section:
            #截图
            im = ImageGrab.grab(bbox=(316,521,1080,998))  # 截屏
            im.save(r"F:\yunweixitong\outputs\report\123.png")  # 保存123.png






