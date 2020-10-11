import telebot
from fpdf import FPDF


token = "905143600:AAFAQIk2RXspo3nsBoCJOyFIvYpXHksyG_E"
bot = telebot.TeleBot(token)



name = ''
surname = ''
prof = ''
age = 0
num = 0
email = ''
adres = ''
ed_places = ''
jobs = ''
expert = ''
skills = []
lans = ''
languages = []

pdf = FPDF()

def is_cyrrylic(symb):
    return True if u'\u0400' <= symb <=u'\u04FF' or u'\u0500' <= symb <= u'\u052F' else False

def titles(self):
    xm = 60
    ym = 15
    pdf.add_page()
    pdf.set_fill_color(210, 215, 223)
    pdf.rect(0, 0, 60, 500, 'F')
    self.set_xy(60, 0)

    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt=name, border=0)
    self.set_xy(xm, ym)

    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt=surname, border=0)
    ym += 25
    self.set_xy(xm, ym)

    self.set_font('Arial', 'BI', 20)
    self.set_text_color(0, 0, 0)
    ym += 10
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt=prof, border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 20
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Education:", border=0)
    for i in range(len(edues)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=edues[i], border=0)

    self.set_font('Arial', 'B', 20)
    self.set_text_color(0, 0, 0)
    ym += 15
    self.set_xy(xm, ym)
    self.cell(w=210.0, h=40.0, txt="Experience:", border=0)
    for i in range(len(jobsb)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=jobsb[i], border=0)

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
    for i in range(len(languages)):
        self.set_font('Arial', size=14)
        self.set_text_color(0, 0, 0)
        ym += 10
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=40.0, txt=languages[i], border=0)

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
    self.cell(w=210.0, h=40.0, txt=num, border=0)
    self.set_xy(5, 60 - 28)
    self.set_font('Arial', 'BIU', 12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="email: ", border=0)
    self.set_xy(5, 65 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt=email, border=0)
    self.set_xy(5, 75 - 28)
    self.set_font('Arial', 'BIU', 12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt="home address: ", border=0)
    self.set_xy(5, 80 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=60.0, h=40.0, txt=adres, border=0)

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
    self.cell(w=210.0, h=25.0, txt=prof, border=0)

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
    for i in range (len(jobsb)):
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        ym += 12
        self.set_xy(xm, ym)
        self.cell(w=210.0, h=25.0, txt=jobsb[i], border=0)

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
    for i in range(len(edues)):
        ym1 += 12
        self.set_font('Arial', 'I', 18)
        self.set_text_color(0, 0, 0)
        self.set_xy(xm1, ym1)
        self.cell(w=210.0, h=25.0, txt=edues[i], border=0)

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
    self.cell(w=200.0, h=10.0, txt=prof, border=0)


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

    for i in range (len(edues)):

        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=edues[i], border=0)

    ym += 10
    self.set_font('Arial', 'B', 20)
    self.set_xy(0, ym)
    self.set_text_color(0, 0, 0)
    self.cell(w=200.0, h=10.0, txt="Experience:", border=0, align='C')
    ym += 10
    pdf.rect(25, ym, 160, 1, 'F')
    ym += 4

    for i in range(len(jobsb)):
        self.set_font('Arial', size=16)
        self.set_xy(25, ym)
        ym += 8
        self.set_text_color(0, 0, 0)
        self.cell(w=200.0, h=10.0, txt=jobsb[i], border=0)

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

#Обработчик для документов и аудиофайлов
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, "Привет! Я бот который сгенерирует тебе резюме. Отправь мне команду /reg чтобы приступить.")

@bot.message_handler(commands=['reg'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как вас зовут?")
        bot.register_next_step_handler(message, get_name) #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Привет! Я бот который сгенерирует тебе резюме. Отправь мне команду /reg чтобы приступить')

def get_name(message): #получаем фамилию
    global name
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        name = message.text
        bot.send_message(message.from_user.id, 'Ваша фамилия?')
        bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        surname = message.text
        bot.send_message(message.from_user.id, 'Ваша специальность:')
        bot.register_next_step_handler(message, prof)


def prof(message):
    global prof
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        prof = message.text
        bot.register_next_step_handler(message, get_age)
        bot.send_message(message.from_user.id, 'Ваш возраст:')


def get_age(message):
    global age
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        age = message.text
        user_m = telebot.types.ReplyKeyboardMarkup(True, False)
        user_m.row("Да", "Нет")
        bot.send_message(message.from_user.id, 'Данные верны? \n'
                                               f'Ваше имя: {name} \n'
                                               f'Ваша фамилия: {surname}\n'
                                               f'Ваша специальность: {prof}\n'
                                               f'Ваш возраст: {age}', reply_markup=user_m)

        bot.register_next_step_handler(message, resy)


def resy(message):
    hide = telebot.types.ReplyKeyboardRemove()
    user_m = telebot.types.ReplyKeyboardMarkup(True, False)
    user_m.row("Да", "Нет")
    if message.text == "Да":
        bot.send_message(message.from_user.id, "Отлично! Продолжаем...", reply_markup=user_m)
        bot.send_message(message.from_user.id, "Введите команду /cont , чтобы заполнить контактные данные", reply_markup=user_m)


    elif message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /reg", reply_markup=hide)

    else:
        bot.send_message(message.from_user.id, 'Привет! Я бот который сгенерирует тебе резюме. Отправь мне команду /reg чтобы приступить')


@bot.message_handler(commands=['cont'])
def get_num(message):
    bot.send_message(message.from_user.id, "Ваш номер телефона:")
    bot.register_next_step_handler(message, number)

def number(message):
    global num
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /cont чтобы исправить')
    else:
        num = message.text
        bot.register_next_step_handler(message, elmail)
        bot.send_message(message.from_user.id, "Ваш адрес электронной почты:")


def elmail(message):
    global email
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /cont чтобы исправить')
    else:
        email = message.text
        bot.register_next_step_handler(message, get_adres)
        bot.send_message(message.from_user.id, "Ваш домашний адрес:")

def get_adres(message):
    global adres
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /cont чтобы исправить')
    else:
        adres = message.text
        user_mcont = telebot.types.ReplyKeyboardMarkup(True, False)
        user_mcont.row("Да", "Нет")
        bot.send_message(message.from_user.id, 'Данные верны? \n'
                                               f'Ваш номер телефона: {num} \n'
                                               f'Ваш адрес эл.почты: {email}\n'
                                               f'Ваш домашний адрес: {adres}', reply_markup=user_mcont)

        bot.register_next_step_handler(message, resy_cont)


def resy_cont(message):
    hide = telebot.types.ReplyKeyboardRemove()
    if message.text == "Да":
        bot.send_message(message.from_user.id, "Отлично! Продолжаем...", reply_markup=hide)
        bot.send_message(message.from_user.id, "Введите команду /about , чтобы заполнить данные о себе")

    elif message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /cont", reply_markup=hide)

    else:
        bot.send_message(message.from_user.id, 'Привет! Я бот который сгенерирует тебе резюме. Отправь мне команду /reg чтобы приступить')

edues = []
@bot.message_handler(commands=['about'])
def adding(message):
    bot.send_message(message.from_user.id, "Образование:")
    bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или перечислите ваше образование "
                                           "через знак запятой")
    bot.register_next_step_handler(message, get_edu)

def get_edu(message):
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /about чтобы исправить')
    else:
        global ed_places
        global edues
        if message.text != '/skip':
            ed_places = message.text
            x = ed_places.replace(" ", "")
            edues = x.split(',')
        else:
            edues.append('None')

        bot.send_message(message.from_user.id, "Места работы: ")
        bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или перечислите места работы "
                                               "через знак запятой")
        bot.register_next_step_handler(message, get_jobs)


jobsb = []
def get_jobs(message):
    global jobs
    global jobsb
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /about чтобы исправить')
    else:
        if message.text != '/skip':
            jobs = message.text
            x = jobs.replace(" ", "")
            jobsb = x.split(',')
        else:
            jobsb.append('None')

        bot.send_message(message.from_user.id, "Языки: ")
        bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или языки которыми владеете "
                                               "через знак запятой")

        bot.register_next_step_handler(message, get_lans)

def get_lans(message):
    global languages
    global lans
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /about чтобы исправить')
    else:
        if message.text != '/skip':
            lans = message.text
            x = lans.replace(" ", "")
            languages = x.split(',')
        else:
            languages.append('None')

        bot.register_next_step_handler(message, exp)
        bot.send_message(message.from_user.id, "Эксперты в:")
        bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или перечислите ваши умения "
                                               "через знак запятой")


def exp(message):
    global expert
    global skills
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /about чтобы исправить')
    else:
        if message.text != '/skip':
            expert = message.text
            x = expert.replace(" ", "")
            skills = x.split(',')
        else:
            skills[0] = 'None'

        user_abcont = telebot.types.ReplyKeyboardMarkup(True, False)
        user_abcont.row("Да", "Нет")
        bot.send_message(message.from_user.id, 'Данные верны? \n'
                                               f'Ваше образование: {edues} \n'
                                               f'Места работы: {jobsb}\n'
                                               f'Места работы: {lans}\n'
                                               f'Эксперты в: {skills}', reply_markup=user_abcont)
        bot.register_next_step_handler(message, resy_about)


def resy_about(message):
    hide = telebot.types.ReplyKeyboardRemove()
    if message.text == "Да":
        bot.send_message(message.from_user.id, "Выберите дизайн", reply_markup=hide)
        bot.send_photo(message.from_user.id, photo=open('templates/first_pattern.jpg', 'rb'), caption='1 стиль')
        bot.send_photo(message.from_user.id, photo=open('templates/second_pattern.jpg', 'rb'), caption='2 стиль')
        bot.send_photo(message.from_user.id, photo=open('templates/third_pattern_1.jpg', 'rb'), caption='3 стиль')


    elif message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /about", reply_markup=hide)

    else:
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы создать новое резюме')
    bot.register_next_step_handler(message, done)


def done(message):
    global name
    global surname
    global age
    global prof
    global num
    global email
    global adres
    global ed_places
    global jobs
    global expert

    if message.text == '1':
        titles(pdf)
        pdf.output('cv.pdf')
        f = open("cv.pdf", "rb")
        bot.send_document(message.chat.id, f)
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы создать новое резюме')

    elif message.text == '2':
        titles1(pdf)
        pdf.output('cv.pdf')
        f = open("cv.pdf", "rb")
        bot.send_document(message.chat.id, f)
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы создать новое резюме')

    elif message.text == '3':
        titles2(pdf)
        pdf.output('cv.pdf')
        f = open("cv.pdf", "rb")
        bot.send_document(message.chat.id, f)
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы создать новое резюме')

    else:
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы создать новое резюме')

bot.polling(none_stop=True)