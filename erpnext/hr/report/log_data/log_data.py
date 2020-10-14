from __future__ import unicode_literals
import frappe
from frappe import msgprint, _

def execute(filters=None):
	columns = [
		{
			'fieldname': 'user_id',
			'label': 'UserID',
			'fieldtype': 'Data',
		},
		{
			'fieldname': 'logdate',
			'label': 'LogDate',
			'fieldtype': 'Data',
		},
	]

	data = frappe.db.sql("""select UserId,LogDate from `biometric` where DATE(LogDate)=%s """, (filters.date))
	return columns, data

