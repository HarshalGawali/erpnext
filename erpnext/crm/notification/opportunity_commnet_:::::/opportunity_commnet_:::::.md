<h3>{{_("New Opportunity Comment Addedd :")}}</h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
{% set  ref_d= frappe.get.doc(reference_doctype,doc.reference_name)%}
<p>Organization Name: {{ ref_d.customer_name}}
<p>Reference Name : {{ doc.reference_name }}</p>
<p>Comment By : {{ doc.comment_email }}</p>
<p>Content : {{ doc.content }}</p>

