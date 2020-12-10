from django.conf import settings
from django.contrib.auth.models import User, Group
from django.db.models import Avg, Sum
from django import template
from balance.models import Balance
from share.models import Share
from loan.models import Loan
from member.models import Member


register = template.Library()


# User=settings.AUTH_USER_MODEL

# @register.inclusion_tag('category/category_layouts/category.html')
# def job_panel():
#     infoForm=InformationForm()
#     return {
#                     'infos':infoForm,
#     }


@register.simple_tag(takes_context=True, name='user_count')
def user_count(context):
    request = context['request']
    users = User.objects.filter(is_superuser=True).count()
    return users


@register.simple_tag(takes_context=True, name='member_count')
def member_count(context):
    request = context['request']
    users = Member.objects.count()
    return users


@register.simple_tag(name='group_count')
def group_count():
    groups = Group.objects.count()
    return groups


@register.simple_tag(takes_context=True, name='groups_name')
def groups_name(context):
    request = context['request']
    for group in request.user.groups:
        return{
            'groups_name': groups_name
        }


# @register.simple_tag(name='total_amount', takes_context=True)
# def total_amount(context):
#     _t = Balance.objects.aggregate(total=Sum('total'))
#     return _t


@register.simple_tag(name='share_amount', takes_context=True)
def share_amount(context):
    rate = 30000
    _hisa = Share.objects.aggregate(total=Sum('hisa'))
    if _hisa['total'] is not None:
        _t = int(_hisa['total']) * rate
    else:
        _t = 0
    return _t


@register.simple_tag(name='share_count')
def share_count(member):
    if member is not None:
        _hisa = Share.objects.filter(member=member).count()
    else:
        _hisa = 0
    return _hisa


@register.simple_tag(name='all_share_count')
def all_share_count():
    if Share.objects.exists():
        _hisa = Share.objects.all().count()
    else:
        _hisa = 0
    return _hisa


@register.simple_tag(name='jamii_amount', takes_context=True)
def jamii_amount(context):
    _jamii = Share.objects.aggregate(total=Sum('jamii'))
    _t = ['total']
    if _jamii['total'] is not None:
        _t = int(_jamii['total'])
    else:
        _t = 0
    return _t


@register.simple_tag(name='fine_amount', takes_context=True)
def fine_amount(context):
    _fine = Share.objects.aggregate(total=Sum('fine'))
    if _fine['total'] is not None:
        _t = int(_fine['total'])
    else:
        _t = 0
    return _t


@register.simple_tag(name='loan_amount')
def loan_amount():
    _loan = Loan.objects.aggregate(total=Sum('amount'))
    if _loan['total'] is None:
        _loan['total'] = 0
    return _loan['total']


@register.simple_tag(name='loan_count')
def loan_count():
    _loan = Loan.objects.filter(status=False).count()
    return _loan


@register.simple_tag(name='insurance_amount')
def insurance_amount():
    _insurance = Loan.objects.aggregate(total=Sum('insurance'))
    if _insurance['total'] is None:
        _insurance['total'] = 0
    return _insurance['total']
