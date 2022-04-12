import os

ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 配置文件路径
ini_dir = os.path.join(ROOT_PATH, "config")

# 日志存储路径
log_dir = os.path.join(ROOT_PATH, "outputs\log")

# 测试报告存储路径
report_dir = os.path.join(ROOT_PATH, r"outputs\report")

# 测试用例存放路径
testcase_dir = os.path.join(ROOT_PATH, "testcases")

# 测试数据存放路径
testdata_dir = os.path.join(ROOT_PATH, "testdatas")

# 文件上传/下载路径
download_dir = os.path.join(ROOT_PATH, "download")
