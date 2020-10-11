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
    pdf.add_page()
    pdf.set_fill_color(210, 215, 223)
    pdf.rect(0, 0, 60, 500, 'F')
    self.set_xy(60, 0)
    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt=name, border=0)
    self.set_xy(60, 15)
    self.set_font('Arial', 'B', 46)
    self.set_text_color(210, 215, 223)
    self.cell(w=210.0, h=60.0, txt=surname, border=0)
    self.set_xy(60, 40)
    self.set_font('Arial', 'BI', 28)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt=prof, border=0)
    ##########################
    ###########################
    self.set_xy(60, 80)
    self.set_font('Arial', "B", 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt="Education:", border=0)
    self.set_xy(60, 90)
    self.set_font('Arial', size=16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt=ed_places, border=0)
    ##################################
    self.set_xy(60, 110)
    self.set_font('Arial', "B", 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt="Experience:", border=0)
    self.set_xy(60, 120)
    self.set_font('Arial', size=16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt=jobs, border=0)
    ##################################
    self.set_xy(60, 140)
    self.set_font('Arial', "B", 16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt="Expert in:", border=0)
    self.set_xy(60, 150)
    self.set_font('Arial', size=16)
    self.set_text_color(0, 0, 0)
    self.cell(w=140, h=20.0, txt=expert, border=0)
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
    self.cell(w=210.0, h=40.0, txt="home addres: ", border=0)
    self.set_xy(5, 80 - 28)
    self.set_font('Arial', size=12)
    self.set_text_color(0, 0, 0)
    self.cell(w=210.0, h=40.0, txt=adres, border=0)



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
            edues = ed_places.split(',')
        else:
            ed_places = 'None'

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
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        if message.text != '/skip':
            jobs = message.text
            jobsb = jobs.split(',')
        else:
            jobs = 'None'

        bot.send_message(message.from_user.id, "Языки: ")
        bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или языки которыми владеете "
                                               "через знак запятой")

        bot.register_next_step_handler(message, get_lans)

def get_lans(message):
    global languages
    global lans
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        if message.text != '/skip':
            lans = message.text
            languages = lans.split(',')
        else:
            lans = 'None'

        bot.register_next_step_handler(message, exp)
        bot.send_message(message.from_user.id, "Эксперты в:")
        bot.send_message(message.from_user.id, "Введите команду /skip чтобы пропустить, или перечислите ваши умения "
                                               "через знак запятой")


def exp(message):
    global expert
    global skills
    if is_cyrrylic(message.text) == True:
        bot.send_message(message.from_user.id, 'Вводите данные на латинице!')
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы исправить')
    else:
        if message.text != '/skip':
            expert = message.text
            skills = expert.split(',')
        else:
            expert = 'None'

        user_abcont = telebot.types.ReplyKeyboardMarkup(True, False)
        user_abcont.row("Да", "Нет")
        bot.send_message(message.from_user.id, 'Данные верны? \n'
                                               f'Ваше образование: {edues} \n'
                                               f'Места работы: {jobsb}\n'
                                               f'Эксперты в: {skills}', reply_markup=user_abcont)
        bot.register_next_step_handler(message, resy_about)


def resy_about(message):
    hide = telebot.types.ReplyKeyboardRemove()
    if message.text == "Да":
        bot.send_message(message.from_user.id, "Одну минуту...", reply_markup=hide)
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

        titles(pdf)
        pdf.output('cv.pdf')
        f = open("cv.pdf", "rb")
        bot.send_document(message.chat.id, f)



    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /about", reply_markup=hide)

    else:
        bot.send_message(message.from_user.id, 'Отправь мне команду /reg чтобы приступить')

bot.polling(none_stop=True)