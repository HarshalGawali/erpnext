<p> New Lead Assigned : </p>

<p>Person Name: {{ doc.lead_name }}</p>
<p>Referecne ID: {{ doc.name }}</p>
<p>Organization Name: {{ doc.company_name }}</p>
<p>Email Address: {{ doc.email_id }}</p>
<p>Lead Owner: {{ doc.lead_owner }}</p>
<p>Next Contact By: {{ doc.contact_by }}</p>

<!-- show last comment -->
{% if comments %}
Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}
{% endif %}