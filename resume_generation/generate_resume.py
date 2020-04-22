#you need to install the fpdf library
# run: pip install fpdf

from fpdf import FPDF

def createPDF():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Times','BI',11)

    contact = open("./resume_generation/test.txt","r")

    for x in contact:
       pdf.multi_cell(200,5, txt = x, align = 'C')
    contact.close()

    education = open('./resume_generation/test2.txt','r')
    pdf.cell(200,5, txt = "Education", align = 'L')
    pdf.set_font('Times','',10)
    for y in education:
        pdf.multi_cell(200,5, txt = y, align = 'L')
    education.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Selected Independent Projects", align = 'L')
    projects = open('./resume_generation/test3.txt', 'r')
    pdf.set_font('Times','',10)
    for z in projects:
       pdf.multi_cell(200,5,txt = z, align = 'L')
    projects.close()

    pdf.set_font('Times','BI',11)
    pdf.cell(200,5, txt = "Experience", align = 'L')
    experience = open('./resume_generation/test4.txt', 'r')
    pdf.set_font('Times','',10)
    for a in experience:
        pdf.multi_cell(200,5,txt = a, align = 'L')
    experience.close()

    pdf.output("test.pdf")


createPDF()
