from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import A4,landscape
from reportlab.lib.styles import ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm,cm
from reportlab.lib import colors
from reportlab.platypus import (
        Paragraph, 
        Table, 
        SimpleDocTemplate, 
        Spacer, 
        TableStyle, 
        Paragraph)
from reportlab.lib.styles import getSampleStyleSheet
from django.db.models import Sum
from reportlab.platypus import Image

#from .models import Persona
from Lectura.models import Lectura
from Cliente.models import Cuenta

class ReportePagos():

    def __init__(self,id):
        self.buf = BytesIO()
        self.rastreo = Cuenta.objects.get(id_cuenta=id)
        self.cuenta=  id
        self.tot_art = Lectura.objects.filter(id_cuenta=self.rastreo.id_cuenta).aggregate(can=Sum('cargo_total'))
        

    def run(self):
        self.doc = SimpleDocTemplate(self.buf,title=f"Comprobante {self.cuenta}",pagesize=A4)
        self.story = []
        self.encabezado()
        self.crearTabla()
        self.doc.build(self.story, onFirstPage=self.numeroPagina, 
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        imagen_logo = Image('Cliente/logo1.png',width=275, height=95,hAlign='CENTER')
        p = Paragraph("7941-0001", self.estiloPC())
        p1 = Paragraph("Cuidemos Nuestros Recursos", self.estiloPC())
        t1 = Paragraph(" Constancia de Pago ", self.estiloPC())
        a = Paragraph(f"PAGO {self.cuenta}", self.estiloPC2())
        a1 = Paragraph(f"Direccion {self.rastreo.dpi.direccion}", self.estiloPC2())
        a4 = Paragraph(f"Fecha de Impresion {datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}", self.estiloPC3())
        self.story.append(imagen_logo)
        self.story.append(p)
        self.story.append(p1)
        self.story.append(t1)
        self.story.append(a)
        self.story.append(a1)
        self.story.append(a4)
        self.story.append(Spacer(1,0.2*inch))

    def crearTabla(self):
        data = [["Mes","Servicio","Consumo","Total"]] \
            +[[x.mes,x.id_cuenta.servicio.nombre, x.consumo,"Q."+str(x.cargo_total)] 
                for x in Lectura.objects.filter(id_cuenta=self.cuenta,estado=1)]\
            +[["Total de Pagos","","","Q."+str(self.tot_art['can'])]]

        table = Table(data,colWidths=[4.5*cm,6.5*cm,2.5*cm,2.5*cm,2.7*cm])
        table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
        ('VALIGN',(-1,-1),(-1,-1),'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, 1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, colors.gray)
    ]))    

        self.story.append(table)

    def estiloPC(self):
        return ParagraphStyle(name='centrado',
                           fontName="Helvetica-Bold",
                           fontSize=10,
                           alignment=1,
                           spaceAfter=3)

    def estiloPC2(self):
        return ParagraphStyle(name='izquierda',
                           fontName="Helvetica",
                           fontSize=10,
                           alignment=0,
                           spaceAfter=2)

    def estiloPC3(self):
        return ParagraphStyle(name='derecha',
                           fontName="Helvetica",
                           fontSize=10,
                           alignment=2,
                           spaceAfter=2)                       


    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Pagina %s" % num
        canvas.drawRightString(200*mm, 20*mm, text)



class ReportePagos2():

    def __init__(self,id,mes):
        self.buf = BytesIO()
        self.rastreo = Cuenta.objects.get(id_cuenta=id)
        self.cuenta=  id
        self.mes = mes
        self.tot_art = Lectura.objects.filter(id_cuenta=self.rastreo.id_cuenta).aggregate(can=Sum('cargo_total'))
        

    def run(self):
        self.doc = SimpleDocTemplate(self.buf,title=f"Comprobante {self.cuenta}",pagesize=A4)
        self.story = []
        self.encabezado()
        self.crearTabla()
        self.doc.build(self.story, onFirstPage=self.numeroPagina, 
            onLaterPages=self.numeroPagina)
        pdf = self.buf.getvalue()
        self.buf.close()
        return pdf

    def encabezado(self):
        imagen_logo = Image('Cliente/logo1.png',width=275, height=95,hAlign='CENTER')
        p = Paragraph("7941-0001", self.estiloPC())
        p1 = Paragraph("Cuidemos Nuestros Recursos", self.estiloPC())
        t1 = Paragraph(" Constancia de Pago ", self.estiloPC())
        a = Paragraph(f"PAGO {self.cuenta}", self.estiloPC2())
        a1 = Paragraph(f"Direccion {self.rastreo.dpi.direccion}", self.estiloPC2())
        a4 = Paragraph(f"Fecha de Impresion {datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}", self.estiloPC3())
        self.story.append(imagen_logo)
        self.story.append(p)
        self.story.append(p1)
        self.story.append(t1)
        self.story.append(a)
        self.story.append(a1)
        self.story.append(a4)
        self.story.append(Spacer(1,0.2*inch))

    def crearTabla(self):
        data = [["Mes","Servicio","Consumo","Total"]] \
            +[[x.mes,x.id_cuenta.servicio.nombre, x.consumo,"Q."+str(x.cargo_total)] 
                for x in Lectura.objects.filter(id_cuenta=self.cuenta,mes=self.mes,estado=1)]\
            +[["Total de Pagos","","","Q."+str(self.tot_art['can'])]]

        table = Table(data,colWidths=[4.5*cm,6.5*cm,2.5*cm,2.5*cm,2.7*cm])
        table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), "CENTER"),
        ('VALIGN',(-1,-1),(-1,-1),'MIDDLE'),
        ('FONTSIZE', (0, 1), (-1, 1), 9),
        ('GRID', (0,0), (-1,-1), 0.5, colors.gray)
    ]))    

        self.story.append(table)

    def estiloPC(self):
        return ParagraphStyle(name='centrado',
                           fontName="Helvetica-Bold",
                           fontSize=10,
                           alignment=1,
                           spaceAfter=3)

    def estiloPC2(self):
        return ParagraphStyle(name='izquierda',
                           fontName="Helvetica",
                           fontSize=10,
                           alignment=0,
                           spaceAfter=2)

    def estiloPC3(self):
        return ParagraphStyle(name='derecha',
                           fontName="Helvetica",
                           fontSize=10,
                           alignment=2,
                           spaceAfter=2)                       


    def numeroPagina(self,canvas,doc):
        num = canvas.getPageNumber()
        text = "Pagina %s" % num
        canvas.drawRightString(200*mm, 20*mm, text)