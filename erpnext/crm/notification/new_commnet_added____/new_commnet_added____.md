<h3>{{_("New Comment Addedd :")}}</h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
<p> Doctype:{{doc.doctype}}<p>
<p>Reference Name : {{ doc.reference_name }}</p>
{% set ref_doc = frappe.get_doc(doc.reference_doctype, doc.reference_name ) %}
<p>Organization Namae : {{ ref_doc.company_name }}</p>
<p>Comment By : {{ doc.comment_email }}</p>
<p>Comment : {{ doc.content }}</p>


