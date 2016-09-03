from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from models import Process, StringParameter, DateParameter
from django.contrib.auth.decorators import login_required
from cbase.views import isLoggedIn
from products.models import Product
from charges.models import Charge, Account
from fees.models import Fee
from readonly.models import CustomerView
from administer.models import CustomUser
from django.db.models import Max
# Create your views here.

@login_required(login_url='/')
def index(request):

    return redirect('/')

@login_required(login_url='/')
def chargeowners(request):

    loggedIn = isLoggedIn(request)
    run = Process.objects.all().filter(code='CHARGEOWNERS')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('processes/fail.html', context, context_instance=RequestContext(request))
        else:
            run.run = False
            run.save()
            invoice_date = DateParameter.objects.all().filter(process__code='CHARGEOWNERS').filter(code='INVDATE')[0]
            due_date = DateParameter.objects.all().filter(process__code='CHARGEOWNERS').filter(code='DUEDATE')[0]
            charge = Product.objects.all().filter(code='DUES').filter(active_flag=True)[0]
            accounts = Account.objects.all().filter(active_flag=True)
            last_charge_num = Charge.objects.all().aggregate(Max('charge_num'))
            inc_charge_num = last_charge_num['charge_num__max']
            start_charge_num = inc_charge_num + 1

            for i, account in enumerate(accounts):

                inc_charge_num = inc_charge_num + 1

                newcharge = Charge(account_id=account.id, amount=charge.price \
                            , charge_num=inc_charge_num, product_id=charge.id \
                            , invoice_date=invoice_date.parameter, due_date=due_date.parameter \
                            , type_code='')
                newcharge.save()

            created_charges = inc_charge_num - (start_charge_num-1)

            context = {'total': created_charges, 'start':start_charge_num, 'end':inc_charge_num}
            return render_to_response('processes/index.html', context, context_instance=RequestContext(request))


        #return redirect('http://www.yahoo.com')

@login_required(login_url='/')
def latefees(request):

    loggedIn = isLoggedIn(request)
    run = Process.objects.all().filter(code='LATEFEES')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('processes/fail.html', context, context_instance=RequestContext(request))
        else:
            run.run = False
            run.save()
            invoice_date = DateParameter.objects.all().filter(process__code='LATEFEES').filter(code='INVDATE')[0]
            due_date = DateParameter.objects.all().filter(process__code='LATEFEES').filter(code='DUEDATE')[0]
            mode = StringParameter.objects.all().filter(process__code='LATEFEES').filter(code='MODE')[0]
            charge = Product.objects.all().filter(code='LATEFEE').filter(active_flag=True)[0]
            fee = Fee.objects.all().filter(code='LATEFEE').filter(active_flag=True)[0]
            accounts = CustomerView.objects.all().filter(balance__gte='1')
            last_charge_num = Charge.objects.all().aggregate(Max('charge_num'))
            inc_charge_num = last_charge_num['charge_num__max']
            start_charge_num = inc_charge_num + 1
            testaccounts = []
            for i, account in enumerate(accounts):
                inc_charge_num = inc_charge_num + 1
                product_price = round(((fee.value/100)*account.balance), 2)
                testaccount = {'account': account.account_id, 'invoice_date': invoice_date.parameter \
                             , 'due_date': due_date.parameter \
                             , 'product': charge.id, 'price': product_price \
                             , 'charge_num': inc_charge_num, 'type_code': ''}
                testaccounts.append(testaccount)
                if mode.parameter == 'C' or mode.parameter == 'c':
                    newcharge = Charge(account_id=account.account_id, amount=product_price \
                                , charge_num=inc_charge_num, product_id=charge.id \
                                , invoice_date=invoice_date.parameter, due_date=due_date.parameter \
                                , type_code='')
                    newcharge.save()
                    mode_string = 'Charge Mode'
                else:
                    mode_string = 'Audit Mode'

            created_charges = inc_charge_num - (start_charge_num-1)

            # context = { 'total': created_charges, 'start':start_charge_num, 'end':inc_charge_num }
            context = { 'total': created_charges, 'start':start_charge_num, 'end':inc_charge_num, 'accounts': testaccounts, 'mode': mode_string }
            return render_to_response('processes/latefees.html', context, context_instance=RequestContext(request))


@login_required(login_url='/')
def accesscontrol(request):

    loggedIn = isLoggedIn(request)
    run = Process.objects.all().filter(code='SETISSTAFF')[0]
    if run.group not in loggedIn[1]:
        context = {}
        return render_to_response('error.html', context, context_instance=RequestContext(request))
    else:

        if run.run == False:
            context = {'fail':'You did not set the run parameter'}
            return render_to_response('processes/fail.html', context, context_instance=RequestContext(request))
        else:
            run.run = False
            run.save()
            mode = StringParameter.objects.all().filter(process__code='SETISSTAFF').filter(code='MODE')[0]
            users = CustomUser.objects.all()

            if mode.parameter == 'G' or mode.parameter == 'R':

                if mode.parameter == 'G':
                    mode_set = 1
                    message = 'Access restored.'
                else:
                    mode_set = 0
                    message = 'Access removed.'

                for i, user in enumerate(users):

                    if user.id > 1:
                        i_user = None
                        i_user = CustomUser.objects.get(pk=user.id)
                        i_user.is_staff = mode_set
                        i_user.save()

                context = {'message': message}
                return render_to_response('processes/access_control.html', context, context_instance=RequestContext(request))
            else:
                context = {'fail':'You did not set a valid mode parameter'}
                return render_to_response('processes/fail.html', context, context_instance=RequestContext(request))