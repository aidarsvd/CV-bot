from fpdf import FPDF
pdf = FPDF()

name = 'Daenerys'
surname = 'Targaryen'
num = "+32 44 34562114"
email = 'dragonmom@mail'
adres = 'Meereen'
edu = ['Pentos high school', 'Khalasar university']
exp = ['Being Khaleesi', 'Raising dragons', 'Protecting Kingdoms']
skills = ['Resistance to fire and high temperature', 'Dragon flying']
languages = ['Valyrian', 'English']





def titles1(self):
    xm = 10
    ym = 10

    xm1 = 120
    ym1 = 56


    pdf.add_page()
    pdf.set_fill_color(138, 255, 185)
    pdf.rect(0, 0, 500, 50, 'F')
    self.set_xy(60, 0)


    self.set_font('Arial', 'B', 40)
    self.set_xy(xm, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=100.0, h=10.0, txt=f"{name} {surname}", border=0)

    self.set_font('Arial', 'I', 16)
    self.set_text_color(0, 0, 0)
    ym += 10

    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt="Queen of the Andals, the Rhoynar, and the First Men, Protector of the Seven Kingdoms,", border=0)
    ym += 6
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=30.0, txt="Khaleesi of the Great Grass Sea, omg etc...", border=0)

    self.set_font('Arial', 'B', 25)
    self.set_text_color(0, 0, 0)
    ym += 30
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt="Contacts:", border=0)


    self.set_font('Arial', 'I', 18)
    self.set_text_color(0, 0, 0)
    ym += 12
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt=f"tel: {num}", border=0)

    self.set_font('Arial', 'I', 18)
    self.set_text_color(0, 0, 0)
    ym += 12
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt=f"e-mail: {email}", border=0)

    self.set_font('Arial', 'I', 18)
    self.set_text_color(0, 0, 0)
    ym += 12
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt=f"home address: {adres}", border=0)


    self.set_font('Arial', 'B', 25)
    self.set_text_color(0, 0, 0)
    ym += 20
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt="Experience:", border=0)
    for i in range (len(exp)):
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        ym += 12
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=25.0, txt=exp[i], border=0)

    self.set_font('Arial', 'B', 25)
    self.set_text_color(0, 0, 0)
    ym += 20
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=25.0, txt="Skills:", border=0)
    for i in range (len(skills)):
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        ym += 12
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=25.0, txt=skills[i], border=0)



    # Second column

    self.set_font('Arial', 'B', 25)
    self.set_text_color(0, 0, 0)
    ym += 30
    self.set_xy(xm1, ym1)
    self.cell(w=210.0, h=25.0, txt="Education:", border=0)
    for i in range(len(edu)):
        ym1 += 12
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        self.set_xy(xm1, ym1)
        self.cell(w=210.0, h=25.0, txt=edu[i], border=0)

    self.set_font('Arial', 'B', 25)
    self.set_text_color(0, 0, 0)
    ym1 += 30
    self.set_xy(xm1, ym1)
    self.cell(w=210.0, h=25.0, txt="Languages:", border=0)
    for i in range(len(languages)):
        ym1 += 12
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        self.set_xy(xm1, ym1)
        self.cell(w=210.0, h=25.0, txt=languages[i], border=0)


titles1(pdf)
pdf.output('second_pattern.pdf')
f = open("../second_pattern.pdf", "rb")