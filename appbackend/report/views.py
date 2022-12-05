from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from reportlab.pdfgen import canvas
from django.conf import settings
import io


def make_pdf(request):
    buffer = io.BytesIO()

    p = canvas.Canvas(buffer)

    p.drawString(100,100, "Hello from Markus and Alek bisch")

    p.showPage()
    p.save()

    buffer.seek(0)
    pdf = buffer.getvalue()

    email = EmailMessage(
        'Report of User',
        'You have generated a new report for the user: USer',
        settings.EMAIL_HOST_USER,
        ['alexander.sej@live.dk'],
    )

    email.attach('test.pdf', pdf, 'application/pdf')
    email.send()

    return HttpResponse("Email send")