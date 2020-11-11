from django.conf import settings
from django.contrib.auth.models import User,Group
from django.db.models import Avg
from django import template
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
    request=context['request']
    users=User.objects.filter(is_superuser=False).count()
    return users

@register.simple_tag(name='group_count') 
def group_count():
    groups=Group.objects.count()
    return groups



@register.simple_tag(takes_context=True, name='groups_name') 
def groups_name(context):
    request=context['request']
    for group in request.user.groups:
        return{
            'groups_name':groups_name
        }
         


