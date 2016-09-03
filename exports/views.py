from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField
# Create your views here.
from cbase.views import isLoggedIn
from customers.models import Customer
from charges.models import Charge 
from payments.models import Payment
from exports.models import Export, StringParameter, DateParameter
from django.http import HttpResponse
from django.conf import settings
import csv


@login_required(login_url='/')
def balance(request):

    loggedIn = isLoggedIn(request)
    run = Export.objects.all().filter(code='ACCOUNTBALANCES')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('exports/fail.html', context, context_instance=RequestContext(request))

        readable = StringParameter.objects.all().filter(export__code='ACCOUNTBALANCES').filter(code='READABLE')[0]

        if readable.parameter.strip() == '':
            readableparam = 'export.csv'
        else:
            readableparam = readable.parameter + '.csv'

        balancestatus = StringParameter.objects.all().filter(export__code='ACCOUNTBALANCES').filter(code='BALANCE')[0]

        balanceparam = balancestatus.parameter
        if balanceparam not in ('A', 'a', 'P', 'p', 'D', 'd'):
            balanceparam = 'A'
            balancestatus.parameter = 'A'
            balancestatus.save()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % (readableparam)

        writer = csv.writer(response)
        writer.writerow(['AccountNumber', 'Name', 'Balance'])

        customers = Customer.objects.filter(active_flag=True).values('id', 'contact_first_name' \
        , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
        , 'postal_code', 'account__account_number', 'account__property__number' \
        , 'account__property__street', 'account__property__section', 'account__property__lot' \
        , 'account__id')

        newcustomers = []

        for i, customer in enumerate(customers):

            payment_var = 0

            payments = Payment.objects.all().filter(account__id=customer['account__id']).filter(type_code='').aggregate( \
                       total_payments=Sum('amount', output_field=FloatField()))


            charges = Charge.objects.all().filter(account__id=customer['account__id']).filter(type_code='').aggregate( \
                       total_charges=Sum('amount', output_field=FloatField()))



            if payments['total_payments'] > 0:
                payment_var = float(str(payments['total_payments']))
            else:
                payment_var = 0

            if charges['total_charges'] > 0:
                charge_var = float(str(charges['total_charges']))
            else: 
                charge_var = 0

            balance = (charge_var - payment_var)

            if balanceparam == 'A':
                writer.writerow([customer['account__account_number'], customer['contact_first_name'] + ' ' + customer['contact_last_name'], balance])
            elif balanceparam == 'P':
                if balance <= 0:
                    writer.writerow([customer['account__account_number'], customer['contact_first_name'] + ' ' + customer['contact_last_name'], balance])
            elif balanceparam == 'D':
                if balance > 0:
                    writer.writerow([customer['account__account_number'], customer['contact_first_name'] + ' ' + customer['contact_last_name'], balance])


        return response

@login_required(login_url='/')
def accountdata(request):

    loggedIn = isLoggedIn(request)
    run = Export.objects.all().filter(code='ACCOUNTDATA')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('exports/fail.html', context, context_instance=RequestContext(request))

        readable = StringParameter.objects.all().filter(export__code='ACCOUNTDATA').filter(code='READABLE')[0]

        if readable.parameter.strip() == '':
            readableparam = 'export.csv'
        else:
            readableparam = readable.parameter + '.csv'

        accounttype = StringParameter.objects.all().filter(export__code='ACCOUNTDATA').filter(code='ACCOUNTTYPE')[0]

        accounttypeparam = accounttype.parameter
        if accounttypeparam not in ('A', 'a', 'H', 'h'):
            accounttypeparam = 'A'
            accounttype.parameter = 'A'
            accounttype.save()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % (readableparam)

        writer = csv.writer(response)
        writer.writerow(['FirstName', 'LastName', 'Country', 'State', 'Address1', 'Address2', 'City', 'PostalCode' \
		                 , 'Account', 'PropertyNum', 'PropertyStreet', 'Section', 'Lot', 'ActiveFlag'])

		
        if accounttypeparam == 'A':
            customers = Customer.objects.filter(active_flag=True).values('id', 'contact_first_name' \
            , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
            , 'postal_code', 'account__account_number', 'account__property__number' \
            , 'account__property__street', 'account__property__section', 'account__property__lot' \
            , 'account__id', 'active_flag')
        else:
            customers = Customer.objects.values('id', 'contact_first_name' \
            , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
            , 'postal_code', 'account__account_number', 'account__property__number' \
            , 'account__property__street', 'account__property__section', 'account__property__lot' \
            , 'account__id', 'active_flag')

        newcustomers = []

        for i, customer in enumerate(customers):
            writer.writerow([customer['contact_first_name'], customer['contact_last_name'] \
			, customer['country'], customer['state'], customer['address_line_1'], customer['address_line_2'], customer['city'] \
            , customer['postal_code'], customer['account__account_number'], customer['account__property__number'] \
            , customer['account__property__street'], customer['account__property__section'], customer['account__property__lot'] \
            , customer['active_flag']])


        return response


@login_required(login_url='/')
def accountdetail(request):

    loggedIn = isLoggedIn(request)
    run = Export.objects.all().filter(code='ACCOUNTACTIVITY')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('exports/fail.html', context, context_instance=RequestContext(request))

        readable = StringParameter.objects.all().filter(export__code='ACCOUNTACTIVITY').filter(code='READABLE')[0]

        if readable.parameter.strip() == '':
            readableparam = 'export.csv'
        else:
            readableparam = readable.parameter + '.csv'

        accounttype = StringParameter.objects.all().filter(export__code='ACCOUNTACTIVITY').filter(code='ACCOUNTTYPE')[0]

        accounttypeparam = accounttype.parameter
        if accounttypeparam not in ('A', 'a', 'H', 'h'):
            accounttypeparam = 'A'
            accounttype.parameter = 'A'
            accounttype.save()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="%s"' % (readableparam)

        writer = csv.writer(response)
        writer.writerow(['Account', 'PaymentAmount', 'ChargeAmount', 'ChargeNum' \
        , 'Memo', 'InstrumentNum', 'Date', 'Type', 'ActiveFlag'])

		
        if accounttypeparam == 'A':
            customers = Customer.objects.filter(active_flag=True).values('id', 'contact_first_name' \
            , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
            , 'postal_code', 'account__account_number', 'account__property__number' \
            , 'account__property__street', 'account__property__section', 'account__property__lot' \
            , 'account__id', 'active_flag')
        else:
            customers = Customer.objects.values('id', 'contact_first_name' \
            , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
            , 'postal_code', 'account__account_number', 'account__property__number' \
            , 'account__property__street', 'account__property__section', 'account__property__lot' \
            , 'account__id', 'active_flag')

        for i, customer in enumerate(customers):

            charges = None
            payments = None

            charges = Charge.objects.filter(account__id=customer['account__id']).values('account' \
            , 'charge_num', 'product', 'amount', 'invoice_date', 'due_date', 'type_code')

            payments = Payment.objects.filter(account__id=customer['account__id']).values('account' \
            , 'amount', 'instrument_number', 'memo', 'payment_date', 'postmark_date', 'processed_date', 'type_code')

            if charges:
                for i, charge in enumerate(charges):
                    writer.writerow([customer['account__account_number'], '', charge['amount'], charge['charge_num'] \
                    , '', '', charge['due_date'], charge['type_code'], customer['active_flag']])

            if payments:
                for i, payment in enumerate(payments):
                    writer.writerow([customer['account__account_number'], payment['amount'], '', '', payment['memo'] \
                    , payment['instrument_number'], payment['payment_date'], payment['type_code'], customer['active_flag']])

        return response
				
