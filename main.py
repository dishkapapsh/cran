import telebot

from packind.settings import settings

bot=telebot.TeleBot(token=settings.bots.bot_token)

@bot.message_handler(commands=['start'])
def start(message):
    mms = f'Приветствую,<b>{message.from_user.first_name}</b>. Cтудент-медик или просто любознательный друг! Здесь ты можешь ознакомится с работой периферической нервной системы, а именно с составной ее частью: черепно-мозговыми нервами.'
    instr = (
        f'Бот представляет небольшое руководство, где ты можешь узнать, что из себя представляют черепно-мозговые нервы, а также изучить их анатомию, классификацию и функции.\n'
        f'Чтобы получить описание нерва, следует ввести его числовое обозначение (от 1 до 12) либо же буквенное название.(Название нерва с заглавной буквы)\n'
        f'Например: 5 или Тройничный'
    )
    bot.send_message(message.chat.id, mms + instr, parse_mode="HTML")

@bot.message_handler(commands=['help'])
def help(message):
    instr = (
        f'Чтобы получить описание нерва, следует ввести его числовое обозначение (от 1 до 12) либо же буквенное название.(Название нерва с заглавной буквы)\n'
        f'Например: 5 или Тройничный'
    )
    bot.send_message(message.chat.id, instr, parse_mode="HTML")

@bot.message_handler()
def get_user_text(message):
    if message.text == '1' or message.text == 'Обонятельный':
        photo1 = open('olfac2.jpg', 'rb')
        photo2 = open('olfac.jpg', 'rb')
        text='Обонятельные нервы – nn. olfactorii (I пара) .\n Структурно I пара черепных нервов не гомологична остальным нервам, так как образуется в резульгате выпячивания стенки мозгового пузыря.\n Он является частью системы обоняния, состоящей из трех нейронов.'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '2' or message.text == 'Зрительный':
        photo1 = open('optic1.jpg', 'rb')
        photo2 = open('optic.jpg', 'rb')
        text ='Зрительный нерв – n. opticus (II пара). Образован из аксонов мультиполярных клеток сетчатки, которые доходят до наружного коленчатого тела, а также из центральных волокон, являющихся элементами обратной связи.\nМиелинизированные отростки ганглиозных клеток формируют зрительный нерв. Он через зрительный канал входит в полость черепа, идет по основанию мозга и кпереди от турецкого \n седла образует перекрест зрительных нервов (chiasma opticum), где нервные волокна от носовой половины сетчатки каждого глаза перекрещиваются, нервные волокна от височной половины сетчатки каждого глаза остаются неперекрещенными. После перекреста зрительные пути называются зрительными трактами. Они формируются из нервных волокон от одноименных половин сетчатки обоих глаз'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '3' or message.text == 'Глазодвигательный':
        photo1 = open('oculo1.jpg', 'rb')
        photo2 = open('oculo2.jpg', 'rb')
        text='Глазодвигательный нерв – n. oculomotoris (III пара). Глазодвигательный нерв является смешанным нервом.\n Ядра глазодвигательных нервов состоят из пяти клеточных групп: два наружных двигательных крупноклеточных ядра, два мелкоклеточных ядра и одно внутреннее, непарное, мелкоклеточное ядро'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '4' or message.text == 'Блоковый':
        photo1 = open('troch1.jpg', 'rb')
        text = 'Блоковой нерв – n. trochlearis (IV пара). Ядра блоковых нервов расположены на уровне нижних холмиков крыши среднего мозга кпереди от центрального серого вещества, ниже ядер глазодвигательного нерва.'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)

    elif message.text == '5' or message.text == 'Тройничный':
        photo1 = open('trigon1.jpg', 'rb')
        photo2 = open('trigon2.jpg', 'rb')
        photo3 = open('trigon3.jpg', 'rb')
        text = 'Тройничный нерв – n. trigeminus (V пара). Тройничный нерв – главный чувствительный нерв лица и ротовой полости, но в его составе имеются двигательные волокна, иннервирующие жевательные мышцы'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)

    elif message.text == '6' or message.text == 'Отводящий':
        photo1 = open('abdun1.jpg', 'rb')
        photo2 = open('abdun2.jpg', 'rb')
        text = 'Отводящий нерв – n. abductens (VI пара). Ядра отводящих нервов расположены по обеим сторонам от средней линии в покрышке нижней части моста вблизи продолговатого мозга и под дном IV желудочка'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '7' or message.text == 'Лицевой':
        photo1 = open('facial1.jpg', 'rb')
        photo2 = open('facial2.jpg', 'rb')
        photo3 = open('facial3.jpg', 'rb')
        text = "Лицевой нерв – n. facialis (VII пара). Лицевой нерв является смешанным нервом.\n В его составе имеются двигательные, парасимпатические и чувствительные волокна, последние два вида волокон выделяют как промежуточный нерв"
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)

    elif message.text == '8' or message.text == 'Преддверно-улитковый':
        photo1 = open('vestibul1.jpg', 'rb')
        photo2 = open('vestibul2.jpg', 'rb')
        photo3 = open('vestibul3jpg.jpg', 'rb')
        photo4 = open('vestibul4.jpg', 'rb')
        text = "Преддверно-улитковый нерв -n. vestibulocochlearis (VIII пара).\nПреддверно-улитковый нерв состоит из двух корешков: нижнего – улиткового и верхнего – преддверного. Объединяет две функционально различные части."
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)
        bot.send_photo(message.chat.id, photo3)
        bot.send_photo(message.chat.id, photo4)

    elif message.text == '9' or message.text == 'Языкоглоточный':
        photo1 = open('glos1.jpg', 'rb')
        photo2 = open('glos2.jpg', 'rb')
        text = 'Языкоглоточный нерв – n. glossopharyngeus (IX пара).\nЯзыкоглоточный нерв содержит 4 вида волокон: чувствительные, двигательные, вкусовые и секреторные'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '10' or message.text == 'Блуждающий':
        photo1 = open('vagus1.jpg', 'rb')
        photo2 = open('vagus2.jpg', 'rb')
        text = 'Блуждающий нерв – n. vagus (X пара). Блуждающий нерв содержит чувствительные, двигательные и вегетативные волокна.'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '11' or message.text == 'Добавочный':
        photo1 = open('accesor.jpg', 'rb')
        photo2 = open('accesor2.jpg', 'rb')
        text = 'Добавочный нерв – n. accessorius (XI пара). Добавочный нерв является двигательным, слагается из блуждающей и спинномозговой частей'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    elif message.text == '12' or message.text == 'Подъязычный':
        photo1 = open('hypoglos1.jpg', 'rb')
        photo2 = open('hypoglos2.jpg', 'rb')
        text = 'Подъязычный нерв – n. hypoglossus (XII пара). Нерв преимущественно двигательный. В его составе идут веточки от язычного нерва, которые имеют чувствительные волокна'
        bot.send_message(message.chat.id, text)
        bot.send_photo(message.chat.id, photo1)
        bot.send_photo(message.chat.id, photo2)

    else:
        bot.send_photo(message.chat.id, 'error')



bot.polling(none_stop=True)




