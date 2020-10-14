<h3>{{_("Lead Overdue Follow-up Reminder :")}}</h3>
<p>Lead ID: {{ doc.name }}</p>
<p>Organization Name: {{ doc.company_name }}</p>
<p>Status: {{ doc.status }}</p>
<p>Contact date: {{ doc.contact_date }}</p>
<p>Contact By: {{ doc.next_contact }}</p>
<P>Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}<P>