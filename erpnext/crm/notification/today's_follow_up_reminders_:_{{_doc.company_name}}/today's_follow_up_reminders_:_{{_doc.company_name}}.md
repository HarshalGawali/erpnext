<h3>{{_("Today's Followups :")}}</h3>

<p>Organization Name: {{ doc.company_name }}</p>
<p>Reference Name : {{ doc.name }}</p>
<p>Email Address: {{ doc.email_id }}</p>
<p>Contact date: {{ doc.contact_date }}</p>
<p>Contact By: {{ doc.next_contact }}</p>
<P>Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}</p>
