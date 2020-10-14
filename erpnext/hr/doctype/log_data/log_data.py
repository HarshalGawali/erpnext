# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe import _, msgprint, scrub
from datetime import datetime
from datetime import datetime, timedelta 
import time
from frappe.utils import fmt_money, formatdate, format_time, now_datetime, get_url_to_form, get_url_to_list, flt, get_link_to_report
from frappe.utils.data import nowdate,today, getdate, cint, add_days, date_diff, get_last_day, add_to_date, flt
from frappe.utils import time_diff
from frappe.utils import time_diff_in_hours

from frappe.model.document import Document
import pyodbc
import mysql.connector

class LogData(Document):
	pass

def fetch_data(dt = nowdate()):
	presentday = datetime.now()
	yesterday = presentday - timedelta(1)
	print("Yesterday = ", yesterday.strftime('%d-%m-%Y'))
	mdate = datetime.strftime(datetime.now() - timedelta(days=1), '%Y-%m-%d')

	print("NOWDATEEEEEEEEEEEEEEEEEEEEEEEEE",mdate)
	return mdate

def scheduler_method():
	date = fetch_data()
	print("SCHEDULERRRRRRRRRRRRRRRRRRRRRRR method log data",date)
	get_date(date)

@frappe.whitelist()
def get_date(date):
	myDB = pyodbc.connect(
		DRIVER='{FreeTDS}',
		SERVER='114.143.174.98',
		PORT='8885',
		DATABASE='etimetracklite1',
		UID="essl12",
		PWD='Zxcasqw@2019#$1@')

	#mydate = '2020-03-19'
	mydate=date
	nxt_date = add_days(mydate, 1)
	print("hellloooooooooooooooo thereeeeeeeeeeeeeeeeee",mydate)
	print("hhhhhhhhhhhhhhhhhhhhhhiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
	cHandler = myDB.cursor()
	cHandler.execute("""select LogID,Emp_code,Direction,Log_Date_Time from AttendancePunch where Log_Date_Time between '%s' and '%s'"""%(mydate,nowdate()))
	   
	connection=mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="root",
	  database="_1bd3e0294da19198"
	)

	curs = connection.cursor() 
	curs.execute("""select * from biometric""")

	lst = []
	result= cHandler.fetchall()
	for row in result:
		lst.append(row)

	lst2 = []
	result2= curs.fetchall()
	for row in result2:
		lst2.append(row)

	t = []
	r = [elem for elem in lst if not elem in lst2]
	for i in r:	
		print(i)
		t.append(i)

	for i in t:
		frappe.db.sql("""Insert into biometric(LogId,UserId,C1,LogDate) values(%s,%s,%s,%s) on duplicate key update LogId=%s, UserId=%s, C1=%s , LogDate=%s""",(i[0],i[1],i[2],i[3],i[0],i[1],i[2],i[3]),as_dict=1)
	print(len(t))

	connection.commit()



