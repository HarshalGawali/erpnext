# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

from erpnext.accounts.report.sales_registers.sales_registers import _execute

def execute(filters=None):
	return _execute(filters, additional_table_columns=[
		#dict(fieldtype='Data', label='Customer GSTIN', fieldname="customer_gstin", width=120),
		dict(fieldtype='Data', label='GSTIN/UIN of Recipient', fieldname="billing_address_gstin", width=140),
		dict(fieldtype='Data', label='Invoice Number', fieldname="invoice", width=120),
		dict(fieldtype='Data', label='Invoice Date', fieldname="posting_date", width=120),
		dict(fieldtype='Currency', label='Invoice Value', fieldname="rounded_total", width=120),

		dict(fieldtype='Data', label='Sate where Supply is Made', fieldname="place_of_supply", width=120),
		dict(fieldtype='Currency', label='Taxble Value', fieldname="net_total", width=120),
	#	dict(fieldtype='Data', label='Export Type', fieldname="export_type", width=120),
	#	dict(fieldtype='Data', label='E-Commerce GSTIN', fieldname="ecommerce_gstin", width=130)
	], additional_query_columns=[
		'customer_gstin',
		'billing_address_gstin',
		'company_gstin',
		'place_of_supply',
		'reverse_charge',
		'gst_category',
		'export_type',
		'ecommerce_gstin'
	])

