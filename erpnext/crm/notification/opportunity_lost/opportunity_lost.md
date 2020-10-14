<h3>{{_("Opportunity Lost :")}}</h3>
<p></p>
<p>Organization Name: {{ doc.title }}</p>
<p>Lead ID : {{ doc.name }}</p>
<p>Contact date: {{ doc.contact_date }}</p>
<p>Contact By: {{ doc.contact_by }}</p>
<p>Status: {{ doc.status }}</p>

<P>Last comment: {{ comments[-1].comment }} by {{ comments[-1].by }}