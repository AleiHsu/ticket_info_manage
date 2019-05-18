# ticket_info_manage
航班信息数据的Web管理展示平台

# 搭建虚拟环境并激活
```shell
virtualenv py2
source py2/bin/activate
```
# 复制本项目
```
git clone https://github.com/lin14543/ticket_info_manage
```
# 安装所需要的包
进入到本项目的根目录下
```
pip install -r requirements.txt
```
# 遇到EnvironmentError: mysql_config not found 怎么解决？
Ubuntu系统
```
sudo apt-get update
sudo apt-get install
sudo apt-get install mysql-server
sudo apt isntall mysql-client
sudo apt-get install libmysqlclient-dev
```
用sudo netstat -tap | grep mysql 查看一下，是否安装了服务
重启数据库
```
sudo service mysql start
```
登陆mysql数据库可以通过如下命令：
```
mysql -u root -p 
```
-u 表示选择登陆的用户名， -p 表示登陆的用户密码，上面命令输入之后会提示输入密码，此时输入密码就可以登录到mysql。

# 运行前记得：
```
python manage.py migrate
```
# 在settings里修改自己的配置
＃启动项目
python manage.py runserver 0.0.0.0:8000
