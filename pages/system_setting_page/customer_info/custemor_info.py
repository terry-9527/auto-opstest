from common.keywords import KeyWords


class CustemorPage(KeyWords):
    '''
    页面元素的定位信息
    '''
    # 系统设置
    system_setting = ('xpath', '//span[text()="系统设置"]')
    # 客户信息
    machineroom_info = ('xpath', '//span[text()=" 客户信息"]')
    # 新建客户按钮
    new_custemor = ('xpath', '//span[text()="新建客户"]')
    # 客户名称输入框
    name_input = ('xpath', '//form/div[1]/div[2]/div/div/input')
    # 备注输入框
    comment_input = ('xpath', '//form/div[2]/div[2]/div/div/input')
    # 确定按钮
    confirm_button = ('xpath', '//span[text()="确 定"]')
    # 确定取消
    cancel_button = ('xpath', '//span[text()="取 消"]')
    # 点击编辑
    edit_operation = ('xpath', '//span[text()="编辑"]')
    # 编辑客户
    edit_customer_info = ('xpath', '//form/div[1]/div[2]/div/div/input')
    # 编辑备注
    edit_notes = ('xpath', '//form/div[2]/div[2]/div/div/input')
    # 确定按钮
    confirm1_button = ('xpath', '//span[text()="确 定"]')
    # 确定取消
    cancel2_button = ('xpath', '//span[text()="取 消"]')
    # 删除
    delete_operation = ('xpath', '//span[text()="删除"]')
    # 确定按钮
    confirm2_button = ('xpath', '//span[text()="确 定"]')


    def new_custemorinfo(self, name, comment):
        self.click_element(*self.system_setting)
        self.click_element(*self.machineroom_info)
        self.click_element(*self.new_custemor)
        self.input_text(*self.name_input, name)
        self.input_text(*self.comment_input, comment)
        self.click_element(*self.confirm_button)

    def edit_custemor(self, name, comment):
        self.click_element(*self.system_setting)
        self.click_element(*self.machineroom_info)
        self.click_elements(*self.edit_operation,list_number=1)
        self.input_text(*self.edit_customer_info, name)
        self.input_text(*self.edit_notes, comment)
        self.click_element(*self.confirm1_button)



