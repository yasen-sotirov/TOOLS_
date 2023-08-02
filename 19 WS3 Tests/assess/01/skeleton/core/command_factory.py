
from commands.base.AddTestGroup import AddTestGroup
from commands.base.Add_test import Add_Test
from commands.base.AddTestRun import AddTestRun
from commands.base.test_report import Test_Report
from commands.base.View_group import View_group


class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):

        cmd, *params = input_line.split()

        if cmd.lower() == 'addtestgroup':
            return AddTestGroup(params,self._app_data)
        
        if cmd.lower() == 'addtest':
            return Add_Test(params,self._app_data)
        
        if cmd.lower() == 'addtestrun':
            return AddTestRun(params,self._app_data)
        
        if cmd.lower() == 'testreport':
            return Test_Report(params,self._app_data)
        
        if cmd.lower() == 'viewgroup':
            return View_group(params,self._app_data)
        
        