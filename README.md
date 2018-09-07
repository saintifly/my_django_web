#django test



Django搭建

一、安装

Linux 下安装python-pip, 然后安装django

 apt install python-pip
pip install django

二、创建工程：工程名称mysite

django-admin.py startproject mysite


三、关闭防火墙

四、允许所有IP访问：

vi settings.py

	ALLOWED_HOSTS = ['*']

