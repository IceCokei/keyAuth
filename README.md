#1.克隆项目
git clone https://github.com/IceCokei/keyAuth.git

#2.python3 安装3.8及其以上

- 命令如下

#3.安装依赖

```
sudo yum update

sudo yum install gcc openssl-devel bzip2-devel libffi-devel zlib-devel wget

cd /opt/

mkdir python3.8

wget https://www.python.org/ftp/python/3.8.8/Python-3.8.8.tgz

tar xzf Python-3.8.8.tgz

cd Python-3.8.8

./configure --enable-optimizations

sudo make altinstall

ln -s /usr/local/bin/python3.8 /usr/local/bin/python3

ln -s /usr/local/bin/pip3.8 /usr/local/bin/pip3

python3.8 --version

yum install python3-pip

pip3 install python-telegram-bot==12.0.0

pip3 install requests

#还缺一个依赖会有提示一样pip3 install xxx
```

#4.改文件ini配置
#等于号前后空一格
[telegram]
#机器人token
TOKEN =
#群组ID
GROUP_ID =
#管理员ID
ADMIN_IDS = 
#用户文件信息存放
DATA_DIR = 
#TG授权ID[管理员ID]
TG_USER_ID = 

#5.发我运行的脚本服务器IP 

#新增加询问用户到期是否续费和定时检测删除到期群员功能
