from __future__ import unicode_literals

import frappe

from frappe.utils import flt

from frappe.utils import cstr, cint, getdate

from frappe import _

from calendar import monthrange



def execute(filters=None):

        if not filters: filters = {}

        salary_slips = get_salary_slips(filters)

        if not salary_slips: return [], []

        #conditions, filters = get_conditions(filters)

        #att_map = get_attendance_list(conditions, filters)



        columns, earning_types, ded_types = get_columns(salary_slips)

        print("\neaaaarning_types",earning_types)

        print("\nded_types",ded_types)

        ss_earning_map = get_ss_earning_map(salary_slips)

        ss_ded_map = get_ss_ded_map(salary_slips)

        doj_map = get_employee_doj_map()



        data = []
	for ss in salary_slips:

                Employer_Contribution = None

                for p in earning_types:

                        if (p == "Employer's contribution to ESIC"):

                                print("Employer_Contribution",ss_earning_map.get(ss.name, {}).get(p))

                                Employer_Contribution = (ss_earning_map.get(ss.name, {}).get(p))

                                break

                        else:

                                Employer_Contribution = None



                ESI_Contribution = None

                for q in ded_types:

                        if (q == "ESIC"):
				print("ESI_Contribution",ss_earning_map.get(ss.name, {}).get(q))

                                ESI_Contribution = (ss_earning_map.get(ss.name, {}).get(q))

                                break

                        else:

                                ESI_Contribution = None





                if (Employer_Contribution == None and  ESI_Contribution == None) != None:



                #row = [ss.name, ss.employee, ss.employee_name, ss.date_of_birth, doj_map.get(ss.employee),  ss.department, ss.designation,

                #       ss.company, ss.start_date, ss.end_date, ss.leave_without_pay, ss.payment_days]



                        row = [ss.esic_no, ss.employee_name, ss.payment_days]
			print("\nTYPE employee_name",type(ss.employee_name))

                        print("\nTYPE ESI no:",type(ss.esi_no))

                        OT = 0.00

                        NSA = 0.00

                        SI = 0.00

                        for e in earning_types:





                                if (e == "Over Time"):

                                        print("Over Time",ss_earning_map.get(ss.name, {}).get(e))

                                        OT = (ss_earning_map.get(ss.name, {}).get(e))

                                        print("\nTYPEOT:",type(OT))

                                        if OT == None:
						OT = 0.00



                                if (e == "Night Shift Allowance"):

                                        print("Night Shift Allowance",ss_earning_map.get(ss.name, {}).get(e))

                                        NSA = (ss_earning_map.get(ss.name, {}).get(e))

                                        print("\nTYPE NSA:",type(NSA))

                                        if NSA == None:

                                                NSA = 0.00

                                

                                if (e == "Shift Incentive"):

                                        print("Shift Incentive",ss_earning_map.get(ss.name, {}).get(e))

                                        SI = (ss_earning_map.get(ss.name, {}).get(e))

                                        print("\nTYPE NSA:",type(SI))
					if SI == None:

                                                SI = 0.00





                        p = ss.gross_pay - OT -SI - NSA

                                        #print("\nESIC E",ss_earning_map.get(ss.name, {}).get(e))

                        row.append(p)



                        for e in earning_types:

                                if (e == "Employer's contribution to ESIC"):

                                        print("\nE    C E",ss_earning_map.get(ss.name, {}).get(e))

                                        row.append(ss_earning_map.get(ss.name, {}).get(e))
			for d in ded_types:

                                if d == "ESIC":

                                        row.append(ss_ded_map.get(ss.name, {}).get(d))

                        #if ss.name == "Gajendra Chavan":



                        print("\nROW:",row)

                        #row += [ss.esi_erning]

                        #row.append(ss.total_loan_repayment)



                        #row += [ss.total_deduction, ss.net_pay]

			data.append(row)

                        print("\nDATA:",data)

                else:

                        data = []

        return columns, data



def get_columns(salary_slips):

        """

        columns = [

                _("Salary Slip ID") + ":Link/Salary Slip:150",_("Employee") + ":Link/Employee:120", _("Employee Name") + "::140",

                _("Date of Joining") + "::80", _("Branch") + ":Link/Branch:120", _("Department") + ":Link/Department:120",

                _("Designation") + ":Link/Designation:120", _("Company") + ":Link/Company:120", _("Start Date") + "::80",

                _("End Date") + "::80", _("Leave Without Pay") + ":Float:130", _("Payment Days") + ":Float:120"

	]

        """

        columns = [_("ESIC No.") + "::120",

                _("Name of Member") + "::140",_("Days Worked ") + ":Float:120",_("ESI Earning") + ":Float:120"

        ]



        salary_components = {_("Earning"): [], _("Deduction"): []}



        for component in frappe.db.sql("""select distinct sd.salary_component, sc.type

                from `tabSalary Detail` sd, `tabSalary Component` sc

                where sc.name=sd.salary_component and sd.amount != 0 and sd.parent in (%s)""" %

                (', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1):

                salary_components[_(component.type)].append(component.salary_component)
	E = []

        for e in salary_components[_("Earning")]:

                if (e == "Employer's contribution to ESIC"):

                        e = "Employer Contribution"

                        E = [(e + ":Currency:120")]

        D = []

        for d in salary_components[_("Deduction")]:

                if (d == "ESIC") :

                        d = "ESI Contribution"

                        D += [(d + ":Currency:120")]

	columns = columns + D + E

        #columns +=  [_("ESI Earning") + "::140"]

        print("\n columns",columns)

        return columns, salary_components[_("Earning")], salary_components[_("Deduction")]



def get_salary_slips(filters):

        filters.update({"from_date": filters.get("from_date"), "to_date":filters.get("to_date")})

        print("\nFILTERS Before:",filters)

        conditions, filters = get_conditions(filters)

        print("\nFILTERS:",filters)

        #salary_slips = frappe.db.sql("""select *, date_of_birth from `tabSalary Slip` INNER JOIN `tabEmployee` ON (`tabSalary Slip`.employee $

        #salary_slips = frappe.db.sql("""select * from `tabSalary Slip`""", as_dict=1)

        salary_slips = frappe.db.sql("""select * from `tabSalary Slip` where %s

				order by employee""" % conditions, filters, as_dict=1)

        print ("\n salary_slips",salary_slips)

        return salary_slips or []



def get_conditions(filters):

        if not (filters.get("month") and filters.get("year")):

                msgprint(_("Please select month and year"), raise_exception=1)



        filters["month"] = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov",

                "Dec"].index(filters.month) + 1



        filters["total_days_in_month"] = monthrange(cint(filters.year), filters.month)[1]
	conditions = " month(posting_date) = %(month)s and year(posting_date) = %(year)s"



        if filters.get("company"): conditions += " and company = %(company)s"

        if filters.get("employee"): conditions += " and employee = %(employee)s"



        return conditions, filters
def get_employee_doj_map():

        return  frappe._dict(frappe.db.sql("""

                                SELECT

                                        employee,

                                        date_of_joining

                                FROM `tabEmployee`

                                """))



def get_ss_earning_map(salary_slips):

        ss_earnings = frappe.db.sql("""select parent, salary_component, amount

                from `tabSalary Detail` where parent in (%s)""" %

                (', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1)

        print("\nss_earnings",ss_earnings)

        ss_earning_map = {}

        for d in ss_earnings:

                ss_earning_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, [])

                ss_earning_map[d.parent][d.salary_component] = flt(d.amount)

        print("\nss_earning_map",ss_earning_map)

        return ss_earning_map



def get_ss_ded_map(salary_slips):

        ss_deductions = frappe.db.sql("""select parent, salary_component, amount

                from `tabSalary Detail` where parent in (%s)""" %

                (', '.join(['%s']*len(salary_slips))), tuple([d.name for d in salary_slips]), as_dict=1)



        ss_ded_map = {}

        for d in ss_deductions:

                ss_ded_map.setdefault(d.parent, frappe._dict()).setdefault(d.salary_component, [])

                ss_ded_map[d.parent][d.salary_component] = flt(d.amount)



        return ss_ded_map



def get_attendance_list(conditions, filters):

        attendance_list = frappe.db.sql("""select employee, day(posting_date) as day_of_month,

                status from `tabSalary Slip` where docstatus = 1 %s order by employee, posting_date""" %

                conditions, filters, as_dict=1)



        att_map = {}

        for d in attendance_list:

                att_map.setdefault(d.employee, frappe._dict()).setdefault(d.day_of_month, "")

                att_map[d.employee][d.day_of_month] = d.status



        return att_map



@frappe.whitelist()

def get_attendance_years():

        year_list = frappe.db.sql_list("""select distinct YEAR(posting_date) from `tabSalary Slip` ORDER BY YEAR(posting_date) DESC""")

        if not year_list:

                year_list = [getdate().year]



        return "\n".join(str(year) for year in year_list)
