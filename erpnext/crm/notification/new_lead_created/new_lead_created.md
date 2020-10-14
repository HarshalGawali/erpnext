<h3>{{_("New Lead")}}</h3>

{% set d = frappe.get_doc("Lead",doc.lead) %}
<p>Person Name: {{ d.lead_name }}</p>
<p>Organization Name: {{ d.company_name }}</p>
<p>Email Address: {{ d.email_id }}</p>
<p>Lead Owner: {{ d.lead_owner }}</p>
<p>Next Contact By: {{ d.contact_by }}</p>