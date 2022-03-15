import pymysql
from selenium import webdriver
from sshtunnel import SSHTunnelForwarder
from utils.read_data import readData


class mysqlDb:

    def __init__(self):
        conf = readData()
        # 获取config.ini文件中数据库相关配置
        self._host = conf.read_config("publicCloud", "host")
        self._port = conf.read_config("publicCloud", "ssh_port")
        self._user = conf.read_config("publicCloud", "ssh_user")
        self._password = conf.read_config("publicCloud", "ssh_pwd")
        self._dbuser = conf.read_config("publicCloud", "dbuser")
        self._dbpwd = conf.read_config("publicCloud", "dbpwd")
        self._dbname = conf.read_config("publicCloud", "dbname")
        self.sshtunnel = self.creat_sshtunnel()
        self.conn = self.login_database()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        self.sshtunnel.stop()

    # 创建SSH tunnel通道
    def creat_sshtunnel(self):
        sshtunnel = SSHTunnelForwarder(
            ssh_address_or_host=self._host,  # 跳板机B地址
            ssh_port=self._port,  # 跳板机B端口
            ssh_username=self._user,  # 跳板机B账号
            ssh_password=self._password,  # 跳板机B密码
            local_bind_address=('127.0.0.1', 22),  # 这里必须填127.0.0.1
            remote_bind_address=('127.0.0.1', 3306)  # 目标机器A地址，端口
        )
        # print("sshtunnel 通道服务创建成功")
        return sshtunnel

    # 连接数据库
    def connect_database(self):
        conn = pymysql.connect(
            host='127.0.0.1',  # 这里必须填127.0.0.1
            port=22,  # 本地映射端口
            user=self._dbuser,  # 目标机器A账号
            password=self._dbpwd,  # 目标机器A密码
            db=self._dbname  # 目标机器A要连的库
        )
        return conn

    def query(self, sql, state="all"):
        self.cursor.execute(sql)
        if state == "all":
            data = self.cursor.fetchall()
        else:
            data = self.cursor.fetchone()
        return data

    def execute(self, sql):
        """
        更新、删除、新增
        :param sql:
        :return:
        """
        try:
            # 使用execute执行sql
            rows = self.cursor.execute(sql)
            # 提交事务
            self.conn.commit()
            return rows
        except Exception as e:
            print("数据库操作异常{0}".format(e))
            # 出现异常，进行回滚操作
            self.conn.rollback()

    def login_database(self):
        # 创建ssh tunnel服务通道
        self.creat_sshtunnel()
        # 开启ssh tunnel服务通道
        self.sshtunnel.start()
        # 连接数据库
        conn = self.connect_database()
        return conn

    def init_database(self, filename):
        # 获取数据库初始化sql语句
        sqls = readData().read_sqls(filename)
        self.sshtunnel.start()
        conn = self.connect_database()
        cursor = conn.cursor()
        for sql in sqls:
            cursor.execute(sql)
        conn.commit()
        conn.close()
        self.sshtunnel.stop()


if __name__ == "__main__":
    db = mysqlDb()
    # conn = db.login_database()
    # cur = db.conn.cursor()
    rows = db.query("select * from t_user",state="one")
    print(rows)
    # print(cur.fetchone())
    # db.logout_database()
