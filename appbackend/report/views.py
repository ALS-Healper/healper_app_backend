import functools
from django.http import FileResponse, HttpResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
#from reportlab.pdfgen import canvas
from django.conf import settings
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from questionnaires.models import QuestionnaireEntry
from users.models import Client
import re



def html_to_pdf(template_src, context_dict={}):
     template = get_template(template_src)
     html  = template.render(context_dict)
     #return html
     result = BytesIO()
     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result, )
     if not pdf.err:
         return result.getvalue()
     return None



def make_pdf(request, id=None):
    client_data = Client.objects.filter(pk=id).first()
    questionnaire_data = [x for x in QuestionnaireEntry.objects.filter(creator=id, creator__thera__pk=request.user.pk, creator__data_access=True)]

    # Senere hvis vi har flere numericentries pr questionnaire ville jeg lave det sådan at "values" holder på flere lister [[],[]] 
    # Har bare lavet flere kvp for at få det til at virke for nu. bar chartet skal have et int for højde og label som jeg bare har harcoded
    graph_data = {"values": [], 
        "labels" : [],
        "input" : [], 
        "yes" : 0,
        "no" : 0}

    for question_entry in questionnaire_data:
        if question_entry.is_completed:
            graph_data["values"].append(question_entry.numericentries.first().response_value)
            graph_data["labels"].append(question_entry.numericentries.first().entry_date.strftime("'%d/%m/%Y'"))
            graph_data["input"].append(question_entry.inputentries.first())
            if question_entry.choiceentries.first().choice_value == "Yes":
                graph_data["yes"] += 1
            else:
                graph_data["no"] += 1


    pdf = html_to_pdf('report/clientReport.html', context_dict={"client" : client_data, "questionnaire_data" : questionnaire_data, "graph_data" : graph_data})
    
    email = EmailMessage(
        f'Report of {client_data.user_ref.username}',
        f'You have generated a new report for the user: {client_data.user_ref.first_name}',
        settings.EMAIL_HOST_USER,
        ['markusharen@gmail.com', "alexander.sej@live.dk", "mr.alek112@gmail.com", "mettemhws@gmail.com"],
        # request.user.email"
    )

    email.attach('test.pdf', pdf, 'application/pdf')
    email.send()
    return HttpResponse("Nice")
    print(id)
    return HttpResponse(pdf)