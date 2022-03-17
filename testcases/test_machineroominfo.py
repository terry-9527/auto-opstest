from common.base_page import BasePage
from pages.system_setting_page.machine_info.machineroom_info_page import MachineRoomInfoPage
import unittest


class TestMachineRoomInfo(BasePage):

    def test_new_machineroom_info(self):
        m = MachineRoomInfoPage(self.driver)
        m.new_machine_room()

