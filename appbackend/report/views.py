from django.http import FileResponse, HttpResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from reportlab.pdfgen import canvas
from django.conf import settings
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from questionnaires.models import QuestionnaireEntry
from users.models import Client


def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     return html
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
     if not pdf.err:
         return result.getvalue()
     return None


def make_pdf(request, id=None):
    client_data = Client.objects.filter(pk=id).first()
    questionnaire_data = list(QuestionnaireEntry.objects.filter(creator=id, creator__thera__pk=request.user.pk, creator__data_access=True))
   
    #buffer = io.BytesIO()

    #p = canvas.Canvas(buffer)

   # p.drawString(100,100, "Hello from Markus and Alek bisch")

    #p.showPage()
    #p.save()

    #buffer.seek(0)
    pdf = html_to_pdf('report/clientReport.html', context_dict={"client" : client_data, "questionnaire_data" : questionnaire_data})
    return HttpResponse(pdf)
    email = EmailMessage(
        'Report of User',
        'You have generated a new report for the user: USer',
        settings.EMAIL_HOST_USER,
        ['markusharen@gmail.com'],
        # , "alexander.sej@live.dk", "mr.alek112@gmail.com", "mettemhws@gmail.com, request.user.email"
    )

    email.attach('test.pdf', pdf, 'application/pdf')
    email.send()

    print(id)
    return HttpResponse(pdf)