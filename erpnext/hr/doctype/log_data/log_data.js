// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Log Data', {
	// refresh: function(frm) {
	"date": function(frm, cdt, cdn){
		frappe.call({
			method:"erpnext.hr.doctype.log_data.log_data.get_date",

			args: {"date": frm.doc.date},

			// route: cur_frm.doc.route,
			callback :function(r){ 

			}
		});
	}
	// }
});
