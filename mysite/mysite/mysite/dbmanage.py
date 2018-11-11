#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
import sys, time

###::::http://www.runoob.com/python/python-mysql.html

###连接数据库
def connectdb(username = 'root', password = "huawei", dbname = ""):

    # �����ݿ�����
    db = MySQLdb.connect("localhost", username, password, dbname, charset='utf8' )
    
    # ʹ��cursor()������ȡ�����α� 
    cursor = db.cursor()
    
    # ʹ��execute����ִ��SQL���
    cursor.execute("SELECT VERSION()")
    
    # ʹ�� fetchone() ������ȡһ������
    data = cursor.fetchone()
    
    print "Database version : %s " % data
    
    if '5.7.23' in data[0]:
        return db
    else:
        return False

#�ر����ݿ�    
def closedb(db):
    
    # �ر����ݿ�����
    db.close()
    
    
def  creatdatabase(db, dbname = "mydatabase"):
    #创建数据库
    cursor = db.cursor()
    sql = 'create database %s'%dbname
    cursor.execute(sql)
    db.commit()
    
    
def creatTable(db, tablename = "userinfo"):

    # ʹ��cursor()������ȡ�����α� 
    cursor = db.cursor()

    # ������ݱ��Ѿ�����ʹ�� execute() ����ɾ����
    cursor.execute("DROP TABLE IF EXISTS %s"%tablename)
    
    # �������ݱ�SQL���
    sql = """CREATE TABLE %s (
             USER_NAME  CHAR(20) NOT NULL,
             USER_PASSWORD  CHAR(20),
             heart_Num INT,  
             Priv INT,
             INCOME FLOAT )"""%tablename
    
    cursor.execute(sql) 
    
def insertTable(db, tablelist=['Mac', 'Mohan', 0, 0, 2000]):

    cursor = db.cursor()
    
    # SQL �������
    sql = "INSERT INTO userinfo(USER_NAME, \
           USER_PASSWORD, heart_Num, Priv, INCOME) \
           VALUES ('%s', '%s', '%d', '%d', '%d' )" % \
           (tablelist[0], tablelist[1], tablelist[2], tablelist[3], tablelist[4])
    try:
        # ִ��sql���
        cursor.execute(sql)
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # ��������ʱ�ع�
        db.rollback()
        
def getTableone(db):
    # ʹ��cursor()������ȡ�����α� 
    cursor = db.cursor()

# SQL ��ѯ���
    sql = "SELECT * FROM userinfo \
           "
    try:
        # ִ��SQL���
        cursor.execute(sql)
        # ��ȡ���м�¼�б�
        results = cursor.fetchall()
        for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # ��ӡ���
            print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                   (fname, lname, age, sex, income )
    except:
        print "Error: unable to fecth data"
        
        
        
def updatedatabase(db):
    
    cursor = db.cursor()
    # SQL �������
    sql = "UPDATE userinfo SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
    try:
        # ִ��SQL���
        cursor.execute(sql)
        # �ύ�����ݿ�ִ��
        db.commit()
    except:
        # ��������ʱ�ع�
        db.rollback()
        
        
def deletedatabase(db):        
# ʹ��cursor()������ȡ�����α� 
    cursor = db.cursor()
    
    # SQL ɾ�����
    sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
    try:
        # ִ��SQL���
        cursor.execute(sql)
        # �ύ�޸�
        db.commit()
    except:
        # ��������ʱ�ع�
        db.rollback()        
 
 
def main():
    #连接数据库
    db = connectdb("root", "huawei", "")
    if db == False:
        print ("connect db fail, please check")
    else:
        print("connect ok") 
        
    #创建数据库
    #creatdatabase(db, 'mydatabase')
    closedb(db)
    #创建数据表及表头   
    db = connectdb("root", "huawei", "mydatabase")
    creatTable(db, 'userinfo')
    time.sleep(2)
    #创建表头信息
    insertTable(db, ["admin", "huawei", 0, 4, 1000])
    insertTable(db, ["test", "Huawei12#$", 0, 4, 1000])
    
    getTableone(db)
    closedb(db)
    
    
    

if __name__ == "__main__":
    sys.exit(main())