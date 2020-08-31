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
        bot.send_message(message.from_user.id, 'Напиши /reg')

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Ваша фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Ваша специальность:')
    bot.register_next_step_handler(message, prof)


def prof(message):
    global prof
    prof = message.text
    bot.register_next_step_handler(message, get_age)
    bot.send_message(message.from_user.id, 'Ваш возраст:')


def get_age(message):
    global age
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
    if message.text == "Да":
        bot.send_message(message.from_user.id, "Отлично! Продолжаем...", reply_markup=hide)
        bot.send_message(message.from_user.id, "Введите команду /cont , чтобы заполнить контактные данные", reply_markup=hide)


    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /reg", reply_markup=hide)

@bot.message_handler(commands=['cont'])
def get_num(message):
    bot.send_message(message.from_user.id, "Ваш номер телефона:")
    bot.register_next_step_handler(message, number)

def number(message):
    global num
    num = message.text
    bot.register_next_step_handler(message, elmail)
    bot.send_message(message.from_user.id, "Ваш адрес электронной почты:")


def elmail(message):
    global email
    email = message.text
    bot.register_next_step_handler(message, get_adres)
    bot.send_message(message.from_user.id, "Ваш домашний адрес:")

def get_adres(message):
    global adres
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

    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /cont", reply_markup=hide)


@bot.message_handler(commands=['about'])
def adding(message):
    bot.send_message(message.from_user.id, "Образование:")
    bot.register_next_step_handler(message, get_edu)

def get_edu(message):
    global ed_places
    ed_places = message.text
    bot.send_message(message.from_user.id, "Места работы: ")
    bot.register_next_step_handler(message, get_jobs)



def get_jobs(message):
    global jobs
    jobs = message.text
    bot.register_next_step_handler(message, exp)
    bot.send_message(message.from_user.id, "Эксперты в:")


def exp(message):
    global expert
    expert = message.text

    user_abcont = telebot.types.ReplyKeyboardMarkup(True, False)
    user_abcont.row("Да", "Нет")
    bot.send_message(message.from_user.id, 'Данные верны? \n'
                                           f'Ваше образование: {ed_places} \n'
                                           f'Места работы: {jobs}\n'
                                           f'Эксперты в: {expert}', reply_markup=user_abcont)
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

        pdf = FPDF()
        pdf.add_page()
        pdf.set_fill_color(210, 215, 223)
        pdf.rect(0, 0, 60, 500, 'F')

        def titles(self):
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

        titles(pdf)

        pdf.output('cv.pdf')

        f = open("cv.pdf", "rb")
        bot.send_document(message.chat.id, f)



    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Чтобы исправить, отправьте команду /about", reply_markup=hide)


bot.polling(none_stop=True)