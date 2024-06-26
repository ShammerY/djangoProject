from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.conf import settings
from django.views import View

from ..models import Request, RequestStatus

from users_mgmt.models import CustomUser

from ..models import Request


class UpdateApproverView(View):

    def post(self, request, request_id, *args, **kwargs):
        user_id = request.POST.get("approvers")
        if user_id is None or user_id == "":
            return redirect("detail_request", request_id=request_id)

        try:
            instance_request = Request.objects.get(pk=request_id)
            user = CustomUser.objects.get(pk=user_id)
            instance_request.approver = user
            new_status = RequestStatus.objects.get(status='Aceptado')
            instance_request.status = new_status
            instance_request.save()
            '''
             subject = 'Cambio de estado de solicitud'
            recipient_list = CustomUser.email
            template='detail_request'
            email = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                [recipient_list]
                
            )
            email.fail_silently=False
            email.send()
            '''
            
            return redirect("detail_request", request_id=request_id)
        
        except (Request.DoesNotExist, CustomUser.DoesNotExist) as e:
            instance_request = Request.objects.get(pk=request_id)
            instance_request.approver = None
            instance_request.save()
            return redirect("detail_request", request_id=request_id)