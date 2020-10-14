// Copyright (c) 2019, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Biometric Attendance', {
	// refresh: function(frm) {
	"date": function(frm, cdt, cdn){
		frappe.call({
			method:"erpnext.hr.doctype.biometric_attendance.biometric_attendance.get_date",

			doctype: "biometric_attendance",
			args: {"date": frm.doc.date},

			// route: cur_frm.doc.route,
			callback :function(r){ 

			}
		});
	},
	// }
});
