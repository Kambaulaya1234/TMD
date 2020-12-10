from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views import View
from .models import Loan, Payment
from django.core.paginator import Paginator
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'loans/loan_index.html'
        loans = Loan.objects.filter(status=False).order_by('-created_at')
        paginator = Paginator(loans, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        context = {
            'Loans': filterItems,
        }
        return render(request, template_name, context)


class CompleteLoanListView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'loans/loan_complete_index.html'
        loans = Loan.objects.filter(status=True).order_by('-created_at')
        paginator = Paginator(loans, 10)
        page = request.GET.get('page')
        filterItems = paginator.get_page(page)
        context = {
            'Loans': filterItems,
        }
        return render(request, template_name, context)


class BaseObject:
    def get_object(self, id):
        loan = Loan.objects.filter(id=id)
        return loan


class RemoveView(View, BaseObject):
    def get(self, *args, **kwargs):
        self.get_object(kwargs['id']).delete()
        messages.success(self.request, 'loan deleted successfully!')
        return redirect('loan:index')


class LoanProgressPaymentView(View, BaseObject):
    def create_loan_payment(self,loan, paid,user):
        _payment = Payment.objects.create(loan=loan, paid=paid,by=user)
        return _payment

    def post(self, *args, **kwargs):
        loan = self.get_object(kwargs['id'])[0]
        _paid = self.request.POST['paid']
        if loan.paid <= (loan.profit_amount+loan.insurance):
            if float(_paid) <= ((loan.profit_amount+loan.insurance) - loan.paid):
                loan.paid += float(_paid)
                self.create_loan_payment(loan,_paid,self.request.user)
                loan.save()
                if loan.paid == (loan.profit_amount+loan.insurance):
                    loan.status = True
                    loan.paid = (loan.profit_amount+loan.insurance)
                    loan.save()
                messages.success(
                    self.request, f'TZS {_paid}/= paid to {loan.member} loan  successfully!')
            else:
                messages.warning(
                    self.request, f'Please consider only remained Amount (TZS { loan.total- loan.paid}/=)')
        return redirect('loan:index')


class LoanShowView(View, BaseObject):
    def get(self, *args, **kwargs):
        _ID = kwargs['id']
        _loan = self.get_object(_ID)[0]
        template_name = 'loans/loan_show_payment.html'
        context = {
            'loan': _loan,
        }
        return render(self.request, template_name, context)
