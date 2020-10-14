<h3>{{_("New Comment Addedd :")}}</h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
{% set  d= frappe.get.doc("lead", "doc.reference_name")%}
<p>Organization Name: {{ d.company_name }}
<p>Reference Name : {{ doc.reference_name }}</p>
<p>Comment By : {{ doc.comment_email }}</p>
<p>Content : {{ doc.content }}</p>
