<h3>{{_("Opportunity Follow up has been Overdued :")}}</h3>
<p>Organization Name: {{ doc.title }}</p>
<p>Opportunity ID : {{ doc.name }}</p>
<p>Contact date: {{ doc.contact_date }}</p>
<p>Contact By: {{ doc.contact_by }}</p>
<P>Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}