<h3><p>No comments have been added to this opportunity since three days :</p></h3>
<p>Refernce Doc : {{ doc.reference_doctype }}</p>
<p> Doctype:{{doc.doctype}}<p>
<p>Reference Name : {{ doc.reference_name }}</p>
{% set ref_doc = frappe.get_doc(doc.reference_doctype, doc.reference_name ) %}

{% if doc.reference_doctype=="Lead" %}
  {% if ref_doc.status=="Lead" %} 
   <p>Organization Name : {{ ref_doc.company_name }}</p>
   <p>Next Followup Date : {{ref_doc.contact_date}}</p>
  {% endif %} 
{% endif %}

{% if doc.reference_doctype=="Lead" %}
  {% if ref_doc.status=="Open" %} 
   <p>Organization Name : {{ ref_doc.company_name }}</p>
   <p>Next Followup Date : {{ref_doc.contact_date}}</p>
  {% endif %} 
{% endif %}


{% if doc.reference_doctype=="Opportunity" %}
  {% if ref_doc.status=="Open" %} 
   <p>Organization Name : {{ ref_doc.customer_name }}</p>
   <p>Next Followup Date : {{ref_doc.contact_date}} </p>
  {% endif %} 
{% endif %}

{% if doc.reference_doctype=="Quotation" %}
  {% if ref_doc.status=="Open" %} 
   <p>Organization Name : {{ ref_doc.customer_name }}</p>
   <p>Quotation Date : {{ref_doc.transaction_date }}</p>
  {% endif %}
{% endif %}

<p>Comment By : {{ doc.comment_email }}</p>
<p>Comment : {{ doc.content }}</p>
