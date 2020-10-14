
# -*- coding: utf-8 -*-
# Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe import _, msgprint, scrub
from datetime import datetime,timedelta
from datetime import datetime
import time
from frappe.utils import fmt_money, formatdate, format_time, now_datetime, get_url_to_form, get_url_to_list, flt, get_link_to_report
from frappe.utils.data import nowdate, getdate, cint, add_days, date_diff, get_last_day, add_to_date, flt
from frappe.utils import time_diff
from frappe.utils import time_diff_in_hours

from frappe.model.document import Document

class BiometricAttendance(Document):
	pass

def fetch_date(dt = nowdate()):
	
	mdate = datetime.strftime(datetime.now() - timedelta(days=2), '%Y-%m-%d')
	#print("NOWDATEEEEEEEEEEEEEEEEEEEEEEEEE",mdate)
	return mdate

def scheduler_method():
	date = fetch_date()
	#print("SCHEDULERRRRRRRRRRRRRRRRRRRRRRR method biometric",date)
	get_date(date)

@frappe.whitelist()
def get_date(date):

	plist=[]
	rlist = []
	vlist=[]
	nlist=[]
	dlist=[]
	mydate = date
	nxt_date = add_days(mydate, 1) 
	d1=frappe.db.sql(""" SELECT t1.name, t1.start_time, t1.end_time,t2.date, t2.employee
			FROM `tabShift Type` t1
			INNER JOIN `tabShift Assignment` t2
			ON t1.name = t2.shift_type
			INNER JOIN `tabEmployee` t3
			ON t2.employee = t3.name
			where t2.docstatus=1 and t3.status='Active' and t3.date_of_joining<%s
		""",mydate,as_dict=1)	#FETCH DATA FROM SHIFT MASTER AND SHIFT ASSIGNMENT 


	for u in d1:
		# print("^^^^^^^^^^^^^^^^^^^^^^^",u["employee"])
		start = u["start_time"] - timedelta(hours=2)	#TWO HOUR BEFORE START TIME 
		end = u["end_time"] + timedelta(hours=4)		#TWO HOUR AFTER END TIME
		start_time = str(start)
		end_t = str(end)
		end_time = end_t[-8:]
		#print(start_time)
		#print(end_time)
		user=u["employee"]
		#print("nxt_date",nxt_date)
		if start_time>end_time:		#FOR NIGHT SHIFT
			#print("///////////////",user)
			dt = frappe.db.sql("""(select UserId,LogDate,DATE(LogDate) from biometric where DATE(LogDate)='%s' and UserId='%s' and TIME(LogDate) between '%s' and '%s' order by LogDate desc limit 1) union (select '%s' as UserId,  CONCAT('%s',' ', '%s')  as LogDate,'%s' as 'DATE(LogDate)') limit 1"""%(mydate,u['employee'],start_time,end_time,u['employee'],mydate,start_time,mydate),as_dict=1)	 #FETCH FIRST PUNCH OF EMPLOYEE
			rt = frappe.db.sql("""(select UserId,LogDate,DATE(LogDate) from biometric where DATE(LogDate)='%s' and UserId='%s' and TIME(LogDate) between '%s' and '%s' order by LogDate asc limit 1) union (select '%s' as UserId, CONCAT('%s',' ', '%s')  as LogDate,'%s' as 'DATE(LogDate)') limit 1"""%(mydate,u['employee'],start_time,end_time,u['employee'],mydate,start_time,mydate),as_dict=1) 	#FETCH LAST PUNCH OF EMPLOYEE
			if start_time>="9:00:00" or start_time<="12:00:00" or start_time<="21:00:00":
				#print("pikabooo")
				rt = frappe.db.sql("""(select LogDate,DATE(LogDate) from biometric where UserId='%s' and LogDate between CONCAT(subdate('%s',1), ' ', '%s') and CONCAT('%s', ' ', '%s') order by LogDate asc limit 1) union (select CONCAT(subdate('%s',1), ' ', '%s') as LogDate,subdate('%s',1) as 'DATE(LogDate)'limit 1) limit 1"""%(u['employee'],nxt_date,start_time,nxt_date,end_time,nxt_date,start_time,nxt_date),as_dict=1)		#FETCH FIRST PUNCH OF EACH EMPLOYEE
				dt = frappe.db.sql("""(select LogDate,DATE(LogDate) from biometric where UserId='%s' and LogDate between subdate(CONCAT('%s', ' ', '%s'),1) and CONCAT('%s',' ', '%s') order by LogDate desc limit 1) union (select LogDate,DATE(LogDate) from biometric where DATE(LogDate)=subdate('%s',1) and UserId='%s' and TIME(LogDate) between '%s' and '23:59:59' order by LogDate desc limit 1) union (select  CONCAT(subdate('%s',1), ' ', '%s') as LogDate,'%s' as 'DATE(LogDate)' limit 1) limit 1"""%(u['employee'],nxt_date,start_time,nxt_date,end_time,nxt_date,u['employee'],start_time,nxt_date,start_time,nxt_date),as_dict=1) 	#FETCH LAST PUNCH OF EACH EMPLOYEE
				

			for r,o in zip(rt,dt):		#MERGE TWO LIST 
				#print("-------------------Day SHift---------------------")
				#print("rrrrrr",r)
				#print("oooooo",o)
				t1 = r["LogDate"]
				t2 = o["LogDate"]
				diff = abs(round(time_diff_in_hours(t2, t1),1))	#DIFFERENCE BETWEEN LIST 1 AND LIST 2
				#print(diff)
				if diff<4.5:
					status="Absent"
				elif(diff>=4.5 and diff<7):
					status="Half Day"
					# print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
				elif diff>=7:
					status = "Present"

				p = user,user,r["DATE(LogDate)"],u["name"],diff,status,t1,t2
				# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",p)
				dlist.append(p)
				#print(diff)

		else:					#FOR OTHER SHIFT
			#print("///////////////",user)
			kt = frappe.db.sql("""(select LogDate,DATE(LogDate) from biometric where UserId='%s' and LogDate between CONCAT(subdate('%s',1), ' ', '%s') and CONCAT('%s', ' ', '%s') order by LogDate asc limit 1) union (select CONCAT(subdate('%s',1), ' ', '%s') as LogDate,subdate('%s',1) as 'DATE(LogDate)'limit 1) limit 1"""%(u['employee'],nxt_date,start_time,nxt_date,end_time,nxt_date,start_time,nxt_date),as_dict=1)		#FETCH FIRST PUNCH OF EACH EMPLOYEE
			jk = frappe.db.sql("""(select LogDate,DATE(LogDate) from biometric where UserId='%s' and LogDate between subdate(CONCAT('%s', ' ', '%s'),1) and CONCAT('%s',' ', '%s') order by LogDate desc limit 1) union (select LogDate,DATE(LogDate) from biometric where DATE(LogDate)=subdate('%s',1) and UserId='%s' and TIME(LogDate) between '%s' and '23:59:59' order by LogDate desc limit 1) union (select  CONCAT(subdate('%s',1), ' ', '%s') as LogDate,'%s' as 'DATE(LogDate)' limit 1) limit 1"""%(u['employee'],nxt_date,start_time,nxt_date,end_time,nxt_date,u['employee'],start_time,nxt_date,start_time,nxt_date),as_dict=1) 	#FETCH LAST PUNCH OF EACH EMPLOYEE
			
			for k,j in zip(kt,jk):		#MERGE TWO LIST 
				print("-------------------Night SHift---------------------")
				print("kkkkkk",k)
				print("jjjjjj",j)
				t1 = k["LogDate"]
				t2 = j["LogDate"]
				diff = abs(round(time_diff_in_hours(t2, t1),1))		#DIFFERENCE BETWEEN LIST 1 AND LIST 2
				if diff<4.5:	
					status="Absent"
				elif(diff>4.5 and diff<7):
					status="Half Day"
				# print("OOOOOOOOOOOOOOOOOOOOOOO")
				elif diff>7:
					status = "Present"
				p = user,user,k["DATE(LogDate)"],u["name"],diff,status,t1,t2
			# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",p)
				dlist.append(p)
				#print(diff)
	for i in dlist:
	
		get_doc(i)
		#print("**********************************")
		insert(i)
			
	return

def get_doc(i):
	attendance = frappe.new_doc("Attendance")
	d2=frappe.db.sql(""" SELECT count(t2.holiday_date)
		FROM `tabEmployee` t1
		INNER JOIN `tabHoliday` t2
		ON t1.holiday_list = t2.parent
		where t1.employee='%s'
		and t2.holiday_date='%s'
	"""%(i[0],i[2]),as_list=1)

	for t in d2:
		#print("YSYSYSYSYYS",t[0])
	
		if(t[0] == 0):
			#print("i[4]",i[4])
			if not frappe.db.exists('Attendance', {'employee':i[0], 'attendance_date':i[2], 'docstatus':('!=', '2')}):
				attendance.attendance_date = i[2]
				attendance.shift = i[3]
				attendance.employee = i[0]
				attendance.working_hours=i[4]
				attendance.status=i[5]
				#print("**********************************")
				attendance.save()
			#print("HIIII")

		elif(t[0] == 1):
			if(i[4] > 0.0):
				#print("i[4]",i[4])
				if not frappe.db.exists('Attendance', {'employee':i[0], 'attendance_date':i[2], 'docstatus':('!=', '2')}):
					attendance.attendance_date = i[2]
					attendance.shift = i[3]
					attendance.employee = i[0]
					attendance.working_hours=i[4]
					attendance.status=i[5]
					#print("++++++++++++++++++++")
					attendance.save()
					#print("HELLO")
			else:
				pass
				#print("-------------------")
		else:
			#print("BYE")
			pass

	return attendance

def insert(i):
	#print("????????????????????????",i)
	frappe.db.sql("""update `tabAttendance` set punch_in='%s',punch_out='%s' where employee='%s' and attendance_date='%s'"""%(i[6],i[7],i[0],i[2]),as_dict=1)

	#print("PUNCH IN",i[6])
	#print("PUNCH OUT",i[7])

