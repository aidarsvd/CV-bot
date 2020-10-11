from fpdf import FPDF
pdf = FPDF()

name = 'Naruto'
surname = 'Uzumaki'
num = "+32 44 34562114"
email = 'dragonmom@mail'
adres = 'Konoha'
edu = ['Konoha shinobi school', 'Business trip with Jiraya']
exp = ['Saving konoha from Pain', 'Lead on 4th war of shinobi', 'Being Hokage']
skills = ['Rasengan', 'Flex with Kurama', 'Flex with Frogs']
languages = ['Japanese', 'English']





def titles2(self):
    xm = 25
    ym = 10
    pdf.add_page()


    self.set_font('Arial', 'B', 26)
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt=f"{name} {surname}", border=0)

    self.set_font('Arial', 'B', 18)
    ym += 10
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="Hokage", border=0)


    self.set_font('Arial', 'B', 16)
    ym += 15
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt=f"tel: {num}", border=0)

    self.set_font('Arial', 'B', 16)
    ym += 10
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt=f"e-mail: {email}", border=0)

    self.set_font('Arial', 'B', 16)
    ym += 10
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt=f"address: {adres}", border=0)


    ym += 20
    self.set_font('Arial', 'B', 20)
    self.set_xy(0, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="Education:", border=0, align='C')
    ym += 10
    pdf.rect(25, ym, 160, 1, 'F')
    ym += 4

    for i in range (len(edu)):

        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=edu[i], border=0)

    ym += 10
    self.set_font('Arial', 'B', 20)
    self.set_xy(0, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="Experience:", border=0, align='C')
    ym += 10
    pdf.rect(25, ym, 160, 1, 'F')
    ym += 4

    for i in range(len(exp)):
        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=exp[i], border=0)

    ym += 10
    self.set_font('Arial', 'B', 20)
    self.set_xy(0, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="Skills:", border=0, align='C')
    ym += 10
    pdf.rect(25, ym, 160, 1, 'F')
    ym += 4

    for i in range(len(skills)):
        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=skills[i], border=0)

    ym += 10
    self.set_font('Arial', 'B', 20)
    self.set_xy(0, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="languages:", border=0, align='C')
    ym += 10
    pdf.rect(25, ym, 160, 1, 'F')
    ym += 4

    for i in range(len(languages)):
        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=languages[i], border=0)




titles2(pdf)
pdf.output('third_pattern.pdf')
f = open("../third_pattern.pdf", "rb")