<h3>{{_("New Comment Addedd :")}}</h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
<p>Organization Name: {{ frappe.db.get_value("Lead", "doc.reference_name", "lead_name")}}
<p>Reference Name : {{ doc.reference_name }}</p>
<p>Comment By : {{ doc.comment_email }}</p>
<p>Content : {{ doc.content }}</p>

