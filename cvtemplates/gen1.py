from fpdf import FPDF
pdf = FPDF()

edu = ['Calderstones School', 'Liverpool School Of Art & Design']
exp = ['Plastic Ono Band', 'The Beatles']
skills = ['Guitar', 'Electric piano', 'Hammond organ', 'Harmonium']
lans = []

lans.append('russian')




def titles(self):
    xm = 60
    ym = 15
    pdf.add_page()
    pdf.set_fill_color(210, 215, 223)
    pdf.rect(0, 0, 60, 500, 'F')
    self.set_xy(60, 0)


    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt="John", border=0)
    self.set_xy(xm, ym)

    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt="Lennon", border=0)
    ym += 25
    self.set_xy(xm, ym)

    self.set_font('Arial', 'BI', 20)
    self.set_text_color(0, 0, 0)
    ym += 10
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Rock singer", border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 20
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Education:", border=0)
    for i in range(len(edu)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=edu[i], border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 15
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Experience:", border=0)
    for i in range(len(exp)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=exp[i], border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 15
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Skills:", border=0)
    for i in range(len(skills)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=skills[i], border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 15
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Languages:", border=0)
    for i in range(len(lans)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=lans[i], border=0)



    self.set_xy(5, 35 - 28)
    self.set_font('Arial', 'B', 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="Contacts:", border=0)
    self.set_xy(5, 45 - 28)
    self.set_font('Arial', 'BIU', 12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="tel: ", border=0)
    self.set_xy(5, 50 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="+44 7911 123456", border=0)
    self.set_xy(5, 60 - 28)
    self.set_font('Arial', 'BIU', 12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="email: ", border=0)
    self.set_xy(5, 65 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="ljohn@mail.uk", border=0)
    self.set_xy(5, 75 - 28)
    self.set_font('Arial', 'BIU', 12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="home addres: ", border=0)
    self.set_xy(5, 80 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=60.0, h=40.0, txt="251 Menlove Ave L25 7SA", border=0)

titles(pdf)
pdf.output('cv.pdf')
f = open("../cv.pdf", "rb")