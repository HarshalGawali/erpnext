# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns = [
	 {
                        'fieldname': 'employee',
                        'label': 'Employee',
                        'fieldtype': 'Data',
                },
                {
                        'fieldname': 'employee_name',
                        'label': 'Employee Name',
                        'fieldtype': 'Data',
                },
                {
                        'fieldname': 'status',
                        'label': 'status',
                        'fieldtype': 'Data'
                },
                {
                        'fieldname': 'punch_in',
                        'label': 'Punch in',
                        'fieldtype': 'Data',
                },
                {
                        'fieldname': 'punch_out',
                        'label': 'Punch out',
                        'fieldtype': 'Data',
                },
                {
                        'fieldname': 'working_hours',
                        'label': 'Working Hours',
                        'fieldtype': 'Data',
                },
	]
	data = frappe.db.sql("""select employee,employee_name,status,punch_in,punch_out,working_hours from `tabAttendance` where attendance_date=%s and (punch_in is not null or punch_out is not null)""", (filters.date))
	return columns, data
