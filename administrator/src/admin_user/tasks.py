from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from celery import shared_task

@shared_task
def send_message(subject, context, recipient_list, html_path, text_apth):
    txt_ = get_template(text_apth).render(context)
    html_ = get_template(html_path).render(context)
    from_email = settings.DEFAULT_FROM_EMAIL
    sent = send_mail(
        subject, txt_, from_email, recipient_list,
        html_message=html_, fail_silently=False,
    )
    return sent