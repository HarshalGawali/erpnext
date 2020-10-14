<h3>{{_("New Lead")}}</h3>

{% set d = frappe.get_doc("Lead",doc.lead) %}
<p>Organization Name: {{ doc.company_name }}</p>
<p>Email Address: {{ d.email_id }}</p>
<p>Next Contact By: {{ d.contact_by }}</p>
<p>Next Contact date: {{ d.contact_date }}</p>