import configparser
import yaml, os
from openpyxl import load_workbook


def getpathInfo():
    current_path = os.path.split(os.path.realpath(__file__))[0]
    root_path = os.path.dirname(current_path)
    return root_path


class readData():
    """
    封账读取数据的方法
    """

    def read_config(self, section, option, filename=None):
        """
        读取配置文件，返回对应的配置值
        :param section:
        :param option:
        :param filename:
        :return:
        """
        root_path = getpathInfo()
        if not filename:
            config_path = os.path.join(root_path, 'config', 'config.ini')
        else:
            config_path = os.path.join(root_path, 'config', filename)
        config = configparser.RawConfigParser()
        config.read(config_path, encoding='utf-8')
        result = config.get(section, option)
        return result

    def read_yaml(self, filename):
        """
        读取yaml用例文件
        :param filename:
        :return:
        """
        root_path = getpathInfo()
        file_path = os.path.join(root_path, 'testdatas', filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            yaml_data = yaml.load(f, Loader=yaml.FullLoader)  # 读取yaml文件内容，返回dict数据
            case_data = []
            for case in yaml_data.values():
                case_data.append(case)
            f.close()
        return case_data

    def read_excel(self, sheetname, file):
        """
        读取Excel用例文件
        :param sheetname: 表名
        :param file: 文件名
        :return: 返回一个列表
        """
        root_path = getpathInfo()
        file_path = os.path.join(root_path, "testdatas", file)
        workbook = load_workbook(file_path)
        sheet = workbook[sheetname]  # 执行使用哪个工作表,根据传进来的表名称决定读取对应的数据
        rows = sheet.rows  # 取出所有行的数据
        cases = []
        # 遍历每一行的数据
        for row in rows:
            list1 = []
            if row[len(row) - 2].value == "True":  # 判断该条用例是否需要执行,execute列的值为True则执行，进行数据读取
                for col in row:
                    if not col.value:  # 处理空单元格，直接添加None
                        list1.append(col.value)
                    elif col.value.startswith('{') and col.value.endswith('}'):
                        list1.append(eval(col.value))  # 获取当前行每一个单元格，单元格的内容需要用value，把str类型转化为dict类型
                    else:
                        list1.append(col.value)
                cases.append(list1)
        return cases

    # Excel写入数据
    def write_excel(self, filename, case_id=None, testresult=None):
        root_path = getpathInfo()
        file_path = os.path.join(root_path, "testdatas", filename)
        workbook = load_workbook(file_path)
        sheetname = workbook.sheetnames  # 获取工作表名称
        sheet = workbook[sheetname[0]]  # 执行使用哪个工作表
        cols = sheet.columns
        col = [col for col in cols]
        list1 = []
        for row in col[0]:
            list1.append(row.value)
        i = 0
        for id in list1:
            if case_id == id:
                i += 1
                break
            i += 1
        sheet.cell(i, sheet.max_column).value = testresult
        workbook.save(file_path)

    def read_sqls(self, filename):

        root_path = getpathInfo()
        file = os.path.join(root_path, "testdatas", filename)
        sqls = []
        with open(file, 'r', encoding='utf-8') as stream:
            for line in stream.readlines():
                if not len(line.strip()) or line.startswith('--'):
                    continue
                sqls.append(line.strip())
        return sqls


if __name__ == '__main__':
    read = readData()
    # sqls = data.read_sqls('initsqls.txt')
    # print(sqls)
    datas = read.read_excel("login", "logincase.xlsx")
    print(datas)
    # data = read.read_config("test_env", "phone")
    # print(data)
