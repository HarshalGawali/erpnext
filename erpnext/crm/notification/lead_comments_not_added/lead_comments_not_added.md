<h3>{{_("No comments have been added to this lead since three days : :")}}</h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
<p>Person Name: {{ frappe.db.get_value("Lead", "doc.reference_name", "lead_name")}}
<p>Organization Name: {{ frappe.db.get_value("Lead", "doc.reference_name", "company_name")}}
<p>Reference Name : {{ doc.reference_name }}</p>
<p>Comment By : {{ doc.comment_email }}</p>
<p>Content : {{ doc.content }}</p>

