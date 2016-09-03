from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, FloatField
# Create your views here.
from cbase.views import isLoggedIn
from customers.models import Customer
from charges.models import Charge 
from payments.models import Payment
from processes.models import Process, StringParameter, DateParameter

@login_required(login_url='/')
def index(request):

    loggedIn = isLoggedIn(request)
    run = Process.objects.all().filter(code='ALLSTATEMENTS')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('statements/fail.html', context, context_instance=RequestContext(request))


        note = StringParameter.objects.all().filter(process__code='ALLSTATEMENTS').filter(code='NOTES')[0]
        statementdate = DateParameter.objects.all().filter(process__code='ALLSTATEMENTS').filter(code='STATEMENTDATE')[0]

        #charges = Charge.objects.filter(account__active_flag=True).filter(type_code='').values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code', 'account__id')

        customers = Customer.objects.filter(active_flag=True).values('id', 'contact_first_name' \
        , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
        , 'postal_code', 'account__account_number', 'account__property__number' \
        , 'account__property__street', 'account__property__section', 'account__property__lot' \
        , 'account__id')

        newcustomers = []

        for i, customer in enumerate(customers):

            newcharges = []
            payment_var = 0

            payments = Payment.objects.all().filter(account__id=customer['account__id']).filter(type_code='').aggregate( \
                       total_payments=Sum('amount', output_field=FloatField()))


            charges = Charge.objects.order_by('invoice_date').filter(account__active_flag=True) \
                      .filter(type_code='').filter(account__id=customer['account__id']) \
                      .values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code' \
                              , 'account__id', 'product__name')

            if payments['total_payments'] > 0:
                payment_var = float(str(payments['total_payments']))
            else:
                payment_var = 0

            for i, charge in enumerate(charges):

                paid_status = ''

                payment_var = payment_var - charge['amount']

                if payment_var >= 0:
                    paid_status = 'Paid'
                elif payment_var < 0:
                    if payment_var + charge['amount'] <= 0:
                        paid_status = 'Unpaid'
                    else:
                        paid_status = 'Partial'

                newcharge = {'charge_num': charge['charge_num'], 'amount': charge['amount'] \
                , 'invoice_date': charge['invoice_date'], 'due_date': charge['due_date'] \
                , 'type_code': charge['type_code'], 'account__id': charge['account__id'] \
                , 'paid_status': paid_status, 'product': charge['product__name']}

                newcharges.append(newcharge)


            if payment_var == 0:
                message = 'Nothing currently due. You currently have a balance of $' + str(format(payment_var, '.2f')) + '. '
            elif payment_var > 0:
                message = 'Nothing currently due. You currently have a positive balance of $' + str(format(payment_var, '.2f')) + ' that will be applied to future bills. '
            else:
                message = '<b>Current Due: $ ' + str(format(((-1)*payment_var), '.2f')).rjust(10, '*') + '</b>'

            newcustomer = {'id': customer['id'], 'contact_first_name': customer['contact_first_name'] \
            , 'contact_last_name': customer['contact_last_name'], 'country': customer['country'] \
            , 'state': customer['state'], 'address_line_1': customer['address_line_1'] \
            , 'address_line_2': customer['address_line_2'], 'city': customer['city'] \
            , 'postal_code': customer['postal_code'] \
            , 'account__account_number': customer['account__account_number'] \
            , 'account__property__number': customer['account__property__number'] \
            , 'account__property__street': customer['account__property__street'] \
            , 'account__property__section': customer['account__property__section'] \
            , 'account__property__lot': customer['account__property__lot'] \
            , 'account__id': customer['account__id'] \
            , 'charges': newcharges
            , 'payments': message}

            newcustomers.append(newcustomer)
            
        context = {'customers':newcustomers, 'note':note, 'statementdate': statementdate }

        return render_to_response('statements/index.html', context, context_instance=RequestContext(request))




@login_required(login_url='/')
def single(request, *args, **kwargs):


    loggedIn = isLoggedIn(request)
    if 'ReadOnly' not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        customer_id = int(kwargs['id'])

        if customer_id == 0:
            return redirect('/')           


        #charges = Charge.objects.filter(account__active_flag=True).filter(type_code='').values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code', 'account__id')

        customers = Customer.objects.filter(active_flag=True).filter(id=customer_id).values('id', 'contact_first_name' \
        , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
        , 'postal_code', 'account__account_number', 'account__property__number' \
        , 'account__property__street', 'account__property__section', 'account__property__lot' \
        , 'account__id')

        newcustomers = []

        for i, customer in enumerate(customers):

            newcharges = []
            payment_var = 0

            payments = Payment.objects.all().filter(account__id=customer['account__id']).filter(type_code='').aggregate( \
                       total_payments=Sum('amount', output_field=FloatField()))


            charges = Charge.objects.order_by('invoice_date').filter(account__active_flag=True) \
                      .filter(type_code='').filter(account__id=customer['account__id']) \
                      .values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code' \
                              , 'account__id', 'product__name')

            if payments['total_payments'] > 0:
                payment_var = float(str(payments['total_payments']))
            else:
                payment_var = 0

            for i, charge in enumerate(charges):

                paid_status = ''

                payment_var = payment_var - charge['amount']

                if payment_var >= 0:
                    paid_status = 'Paid'
                elif payment_var < 0:
                    if payment_var + charge['amount'] <= 0:
                        paid_status = 'Unpaid'
                    else:
                        paid_status = 'Partial'

                newcharge = {'charge_num': charge['charge_num'], 'amount': charge['amount'] \
                , 'invoice_date': charge['invoice_date'], 'due_date': charge['due_date'] \
                , 'type_code': charge['type_code'], 'account__id': charge['account__id'] \
                , 'paid_status': paid_status, 'product': charge['product__name']}

                newcharges.append(newcharge)

            if payment_var == 0:
                message = 'Nothing currently due. You currently have a balance of $' + str(format(payment_var, '.2f')) + '. '
            elif payment_var > 0:
                message = 'Nothing currently due. You currently have a positive balance of $' + str(format(payment_var, '.2f')) + ' that will be applied to future bills. '
            else:
                message = '<b>Current Due: $ ' + str(format(((-1)*payment_var), '.2f')).rjust(10, '*') + '</b>'


            newcustomer = {'id': customer['id'], 'contact_first_name': customer['contact_first_name'] \
            , 'contact_last_name': customer['contact_last_name'], 'country': customer['country'] \
            , 'state': customer['state'], 'address_line_1': customer['address_line_1'] \
            , 'address_line_2': customer['address_line_2'], 'city': customer['city'] \
            , 'postal_code': customer['postal_code'] \
            , 'account__account_number': customer['account__account_number'] \
            , 'account__property__number': customer['account__property__number'] \
            , 'account__property__street': customer['account__property__street'] \
            , 'account__property__section': customer['account__property__section'] \
            , 'account__property__lot': customer['account__property__lot'] \
            , 'account__id': customer['account__id'] \
            , 'charges': newcharges
            , 'payments': message}

            newcustomers.append(newcustomer)

        context = {'customers':newcustomers}

        return render_to_response('statements/single.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def balance(request):

    loggedIn = isLoggedIn(request)
    run = Process.objects.all().filter(code='BALANCEDUE')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('statements/fail.html', context, context_instance=RequestContext(request))

        note = StringParameter.objects.all().filter(process__code='BALANCEDUE').filter(code='NOTES')[0]
        statementdate = DateParameter.objects.all().filter(process__code='BALANCEDUE').filter(code='STATEMENTDATE')[0]


        #charges = Charge.objects.filter(account__active_flag=True).filter(type_code='').values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code', 'account__id')

        customers = Customer.objects.filter(active_flag=True).values('id', 'contact_first_name' \
        , 'contact_last_name', 'country', 'state', 'address_line_1', 'address_line_2', 'city' \
        , 'postal_code', 'account__account_number', 'account__property__number' \
        , 'account__property__street', 'account__property__section', 'account__property__lot' \
        , 'account__id')

        newcustomers = []

        for i, customer in enumerate(customers):

            newcharges = []
            payment_var = 0

            payments = Payment.objects.all().filter(account__id=customer['account__id']).filter(type_code='').aggregate( \
                       total_payments=Sum('amount', output_field=FloatField()))


            charges = Charge.objects.order_by('invoice_date').filter(account__active_flag=True) \
                      .filter(type_code='').filter(account__id=customer['account__id']) \
                      .values('charge_num', 'amount', 'invoice_date', 'due_date', 'type_code' \
                              , 'account__id', 'product__name')

            if payments['total_payments'] > 0:
                payment_var = float(str(payments['total_payments']))
            else:
                payment_var = 0

            for i, charge in enumerate(charges):

                paid_status = ''

                payment_var = payment_var - charge['amount']

                if payment_var >= 0:
                    paid_status = 'Paid'
                elif payment_var < 0:
                    if payment_var + charge['amount'] <= 0:
                        paid_status = 'Unpaid'
                    else:
                        paid_status = 'Partial'

                newcharge = {'charge_num': charge['charge_num'], 'amount': charge['amount'] \
                , 'invoice_date': charge['invoice_date'], 'due_date': charge['due_date'] \
                , 'type_code': charge['type_code'], 'account__id': charge['account__id'] \
                , 'paid_status': paid_status, 'product': charge['product__name']}

                newcharges.append(newcharge)


            if payment_var == 0:
                message = 'Nothing currently due. You currently have a balance of $' + str(format(payment_var, '.2f')) + '. '
            elif payment_var > 0:
                message = 'Nothing currently due. You currently have a positive balance of $' + str(format(payment_var, '.2f')) + ' that will be applied to future bills. '
            else:
                message = '<b>Current Due: $ ' + str(format(((-1)*payment_var), '.2f')).rjust(10, '*') + '</b>'
                newcustomer = {'id': customer['id'], 'contact_first_name': customer['contact_first_name'] \
                , 'contact_last_name': customer['contact_last_name'], 'country': customer['country'] \
                , 'state': customer['state'], 'address_line_1': customer['address_line_1'] \
                , 'address_line_2': customer['address_line_2'], 'city': customer['city'] \
                , 'postal_code': customer['postal_code'] \
                , 'account__account_number': customer['account__account_number'] \
                , 'account__property__number': customer['account__property__number'] \
                , 'account__property__street': customer['account__property__street'] \
                , 'account__property__section': customer['account__property__section'] \
                , 'account__property__lot': customer['account__property__lot'] \
                , 'account__id': customer['account__id'] \
                , 'charges': newcharges
                , 'payments': message}

                newcustomers.append(newcustomer)

        context = {'customers':newcustomers, 'note':note, 'statementdate': statementdate}

        return render_to_response('statements/index.html', context, context_instance=RequestContext(request))
