import json

super_dict = {
    "in": [
        ["There is a book in the bag.", "В сумке есть книга."],
        ["The cat is in the house.", "Кот в доме."],
        ["He lives in New York.", "Он живет в Нью-Йорке."]
    ],
    "it": [
        ["It is raining outside.", "На улице идет дождь."],
        ["It is a beautiful day.", "Это прекрасный день."],
        ["It is important to be honest.", "Важно быть честным."]
    ],
    "you": [
        ["Can you help me, please?", "Можешь помочь мне, пожалуйста?"],
        ["What are you doing?", "Что ты делаешь?"],
        ["You are my best friend.", "Ты мой лучший друг."]
    ],
    "that": [
        ["I know that you are busy.", "Я знаю, что ты занят."],
        ["Is that your car?", "Это твоя машина?"],
        ["He said that he would come later.", "Он сказал, что придет позже."]
    ],
    "he": [
        ["He is a doctor.", "Он врач."],
        ["He likes to read books.", "Он любит читать книги."],
        ["He will be here soon.", "Он скоро будет здесь."]
    ],
    "was": [
        ["He was tired after work.", "Он был уставшим после работы."],
        ["It was a beautiful sunset.", "Это был красивый закат."],
        ["She was my best friend.", "Она была моим лучшим другом."]
    ],
    "for": [
        ["I bought flowers for her birthday.", "Я купил цветы на ее день рождения."],
        ["This book is for you.", "Эта книга для тебя."],
        ["He is studying for his exams.", "Он готовится к экзаменам."]
    ],
    "on": [
        ["The keys are on the table.", "Ключи на столе."],
        ["We went for a walk on the beach.", "Мы пошли гулять на пляж."],
        ["She is on vacation.", "Она в отпуске."]
    ],
    "are": [
        ["They are my classmates.", "Они мои одноклассники."],
        ["Where are you from?", "Откуда вы?"],
        ["What are you doing tonight?", "Что вы делаете сегодня вечером?"]
    ],
    "with": [
        ["I went to the park with my friends.", "Я пошел в парк с друзьями."],
        ["He is good with computers.", "Он хорошо разбирается в компьютерах."],
        ["She is with her family.", "Она с семьей."]
    ],
    "as": [
        ["He works as a teacher.", "Он работает учителем."],
        ["She sang as if she were a professional.", "Она пела, как будто была профессионалом."],
        ["As you know, tomorrow is a holiday.", "Как вы знаете, завтра праздник."]
    ],
    "I": [
        ["I am happy.", "Я счастлив."],
        ["Can I help you?", "Могу я вам помочь?"],
        ["I love to travel.", "Я люблю путешествовать."]
    ],
    "his": [
        ["He took off his coat.", "Он снял свое пальто."],
        ["His car is parked outside.", "Его машина припаркована снаружи."],
        ["I met his brother yesterday.", "Я встретился с его братом вчера."]
    ],
    "they": [
        ["They are coming to the party.", "Они идут на вечеринку."],
        ["Do they like pizza?", "Они любят пиццу?"],
        ["They have a big house.", "У них большой дом."]
    ],
    "be": [
        ["To be or not to be, that is the question.", "Быть или не быть, вот в чем вопрос."],
        ["She wants to be a doctor.", "Она хочет быть врачом."],
        ["It will be sunny tomorrow.", "Завтра будет солнечно."]
    ],
    "at": [
        ["I'll meet you at the cafe.", "Я встречу тебя в кафе."],
        ["He is good at playing guitar.", "Он хорошо играет на гитаре."],
        ["She works at the hospital.", "Она работает в больнице."]
    ],
    "one": [
        ["I have one brother.", "У меня один брат."],
        ["This is the one I like.", "Это тот, который мне нравится."],
        ["One of them is missing.", "Один из них пропал."]
    ],
    "have": [
        ["I have a dog.", "У меня есть собака."],
        ["She doesn't have any money.", "У нее нет денег."],
        ["We have to leave now.", "Нам нужно уйти сейчас."]
    ],
    "this": [
        ["This is my book.", "Это моя книга."],
        ["What is this?", "Что это?"],
        ["I don't like this color.", "Мне не нравится этот цвет."]
    ],
    "from": [
        ["She is from France.", "Она из Франции."],
        ["I got a gift from my friend.", "Я получил подарок от друга."],
        ["Where are you from?", "Откуда ты?"]
    ],
    "or": [
        ["Do you want tea or coffee?", "Хочешь чай или кофе?"],
        ["You can have it now or later.", "Ты можешь взять это сейчас или позже."],
        ["Is this the first floor or the second?", "Это первый этаж или второй?"]
    ],
    "had": [
        ["He had a headache yesterday.", "У него была головная боль вчера."],
        ["I wish I had more time.", "Жаль, что у меня нет больше времени."],
        ["She had a great time at the party.", "Она хорошо провела время на вечеринке."]
    ],
    "by": [
        ["I arrived by train.", "Я прибыл на поезде."],
        ["This was written by Shakespeare.", "Это было написано Шекспиром."],
        ["We'll finish the project by next week.", "Мы закончим проект к следующей неделе."]
    ],
    "not": [
        ["I am not hungry.", "Я не голоден."],
        ["She did not come to the party.", "Она не пришла на вечеринку."],
        ["It's not too late to change your mind.", "Еще не поздно передумать."]
    ],
    "word": [
        ["Can you spell this word?", "Можешь ты произнести это слово по буквам?"],
        ["I don't understand this word.", "Я не понимаю это слово."],
        ["He wrote down the word on the paper.", "Он записал слово на бумаге."]
    ],
    "but": [
        ["I want to go, but I can't.", "Я хочу пойти, но не могу."],
        ["She is tired but happy.", "Она устала, но счастлива."],
        ["The weather is cold, but sunny.", "Погода холодная, но солнечная."]
    ],
    "what": [
        ["What is your name?", "Как тебя зовут?"],
        ["I don't know what to do.", "Я не знаю, что делать."],
        ["What time is it?", "Который час?"]
    ],
    "some": [
        ["Do you have some time?", "У тебя есть время?"],
        ["She bought some fruits at the market.", "Она купила некоторые фрукты на рынке."],
        ["There are some books on the shelf.", "На полке есть несколько книг."]
    ],
    "we": [
        ["We are going to the movies.", "Мы идем в кино."],
        ["Can we meet tomorrow?", "Можем ли мы встретиться завтра?"],
        ["We have a meeting at 3 PM.", "У нас встреча в 3 часа дня."]
    ],
    "can": [
        ["I can speak English.", "Я могу говорить по-английски."],
        ["Can you help me, please?", "Можешь помочь мне, пожалуйста?"],
        ["He can swim very well.", "Он отлично умеет плавать."]
    ],
    "out": [
        ["She went out for a walk.", "Она вышла погулять."],
        ["The lights went out.", "Свет погас."],
        ["We need to find out what happened.", "Нам нужно выяснить, что произошло."]
    ],
    "other": [
        ["He has two cars; the other one is red.", "У него две машины, другая красная."],
        ["What other books do you have?", "Какие другие книги у вас есть?"],
        ["He is busy, so I'll ask the other person.", "Он занят, так что я спрошу другого человека."]
    ],
    "were": [
        ["They were at the restaurant.", "Они были в ресторане."],
        ["The keys were on the table.", "Ключи были на столе."],
        ["Where were you yesterday?", "Где вы были вчера?"]
    ],
    "all": [
        ["She ate all the cookies.", "Она съела все печенья."],
        ["We are all going to the party.", "Мы все идем на вечеринку."],
        ["All the students passed the exam.", "Все студенты сдали экзамен."]
    ],
    "there": [
        ["There is a cat on the roof.", "На крыше сидит кошка."],
        ["There are many books on the shelf.", "На полке много книг."],
        ["There will be a meeting tomorrow.", "Завтра будет собрание."]
    ],
    "when": [
        ["When will you arrive?", "Когда ты приедешь?"],
        ["I was sleeping when you called.", "Я спал, когда ты звонил."],
        ["When did you last see her?", "Когда ты в последний раз видел ее?"]
    ],
    "up": [
        ["He stood up and left the room.", "Он встал и вышел из комнаты."],
        ["The sun is up.", "Солнце взошло."],
        ["I need to clean up the kitchen.", "Мне нужно убрать на кухне."]
    ],
    "use": [
        ["How do you use this machine?", "Как вы пользуетесь этой машиной?"],
        ["I use this app every day.", "Я использую это приложение каждый день."],
        ["You can use my car.", "Вы можете использовать мою машину."]
    ],
    "your": [
        ["What is your name?", "Как вас зовут?"],
        ["Where is your house?", "Где ваш дом?"],
        ["Is this your bag?", "Это ваша сумка?"]
    ],
    "how": [
        ["How are you?", "Как вы?"],
        ["How much does it cost?", "Сколько это стоит?"],
        ["How do you spell your name?", "Как ты пишешь свое имя по буквам?"]
    ],
    "said": [
        ["She said she would come.", "Она сказала, что придет."],
        ["What did he say?", "Что он сказал?"],
        ["He said he likes chocolate.", "Он сказал, что любит шоколад."]
    ],
    "an": [
        ["I need an umbrella.", "Мне нужен зонт."],
        ["He is an engineer.", "Он инженер."],
        ["She bought an apple.", "Она купила яблоко."]
    ],
    "each": [
        ["Each person has a different opinion.", "У каждого человека свое мнение."],
        ["Each student should have a book.", "У каждого студента должна быть книга."],
        ["I gave them each a present.", "Я подарил им каждому по подарку."]
    ],
    "she": [
        ["She is my sister.", "Она моя сестра."],
        ["She went to the store.", "Она пошла в магазин."],
        ["She likes to read books.", "Она любит читать книги."]
    ],
    "which": [
        ["Which book do you prefer?", "Какую книгу вы предпочитаете?"],
        ["Which one is yours?", "Какой из них ваш?"],
        ["I don't know which way to go.", "Я не знаю, куда идти."]
    ],
    "do": [
        ["What do you want to do?", "Что вы хотите сделать?"],
        ["What does he do for a living?", "Чем он зарабатывает на жизнь?"],
        ["I have to do my homework.", "Мне нужно сделать свою домашнюю работу."]
    ],
    "their": [
        ["They lost their keys.", "Они потеряли свои ключи."],
        ["The children love their toys.", "Дети любят свои игрушки."],
        ["Each family has their own traditions.", "У каждой семьи свои традиции."]
    ],
    "time": [
        ["What time is it?", "Который час?"],
        ["We had a great time at the party.", "Мы отлично провели время на вечеринке."],
        ["Time flies when you're having fun.", "Время летит, когда весело."]
    ],
    "if": [
        ["What will you do if it rains?", "Что вы будете делать, если пойдет дождь?"],
        ["I'll go to the beach if the weather is nice.", "Я поеду на пляж, если будет хорошая погода."],
        ["If you need help, just ask.", "Если вам нужна помощь, просто спросите."]
    ],
    "will": [
        ["I will call you later.", "Я позвоню тебе позже."],
        ["She will arrive tomorrow.", "Она приедет завтра."],
        ["Will you come to the party?", "Придешь ли ты на вечеринку?"]
    ],
    "way": [
        ["Which way is the beach?", "Какой путь к пляжу?"],
        ["There is no easy way to success.", "Нет легкого пути к успеху."],
        ["He found a way to solve the problem.", "Он нашел способ решить проблему."]
    ],
    "about": [
        ["What are you talking about?", "О чем вы говорите?"],
        ["Tell me about your trip.", "Расскажите мне о своей поездке."],
        ["I don't know much about this topic.", "Я не очень много знаю об этой теме."]
    ],
    "many": [
        ["How many apples do you want?", "Сколько яблок ты хочешь?"],
        ["There are many books on the shelf.", "На полке много книг."],
        ["How many people came to the party?", "Сколько человек пришло на вечеринку?"]
    ],
    "then": [
        ["We went to the park, and then to the zoo.", "Мы пошли в парк, а затем в зоопарк."],
        ["If you finish your homework, then you can play.",
         "Если ты закончишь свою домашнюю работу, тогда можешь поиграть."],
        ["He finished his meal, then left the restaurant.", "Он закончил свой обед, затем вышел из ресторана."]
    ],
    "them": [
        ["I gave them a gift.", "Я подарил им подарок."],
        ["Did you see them at the party?", "Ты видел их на вечеринке?"],
        ["I know them well.", "Я хорошо их знаю."]
    ],
    "write": [
        ["Can you write your name here?", "Можешь ли ты написать свое имя здесь?"],
        ["She likes to write stories.", "Она любит писать рассказы."],
        ["He will write a letter to his friend.", "Он напишет письмо другу."]
    ],
    "would": [
        ["I would like to go on vacation.", "Я бы хотел поехать в отпуск."],
        ["She said she would call me later.", "Она сказала, что позвонит мне позже."],
        ["He would help if he could.", "Он помог бы, если бы смог."]
    ],
    "like": [
        ["What do you like to do in your free time?", "Что вам нравится делать в свободное время?"],
        ["She doesn't like coffee.", "Ей не нравится кофе."],
        ["I like this song.", "Мне нравится эта песня."]
    ],
    "so": [
        ["I am so tired.", "Я так устал."],
        ["She is not feeling well, so she stayed home.", "Ей плохо, поэтому она осталась дома."],
        ["He was late, so he missed the train.", "Он опоздал, поэтому пропустил поезд."]
    ],
    "these": [
        ["These are my favorite books.", "Это мои любимые книги."],
        ["She wants to buy these shoes.", "Она хочет купить эти туфли."],
        ["I don't like these colors.", "Мне не нравятся эти цвета."]
    ],
    "her": [
        ["I gave her a present.", "Я подарил ей подарок."],
        ["Do you know her?", "Ты знаешь ее?"],
        ["Her car is parked outside.", "Ее машина припаркована снаружи."]
    ],
    "long": [
        ["How long have you been waiting?", "Как долго ты ждешь?"],
        ["She has long hair.", "У нее длинные волосы."],
        ["I haven't seen him in a long time.", "Я не видел его очень давно."]
    ],
    "make": [
        ["Can you make a cake?", "Можешь ли ты приготовить торт?"],
        ["She wants to make a good impression.", "Она хочет произвести хорошее впечатление."],
        ["He will make a decision soon.", "Он примет решение скоро."]
    ],
    "thing": [
        ["What is that thing on the table?", "Что это за штука на столе?"],
        ["She likes to try new things.", "Она любит пробовать новые вещи."],
        ["He forgot to bring his things.", "Он забыл взять свои вещи."]
    ],
    "see": [
        ["I see a bird in the tree.", "Я вижу птицу на дереве."],
        ["Can you see the stars?", "Ты видишь звезды?"],
        ["She wants to see the world.", "Она хочет увидеть мир."]
    ],
    "him": [
        ["I gave him a book.", "Я дал ему книгу."],
        ["Did you talk to him?", "Ты говорил с ним?"],
        ["She likes him a lot.", "Она очень его любит."]
    ],
    "two": [
        ["I have two brothers.", "У меня два брата."],
        ["There are two apples on the table.", "На столе два яблока."],
        ["She needs two tickets.", "Ей нужно два билета."]
    ],
    "has": [
        ["She has a cat.", "У нее есть кот."],
        ["He has a new job.", "У него новая работа."],
        ["She has been to Paris.", "Она была в Париже."]
    ],
    "look": [
        ["Look at the beautiful sunset.", "Посмотрите на красивый закат."],
        ["She looks happy.", "Она выглядит счастливой."],
        ["Can you look for my keys?", "Можешь ли ты поискать мои ключи?"]
    ],
    "more": [
        ["I need more time.", "Мне нужно больше времени."],
        ["She wants more information.", "Она хочет больше информации."],
        ["We need more space.", "Нам нужно больше места."]
    ],
    "day": [
        ["Today is a beautiful day.", "Сегодня прекрасный день."],
        ["She likes to start her day early.", "Она любит начинать день рано."],
        ["He has a busy day ahead.", "У него на сегодня намечен насыщенный день."]
    ],
    "could": [
        ["I could swim when I was a child.", "Я умел плавать, когда был ребенком."],
        ["She could speak three languages.", "Она могла говорить на трех языках."],
        ["He could come later.", "Он мог бы прийти позже."]
    ],
    "go": [
        ["I want to go to the beach.", "Я хочу пойти на пляж."],
        ["She will go to the store.", "Она пойдет в магазин."],
        ["We can go together.", "Мы можем пойти вместе."]
    ],
    "come": [
        ["Please come to the party.", "Пожалуйста, приходите на вечеринку."],
        ["She will come with us.", "Она придет с нами."],
        ["He didn't come to work yesterday.", "Он не пришел на работу вчера."]
    ],
    "did": [
        ["What did you do yesterday?", "Что вы делали вчера?"],
        ["She did her homework.", "Она сделала свою домашнюю работу."],
        ["He did a great job.", "Он сделал отличную работу."]
    ],
    "number": [
        ["What is your phone number?", "Какой у вас номер телефона?"],
        ["There are a large number of books in the library.", "В библиотеке большое количество книг."],
        ["The number of students in the class is increasing.", "Количество студентов в классе увеличивается."]
    ],
    "sound": [
        ["I like the sound of the waves.", "Мне нравится звук волн."],
        ["The alarm clock makes a loud sound.", "Будильник издает громкий звук."],
        ["The door made a creaking sound.", "Дверь издала скрипучий звук."]
    ],
    "no": [
        ["No, I don't want any coffee.", "Нет, я не хочу кофе."],
        ["There is no time left.", "Времени не осталось."],
        ["She said no to the offer.", "Она отказалась от предложения."]
    ],
    "most": [
        ["Most people like chocolate.", "Большинство людей любят шоколад."],
        ["She spends most of her time studying.", "Она проводит большую часть времени за учебой."],
        ["He won most of the games.", "Он выиграл большинство игр."]
    ],
    "people": [
        ["There are many people at the party.", "На вечеринке много людей."],
        ["Some people prefer tea over coffee.", "Некоторые люди предпочитают чай кофе."],
        ["She loves to be around people.", "Она любит находиться среди людей."]
    ],
    "my": [
        ["This is my book.", "Это моя книга."],
        ["I love my family.", "Я люблю свою семью."],
        ["He is my best friend.", "Он мой лучший друг."]
    ],
    "over": [
        ["The bridge goes over the river.", "Мост перекидывает реку."],
        ["He jumped over the fence.", "Он перепрыгнул через забор."],
        ["The game is over.", "Игра окончена."]
    ],
    "know": [
        ["Do you know her?", "Ты знаешь ее?"],
        ["I know how to swim.", "Я умею плавать."],
        ["She wants to know more about it.", "Она хочет узнать больше об этом."]
    ],
    "water": [
        ["She likes to drink water.", "Она любит пить воду."],
        ["There is not enough water in the bottle.", "В бутылке недостаточно воды."],
        ["The plants need water.", "Растениям нужна вода."]
    ],
    "than": [
        ["She is taller than her sister.", "Она выше своей сестры."],
        ["I would rather stay home than go out.", "Я бы предпочел остаться дома, чем выйти."],
        ["He has more books than me.", "У него больше книг, чем у меня."]
    ],
    "call": [
        ["Can you call me later?", "Можешь ли ты позвонить мне позже?"],
        ["She called her friend yesterday.", "Она позвонила своей подруге вчера."],
        ["I need to make a call.", "Мне нужно позвонить."]
    ],
    "first": [
        ["This is the first time I've been here.", "Это мой первый раз здесь."],
        ["She finished first in the race.", "Она первой финишировала на гонке."],
        ["He came first in the exam.", "Он первым пришел на экзамен."]
    ],
    "who": [
        ["Who is that girl?", "Кто эта девушка?"],
        ["Who is coming to the party?", "Кто придет на вечеринку?"],
        ["Who did you talk to?", "С кем ты разговаривал?"]
    ],
    "may": [
        ["May I ask you a question?", "Могу я задать вам вопрос?"],
        ["It may rain tomorrow.", "Завтра может пойти дождь."],
        ["She may come later.", "Она может прийти позже."]
    ],
    "down": [
        ["The ball rolled down the hill.", "Мяч скатился вниз с холма."],
        ["She wrote down the address.", "Она записала адрес."],
        ["He was feeling down after the news.", "Он печалился после новостей."]
    ],
    "side": [
        ["He sat on the left side.", "Он сидел слева."],
        ["The car is parked on the other side.", "Машина припаркована на другой стороне."],
        ["She injured her leg on the side.", "Она поранила ногу сбоку."]
    ],
    "been": [
        ["I have been to Paris.", "Я был в Париже."],
        ["She has been studying for hours.", "Она учится уже часы."],
        ["He has been waiting for you.", "Он ждет тебя."]
    ],
    "now": [
        ["I am busy right now.", "Я сейчас занят."],
        ["She is sleeping now.", "Она спит сейчас."],
        ["Now is the time to act.", "Сейчас время действовать."]
    ],
    "find": [
        ["Can you help me find my keys?", "Можешь ли ты помочь мне найти мои ключи?"],
        ["She couldn't find her glasses.", "Она не могла найти свои очки."],
        ["I need to find a new job.", "Мне нужно найти новую работу."]
    ],
    "any": [
        ["Do you have any questions?", "У вас есть какие-нибудь вопросы?"],
        ["I don't have any money.", "У меня нет денег."],
        ["Can I help in any way?", "Могу я помочь как-нибудь?"]
    ],
    "new": [
        ["She got a new job.", "Она нашла новую работу."],
        ["He bought a new car.", "Он купил новую машину."],
        ["Do you like my new dress?", "Тебе нравится мое новое платье?"]
    ],
    "work": [
        ["She goes to work by bus.", "Она ездит на работу на автобусе."],
        ["He is working on a new project.", "Он работает над новым проектом."],
        ["She works as a teacher.", "Она работает учительницей."]
    ],
    "part": [
        ["She played a part in the movie.", "Она сыграла роль в фильме."],
        ["This is an important part of the process.", "Это важная часть процесса."],
        ["He wants to be part of the team.", "Он хочет быть частью команды."]
    ],
    "take": [
        ["Can you take me home?", "Можешь отвезти меня домой?"],
        ["She will take the bus.", "Она поедет на автобусе."],
        ["He needs to take his medicine.", "Он должен принять свои лекарства."]
    ],
    "get": [
        ["I need to get some sleep.", "Мне нужно немного поспать."],
        ["She will get the tickets.", "Она купит билеты."],
        ["He needs to get a haircut.", "Ему нужно подстричься."]
    ],
    "place": [
        ["Can you show me the place on the map?", "Можешь показать мне место на карте?"],
        ["She found a nice place to live.", "Она нашла хорошее место для жизни."],
        ["He took first place in the competition.", "Он занял первое место в соревновании."]
    ],
    "made": [
        ["She made a cake for the party.", "Она сделала торт для вечеринки."],
        ["He made a mistake.", "Он сделал ошибку."],
        ["The dress is made of silk.", "Платье сделано из шелка."]
    ],
    "live": [
        ["Where do you live?", "Где ты живешь?"],
        ["She wants to live in a big city.", "Она хочет жить в большом городе."],
        ["He has lived here for years.", "Он живет здесь уже много лет."]
    ],
    "where": [
        ["Where is the nearest bank?", "Где ближайший банк?"],
        ["Where did you go yesterday?", "Куда вы ходили вчера?"],
        ["Where can I find a good restaurant?", "Где я могу найти хороший ресторан?"]
    ],
    "after": [
        ["I will call you after dinner.", "Я позвоню тебе после ужина."],
        ["She always goes for a walk after work.", "Она всегда гуляет после работы."],
        ["He arrived shortly after midnight.", "Он прибыл вскоре после полуночи."]
    ],
    "back": [
        ["Can you move the chair back?", "Можешь передвинуть стул назад?"],
        ["She will be back in an hour.", "Она вернется через час."],
        ["He went back to his hometown.", "Он вернулся в свой родной город."]
    ],
    "little": [
        ["He has a little money.", "У него немного денег."],
        ["She likes to read a little before bed.", "Она любит почитать перед сном."],
        ["I have very little time.", "У меня очень мало времени."]
    ],
    "only": [
        ["This is the only book I have.", "Это единственная книга, которую у меня есть."],
        ["He was the only person at the party.", "Он был единственным человеком на вечеринке."],
        ["I can only stay for a few minutes.", "Я могу остаться только на несколько минут."]
    ],
    "round": [
        ["The Earth goes round the sun.", "Земля вращается вокруг солнца."],
        ["She wore a round hat.", "Она надела круглую шляпу."],
        ["We will have a round of drinks.", "Мы выпьем раунд напитков."]
    ],
    "man": [
        ["He is a tall man.", "Он высокий мужчина."],
        ["The man in the hat waved at us.", "Человек в шляпе махнул нам."],
        ["She married a rich man.", "Она вышла замуж за богатого мужчину."]
    ],
    "year": [
        ["This year has been difficult.", "Этот год был сложным."],
        ["She was born in the same year as me.", "Она родилась в том же году, что и я."],
        ["He will turn thirty next year.", "Ему исполнится тридцать лет в следующем году."]
    ],
    "came": [
        ["She came to visit us yesterday.", "Она пришла навестить нас вчера."],
        ["He came running when he heard the news.", "Он прибежал, когда услышал новость."],
        ["The package came in the mail.", "Посылка пришла по почте."]
    ],
    "show": [
        ["Can you show me how to do it?", "Можешь ли ты показать мне, как это делать?"],
        ["She will show us her new painting.", "Она покажет нам свою новую картину."],
        ["The exhibit will show many famous artworks.", "Выставка покажет много известных произведений искусства."]
    ],
    "every": [
        ["She goes for a walk every morning.", "Она гуляет каждое утро."],
        ["He visits his parents every weekend.", "Он навещает своих родителей каждые выходные."],
        ["We have a meeting every Monday.", "У нас собрание каждый понедельник."]
    ],
    "good": [
        ["She is a good friend.", "Она хороший друг."],
        ["He did a good job on the project.", "Он хорошо поработал над проектом."],
        ["This soup tastes really good.", "Этот суп действительно вкусный."]
    ],
    "me": [
        ["Can you help me?", "Можешь ли ты мне помочь?"],
        ["She gave me a present.", "Она подарила мне подарок."],
        ["He told me the news.", "Он сообщил мне новость."]
    ],
    "give": [
        ["Can you give me some advice?", "Можешь ли ты дать мне немного совета?"],
        ["She will give a speech at the conference.", "Она выступит с речью на конференции."],
        ["He gave me a book for my birthday.", "Он подарил мне книгу на мой день рождения."]
    ],
    "our": [
        ["This is our house.", "Это наш дом."],
        ["We will have our meeting tomorrow.", "У нас будет наше собрание завтра."],
        ["She is one of our best employees.", "Она одна из наших лучших сотрудников."]
    ],
    "under": [
        ["The cat is under the table.", "Кот под столом."],
        ["She found her keys under the bed.", "Она нашла свои ключи под кроватью."],
        ["We are under a lot of pressure.", "Мы находимся под большим давлением."]
    ],
    "name": [
        ["What is your name?", "Как тебя зовут?"],
        ["She forgot his name.", "Она забыла его имя."],
        ["He signed his name on the contract.", "Он подписал свое имя в контракте."]
    ],
    "very": [
        ["She is very happy.", "Она очень счастлива."],
        ["He lives very far from here.", "Он живет очень далеко отсюда."],
        ["It's very cold outside.", "Снаружи очень холодно."]
    ],
    "through": [
        ["We walked through the forest.", "Мы прошли через лес."],
        ["She read through the entire book.", "Она прочитала весь книгу до конца."],
        ["He looked through the window.", "Он посмотрел через окно."]
    ],
    "just": [
        ["He just left.", "Он только что ушел."],
        ["She just finished her homework.", "Она только что закончила домашнюю работу."],
        ["I just want to rest.", "Я просто хочу отдохнуть."]
    ],
    "form": [
        ["Fill out this form, please.", "Пожалуйста, заполните эту форму."],
        ["She will form a committee.", "Она создаст комитет."],
        ["This is a different form of art.", "Это другая форма искусства."]
    ],
    "sentence": [
        ["Please write a sentence using this word.", "Пожалуйста, напишите предложение, используя это слово."],
        ["He was sentenced to five years in prison.", "Ему вынесли приговор на пять лет тюрьмы."],
        ["She formed the sentence carefully.", "Она тщательно составила предложение."]
    ],
    "great": [
        ["She did a great job on the project.", "Она отлично справилась с проектом."],
        ["It was a great party.", "Это была отличная вечеринка."],
        ["He achieved great success.", "Он достиг большого успеха."]
    ],
    "think": [
        ["What do you think about this idea?", "Что вы думаете об этой идее?"],
        ["She thinks he is lying.", "Она думает, что он лжет."],
        ["He didn't think it was important.", "Он не думал, что это важно."]
    ],
    "say": [
        ["She didn't say anything.", "Она ничего не сказала."],
        ["He will say goodbye before leaving.", "Он попрощается перед уходом."],
        ["What did he say?", "Что он сказал?"]
    ],
    "help": [
        ["Can you help me with this problem?", "Можешь ли ты помочь мне с этой проблемой?"],
        ["She always helps her friends.", "Она всегда помогает своим друзьям."],
        ["He needs help moving the furniture.", "Ему нужна помощь в переноске мебели."]
    ],
    "low": [
        ["The temperature is low today.", "Сегодня низкая температура."],
        ["She has a low voice.", "У нее низкий голос."],
        ["He bought the painting at a low price.", "Он купил картину по низкой цене."]
    ],
    "line": [
        ["Please stand in line.", "Пожалуйста, станьте в очередь."],
        ["She drew a straight line.", "Она нарисовала прямую линию."],
        ["He crossed the finish line first.", "Он первым пересек финишную черту."]
    ],
    "differ": [
        ["Their opinions differ on this matter.", "Их мнения различаются по этому вопросу."],
        ["The two cars differ in price.", "Два автомобиля отличаются по цене."],
        ["Her approach differs from mine.", "Ее подход отличается от моего."]
    ],
    "turn": [
        ["It's your turn to speak.", "Твоя очередь говорить."],
        ["She took a left turn.", "Она повернула налево."],
        ["He will turn the key in the lock.", "Он повернет ключ в замке."]
    ],
    "cause": [
        ["What was the cause of the accident?", "Какова была причина аварии?"],
        ["She will cause trouble if she continues.", "Она наверняка натворит беды, если продолжит."],
        ["He fought for a good cause.", "Он боролся за благородную цель."]
    ],
    "much": [
        ["I don't have much time.", "У меня нет много времени."],
        ["She doesn't eat much meat.", "Она не ест много мяса."],
        ["How much does it cost?", "Сколько это стоит?"]
    ],
    "mean": [
        ["What does this word mean?", "Что означает это слово?"],
        ["She didn't mean to hurt your feelings.", "Она не имела в виду обидеть вас."],
        ["He meant what he said.", "Он имел в виду то, что сказал."]
    ],
    "before": [
        ["We met before.", "Мы встречались раньше."],
        ["She arrived before the others.", "Она приехала раньше остальных."],
        ["He had never seen her before.", "Он никогда раньше не видел ее."]
    ],
    "move": [
        ["Can you help me move this table?", "Можешь помочь мне передвинуть этот стол?"],
        ["She will move to a new city.", "Она переедет в новый город."],
        ["He made a quick move to catch the ball.", "Он сделал быстрое движение, чтобы поймать мяч."]
    ],
    "right": [
        ["Turn right at the next intersection.", "Поверните направо на следующем перекрестке."],
        ["She was right about the answer.", "Она была права в ответе."],
        ["He stood up for what he believed was right.", "Он выступил за то, во что верил."]
    ],
    "boy": [
        ["He is a little boy.", "Он маленький мальчик."],
        ["She has a baby boy.", "У нее мальчик-младенец."],
        ["The boy ran after the ball.", "Мальчик побежал за мячом."]
    ],
    "old": [
        ["She has an old car.", "У нее старая машина."],
        ["He is an old friend of mine.", "Он мой старый друг."],
        ["The building is very old.", "Здание очень старое."]
    ],
    "too": [
        ["She ate too much cake.", "Она съела слишком много пирога."],
        ["He was too tired to go out.", "Он был слишком устал, чтобы выйти на улицу."],
        ["This shirt is too small for me.", "Эта рубашка слишком мала для меня."]
    ],
    "same": [
        ["We have the same birthday.", "У нас одинаковые дни рождения."],
        ["She wore the same dress as me.", "Она надела тот же самый платье, что и я."],
        ["He said the same thing yesterday.", "Он сказал то же самое вчера."]
    ],
    "tell": [
        ["Can you tell me the time?", "Можешь ли ты сказать мне время?"],
        ["She told him the news.", "Она сообщила ему новость."],
        ["He can't tell the difference.", "Он не может определить разницу."]
    ],
    "does": [
        ["What does this button do?", "Что делает этот кнопка?"],
        ["She does her homework every day.", "Она делает свою домашнюю работу каждый день."],
        ["He does a great job at work.", "Он хорошо справляется с работой."]
    ],
    "set": [
        ["Please set the table for dinner.", "Пожалуйста, накройте стол к ужину."],
        ["She set her alarm clock for 7 AM.", "Она установила будильник на 7 утра."],
        ["He set a new record.", "Он установил новый рекорд."]
    ],
    "three": [
        ["She has three cats.", "У нее три кошки."],
        ["He bought three tickets.", "Он купил три билета."],
        ["The meeting will start in three minutes.", "Собрание начнется через три минуты."]
    ],
    "want": [
        ["What do you want for dinner?", "Что вы хотите на ужин?"],
        ["She wants to go to the beach.", "Она хочет пойти на пляж."],
        ["He wants a new bike for his birthday.", "Он хочет новый велосипед на свой день рождения."]
    ],
    "air": [
        ["The air in the mountains is fresh.", "Воздух в горах свежий."],
        ["She opened the window to let in some air.", "Она открыла окно, чтобы впустить немного воздуха."],
        ["He is a pilot in the air force.", "Он пилот военно-воздушных сил."]
    ],
    "well": [
        ["She is feeling well today.", "Сегодня она чувствует себя хорошо."],
        ["He speaks Spanish very well.", "Он очень хорошо говорит по-испански."],
        ["The company is doing well financially.", "Компания хорошо справляется финансово."]
    ],
    "also": [
        ["She is also coming to the party.", "Она тоже идет на вечеринку."],
        ["He is studying French, and also German.", "Он учит французский, а также немецкий."],
        ["She is not only smart but also kind.", "Она не только умна, но и добра."]
    ],
    "play": [
        ["Can you play the piano?", "Ты умеешь играть на пианино?"],
        ["She plays basketball every Saturday.", "Она играет в баскетбол каждую субботу."],
        ["He played a prank on his friend.", "Он сыграл розыгрыш над своим другом."]
    ],
    "small": [
        ["This is a small town.", "Это небольшой город."],
        ["She wears a small shoe size.", "Она носит маленький размер обуви."],
        ["He has a small garden in his backyard.", "У него маленький сад на заднем дворе."]
    ],
    "end": [
        ["This is the end of the road.", "Это конец дороги."],
        ["She reached the end of the book.", "Она достигла конца книги."],
        ["He is waiting for the end of the movie.", "Он ждет конца фильма."]
    ],
    "put": [
        ["Please put the book on the table.", "Пожалуйста, положите книгу на стол."],
        ["He put his keys in his pocket.", "Он положил свои ключи в карман."],
        ["She put on her shoes and left.", "Она надела свои ботинки и ушла."]
    ],
    "home": [
        ["She is at home right now.", "Она сейчас дома."],
        ["He went home after work.", "Он пошел домой после работы."],
        ["Their home is near the park.", "Их дом находится рядом с парком."]
    ],
    "read": [
        ["Can you read this book?", "Вы можете прочитать эту книгу?"],
        ["She read the newspaper every morning.", "Она читала газету каждое утро."],
        ["He read the letter aloud.", "Он прочитал письмо вслух."]
    ],
    "hand": [
        ["She held his hand tightly.", "Она крепко держала его за руку."],
        ["He gave her a hand with the bags.", "Он помог ей с сумками."],
        ["The clock's hands showed ten o'clock.", "Стрелки часов показывали десять часов."]
    ],
    "port": [
        ["The ship arrived at the port.", "Корабль прибыл в порт."],
        ["He plugged the device into the USB port.", "Он вставил устройство в USB-порт."],
        ["This city is a major port for trade.", "Этот город является крупным портом для торговли."]
    ],
    "large": [
        ["She has a large collection of books.", "У нее большая коллекция книг."],
        ["He lives in a large house.", "Он живет в большом доме."],
        ["They saw a large elephant at the zoo.", "Они увидели большого слона в зоопарке."]
    ],
    "spell": [
        ["Can you spell your name for me?", "Можете ли вы переписать свое имя для меня по буквам?"],
        ["She cast a spell on the wicked witch.", "Она наложила заклятие на злую ведьму."],
        ["He learned to spell his first word.", "Он научился правильно писать свое первое слово."]
    ],
    "add": [
        ["Please add sugar to my coffee.", "Пожалуйста, добавьте сахар в мой кофе."],
        ["He will add a new feature to the software.", "Он добавит новую функцию в программное обеспечение."],
        ["She added her signature at the bottom.", "Она добавила свою подпись внизу."]
    ],
    "even": [
        ["He didn't even say goodbye.", "Он даже не попрощался."],
        ["She always arrives at work even earlier.", "Она всегда приходит на работу даже раньше."],
        ["They couldn't even agree on a time.", "Они даже не могли договориться о времени."]
    ],
    "land": [
        ["The plane will land in ten minutes.", "Самолет приземлится через десять минут."],
        ["They bought land to build their house.", "Они купили землю, чтобы построить свой дом."],
        ["He saw land after days at sea.", "Он увидел сушу после дней в море."]
    ],
    "here": [
        ["She is waiting for you here.", "Она ждет вас здесь."],
        ["He came here to find work.", "Он приехал сюда, чтобы найти работу."],
        ["The keys are not here.", "Ключи здесь не находятся."]
    ],
    "must": [
        ["You must finish your homework before dinner.", "Ты должен закончить домашнее задание до ужина."],
        ["She must be at least 18 to enter.", "Ей должно быть как минимум 18 лет, чтобы войти."],
        ["He must follow the rules.", "Он должен следовать правилам."]
    ],
    "big": [
        ["She has a big dog.", "У нее большая собака."],
        ["He bought a big house.", "Он купил большой дом."],
        ["They had a big party last night.", "Вчера они устроили большую вечеринку."]
    ],
    "high": [
        ["She climbed to the top of the high mountain.", "Она поднялась на вершину высокой горы."],
        ["He has a high fever.", "У него высокая температура."],
        ["The plane flew at a high altitude.", "Самолет летел на высокой высоте."]
    ],
    "such": [
        ["She has never seen such a beautiful sunset.", "Она никогда не видела такого красивого заката."],
        ["He never said such things.", "Он никогда не говорил такие вещи."],
        ["They face such challenges every day.", "Они сталкиваются с такими вызовами каждый день."]
    ],
    "follow": [
        ["You should follow the instructions.", "Вы должны следовать инструкциям."],
        ["She decided to follow her dreams.", "Она решила следовать своим мечтам."],
        ["He will follow his friend's advice.", "Он последует совету своего друга."]
    ],
    "act": [
        ["She will act in the school play.", "Она будет играть в школьной постановке."],
        ["He must act quickly to save her.", "Он должен действовать быстро, чтобы спасти ее."],
        ["They will act on your suggestion.", "Они выполнят ваше предложение."]
    ],
    "why": [
        ["Why did you do that?", "Почему ты это сделал?"],
        ["She asked him why he was late.", "Она спросила его, почему он опоздал."],
        ["He couldn't understand why she was crying.", "Он не мог понять, почему она плакала."]
    ],
    "ask": [
        ["Can I ask you a question?", "Могу я задать вам вопрос?"],
        ["She asked her teacher for help.", "Она попросила своего учителя о помощи."],
        ["He will ask his boss for a raise.", "Он попросит своего начальника о повышении зарплаты."]
    ],
    "men": [
        ["The men were working in the field.", "Мужчины работали на поле."],
        ["She respects men who treat women equally.", "Она уважает мужчин, которые относятся к женщинам справедливо."],
        ["He will join the group of men.", "Он присоединится к группе мужчин."]
    ],
    "change": [
        ["She decided to change her job.", "Она решила поменять свою работу."],
        ["He needs to change his attitude.", "Ему нужно изменить свое отношение."],
        ["They hope to bring about change.", "Они надеются вызвать изменения."]
    ],
    "went": [
        ["She went to the store.", "Она пошла в магазин."],
        ["He went home after the party.", "Он пошел домой после вечеринки."],
        ["They went on vacation to Italy.", "Они поехали в отпуск в Италию."]
    ],
    "light": [
        ["The room was filled with light.", "Комната была полна света."],
        ["She turned off the light before leaving.", "Она выключила свет перед уходом."],
        ["He will light the candles on the cake.", "Он зажжет свечи на торте."]
    ],
    "kind": [
        ["She is a kind person.", "Она добрый человек."],
        ["He received a kind invitation to the event.", "Он получил доброе приглашение на мероприятие."],
        ["They showed great kindness to the refugees.", "Они проявили большую доброту к беженцам."]
    ],
    "off": [
        ["She turned off the lights.", "Она выключила свет."],
        ["He fell off his bike.", "Он упал с велосипеда."],
        ["The meeting is off.", "Собрание отменено."]
    ],
    "need": [
        ["She needs help with her homework.", "Ей нужна помощь с домашним заданием."],
        ["He needs to buy groceries.", "Ему нужно купить продукты."],
        ["They need more time to finish the project.", "Им нужно больше времени, чтобы завершить проект."]
    ],
    "house": [
        ["They live in a big house.", "Они живут в большом доме."],
        ["She cleaned the house yesterday.", "Она убрала дом вчера."],
        ["He will paint the house next month.", "Он покрасит дом в следующем месяце."]
    ],
    "picture": [
        ["She drew a picture of her cat.", "Она нарисовала картину своего кота."],
        ["He took a picture of the sunset.", "Он сделал снимок заката."],
        ["They hung a picture on the wall.", "Они повесили картину на стену."]
    ],
    "try": [
        ["Can you try again?", "Можете ли вы попробовать еще раз?"],
        ["She will try her best to finish on time.", "Она постарается завершить работу вовремя."],
        ["He tried the new restaurant last night.", "Он попробовал новый ресторан прошлой ночью."]
    ],
    "us": [
        ["She gave us a gift.", "Она подарила нам подарок."],
        ["He showed us the way.", "Он показал нам путь."],
        ["They will join us for dinner.", "Они присоединятся к нам на ужин."]
    ],
    "again": [
        ["Can you say that again?", "Можешь ли ты сказать это еще раз?"],
        ["She will try again tomorrow.", "Она попробует снова завтра."],
        ["He read the book again.", "Он прочитал книгу снова."]
    ],
    "animal": [
        ["The zoo has many exotic animals.", "В зоопарке много экзотических животных."],
        ["She loves all kinds of animals.", "Она любит всех видов животных."],
        ["He wants to study animal behavior.", "Он хочет изучать поведение животных."]
    ],
    "point": [
        ["Can you point to the map?", "Можешь показать на карте?"],
        ["She made a good point in the meeting.", "Она высказала хорошую точку зрения на собрании."],
        ["He reached the highest point of the mountain.", "Он достиг самой высокой точки горы."]
    ],
    "mother": [
        ["She is a loving mother.", "Она любящая мать."],
        ["He called his mother to wish her a happy birthday.",
         "Он позвонил своей матери, чтобы поздравить ее с днем рождения."],
        ["She will visit her mother this weekend.", "Она навестит свою мать на этой выходных."]
    ],
    "world": [
        ["She dreams of traveling the world.", "Она мечтает путешествовать по всему миру."],
        ["He is famous all over the world.", "Он известен во всем мире."],
        ["They believe in a better world.", "Они верят в лучший мир."]
    ],
    "near": [
        ["The store is near the park.", "Магазин рядом с парком."],
        ["She lives near her workplace.", "Она живет недалеко от своего места работы."],
        ["He found a nice restaurant near the hotel.", "Он нашел хороший ресторан недалеко от отеля."]
    ],
    "build": [
        ["They will build a new house.", "Они построят новый дом."],
        ["She wants to build a career in finance.", "Она хочет построить карьеру в финансах."],
        ["He helped build the bridge.", "Он помог построить мост."]
    ],
    "self": [
        ["She needs some time for self-reflection.", "Ей нужно время для саморефлексии."],
        ["He will do it himself.", "Он сделает это сам."],
        ["They believe in self-improvement.", "Они верят в самосовершенствование."]
    ],
    "earth": [
        ["The earth revolves around the sun.", "Земля вращается вокруг солнца."],
        ["She planted trees to help the earth.", "Она посадила деревья, чтобы помочь земле."],
        ["He studies the earth's atmosphere.", "Он изучает атмосферу Земли."]
    ],
    "father": [
        ["He is a good father.", "Он хороший отец."],
        ["She called her father on his birthday.", "Она позвонила своему отцу в день его рождения."],
        ["He will visit his father this weekend.", "Он навестит своего отца на этих выходных."]
    ],
    "head": [
        ["She has a headache.", "У нее болит голова."],
        ["He is the head of the company.", "Он глава компании."],
        ["They need to head north.", "Они должны направиться на север."]
    ],
    "stand": [
        ["She can't stand the heat.", "Она не выносит жару."],
        ["He will stand by his decision.", "Он будет придерживаться своего решения."],
        ["They watched him stand on the podium.", "Они смотрели, как он стоял на пьедестале."]
    ],
    "own": [
        ["She has her own business.", "У нее собственный бизнес."],
        ["He bought his own car.", "Он купил свою собственную машину."],
        ["They want to have their own house.", "Они хотят иметь свой собственный дом."]
    ],
    "page": [
        ["She turned the page of the book.", "Она перевернула страницу книги."],
        ["He wrote his name at the top of the page.", "Он написал свое имя вверху страницы."],
        ["They read the entire page.", "Они прочитали всю страницу."]
    ],
    "should": [
        ["You should eat more vegetables.", "Ты должен есть больше овощей."],
        ["She should call her parents more often.", "Она должна звонить своим родителям чаще."],
        ["He should arrive soon.", "Он должен скоро приехать."]
    ],
    "country": [
        ["She loves her country.", "Она любит свою страну."],
        ["He traveled to many countries.", "Он путешествовал по многим странам."],
        ["They will represent their country at the Olympics.",
         "Они будут представлять свою страну на Олимпийских играх."]
    ],
    "found": [
        ["They found a lost dog.", "Они нашли потерявшуюся собаку."],
        ["He founded a successful company.", "Он основал успешную компанию."],
        ["She found her keys in the drawer.", "Она нашла свои ключи в ящике."]
    ],
    "answer": [
        ["Can you answer the phone?", "Можешь ли ты ответить на телефон?"],
        ["She found the answer to the question.", "Она нашла ответ на вопрос."],
        ["He will answer the email tomorrow.", "Он ответит на письмо завтра."]
    ],
    "school": [
        ["She goes to school every day.", "Она ходит в школу каждый день."],
        ["He dropped out of school last year.", "Он бросил школу в прошлом году."],
        ["They will start school in September.", "Они начнут учебу в сентябре."]
    ],
    "grow": [
        ["The flowers will grow in the spring.", "Цветы будут расти весной."],
        ["She wants to grow vegetables in her garden.", "Она хочет выращивать овощи в своем саду."],
        ["He watched his son grow into a man.", "Он смотрел, как его сын вырос в мужчину."]
    ],
    "study": [
        ["She likes to study in the library.", "Ей нравится учиться в библиотеке."],
        ["He will study medicine at university.", "Он будет изучать медицину в университете."],
        ["They study hard for their exams.", "Они усердно готовятся к экзаменам."]
    ],
    "still": [
        ["She is still waiting for a reply.", "Она все еще ждет ответа."],
        ["He still lives in the same house.", "Он все еще живет в том же доме."],
        ["They are still considering their options.", "Они все еще рассматривают свои варианты."]
    ],
    "learn": [
        ["She wants to learn French.", "Она хочет выучить французский."],
        ["He learns from his mistakes.", "Он учится на своих ошибках."],
        ["They learn something new every day.", "Они узнают что-то новое каждый день."]
    ],
    "plant": [
        ["She planted flowers in the garden.", "Она посадила цветы в саду."],
        ["He will plant trees in the park.", "Он посадит деревья в парке."],
        ["They planted vegetables in the spring.", "Они посадили овощи весной."]
    ],
    "cover": [
        ["She used a blanket to cover herself.", "Она использовала одеяло, чтобы укрыться."],
        ["He will cover the book with paper.", "Он накроет книгу бумагой."],
        ["They covered the table with a cloth.", "Они покрыли стол скатертью."]
    ],
    "food": [
        ["She cooked delicious food for dinner.", "Она приготовила вкусную еду на ужин."],
        ["He likes to try different foods.", "Он любит пробовать разную еду."],
        ["They need to buy more food for the party.", "Им нужно купить больше еды на вечеринку."]
    ],
    "sun": [
        ["She enjoys sitting in the sun.", "Она любит сидеть на солнце."],
        ["He will watch the sunset in the evening.", "Он посмотрит на закат вечером."],
        ["They went sunbathing at the beach.", "Они отправились загорать на пляж."]
    ],
    "four": [
        ["She has four brothers.", "У нее четыре брата."],
        ["He will be four years old next month.", "Ему будет четыре года в следующем месяце."],
        ["They found four apples in the basket.", "Они нашли четыре яблока в корзине."]
    ],
    "between": [
        ["She sat between her two friends.", "Она сидела между своими двумя друзьями."],
        ["He had to choose between two options.", "Ему пришлось выбирать между двумя вариантами."],
        ["They live between the mountains and the sea.", "Они живут между горами и морем."]
    ],
    "state": [
        ["She lives in the state of California.", "Она живет в штате Калифорния."],
        ["He will represent his state in the competition.", "Он будет представлять свой штат в соревновании."],
        ["They visited the capital of their state.", "Они посетили столицу своего штата."]
    ],
    "keep": [
        ["She likes to keep her room tidy.", "Ей нравится держать свою комнату в порядке."],
        ["He will keep the promise he made.", "Он выполнит обещание, которое дал."],
        ["They need to keep the door closed.", "Им нужно держать дверь закрытой."]
    ],
    "eye": [
        ["She has brown eyes.", "У нее коричневые глаза."],
        ["He will keep an eye on the situation.", "Он будет следить за ситуацией."],
        ["They couldn't believe their eyes.", "Они не могли поверить своим глазам."]
    ],
    "never": [
        ["She never eats meat.", "Она никогда не ест мясо."],
        ["He never forgets his keys.", "Он никогда не забывает свои ключи."],
        ["They never miss a chance to travel.", "Они никогда не упускают возможность путешествовать."]
    ],
    "last": [
        ["She saw him last night.", "Она видела его прошлой ночью."],
        ["He will go to bed early tonight, unlike last night.",
         "Сегодня вечером он пойдет спать рано, в отличие от вчерашнего вечера."],
        ["They went to the beach last weekend.", "Они поехали на пляж на прошлых выходных."]
    ],
    "let": [
        ["She will let her sister borrow her dress.", "Она позволит своей сестре одолжить свое платье."],
        ["He won't let anyone ruin his plans.", "Он не позволит никому испортить свои планы."],
        ["They let the dog run free in the yard.", "Они позволили собаке бегать по двору на свободе."]
    ],
    "thought": [
        ["She had a thought about starting her own business.",
         "У нее была мысль о том, чтобы начать свой собственный бизнес."],
        ["He will give some thought to the proposal.", "Он обдумает предложение."],
        ["They shared their thoughts on the matter.", "Они поделились своими мыслями по этому вопросу."]
    ],
    "city": [
        ["She lives in a big city.", "Она живет в большом городе."],
        ["He will visit the city center.", "Он посетит центр города."],
        ["They love exploring new cities.", "Они любят исследовать новые города."]
    ],
    "tree": [
        ["She planted a tree in the garden.", "Она посадила дерево в саду."],
        ["He will climb the tree to get the ball.", "Он заберется на дерево, чтобы достать мяч."],
        ["They sat under the shade of a tree.", "Они сидели в тени дерева."]
    ],
    "cross": [
        ["She will cross the street at the crosswalk.", "Она перейдет улицу по пешеходному переходу."],
        ["He crossed the river on a bridge.", "Он пересек реку по мосту."],
        ["They crossed paths with an old friend.", "Они пересеклись на дороге со старым другом."]
    ],
    "farm": [
        ["She grew up on a farm.", "Она выросла на ферме."],
        ["He will work on a farm during the summer.", "Летом он будет работать на ферме."],
        ["They visited a dairy farm last weekend.", "Они посетили молочную ферму на прошлых выходных."]
    ],
    "hard": [
        ["She works hard every day.", "Она усердно работает каждый день."],
        ["He will try hard to win the race.", "Он постарается по максимуму, чтобы выиграть гонку."],
        ["They faced many hard challenges.", "Они столкнулись с многими трудными задачами."]
    ],
    "start": [
        ["She will start her new job next week.", "Она начнет свою новую работу на следующей неделе."],
        ["He started his own business last year.", "Он запустил свой собственный бизнес в прошлом году."],
        ["They want to start a family soon.", "Они хотят вскоре основать семью."]
    ],
    "might": [
        ["She might go to the concert if she finishes her work.",
         "Она может пойти на концерт, если закончит свою работу."],
        ["He might need help with the project.", "Ему может понадобиться помощь с проектом."],
        ["They might visit their relatives next weekend.",
         "Они могут навестить своих родственников на следующих выходных."]
    ],
    "story": [
        ["She likes to read stories before bedtime.", "Ей нравится читать рассказы перед сном."],
        ["He will tell them the story of his adventures.", "Он расскажет им историю своих приключений."],
        ["They listened to the story with interest.", "Они слушали историю с интересом."]
    ],
    "saw": [
        ["She saw him at the party last night.", "Она видела его на вечеринке прошлой ночью."],
        ["He saw a shooting star in the sky.", "Он увидел падающую звезду на небе."],
        ["They saw a movie at the cinema.", "Они посмотрели фильм в кинотеатре."]
    ],
    "far": [
        ["She lives far from the city.", "Она живет далеко от города."],
        ["He will go as far as he can.", "Он пойдет так далеко, насколько сможет."],
        ["They walked far to reach the village.", "Они прошли далеко, чтобы добраться до деревни."]
    ],
    "sea": [
        ["She likes to swim in the sea.", "Ей нравится плавать в море."],
        ["He will go fishing in the sea.", "Он пойдет рыбачить в море."],
        ["They went sailing on the sea.", "Они пошли парить на море."]
    ],
    "draw": [
        ["She likes to draw pictures.", "Ей нравится рисовать картинки."],
        ["He will draw a map for their trip.", "Он нарисует карту для их поездки."],
        ["They drew a plan for the new building.", "Они нарисовали план нового здания."]
    ],
    "left": [
        ["She left her keys at home.", "Она оставила свои ключи дома."],
        ["He will turn left at the next intersection.", "Он повернет налево на следующем перекрестке."],
        ["They left early to avoid traffic.", "Они вышли пораньше, чтобы избежать пробок."]
    ],
    "late": [
        ["She arrived late to the meeting.", "Она пришла на собрание поздно."],
        ["He will be late for dinner.", "Он опоздает на ужин."],
        ["They stayed out late last night.", "Они задержались допоздна прошлой ночью."]
    ],
    "run": [
        ["She likes to run in the park.", "Ей нравится бегать в парке."],
        ["He will run a marathon next month.", "Он примет участие в марафоне в следующем месяце."],
        ["They ran to catch the bus.", "Они побежали, чтобы поймать автобус."]
    ],
    "don't": [
        ["She doesn't like coffee.", "Она не любит кофе."],
        ["He doesn't want to go to the party.", "Он не хочет идти на вечеринку."],
        ["They don't have enough money to travel.", "У них нет достаточно денег для путешествия."]
    ],
    "while": [
        ["She read a book while waiting for the train.", "Она читала книгу, пока ждала поезд."],
        ["He will listen to music while jogging.", "Он будет слушать музыку во время пробежки."],
        ["They talked for a while before saying goodbye.", "Они поговорили некоторое время перед прощанием."]
    ],
    "press": [
        ["She will press the button to start the machine.", "Она нажмет кнопку, чтобы запустить машину."],
        ["He pressed his shirt before the interview.", "Он погладил свою рубашку перед собеседованием."],
        ["They pressed the grapes to make wine.", "Они отжали виноград, чтобы сделать вино."]
    ],
    "close": [
        ["She likes to sit close to the window.", "Ей нравится сидеть близко к окну."],
        ["He will close the door behind him.", "Он закроет за собой дверь."],
        ["They need to close the gate to keep the dog in.", "Им нужно закрыть ворота, чтобы собака не убежала."]
    ],
    "night": [
        ["She goes to bed early every night.", "Она ложится спать рано каждый вечер."],
        ["He will stay up all night to finish the project.", "Он пробудет всю ночь, чтобы закончить проект."],
        ["They went for a walk at night.", "Они пошли гулять ночью."]
    ],
    "real": [
        ["She thought it was a dream, but it was real.", "Она думала, что это сон, но это было реально."],
        ["He will face real challenges in his new job.", "Его ждут реальные трудности на новой работе."],
        ["They want to buy a real Christmas tree this year.", "Они хотят купить настоящую ёлку на этот год."]
    ],
    "life": [
        ["She enjoys life in the countryside.", "Она наслаждается жизнью за городом."],
        ["He will change his life for the better.", "Он изменит свою жизнь к лучшему."],
        ["They discussed the meaning of life.", "Они обсуждали смысл жизни."]
    ],
    "few": [
        ["She has few friends, but they are close.", "У нее мало друзей, но они близкие."],
        ["He will need a few more minutes to finish.", "Ему понадобится еще несколько минут, чтобы закончить."],
        ["They had a few options to choose from.", "У них было несколько вариантов на выбор."]
    ],
    "north": [
        ["She lives in the north of the country.", "Она живет на севере страны."],
        ["He will travel north for his vacation.", "Он отправится на север на каникулы."],
        ["They explored the north of the island.", "Они исследовали север острова."]
    ],
    "open": [
        ["She will open the door for her guests.", "Она откроет дверь для своих гостей."],
        ["He opened the window to let in some fresh air.", "Он открыл окно, чтобы впустить свежий воздух."],
        ["They opened a new branch of their business.", "Они открыли новое подразделение своего бизнеса."]
    ],
    "seem": [
        ["She seems happy today.", "Сегодня она кажется счастливой."],
        ["He will do whatever it takes to seem confident.", "Он сделает все, что угодно, чтобы казаться уверенным."],
        ["They seem to know each other well.", "Они, кажется, хорошо знают друг друга."]
    ],
    "together": [
        ["She likes to spend time together with her family.", "Ей нравится проводить время вместе с семьей."],
        ["He will work together with his colleagues on the project.",
         "Он будет работать вместе с коллегами над проектом."],
        ["They went on vacation together last summer.", "Они поехали в отпуск вместе прошлым летом."]
    ],
    "next": [
        ["She will see him again next week.", "Она увидит его снова на следующей неделе."],
        ["He will try again next time.", "Он попробует снова в следующий раз."],
        ["They are planning their next vacation.", "Они планируют свой следующий отпуск."]
    ],
    "white": [
        ["She likes to wear white clothes in summer.", "Летом ей нравится носить белую одежду."],
        ["He will paint the walls white.", "Он покрасит стены в белый цвет."],
        ["They decorated the room with white furniture.", "Они украсили комнату белой мебелью."]
    ],
    "children": [
        ["She works with children at the daycare.", "Она работает с детьми в детском саду."],
        ["He will read a bedtime story to his children.", "Он будет читать детям сказку перед сном."],
        ["They took their children to the playground.", "Они взяли своих детей на детскую площадку."]
    ],
    "begin": [
        ["She will begin her presentation with an introduction.", "Она начнет свою презентацию с введения."],
        ["He began his career in journalism.", "Он начал свою карьеру в журналистике."],
        ["They want to begin the project as soon as possible.", "Они хотят начать проект как можно скорее."]
    ],
    "got": [
        ["She got a new job.", "У нее новая работа."],
        ["He got a gift for his birthday.", "Он получил подарок на день рождения."],
        ["They got tickets for the concert.", "Они купили билеты на концерт."]
    ],
    "walk": [
        ["She likes to take a walk in the park.", "Ей нравится гулять в парке."],
        ["He will walk the dog in the evening.", "Он выгуляет собаку вечером."],
        ["They went for a long walk in the countryside.", "Они отправились на длинную прогулку за город."]
    ],
    "example": [
        ["Let me give you an example.", "Позвольте мне привести вам пример."],
        ["Here's an example of what not to do.", "Вот пример того, что не нужно делать."],
        ["Could you please provide an example of how to use this software?",
         "Могли бы вы, пожалуйста, привести пример использования этого программного обеспечения?"]
    ],
    "ease": [
        ["She completed the task with ease.", "Она справилась с заданием легко."],
        ["The new software will ease the process.", "Новое программное обеспечение упростит процесс."],
        ["He breathed a sigh of ease as he finally completed the task.",
         "Он вздохнул облегченно, когда наконец завершил задание"]
    ],
    "paper": [
        ["She wrote her thoughts on paper.", "Она записала свои мысли на бумаге."],
        ["He will wrap the gift in paper.", "Он завернет подарок в бумагу."],
        ["They submitted their paper for review.", "Они представили свою работу на рецензию."]
    ],
    "group": [
        ["She belongs to a study group.", "Она принадлежит к учебной группе."],
        ["He will meet with the group tomorrow.", "Он встретится с группой завтра."],
        ["They formed a new discussion group.", "Они создали новую группу для обсуждения."]
    ],
    "always": [
        ["She always arrives on time.", "Она всегда приходит вовремя."],
        ["He will always remember this moment.", "Он всегда будет помнить этот момент."],
        ["They always go for a walk after dinner.", "Они всегда идут гулять после ужина."]
    ],
    "music": [
        ["She listens to music every day.", "Она слушает музыку каждый день."],
        ["He will play music at the party.", "Он будет играть музыку на вечеринке."],
        ["They studied classical music in school.", "Они изучали классическую музыку в школе."]
    ],
    "those": [
        ["She wants those shoes.", "Она хочет те туфли."],
        ["He will buy those books tomorrow.", "Он купит те книги завтра."],
        ["They need to return those items.", "Им нужно вернуть эти вещи."]
    ],
    "both": [
        ["She likes both coffee and tea.", "Ей нравится и кофе, и чай."],
        ["He will choose both options.", "Он выберет оба варианта."],
        ["They are both happy with the decision.", "Они оба довольны решением."]
    ],
    "mark": [
        ["She made a mark on the paper.", "Она поставила отметку на бумаге."],
        ["He will mark the date on the calendar.", "Он отметит дату в календаре."],
        ["They received a high mark on the test.", "Они получили высокую оценку на тесте."]
    ],
    "often": [
        ["She often goes for a walk.", "Она часто гуляет."],
        ["He will often visit his grandparents.", "Он часто будет навещать своих бабушку и дедушку."],
        ["They often have lunch together.", "Они часто обедают вместе."]
    ],
    "letter": [
        ["She received a letter from her friend.", "Она получила письмо от своего друга."],
        ["He will write a letter to his parents.", "Он напишет письмо своим родителям."],
        ["They sent a letter of complaint to the company.", "Они отправили письмо с жалобой в компанию."]
    ],
    "until": [
        ["She will wait until he arrives.", "Она подождет, пока он придет."],
        ["He won't leave until you return.", "Он не уйдет, пока ты не вернешься."],
        ["They will stay until the end of the movie.", "Они останутся до конца фильма."]
    ],
    "mile": [
        ["She walked a mile every day.", "Она каждый день проходила милю."],
        ["He will drive for miles to reach the beach.", "Он проедет много миль, чтобы добраться до пляжа."],
        ["They hiked several miles in the mountains.", "Они преодолели несколько миль в горах."]
    ],
    "river": [
        ["She likes to swim in the river.", "Она любит плавать в реке."],
        ["He will go fishing by the river.", "Он пойдет рыбачить у реки."],
        ["They had a picnic next to the river.", "Они устроили пикник рядом с рекой."]
    ],
    "car": [
        ["She drives a car to work.", "Она ездит на машине на работу."],
        ["He will rent a car for the trip.", "Он арендует машину на поездку."],
        ["They bought a new car last month.", "Они купили новую машину в прошлом месяце."]
    ],
    "feet": [
        ["She stood on her feet all day.", "Она стояла на ногах весь день."],
        ["He will walk a few more feet.", "Он пройдет еще несколько футов."],
        ["They soaked their feet in warm water.", "Они вымочили ноги в теплой воде."]
    ],
    "care": [
        ["She takes care of her plants.", "Она заботится о своих растениях."],
        ["He will need special care after surgery.", "После операции ему потребуется особый уход."],
        ["They provide care for the elderly.", "Они обеспечивают уход за престарелыми."]
    ],
    "second": [
        ["She finished in second place.", "Она финишировала на втором месте."],
        ["He will decide in a second.", "Он примет решение моментально."],
        ["They met for the second time.", "Они встретились во второй раз."]
    ],
    "book": [
        ["She reads a book before bed.", "Она читает книгу перед сном."],
        ["He will buy a new book tomorrow.", "Завтра он купит новую книгу."],
        ["They borrowed a book from the library.", "Они одолжили книгу из библиотеки."]
    ],
    "carry": [
        ["She will carry the groceries home.", "Она понесет продукты домой."],
        ["He carried her bags up the stairs.", "Он поднял ее сумки по лестнице."],
        ["They carry a map when hiking.", "Они берут с собой карту, когда отправляются в поход."]
    ],
    "took": [
        ["She took the last cookie.", "Она взяла последнее печенье."],
        ["He took a picture of the sunset.", "Он сделал снимок заката."],
        ["They took a break from work.", "Они взяли перерыв от работы."]
    ],
    "science": [
        ["She studies science at university.", "Она учится на факультете наук в университете."],
        ["He will conduct a science experiment.", "Он проведет научный эксперимент."],
        ["They are interested in space science.", "Их интересует космическая наука."]
    ],
    "eat": [
        ["She likes to eat fruit for breakfast.", "Она любит есть фрукты на завтрак."],
        ["He will eat lunch at his desk.", "Он будет обедать за своим рабочим столом."],
        ["They eat dinner together as a family.", "Они ужинают вместе как семья."]
    ],
    "room": [
        ["She cleaned her room before guests arrived.", "Она убрала свою комнату, пока гости не пришли."],
        ["He will decorate the room for the party.", "Он украсит комнату к вечеринке."],
        ["They rented a room for the night.", "Они сняли комнату на ночь."]
    ],
    "friend": [
        ["She met her friend for coffee.", "Она встретилась с подругой на кофе."],
        ["He will introduce his friend to everyone.", "Он познакомит своего друга со всеми."],
        ["They have been friends for many years.", "Они дружат уже много лет."]
    ],
    "began": [
        ["She began her journey early in the morning.", "Она начала свое путешествие рано утром."],
        ["He will began the project next week.", "Он начнет проект на следующей неделе."],
        ["They began their performance with a song.", "Они начали свое выступление с песни."]
    ],
    "idea": [
        ["She had a brilliant idea.", "У нее была блестящая идея."],
        ["He will share his idea with the team.", "Он поделится своей идеей с командой."],
        ["They brainstormed ideas for the event.", "Они мозговали над идеями для мероприятия."]
    ],
    "fish": [
        ["She caught a fish in the lake.", "Она поймала рыбу в озере."],
        ["He will cook the fish for dinner.", "Он приготовит рыбу на ужин."],
        ["They went fishing early in the morning.", "Они пошли на рыбалку рано утром."]
    ],
    "mountain": [
        ["She hiked to the top of the mountain.", "Она поднялась на вершину горы."],
        ["He will climb the mountain next summer.", "Летом он взберется на гору."],
        ["They admired the view from the mountain.", "Они любовались видом с горы."]
    ],
    "stop": [
        ["She will stop at the store on her way home.", "Она остановится в магазине по дороге домой."],
        ["He stopped to take a break.", "Он остановился, чтобы передохнуть."],
        ["They need to make a quick stop for gas.", "Им нужно сделать быструю остановку за бензином."]
    ],
    "once": [
        ["She visited Paris once.", "Она однажды посетила Париж."],
        ["He will try skydiving once.", "Он попробует прыжок с парашютом один раз."],
        ["They went on a cruise once.", "Они совершили круиз однажды."]
    ],
    "base": [
        ["She built the cake on a chocolate base.", "Она построила торт на шоколадной основе."],
        ["He will use this as the base for his argument.",
         "Он будет использовать это в качестве основы для своего аргумента."],
        ["They built the base of the house first.", "Они сначала построили основание дома."]
    ],
    "hear": [
        ["She heard the sound of footsteps.", "Она услышала звук шагов."],
        ["He will hear the news soon.", "Он скоро услышит новости."],
        ["They heard a rumor about the new project.", "Они услышали слух о новом проекте."]
    ],
    "horse": [
        ["She rode a horse on the beach.", "Она ездила на лошади на пляже."],
        ["He will take care of the horse.", "Он позаботится о лошади."],
        ["They watched the horse race.", "Они наблюдали за скачками."]
    ],
    "cut": [
        ["She will cut the cake into slices.", "Она разрежет торт на кусочки."],
        ["He cut his finger while cooking.", "Он порезал палец, готовя еду."],
        ["They need to cut the grass in the garden.", "Им нужно подстричь траву в саду."]
    ],
    "sure": [
        ["She is sure of her decision.", "Она уверена в своем решении."],
        ["He will make sure everything is ready.", "Он убедится, что все готово."],
        ["They are sure they locked the door.", "Они уверены, что заперли дверь."]
    ],
    "watch": [
        ["She likes to watch the sunset.", "Ей нравится наблюдать за закатом."],
        ["He will watch the movie tonight.", "Он посмотрит фильм сегодня вечером."],
        ["They watch the birds in the garden.", "Они наблюдают за птицами в саду."]
    ],
    "color": [
        ["She painted the walls a bright color.", "Она покрасила стены ярким цветом."],
        ["He will choose a color for the car.", "Он выберет цвет для машины."],
        ["They mixed different colors to get the right shade.",
         "Они смешали разные цвета, чтобы получить нужный оттенок."]
    ],
    "face": [
        ["She washed her face before bed.", "Она вымыла лицо перед сном."],
        ["He will shave his face in the morning.", "Он побреет лицо утром."],
        ["They need to clean the paint off the face of the clock.", "Им нужно очистить от краски лицо часов."]
    ],
    "wood": [
        ["She built a fire with wood.", "Она разожгла огонь дровами."],
        ["He will carve a sculpture out of wood.", "Он вырежет скульптуру из дерева."],
        ["They used reclaimed wood for the table.", "Они использовали восстановленное дерево для стола."]
    ],
    "main": [
        ["She made the main course for dinner.", "Она приготовила основное блюдо на ужин."],
        ["He will focus on the main issue.", "Он сосредоточится на главной проблеме."],
        ["They found the main entrance.", "Они нашли главный вход."]
    ],
    "enough": [
        ["She has enough money for the trip.", "У нее достаточно денег на поездку."],
        ["He will run fast enough to win.", "Он будет бегать достаточно быстро, чтобы выиграть."],
        ["They arrived early enough to get good seats.", "Они прибыли достаточно рано, чтобы занять хорошие места."]
    ],
    "plain": [
        ["She likes her coffee plain.", "Она любит свой кофе простым."],
        ["He will choose the plain white shirt.", "Он выберет простую белую рубашку."],
        ["They prefer the plain version without toppings.", "Они предпочитают простую версию без начинки."]
    ],
    "girl": [
        ["She played with the girl in the park.", "Она играла с девочкой в парке."],
        ["He will take his daughter to the park.", "Он возьмет свою дочь в парк."],
        ["They watched the girl dance.", "Они наблюдали за тем, как девочка танцует."]
    ],
    "usual": [
        ["She followed her usual routine.", "Она придерживалась своего обычного распорядка дня."],
        ["He will order his usual drink.", "Он заказал свой обычный напиток."],
        ["They went about their usual business.", "Они занялись своими обычными делами."]
    ],
    "young": [
        ["She works with young children.", "Она работает с маленькими детьми."],
        ["He will meet with young entrepreneurs.", "Он встретится с молодыми предпринимателями."],
        ["They were once young and carefree.", "Они когда-то были молоды и беззаботны."]
    ],
    "ready": [
        ["She is ready to start.", "Она готова начать."],
        ["He will get ready for the party.", "Он приготовится к вечеринке."],
        ["They are ready for whatever comes next.", "Они готовы к любым последующим событиям."]
    ],
    "above": [
        ["She saw the birds flying above.", "Она увидела птиц, летающих над головой."],
        ["He will aim for a grade above.", "Он будет стремиться к оценке выше среднего."],
        ["They climbed the mountain above the clouds.", "Они поднялись на гору над облаками."]
    ],
    "ever": [
        ["She made the best cake ever.", "Она испекла самый вкусный торт в жизни."],
        ["He will never forget this moment ever.", "Он никогда не забудет этот момент."],
        ["They had the most fun ever on that trip.", "Они больше всего повеселились на этой поездке."]
    ],
    "red": [
        ["She wore a red dress to the party.", "На вечеринке она надела красное платье."],
        ["He will paint the walls red.", "Он покрасит стены в красный цвет."],
        ["They saw a red fox in the forest.", "Они увидели красную лису в лесу."]
    ],
    "list": [
        ["She made a list of groceries to buy.", "Она составила список продуктов для покупки."],
        ["He will add it to the list.", "Он добавит это в список."],
        ["They checked off each item on the list.", "Они отметили каждый пункт в списке."]
    ],
    "though": [
        ["She went out, though it was raining.", "Она вышла, хотя шел дождь."],
        ["He will come, even though he's tired.", "Он придет, даже если устал."],
        ["Though it was late, they continued working.", "Хотя было поздно, они продолжили работу."]
    ],
    "feel": [
        ["She feels happy today.", "Сегодня она чувствует себя счастливой."],
        ["He will feel better after some rest.", "После отдыха ему станет лучше."],
        ["They feel confident about the presentation.", "Они уверены в своей презентации."]
    ],
    "talk": [
        ["She likes to talk with her friends.", "Она любит разговаривать со своими друзьями."],
        ["He will talk to the manager about it.", "Он поговорит с менеджером об этом."],
        ["They talked for hours on the phone.", "Они разговаривали по телефону несколько часов."]
    ],
    "bird": [
        ["She saw a bird in the garden.", "Она увидела птицу в саду."],
        ["He will watch the birds in the park.", "Он будет наблюдать за птицами в парке."],
        ["They heard the birds chirping outside.", "Они слышали, как птицы щебечут на улице."]
    ],
    "soon": [
        ["She will be home soon.", "Она скоро будет дома."],
        ["He will finish the project soon.", "Он скоро закончит проект."],
        ["They will arrive soon.", "Они скоро прибудут."]
    ],
    "body": [
        ["She took care of her body.", "Она заботилась о своем теле."],
        ["He will exercise to keep his body healthy.", "Он будет заниматься спортом, чтобы сохранить здоровье."],
        ["They learned about the human body in school.", "Они изучали человеческое тело в школе."]
    ],
    "dog": [
        ["She has a dog as a pet.", "У нее есть собака в качестве домашнего животного."],
        ["He will take his dog for a walk.", "Он выгуляет свою собаку."],
        ["They trained their dog to do tricks.", "Они научили свою собаку выполнять трюки."]
    ],
    "family": [
        ["She spends time with her family on weekends.", "Она проводит время с семьей по выходным."],
        ["He will visit his family during the holidays.", "Он посетит свою семью на праздниках."],
        ["They are a close-knit family.", "Они - сплоченная семья."]
    ],
    "direct": [
        ["She will direct the play.", "Она будет режиссировать пьесу."],
        ["He directed the film.", "Он снял фильм."],
        ["They hired a direct flight.", "Они заказали прямой рейс."]
    ],
    "pose": [
        ["She struck a pose for the camera.", "Она приняла позу для фотоаппарата."],
        ["He will pose for a portrait.", "Он позирует для портрета."],
        ["They posed as tourists.", "Они выдавали себя за туристов."]
    ],
    "leave": [
        ["She will leave early tomorrow.", "Завтра она уйдет рано."],
        ["He will leave a note on the door.", "Он оставит записку на двери."],
        ["They left their keys on the table.", "Они оставили ключи на столе."]
    ],
    "song": [
        ["She sang a song for her friends.", "Она спела песню для своих друзей."],
        ["He will write a song for his girlfriend.", "Он напишет песню для своей подруги."],
        ["They listened to their favorite song.", "Они слушали свою любимую песню."]
    ],
    "measure": [
        ["She used a ruler to measure the length.", "Она использовала линейку, чтобы измерить длину."],
        ["He will measure the ingredients for the recipe.", "Он измерит ингредиенты по рецепту."],
        ["They measured the distance between the two points.", "Они измерили расстояние между двумя точками."]
    ],
    "door": [
        ["She closed the door behind her.", "Она закрыла за собой дверь."],
        ["He will paint the door red.", "Он покрасит дверь в красный цвет."],
        ["They knocked on the door.", "Они постучали в дверь."]
    ],
    "product": [
        ["She bought a new beauty product.", "Она купила новый косметический продукт."],
        ["He will develop a new product.", "Он разработает новый продукт."],
        ["They launched the product last month.", "Они запустили продукт в прошлом месяце."]
    ],
    "black": [
        ["She wore a black dress to the party.", "На вечеринку она надела черное платье."],
        ["He will paint the wall black.", "Он покрасит стену в черный цвет."],
        ["They saw a black cat crossing their path.", "Они увидели черного кота, перебегающего дорогу."]
    ],
    "short": [
        ["She is short for her age.", "Она невысокого роста для своего возраста."],
        ["He will cut his hair short.", "Он подстрижет волосы коротко."],
        ["They took a short break.", "Они сделали короткий перерыв."]
    ],
    "numeral": [
        ["She learned Roman numerals in school.", "Она изучала римские цифры в школе."],
        ["He will write the numeral in digits.", "Он напишет цифру цифрами."],
        ["They practiced converting numerals.", "Они тренировались в преобразовании цифр."]
    ],
    "class": [
        ["She is in the math class.", "Она учится в математическом классе."],
        ["He will teach a cooking class.", "Он будет вести урок по кулинарии."],
        ["They attend the same class.", "Они посещают один и тот же класс."]
    ],
    "wind": [
        ["She felt the wind in her hair.", "Она почувствовала ветер в своих волосах."],
        ["He will wind the clock.", "Он будет заводить часы."],
        ["They heard the wind howling outside.", "Они слышали, как ветер завывал на улице."]
    ],
    "question": [
        ["She asked a question.", "Она задала вопрос."],
        ["He will answer the question.", "Он ответит на вопрос."],
        ["They discussed the question in detail.", "Они обсудили вопрос подробно."]
    ],
    "happen": [
        ["She wondered what would happen next.", "Она задавалась вопросом, что произойдет дальше."],
        ["He will make it happen.", "Он сделает так, чтобы это произошло."],
        ["They saw it happen before their eyes.", "Они видели, как это произошло перед их глазами."]
    ],
    "complete": [
        ["She completed the task on time.", "Она завершила задачу вовремя."],
        ["He will complete the form.", "Он заполнит форму."],
        ["They achieved complete success.", "Они достигли полного успеха."]
    ],
    "ship": [
        ["She received a package by ship.", "Она получила посылку по морю."],
        ["He will ship the order tomorrow.", "Он отправит заказ завтра."],
        ["They tracked the ship's progress online.", "Они отслеживали прогресс корабля онлайн."]
    ],
    "area": [
        ["She explored the area.", "Она исследовала район."],
        ["He will measure the area.", "Он измерит площадь."],
        ["They live in a rural area.", "Они живут в сельской местности."]
    ],
    "half": [
        ["She ate half the cake.", "Она съела половину торта."],
        ["He will finish in half an hour.", "Он закончит через полчаса."],
        ["They split the bill in half.", "Они поделили счет пополам."]
    ],
    "rock": [
        ["She climbed the rock.", "Она взобралась на скалу."],
        ["He will skip the rock across the water.", "Он будет кидать камень через воду."],
        ["They found fossils in the rock.", "Они нашли ископаемые в скале."]
    ],
    "order": [
        ["She placed an order for pizza.", "Она сделала заказ на пиццу."],
        ["He will order from the menu.", "Он закажет по меню."],
        ["They received their order promptly.", "Они получили свой заказ быстро."]
    ],
    "fire": [
        ["She built a fire to keep warm.", "Она разожгла огонь, чтобы согреться."],
        ["He will light the fire.", "Он зажжет огонь."],
        ["They roasted marshmallows over the fire.", "Они жарили зефир над огнем."]
    ],
    "south": [
        ["She traveled south for the winter.", "Она поехала на юг на зиму."],
        ["He will move south for a job.", "Он переедет на юг ради работы."],
        ["They have a house in the south of France.", "У них есть дом на юге Франции."]
    ],
    "problem": [
        ["She solved the math problem.", "Она решила математическую задачу."],
        ["He will fix the problem.", "Он исправит проблему."],
        ["They encountered a problem with the software.", "У них возникла проблема с программным обеспечением."]
    ],
    "piece": [
        ["She cut a piece of cake.", "Она отрезала кусок торта."],
        ["He will play a piece of music.", "Он сыграет музыкальное произведение."],
        ["They put together a puzzle piece.", "Они соединили часть головоломки."]
    ],
    "told": [
        ["She told her friend a secret.", "Она рассказала своей подруге секрет."],
        ["He will tell the truth.", "Он скажет правду."],
        ["They told stories around the campfire.", "Они рассказывали истории у костра."]
    ],
    "knew": [
        ["She knew the answer.", "Она знала ответ."],
        ["He will knew what to do.", "Он знал, что делать."],
        ["They knew each other from childhood.", "Они знали друг друга с детства."]
    ],
    "pass": [
        ["She watched the cars pass by.", "Она наблюдала, как машины проходят мимо."],
        ["He will pass the test.", "Он сдаст экзамен."],
        ["They let him pass through the gate.", "Они пустили его через ворота."]
    ],
    "since": [
        ["She has been waiting since morning.", "Она ждет с утра."],
        ["He will stay here since he likes it.", "Он останется здесь, так как ему здесь нравится."],
        ["They have known each other since childhood.", "Они знают друг друга с детства."]
    ],
    "top": [
        ["She reached the top of the mountain.", "Она достигла вершины горы."],
        ["He will put the cherry on top.", "Он поставит вишенку на торте."],
        ["They live at the top of the building.", "Они живут на верхнем этаже здания."]
    ],
    "whole": [
        ["She ate the whole cake.", "Она съела весь торт."],
        ["He will spend the whole day here.", "Он проведет здесь весь день."],
        ["They completed the whole project.", "Они завершили весь проект."]
    ],
    "king": [
        ["She dressed as a king for Halloween.", "Она оделась в короля на Хэллоуин."],
        ["He will crown the new king.", "Он коронует нового короля."],
        ["They admired the courage of the king.", "Они восхищались храбростью короля."]
    ],
    "space": [
        ["She gazed at the stars in the night space.", "Она смотрела на звезды в ночном космосе."],
        ["He will explore outer space one day.", "Он однажды исследует внешний космос."],
        ["They learned about space travel in school.", "Они учились о космических полетах в школе."]
    ],
    "heard": [
        ["She heard a strange noise in the attic.", "Она услышала странный шум на чердаке."],
        ["He will make sure his voice is heard.", "Он убедится, что его голос будет услышан."],
        ["They heard the news on the radio.", "Они услышали новости по радио."]
    ],
    "best": [
        ["She did her best on the test.", "Она сделала все возможное на экзамене."],
        ["He will choose the best option.", "Он выберет лучший вариант."],
        ["They had the best time of their lives.", "Они провели лучшее время своей жизни."]
    ],
    "hour": [
        ["She waited for an hour.", "Она ждала час."],
        ["He will arrive in an hour.", "Он прибудет через час."],
        ["They spent an hour discussing the problem.", "Они потратили час на обсуждение проблемы."]
    ],
    "better": [
        ["She felt better after resting.", "Ей стало лучше после отдыха."],
        ["He will do better next time.", "В следующий раз он сделает лучше."],
        ["They found a better solution.", "Они нашли лучшее решение."]
    ],
    "true": [
        ["She spoke nothing but the true.", "Она говорила только правду."],
        ["He will always stay true to his values.", "Он всегда будет верен своим принципам."],
        ["They discovered the true meaning of friendship.", "Они открыли истинный смысл дружбы."]
    ],
    "during": [
        ["She fell asleep during the movie.", "Она заснула во время фильма."],
        ["He will take notes during the lecture.", "Он будет делать записи во время лекции."],
        ["They met during their college years.", "Они встретились во время учебы в колледже."]
    ],
    "hundred": [
        ["She counted to a hundred.", "Она считала до ста."],
        ["He will run a hundred miles.", "Он пробежит сто миль."],
        ["They sold a hundred tickets for the concert.", "Они продали сто билетов на концерт."]
    ],
    "five": [
        ["She has five siblings.", "У нее пять братьев и сестер."],
        ["He will arrive in five minutes.", "Он прибудет через пять минут."],
        ["They celebrated five years of marriage.", "Они отметили пять лет брака."]
    ],
    "remember": [
        ["She tried to remember the lyrics.", "Она пыталась вспомнить текст песни."],
        ["He will always remember this moment.", "Он всегда будет помнить этот момент."],
        ["They remembered their childhood adventures.", "Они вспомнили свои детские приключения."]
    ],
    "step": [
        ["She took a step forward.", "Она сделала шаг вперед."],
        ["He will follow in his father's step.", "Он пойдет по стопам своего отца."],
        ["They climbed the steps to the temple.", "Они поднимались по ступеням к храму."]
    ],
    "early": [
        ["She woke up early to watch the sunrise.", "Она проснулась рано, чтобы посмотреть на восход солнца."],
        ["He will arrive early for the meeting.", "Он прибудет рано на встречу."],
        ["They started their day early.", "Они начали свой день рано."]
    ],
    "hold": [
        ["She asked him to hold her hand.", "Она попросила его взять ее за руку."],
        ["He will hold the door open.", "Он будет держать дверь открытой."],
        ["They held a meeting to discuss the issue.", "Они провели совещание, чтобы обсудить проблему."]
    ],
    "west": [
        ["She traveled west to see the ocean.", "Она поехала на запад, чтобы увидеть океан."],
        ["He will move out west for a job.", "Он переедет на запад ради работы."],
        ["They watched the sun set in the west.", "Они наблюдали, как солнце заходит на западе."]
    ],
    "ground": [
        ["She found a coin on the ground.", "Она нашла монету на земле."],
        ["He will break new ground with his research.", "Он разорвет новые горизонты в своих исследованиях."],
        ["They walked on the soft ground of the forest.", "Они шли по мягкой почве леса."]
    ],
    "interest": [
        ["She developed an interest in painting.", "У нее появился интерес к живописи."],
        ["He will pursue his interests.", "Он будет развивать свои интересы."],
        ["They discussed common interests.", "Они обсудили общие интересы."]
    ],
    "reach": [
        ["She reached for the stars.", "Она стремилась к звездам."],
        ["He will reach his destination by noon.", "Он доберется до места назначения к полудню."],
        ["They reached a compromise.", "Они достигли компромисса."]
    ],
    "fast": [
        ["She ran fast to catch the bus.", "Она быстро побежала, чтобы успеть на автобус."],
        ["He will fast for twenty-four hours.", "Он будет поститься сутки."],
        ["They were moving too fast.", "Они двигались слишком быстро."]
    ],
    "verb": [
        ["She identified the verb in the sentence.", "Она определила глагол в предложении."],
        ["He will conjugate the verb correctly.", "Он спрягет глагол правильно."],
        ["They learned about action verbs.", "Они учились о действительных глаголах."]
    ],
    "sing": [
        ["She likes to sing in the shower.", "Она любит петь в душе."],
        ["He will sing at the concert.", "Он выступит на концерте."],
        ["They sang their favorite song together.", "Они спели свою любимую песню вместе."]
    ],
    "listen": [
        ["She listened to the birds chirping.", "Она слушала, как птицы щебечут."],
        ["He will listen to the advice.", "Он выслушает совет."],
        ["They listened to classical music.", "Они слушали классическую музыку."]
    ],
    "six": [
        ["She turned six last week.", "На прошлой неделе ей исполнилось шесть лет."],
        ["He will leave at six o'clock.", "Он уйдет в шесть часов."],
        ["They divided the pizza into six slices.", "Они разделили пиццу на шесть кусков."]
    ],
    "table": [
        ["She set the table for dinner.", "Она накрыла стол для ужина."],
        ["He will reserve a table at the restaurant.", "Он зарезервирует столик в ресторане."],
        ["They sat around the table and talked.", "Они сели вокруг стола и поговорили."]
    ],
    "travel": [
        ["She loves to travel to new places.", "Она любит путешествовать в новые места."],
        ["He will travel around the world.", "Он объедет весь мир."],
        ["They traveled by train.", "Они путешествовали на поезде."]
    ],
    "less": [
        ["She ate less sugar.", "Она ела меньше сахара."],
        ["He will spend less money.", "Он потратит меньше денег."],
        ["They had less time than expected.", "У них было меньше времени, чем ожидалось."]
    ],
    "morning": [
        ["She enjoys a cup of coffee in the morning.", "Она наслаждается чашкой кофе по утрам."],
        ["He will go for a run in the morning.", "Он пойдет побегать утром."],
        ["They met early in the morning.", "Они встретились рано утром."]
    ],
    "ten": [
        ["She has ten fingers.", "У нее десять пальцев."],
        ["He will be back in ten minutes.", "Он вернется через десять минут."],
        ["They scored ten points in the game.", "Они набрали десять очков в игре."]
    ],
    "simple": [
        ["She prefers simple solutions.", "Она предпочитает простые решения."],
        ["He will explain it in simple terms.", "Он объяснит это простыми словами."],
        ["They followed a simple recipe.", "Они следовали простому рецепту."]
    ],
    "several": [
        ["She met with several friends.", "Она встретилась с несколькими друзьями."],
        ["He will take several books with him.", "Он возьмет с собой несколько книг."],
        ["They discussed several options.", "Они обсудили несколько вариантов."]
    ],
    "vowel": [
        ["She identified the vowel in the word.", "Она определила гласную букву в слове."],
        ["He will teach the children about vowels.", "Он научит детей гласным буквам."],
        ["They practiced pronouncing vowel sounds.", "Они тренировались в произношении гласных звуков."]
    ],
    "toward": [
        ["She walked toward the sunset.", "Она шла к закату."],
        ["He will take steps toward his goal.", "Он сделает шаги к своей цели."],
        ["They sailed toward the horizon.", "Они плыли к горизонту."]
    ],
    "war": [
        ["She studied the history of war.", "Она изучала историю войн."],
        ["He will fight in the war.", "Он будет сражаться в войне."],
        ["They lived through the horrors of war.", "Они пережили ужасы войны."]
    ],
    "lay": [
        ["She watched the hen lay eggs.", "Она наблюдала, как курица несет яйца."],
        ["He will lay the groundwork for the project.", "Он заложит основу для проекта."],
        ["They lay down on the grass to rest.", "Они легли на траву, чтобы отдохнуть."]
    ],
    "against": [
        ["She leaned against the wall.", "Она прислонилась к стене."],
        ["He will defend against the attack.", "Он защитится от нападения."],
        ["They stood united against injustice.", "Они стояли единым фронтом против несправедливости."]
    ],
    "pattern": [
        ["She noticed a pattern in the behavior.", "Она заметила закономерность в поведении."],
        ["He will follow a pattern.", "Он пойдет по образцу."],
        ["They recognized the pattern of the design.", "Они узнали узор дизайна."]
    ],
    "slow": [
        ["She walked at a slow pace.", "Она шла медленным шагом."],
        ["He will take the slow route.", "Он выберет медленный путь."],
        ["They enjoyed a slow evening.", "Они наслаждались медленным вечером."]
    ],
    "center": [
        ["She found peace in the center of the garden.", "Она нашла покой в центре сада."],
        ["He will place the vase in the center of the table.", "Он поставит вазу в центре стола."],
        ["They gathered in the center of town.", "Они собрались в центре города."]
    ],
    "love": [
        ["She confessed her love for him.", "Она призналась в любви к нему."],
        ["He will always love her.", "Он всегда будет любить ее."],
        ["They shared a love of music.", "У них была общая любовь к музыке."]
    ],
    "person": [
        ["She is a kind person.", "Она добрый человек."],
        ["He will talk to the person in charge.", "Он поговорит с ответственным человеком."],
        ["They saw a suspicious person lurking around.", "Они увидели подозрительного человека, бродящего вокруг."]
    ],
    "money": [
        ["She saved money for a rainy day.", "Она копила деньги на черный день."],
        ["He will invest his money wisely.", "Он разумно вложит свои деньги."],
        ["They pooled their money to buy a gift.", "Они объединили свои средства, чтобы купить подарок."]
    ],
    "serve": [
        ["She likes to serve others.", "Она любит служить другим."],
        ["He will serve his country.", "Он будет служить своей стране."],
        ["They hired a butler to serve at the party.", "Они наняли дворецкого, чтобы обслуживать на вечеринке."]
    ],
    "appear": [
        ["She made it appear effortless.", "Она сделала так, чтобы это выглядело легко."],
        ["He will appear on television.", "Он выступит по телевидению."],
        ["They watched the magician make a rabbit appear.", "Они смотрели, как фокусник заставлял кролика появляться."]
    ],
    "road": [
        ["She walked down the winding road.", "Она шла по извилистой дороге."],
        ["He will take the scenic road.", "Он выберет живописную дорогу."],
        ["They drove on the dirt road.", "Они ехали по грунтовой дороге."]
    ],
    "map": [
        ["She studied the map of the city.", "Она изучала карту города."],
        ["He will draw a map of the route.", "Он нарисует карту маршрута."],
        ["They used a map to navigate through the forest.", "Они использовали карту для ориентации в лесу."]
    ],
    "rain": [
        ["She danced in the rain.", "Она танцевала под дождем."],
        ["He will bring an umbrella in case of rain.", "Он возьмет зонтик на случай дождя."],
        ["They watched the rain pour down from the sky.", "Они смотрели, как дождь ливнем обрушивался с неба."]
    ],
    "rule": [
        ["She followed the rule of law.", "Она следовала правилам закона."],
        ["He will enforce the rule.", "Он будет соблюдать правило."],
        ["They broke the rule and suffered the consequences.", "Они нарушили правило и понесли последствия."]
    ],
    "govern": [
        ["She governed with compassion.", "Она управляла с состраданием."],
        ["He will govern fairly.", "Он будет правильно управлять."],
        ["They believed in self-governance.", "Они верили в самоуправление."]
    ],
    "pull": [
        ["She tried to pull the door open.", "Она попыталась открыть дверь, потянув за нее."],
        ["He will pull the lever to start the engine.", "Он потянет за рычаг, чтобы запустить двигатель."],
        ["They had to pull the car out of the mud.", "Им пришлось вытащить машину из грязи."]
    ],
    "cold": [
        ["She shivered in the cold wind.", "Она дрожала от холодного ветра."],
        ["He will wear a coat in the cold weather.", "Он наденет пальто в холодную погоду."],
        ["They caught a cold from being outside too long.",
         "Они простудились от того, что провели слишком много времени на улице."]
    ],
    "notice": [
        ["She didn't notice the sign.", "Она не заметила знак."],
        ["He will notice the changes.", "Он заметит изменения."],
        ["They noticed a strange sound coming from the attic.", "Они заметили странный звук, идущий с чердака."]
    ],
    "voice": [
        ["She recognized his voice.", "Она узнала его голос."],
        ["He will raise his voice to be heard.", "Он повысит голос, чтобы быть услышанным."],
        ["They listened to the soothing voice on the meditation tape.",
         "Они слушали успокаивающий голос на медитационной записи."]
    ],
    "unit": [
        ["She measured the length in units of meters.", "Она измерила длину в метрах."],
        ["He will assemble the unit himself.", "Он соберет блок самостоятельно."],
        ["They live in a housing unit.", "Они живут в жилом блоке."]
    ],
    "power": [
        ["She felt the power of the storm.", "Она почувствовала мощь бури."],
        ["He will harness the power of the sun.", "Он освоит энергию солнца."],
        ["They used the power of persuasion to convince him.", "Они использовали силу убеждения, чтобы убедить его."]
    ],
    "town": [
        ["She grew up in a small town.", "Она выросла в небольшом городе."],
        ["He will visit the town square.", "Он посетит городскую площадь."],
        ["They explored the historic town.", "Они изучили исторический город."]
    ],
    "fine": [
        ["She paid the fine for parking illegally.", "Она заплатила штраф за неправильную парковку."],
        ["He will be just fine.", "Он будет в порядке."],
        ["They enjoyed a fine meal at the restaurant.", "Они насладились прекрасным ужином в ресторане."]
    ],
    "certain": [
        ["She was certain of her decision.", "Она была уверена в своем решении."],
        ["He will make certain to double-check the details.", "Он убедится, что проверит детали дважды."],
        ["They were certain they had the right answer.", "Они были уверены, что знают правильный ответ."]
    ],
    "fly": [
        ["She watched the birds fly overhead.", "Она смотрела, как птицы летали над головой."],
        ["He will fly to Europe for vacation.", "Он полетит в Европу на отпуск."],
        ["They couldn't fly kites in the rainy weather.", "Они не могли запустить воздушного змея в дождливую погоду."]
    ],
    "fall": [
        ["She slipped and fell on the ice.", "Она поскользнулась и упала на лед."],
        ["He will fall asleep reading a book.", "Он заснет, читая книгу."],
        ["They watched the leaves fall from the trees.", "Они наблюдали, как листья падают с деревьев."]
    ],
    "lead": [
        ["She will lead the team to victory.", "Она приведет команду к победе."],
        ["He will lead the discussion.", "Он будет вести обсуждение."],
        ["They followed the lead of their teacher.", "Они следовали примеру своего учителя."]
    ],
    "cry": [
        ["She felt like she wanted to cry.", "Ей захотелось заплакать."],
        ["He will cry tears of joy.", "Он прольет слезы радости."],
        ["They heard the baby cry in the night.", "Они слышали, как младенец плакал ночью."]
    ],
    "dark": [
        ["She was afraid of the dark.", "Она боялась темноты."],
        ["He will paint the room a dark color.", "Он покрасит комнату темным цветом."],
        ["They couldn't see in the dark room.", "Они не могли видеть в темной комнате."]
    ],
    "machine": [
        ["She operated the machine with skill.", "Она управляла машиной искусно."],
        ["He will repair the machine.", "Он починит машину."],
        ["They used the machine to make copies.", "Они использовали машину для копирования."]
    ],
    "note": [
        ["She wrote a note to remind herself.", "Она написала записку, чтобы напомнить себе."],
        ["He will take note of the details.", "Он обратит внимание на детали."],
        ["They left a note for the neighbors.", "Они оставили записку соседям."]
    ],
    "wait": [
        ["She had to wait in line.", "Ей пришлось подождать в очереди."],
        ["He will wait for her to finish.", "Он подождет, пока она закончит."],
        ["They couldn't wait to open their presents.", "Они не могли дождаться, чтобы открыть подарки."]
    ],
    "plan": [
        ["She made a plan for the weekend.", "Она составила план на выходные."],
        ["He will plan the itinerary for the trip.", "Он разработает маршрут поездки."],
        ["They followed the plan carefully.", "Они внимательно следовали плану."]
    ],
    "figure": [
        ["She couldn't figure out the puzzle.", "Она не могла разгадать головоломку."],
        ["He will figure prominently in the meeting.", "Он будет играть важную роль на совещании."],
        ["They worked together to figure the problem out.", "Они вместе решали проблему."]
    ],
    "star": [
        ["She wished upon a star.", "Она загадала желание на звезду."],
        ["He will star in the school play.", "Он сыграет главную роль в школьной постановке."],
        ["They gazed at the stars in wonder.", "Они смотрели на звезды с удивлением."]
    ],
    "box": [
        ["She packed her belongings in a box.", "Она упаковала свои вещи в коробку."],
        ["He will think outside the box.", "Он будет думать нестандартно."],
        ["They received a package in the mail.", "Они получили посылку по почте."]
    ],
    "noun": [
        ["She learned about nouns in grammar class.", "Она училась о существительных на уроке грамматики."],
        ["He will identify the noun in the sentence.", "Он определит существительное в предложении."],
        ["They practiced writing sentences with nouns.", "Они тренировались писать предложения с существительными."]
    ],
    "field": [
        ["She ran across the field.", "Она побежала через поле."],
        ["He will work in the field of medicine.", "Он будет работать в медицинской сфере."],
        ["They played soccer in the open field.", "Они играли в футбол на открытом поле."]
    ],
    "rest": [
        ["She needed to rest after a long day.", "Ей нужно было отдохнуть после долгого дня."],
        ["He will take a rest break.", "Он сделает перерыв на отдых."],
        ["They found rest in the peaceful surroundings.", "Они нашли покой в мирной обстановке."]
    ],
    "correct": [
        ["She corrected her mistake.", "Она исправила свою ошибку."],
        ["He will provide the correct answer.", "Он даст правильный ответ."],
        ["They reviewed the correct procedure.", "Они пересмотрели правильную процедуру."]
    ],
    "able": [
        ["She was able to solve the problem.", "Она смогла решить проблему."],
        ["He will be able to attend the meeting.", "Он сможет присутствовать на совещании."],
        ["They were able to finish the project on time.", "Они смогли закончить проект вовремя."]
    ],
    "pound": [
        ["She heard the pound of footsteps.", "Она услышала гул шагов."],
        ["He will pound the nail into the wood.", "Он забьет гвоздь в дерево."],
        ["They measured the flour in pounds.", "Они измерили муку в фунтах."]
    ],
    "done": [
        ["She was done with her homework.", "Она закончила свою домашнюю работу."],
        ["He will be done with the project by Friday.", "Он закончит проект к пятнице."],
        ["They were finally done moving into the new house.", "Они наконец закончили переезд в новый дом."]
    ],
    "beauty": [
        ["She admired the beauty of the sunset.", "Она восхищалась красотой заката."],
        ["He will capture the beauty of nature in his painting.", "Он запечатлит красоту природы на своей картине."],
        ["They appreciated the beauty of the artwork.", "Они оценили красоту произведения искусства."]
    ],
    "drive": [
        ["She learned to drive a car.", "Она научилась водить машину."],
        ["He will drive to the airport.", "Он поедет на машине в аэропорт."],
        ["They enjoyed a scenic drive through the countryside.",
         "Они наслаждались живописной поездкой по сельской местности."]
    ],
    "stood": [
        ["She stood in line at the grocery store.", "Она стояла в очереди в продуктовом магазине."],
        ["He will stood up for what he believed in.", "Он встанет на защиту своих убеждений."],
        ["They stood together against injustice.", "Они стояли вместе против несправедливости."]
    ],
    "contain": [
        ["She opened the box to see what it contained.", "Она открыла коробку, чтобы увидеть, что в ней содержится."],
        ["He will contain his anger.", "Он сдержит свой гнев."],
        ["They labeled the jars to indicate what they contain.",
         "Они пометили банки, чтобы показать, что они содержат."]
    ],
    "front": [
        ["She sat in the front row.", "Она сидела в первом ряду."],
        ["He will lead from the front.", "Он будет вести с переди."],
        ["They stood at the front of the crowd.", "Они стояли впереди толпы."]
    ],
    "teach": [
        ["She wanted to teach English overseas.", "Она хотела преподавать английский за границей."],
        ["He will teach the class how to solve equations.", "Он научит класс, как решать уравнения."],
        ["They learned valuable lessons from their parents.", "Они получили ценные уроки от своих родителей."]
    ],
    "week": [
        ["She planned her schedule for the week.", "Она спланировала свое расписание на неделю."],
        ["He will spend the week at the beach.", "Он проведет неделю на пляже."],
        ["They worked hard all week.", "Они работали усердно всю неделю."]
    ],
    "final": [
        ["She made the final decision.", "Она приняла окончательное решение."],
        ["He will take the final exam next week.", "Он сдаст экзамен на следующей неделе."],
        ["They reached the final chapter of the book.", "Они добрались до последней главы книги."]
    ],
    "gave": [
        ["She gave her friend a gift.", "Она подарила своему другу подарок."],
        ["He will gave his seat to the elderly woman.", "Он уступит свое место пожилой женщине."],
        ["They gave generously to the charity.", "Они щедро отдали на благотворительность."]
    ],
    "green": [
        ["She planted green beans in the garden.", "Она посадила зеленые бобы в саду."],
        ["He will paint the walls green.", "Он покрасит стены зеленым цветом."],
        ["They enjoyed the green scenery on their hike.", "Они наслаждались зеленой природой во время похода."]
    ],
    "oh": [
        ["She exclaimed, 'Oh, I see!'", "Она воскликнула: 'О, поняла!'"],
        ["He will say, 'Oh, no!'", "Он скажет: 'О, нет!'"],
        ["They sighed and said, 'Oh, well.'", "Они вздохнули и сказали: 'О, ну и ладно.'"]
    ],
    "quick": [
        ["She made a quick decision.", "Она приняла быстрое решение."],
        ["He will take a quick shower.", "Он быстро примет душ."],
        ["They enjoyed a quick snack before the movie.", "Они насладились быстрым перекусом перед фильмом."]
    ],
    "develop": [
        ["She wanted to develop her photography skills.", "Она хотела развить свои навыки фотографии."],
        ["He will develop a plan for the project.", "Он разработает план проекта."],
        ["They watched the city develop over time.", "Они наблюдали, как город развивался со временем."]
    ],
    "ocean": [
        ["She dreamed of sailing across the ocean.", "Она мечтала переплыть океан на паруснике."],
        ["He will scuba dive in the ocean.", "Он погрузится с аквалангом в океан."],
        ["They walked along the ocean shore.", "Они гуляли по берегу океана."]
    ],
    "warm": [
        ["She wrapped herself in a warm blanket.", "Она завернулась в теплый плед."],
        ["He will warm his hands by the fire.", "Он разогреет свои руки у огня."],
        ["They enjoyed the warm sunshine.", "Они наслаждались теплыми солнечными лучами."]
    ],
    "free": [
        ["She felt free when she danced.", "Она чувствовала себя свободной, когда танцевала."],
        ["He will set the bird free.", "Он выпустит птицу на волю."],
        ["They received free samples at the store.", "Они получили бесплатные образцы в магазине."]
    ],
    "minute": [
        ["She waited for him for a minute.", "Она подождала его минуту."],
        ["He will take a minute to think.", "Он выделит минуту на раздумья."],
        ["They arrived at the last minute.", "Они прибыли в последнюю минуту."]
    ],
    "strong": [
        ["She felt strong after exercising.", "Она почувствовала себя сильной после упражнений."],
        ["He will be a strong leader.", "Он будет сильным лидером."],
        ["They formed a strong bond over time.", "Они сформировали крепкую связь со временем."]
    ],
    "special": [
        ["She received a special gift for her birthday.", "Она получила особый подарок на свой день рождения."],
        ["He will reserve a special table at the restaurant.", "Он зарезервирует особый стол в ресторане."],
        ["They shared a special moment together.", "Они разделили особый момент вместе."]
    ],
    "mind": [
        ["She couldn't get him out of her mind.", "Она не могла выкинуть его из головы."],
        ["He will make up his mind by tomorrow.", "Он примет решение к завтрашнему дню."],
        ["They had a meeting of the minds.", "У них было совещание умов."]
    ],
    "behind": [
        ["She left her keys behind.", "Она оставила свои ключи позади."],
        ["He will lag behind if he doesn't hurry.", "Он будет отстает, если не поторопится."],
        ["They found treasure hidden behind the wall.", "Они нашли сокровище, спрятанное за стеной."]
    ],
    "clear": [
        ["She had a clear view of the mountains.", "У нее был открытый вид на горы."],
        ["He will make his intentions clear.", "Он прояснит свои намерения."],
        ["They reached a clear consensus.", "Они достигли четкого консенсуса."]
    ],
    "tail": [
        ["She held onto the dog's tail.", "Она держалась за хвост собаки."],
        ["He will tail the suspect.", "Он будет следить за подозреваемым."],
        ["They saw a squirrel with a bushy tail.", "Они увидели белку с пушистым хвостом."]
    ],
    "produce": [
        ["She will produce a report by the deadline.", "Она подготовит отчет к дедлайну."],
        ["He will produce a play at the theater.", "Он поставит пьесу в театре."],
        ["They grow and produce their own vegetables.", "Они выращивают и производят свои овощи."]
    ],
    "fact": [
        ["She presented the facts of the case.", "Она представила факты дела."],
        ["He will verify the fact with a reliable source.", "Он проверит факт у надежного источника."],
        ["They learned interesting facts about dinosaurs.", "Они узнали интересные факты о динозаврах."]
    ],
    "street": [
        ["She walked down the street.", "Она прошла по улице."],
        ["He will park on the street.", "Он припаркуется на улице."],
        ["They lived on the same street.", "Они жили на одной и той же улице."]
    ],
    "inch": [
        ["She measured the board in inches.", "Она измерила доску в дюймах."],
        ["He will inch closer to the edge.", "Он приблизится к краю на дюйм."],
        ["They moved an inch at a time.", "Они двигались по дюйму за раз."]
    ],
    "multiply": [
        ["She needs to multiply the ingredients for more servings.",
         "Ей нужно умножить ингредиенты для большего количества порций."],
        ["He will multiply his efforts to finish the project on time.",
         "Он усилит свои усилия, чтобы закончить проект вовремя."],
        ["They learned how to multiply numbers in math class.", "Они узнали, как умножать числа на уроке математики."]
    ],
    "nothing": [
        ["She found nothing in the box.", "Она не нашла ничего в коробке."],
        ["He will stop at nothing to achieve his goal.", "Он не остановится ни перед чем, чтобы достичь своей цели."],
        ["They had nothing to do on a rainy day.", "У них не было ничего делать в дождливый день."]
    ],
    "course": [
        ["She changed her course of action.", "Она изменила свою линию поведения."],
        ["He will take a course in computer programming.", "Он пройдет курс по компьютерному программированию."],
        ["They plotted a course on the map.", "Они нанесли маршрут на карте."]
    ],
    "stay": [
        ["She decided to stay home instead.", "Она решила остаться дома вместо этого."],
        ["He will stay in a hotel downtown.", "Он остановится в гостинице в центре города."],
        ["They planned to stay for the weekend.", "Они планировали остаться на выходные."]
    ],
    "wheel": [
        ["She turned the wheel to the left.", "Она повернула руль налево."],
        ["He will spin the wheel of fortune.", "Он будет крутить колесо фортуны."],
        ["They rode bicycles with training wheels.", "Они катались на велосипедах с дополнительными колесами."]
    ],
    "full": [
        ["She felt full after the big meal.", "Она почувствовала себя сытой после большого ужина."],
        ["He will give his full attention to the speaker.", "Он уделяет полное внимание докладчику."],
        ["They had a full schedule for the day.", "У них было полное расписание на день."]
    ],
    "force": [
        ["She used force to open the door.", "Она использовала силу, чтобы открыть дверь."],
        ["He will apply force to move the heavy object.", "Он приложит усилие, чтобы переместить тяжелый объект."],
        ["They faced a powerful force of nature.", "Они столкнулись с могущественной силой природы."]
    ],
    "blue": [
        ["She painted the sky blue.", "Она покрасила небо в голубой цвет."],
        ["He will wear a blue shirt to the party.", "Он наденет голубую рубашку на вечеринку."],
        ["They admired the deep blue of the ocean.", "Они восхищались глубоким синим цветом океана."]
    ],
    "object": [
        ["She found a mysterious object in the attic.", "Она нашла загадочный объект на чердаке."],
        ["He will object to the proposal at the meeting.", "Он возразит против предложения на совещании."],
        ["They analyzed the object under a microscope.", "Они проанализировали объект под микроскопом."]
    ],
    "decide": [
        ["She couldn't decide between the two options.", "Она не могла решить между двумя вариантами."],
        ["He will decide on a course of action.", "Он выберет линию поведения."],
        ["They need to decide quickly.", "Им нужно быстро принять решение."]
    ],
    "surface": [
        ["She wiped the surface of the table.", "Она вытерла поверхность стола."],
        ["He will explore the surface of Mars.", "Он исследует поверхность Марса."],
        ["They discovered a hidden city beneath the surface.", "Они обнаружили скрытый город под поверхностью."]
    ],
    "deep": [
        ["She swam in the deep end of the pool.", "Она плавала в глубоком конце бассейна."],
        ["He will dive deep to find the treasure.", "Он погрузится глубоко, чтобы найти сокровище."],
        ["They delved deep into the mystery.", "Они погрузились глубоко в тайну."]
    ],
    "moon": [
        ["She admired the full moon.", "Она восхищалась полной луной."],
        ["He will study the phases of the moon.", "Он изучит фазы луны."],
        ["They watched the moon rise over the horizon.", "Они наблюдали, как луна взошла над горизонтом."]
    ],
    "island": [
        ["She dreamed of living on a tropical island.", "Она мечтала жить на тропическом острове."],
        ["He will explore the deserted island.", "Он исследует пустынный остров."],
        ["They visited an island in the Caribbean.", "Они посетили остров в Карибском море."]
    ],
    "foot": [
        ["She injured her foot while hiking.", "Она травмировала ногу во время похода."],
        ["He will measure the room in square feet.", "Он измерит комнату в квадратных футах."],
        ["They walked barefoot on the sand.", "Они гуляли босиком по песку."]
    ],
    "system": [
        ["She installed a new operating system on her computer.",
         "Она установила новую операционную систему на свой компьютер."],
        ["He will design a new system for tracking expenses.", "Он разработает новую систему учета расходов."],
        ["They studied the solar system in science class.", "Они изучали солнечную систему на уроке науки."]
    ],
    "busy": [
        ["She was too busy to attend the meeting.", "У нее было слишком много дел, чтобы присутствовать на совещании."],
        ["He will be busy with work all day.", "Он будет занят работой весь день."],
        ["They had a busy schedule ahead.", "У них было насыщенное расписание на следующий день."]
    ],
    "test": [
        ["She studied hard for the test.", "Она усердно готовилась к тесту."],
        ["He will take the test next week.", "Он сдаст экзамен на следующей неделе."],
        ["They reviewed the test results.", "Они пересмотрели результаты теста."]
    ],
    "record": [
        ["She broke the record for the fastest mile.", "Она побила рекорд по быстрому милю."],
        ["He will set a new record for sales.", "Он установит новый рекорд продаж."],
        ["They listened to the record on the turntable.", "Они слушали пластинку на проигрывателе."]
    ],
    "boat": [
        ["She went fishing in a small boat.", "Она пошла на рыбалку на маленькой лодке."],
        ["He will rent a boat for the weekend.", "Он снимет лодку на выходные."],
        ["They sailed the boat across the lake.", "Они плыли на лодке через озеро."]
    ],
    "common": [
        ["She found common ground with her new colleague.", "Она нашла общий язык со своим новым коллегой."],
        ["He will use common sense to solve the problem.",
         "Он будет использовать здравый смысл, чтобы решить проблему."],
        ["They shared a common interest in photography.", "У них был общий интерес к фотографии."]
    ],
    "gold": [
        ["She discovered a vein of gold in the mountains.", "Она обнаружила золотую жилу в горах."],
        ["He will invest in gold for his retirement.", "Он вложит деньги в золото для своей пенсии."],
        ["They found buried treasure made of gold.", "Они нашли зарытое сокровище из золота."]
    ],
    "possible": [
        ["She thought winning was possible.", "Она думала, что победа возможна."],
        ["He will explore all possible options.", "Он рассмотрит все возможные варианты."],
        ["They faced every possible scenario.", "Они столкнулись с каждым возможным сценарием."]
    ],
    "plane": [
        ["She flew on a plane for the first time.", "Она впервые полетела на самолете."],
        ["He will travel by plane to the conference.", "Он поедет на конференцию на самолете."],
        ["They watched the plane take off.", "Они смотрели, как самолет взлетает."]
    ],
    "stead": [
        ["She stood stead against the wind.", "Она стояла неподвижно против ветра."],
        ["He will be stead in his decision.", "Он будет непоколебим в своем решении."],
        ["They walked stead through the storm.", "Они прошли через бурю непоколебимо."]
    ],
    "dry": [
        ["She hung the clothes out to dry.", "Она повесила белье, чтобы оно высохло."],
        ["He will dry the dishes with a towel.", "Он вытрет посуду полотенцем."],
        ["They enjoyed the dry weather.", "Они наслаждались сухой погодой."]
    ],
    "wonder": [
        ["She wondered about the meaning of life.", "Она задумывалась о смысле жизни."],
        ["He will wonder at the beauty of nature.", "Он будет восхищаться красотой природы."],
        ["They marveled at the wonder of the universe.", "Они удивлялись чудесам вселенной."]
    ],
    "laugh": [
        ["She laughed at his joke.", "Она посмеялась над его шуткой."],
        ["He will laugh when he hears the news.", "Он засмеется, когда услышит новости."],
        ["They shared a laugh over coffee.", "Они разделили смех за чашкой кофе."]
    ],
    "thousand": [
        ["She counted to a thousand.", "Она посчитала до тысячи."],
        ["He will travel a thousand miles.", "Он проедет тысячи миль."],
        ["They donated a thousand dollars to charity.", "Они пожертвовали тысячу долларов на благотворительность."]
    ],
    "ago": [
        ["She met him years ago.", "Она встретила его много лет назад."],
        ["He will finish the project days ago.", "Он закончит проект давно."],
        ["They visited the museum weeks ago.", "Они посетили музей несколько недель назад."]
    ],
    "ran": [
        ["She ran in the race.", "Она участвовала в забеге."],
        ["He will run for president.", "Он будет баллотироваться на должность президента."],
        ["They ran from danger.", "Они убежали от опасности."]
    ],
    "check": [
        ["She will check her email for updates.", "Она проверит свою электронную почту на наличие обновлений."],
        ["He will check the list one more time.", "Он проверит список еще раз."],
        ["They checked the ingredients for allergies.", "Они проверили ингредиенты на наличие аллергии."]
    ],
    "game": [
        ["She played a game of chess.", "Она сыграла партию шахмат."],
        ["He will watch the football game on TV.", "Он будет смотреть футбольный матч по телевизору."],
        ["They organized a game of charades.", "Они организовали игру в мимику."]
    ],
    "shape": [
        ["She cut the dough into the shape of hearts.", "Она вырезала тесто в форме сердец."],
        ["He will shape the clay into a vase.", "Он сделает из глины вазу."],
        ["They admired the shape of the mountains.", "Они восхищались формой гор."]
    ],
    "equate": [
        ["She will equate success with happiness.", "Она будет равнять успех с счастьем."],
        ["He will equate beauty with perfection.", "Он будет приравнивать красоту к совершенству."],
        ["They equate wealth with success.", "Они равняют богатство с успехом."]
    ],
    "hot": [
        ["She poured hot water into the teapot.", "Она налила горячую воду в заварочный чайник."],
        ["He will eat hot soup on a cold day.", "Он съест горячий суп в холодный день."],
        ["They felt hot after exercising.", "Они почувствовали себя горячими после упражнений."]
    ],
    "miss": [
        ["She will miss her train if she doesn't hurry.", "Она опоздает на поезд, если не поторопится."],
        ["He will miss his friends when he moves.", "Он будет скучать по своим друзьям, когда переедет."],
        ["They missed the opportunity to see the concert.", "Они упустили возможность посмотреть концерт."]
    ],
    "brought": [
        ["She brought snacks for the road trip.", "Она принесла закуски для поездки на дорогу."],
        ["He will brought a gift for the host.", "Он принесет подарок для хозяина."],
        ["They brought blankets for the picnic.", "Они принесли одеяла для пикника."]
    ],
    "heat": [
        ["She turned up the heat on the stove.", "Она повысила нагрев на плите."],
        ["He will feel the heat of the sun.", "Он почувствует жар солнца."],
        ["They endured the heat of the desert.", "Они выдержали жар пустыни."]
    ],
    "snow": [
        ["She watched the snow fall from the sky.", "Она смотрела, как снег падает с неба."],
        ["He will shovel the snow from the driveway.", "Он будет чистить снег с подъезда."],
        ["They played in the snow.", "Они играли в снегу."]
    ],
    "tire": [
        ["She will change the tire on her car.", "Она заменит шину на своей машине."],
        ["He will feel tired after the long day.", "Он будет уставший после долгого дня."],
        ["They need to buy new tires for the bike.", "Им нужно купить новые покрышки для велосипеда."]
    ],
    "bring": [
        ["She will bring a cake to the party.", "Она принесет торт на вечеринку."],
        ["He brought flowers for his girlfriend.", "Он принес цветы своей девушке."],
        ["They need to bring their passports.", "Им нужно принести свои паспорта."]
    ],
    "yes": [
        ["She nodded yes in agreement.", "Она кивнула головой в знак согласия."],
        ["He said yes to the proposal.", "Он сказал «да» на предложение."],
        ["They shouted yes when they won.", "Они закричали «да», когда выиграли."]
    ],
    "distant": [
        ["She gazed at the distant stars.", "Она глядела на далекие звезды."],
        ["He comes from a distant land.", "Он приходит из далекой страны."],
        ["They remembered distant memories.", "Они вспоминали далекие воспоминания."]
    ],
    "fill": [
        ["She will fill the glass with water.", "Она наполнит стакан водой."],
        ["He filled the room with laughter.", "Он наполнил комнату смехом."],
        ["They need to fill out the form.", "Им нужно заполнить форму."]
    ],
    "east": [
        ["She watched the sun rise in the east.", "Она наблюдала, как восходит солнце на востоке."],
        ["He lives in the east of the city.", "Он живет на востоке города."],
        ["They traveled east for their vacation.", "Они отправились на восток на каникулы."]
    ],
    "paint": [
        ["She will paint the walls blue.", "Она покрасит стены в синий цвет."],
        ["He painted a portrait of his wife.", "Он нарисовал портрет своей жены."],
        ["They used paint to decorate the room.", "Они использовали краску для украшения комнаты."]
    ],
    "language": [
        ["She speaks three languages fluently.", "Она свободно говорит на трех языках."],
        ["He studied the French language in school.", "Он изучал французский язык в школе."],
        ["They are learning a new language online.", "Они изучают новый язык онлайн."]
    ],
    "among": [
        ["She sat among her friends at the table.", "Она сидела среди своих друзей за столом."],
        ["He found himself among strangers.", "Он оказался среди незнакомцев."],
        ["They shared the food among themselves.", "Они поделили еду между собой."]
    ],
    "grand": [
        ["She inherited a grand estate from her grandfather.", "Она унаследовала великое имение от своего деда."],
        ["He planned a grand celebration for his birthday.",
         "Он запланировал великолепное празднование своего дня рождения."],
        ["They admired the grand architecture of the palace.", "Они восхищались величественной архитектурой дворца."]
    ],
    "ball": [
        ["She caught the ball with one hand.", "Она поймала мяч одной рукой."],
        ["He kicked the ball into the goal.", "Он ударил мяч в ворота."],
        ["They played ball in the park.", "Они играли в мяч на площадке."]
    ],
    "yet": [
        ["She hasn't finished her homework yet.", "Она еще не закончила свою домашнюю работу."],
        ["He hasn't decided where to go yet.", "Он еще не решил, куда пойти."],
        ["They haven't arrived yet.", "Они еще не прибыли."]
    ],
    "wave": [
        ["She waved goodbye from the window.", "Она помахала на прощание из окна."],
        ["He surfed on the wave.", "Он серфил на волне."],
        ["They watched the wave crash against the shore.", "Они смотрели, как волна разбивается о берег."]
    ],
    "drop": [
        ["She spilled a drop of milk.", "Она пролила каплю молока."],
        ["He felt a raindrop on his nose.", "Он почувствовал каплю дождя на своем носу."],
        ["They watched the water drop from the faucet.", "Они наблюдали, как вода капает из крана."]
    ],
    "heart": [
        ["She felt her heart race with excitement.", "Она чувствовала, как ее сердце бьется от волнения."],
        ["He gave her his heart.", "Он отдал ей свое сердце."],
        ["They poured their hearts into the project.", "Они вложили свои сердца в проект."]
    ],
    "am": [
        ["She am a student.", "Она студентка."],
        ["He am the boss.", "Он начальник."],
        ["They am happy.", "Они счастливы."]
    ],
    "present": [
        ["She received a present on her birthday.", "Она получила подарок на свой день рождения."],
        ["He will present his findings at the conference.", "Он представит свои результаты на конференции."],
        ["They are present at the meeting.", "Они присутствуют на собрании."]
    ],
    "heavy": [
        ["She struggled to lift the heavy box.", "Ей было трудно поднять тяжелую коробку."],
        ["He carried the heavy load on his shoulders.", "Он нес тяжелый груз на плечах."],
        ["They used a crane to lift the heavy equipment.", "Они использовали кран, чтобы поднять тяжелое оборудование."]
    ],
    "dance": [
        ["She danced gracefully across the stage.", "Она танцевала изящно по сцене."],
        ["He danced with his partner at the ball.", "Он танцевал с партнершей на балу."],
        ["They learned to dance salsa.", "Они научились танцевать сальсу."]
    ],
    "engine": [
        ["She studied mechanical engineering.", "Она изучала механическое инженерное дело."],
        ["He repaired the engine of his car.", "Он отремонтировал двигатель своей машины."],
        ["They designed a new engine for the airplane.", "Они разработали новый двигатель для самолета."]
    ],
    "position": [
        ["She took a position as a teacher.", "Она заняла должность учителя."],
        ["He held a high-ranking position in the company.", "Он занимал высокопоставленную должность в компании."],
        ["They found themselves in a difficult position.", "Они оказались в трудном положении."]
    ],
    "arm": [
        ["She broke her arm in the fall.", "Она сломала руку при падении."],
        ["He will arm himself with knowledge.", "Он вооружится знаниями."],
        ["They linked arms as they walked.", "Они связались за руки, пока шли."]
    ],
    "wide": [
        ["She opened her arms wide.", "Она раскрыла свои руки широко."],
        ["He had a wide smile on his face.", "На его лице была широкая улыбка."],
        ["They admired the wide expanse of the desert.", "Они восхищались широким пространством пустыни."]
    ],
    "sail": [
        ["She sailed across the ocean.", "Она переплыла океан."],
        ["He will sail on a yacht.", "Он поплывет на яхте."],
        ["They sailed into the sunset.", "Они плыли в закат."]
    ],
    "material": [
        ["She used fabric as a material for her dress.",
         "Она использовала ткань в качестве материала для своего платья."],
        ["He will study the properties of the material.", "Он изучит свойства материала."],
        ["They bought building material for the house.", "Они купили строительный материал для дома."]
    ],
    "size": [
        ["She measured the size of the room.", "Она измерила размер комнаты."],
        ["He will choose the right size of shoes.", "Он выберет правильный размер обуви."],
        ["They compared the size of the boxes.", "Они сравнили размер коробок."]
    ],
    "vary": [
        ["She found that prices vary from store to store.",
         "Она обнаружила, что цены различаются от магазина к магазину."],
        ["He will vary his workout routine.", "Он изменит свою тренировочную программу."],
        ["They experienced weather that varied greatly.", "Они испытали разнообразную погоду."]
    ],
    "settle": [
        ["She will settle in her new home.", "Она устроится в своем новом доме."],
        ["He settled the dispute peacefully.", "Он уладил спор мирно."],
        ["They decided to settle in the countryside.", "Они решили поселиться за городом."]
    ],
    "speak": [
        ["She will speak at the conference.", "Она выступит на конференции."],
        ["He speaks three languages fluently.", "Он свободно говорит на трех языках."],
        ["They spoke softly in the library.", "Они говорили тихо в библиотеке."]
    ],
    "weight": [
        ["She lifted weights at the gym.", "Она поднимала гантели в спортзале."],
        ["He will check his weight on the scale.", "Он проверит свой вес на весах."],
        ["They struggled under the weight of the burden.", "Они боролись под тяжестью бремени."]
    ],
    "general": [
        ["She gave a general overview of the topic.", "Она дала общий обзор темы."],
        ["He studied general principles of economics.", "Он изучал общие принципы экономики."],
        ["They discussed general strategies for success.", "Они обсудили общие стратегии успеха."]
    ],
    "ice": [
        ["She put ice in her drink to cool it down.", "Она положила лед в свой напиток, чтобы охладить его."],
        ["He skated on the ice.", "Он катался на коньках по льду."],
        ["They enjoyed ice cream on a hot day.", "Они наслаждались мороженым в жаркий день."]
    ],
    "matter": [
        ["She realized that actions matter more than words.",
         "Она поняла, что поступки имеют большее значение, чем слова."],
        ["He will investigate the matter further.", "Он проведет дальнейшее расследование вопроса."],
        ["They discussed a serious matter.", "Они обсуждали серьезное дело."]
    ],
    "circle": [
        ["She drew a circle on the paper.", "Она нарисовала круг на бумаге."],
        ["He will join the discussion circle.", "Он присоединится к кругу обсуждения."],
        ["They formed a circle around the campfire.", "Они образовали круг вокруг костра."]
    ],
    "pair": [
        ["She bought a pair of shoes.", "Она купила пару обуви."],
        ["He will pair the socks.", "Он сведет носки в пары."],
        ["They danced as a pair.", "Они танцевали в паре."]
    ],
    "include": [
        ["She will include her friends in the plan.", "Она включит своих друзей в план."],
        ["He included a list of references with his report.", "Он приложил список литературы к своему отчету."],
        ["They decided to include dessert with the meal.", "Они решили включить десерт к обеду."]
    ],
    "divide": [
        ["She will divide the cake into equal slices.", "Она разделит торт на равные куски."],
        ["He divided his time between work and family.", "Он разделил свое время между работой и семьей."],
        ["They divided the money among themselves.", "Они поделили деньги между собой."]
    ],
    "syllable": [
        ["She counted the syllables in each word.", "Она посчитала слоги в каждом слове."],
        ["He will emphasize the first syllable.", "Он подчеркнет первый слог."],
        ["They practiced pronouncing difficult syllables.", "Они практиковали произношение сложных слогов."]
    ],
    "felt": [
        ["She felt a sense of accomplishment.", "Она почувствовала чувство достижения."],
        ["He will felt the wool into fabric.", "Он превратит шерсть в ткань."],
        ["They felt the warmth of the sun on their skin.", "Они почувствовали тепло солнца на своей коже."]
    ],
    "perhaps": [
        ["She will perhaps come to the party.", "Может быть, она придет на вечеринку."],
        ["He perhaps forgot about the meeting.", "Может быть, он забыл о собрании."],
        ["They will perhaps leave early.", "Может быть, они уйдут рано."]
    ],
    "pick": [
        ["She will pick flowers in the garden.", "Она соберет цветы в саду."],
        ["He picked the best apples from the tree.", "Он сорвал лучшие яблоки с дерева."],
        ["They need to pick a winner for the contest.", "Им нужно выбрать победителя конкурса."]
    ],
    "sudden": [
        ["She felt a sudden gust of wind.", "Она почувствовала внезапный порыв ветра."],
        ["He made a sudden decision to quit his job.", "Он принял внезапное решение уйти с работы."],
        ["They were caught off guard by the sudden rain.", "Их застали врасплох внезапным дождем."]
    ],
    "count": [
        ["She will count the number of books on the shelf.", "Она посчитает количество книг на полке."],
        ["He counted the money in his wallet.", "Он посчитал деньги в своем кошельке."],
        ["They counted the days until the vacation.", "Они считали дни до отпуска."]
    ],
    "square": [
        ["She drew a square on the paper.", "Она нарисовала квадрат на бумаге."],
        ["He squared the numbers in his calculations.", "Он возвел числа в квадрат в своих расчетах."],
        ["They stood in a square formation.", "Они стояли в квадратной формации."]
    ],
    "reason": [
        ["She will reason with him to find a solution.", "Она попытается убедить его найти решение."],
        ["He had a good reason for being late.", "У него была веская причина для опоздания."],
        ["They reasoned that it was too late to go out.", "Они рассудили, что уже слишком поздно выходить."]
    ],
    "length": [
        ["She measured the length of the table.", "Она измерила длину стола."],
        ["He will discuss the length of the project.", "Он обсудит продолжительность проекта."],
        ["They debated the ideal length of a movie.", "Они спорили о идеальной длине фильма."]
    ],
    "represent": [
        ["She will represent her country at the conference.", "Она представит свою страну на конференции."],
        ["He represented his client in court.", "Он представил своего клиента в суде."],
        ["They chose him to represent their interests.", "Они выбрали его, чтобы представлять свои интересы."]
    ],
    "art": [
        ["She studied art history in college.", "Она изучала историю искусства в колледже."],
        ["He will create a piece of art.", "Он создаст произведение искусства."],
        ["They appreciate all forms of art.", "Они ценят все формы искусства."]
    ],
    "subject": [
        ["She will teach the subject of mathematics.", "Она будет преподавать математику."],
        ["He studied the subject of astronomy.", "Он изучал астрономию."],
        ["They discussed the subject of politics.", "Они обсуждали тему политики."]
    ],
    "region": [
        ["She lives in the mountainous region.", "Она живет в горной местности."],
        ["He explored the region on foot.", "Он исследовал местность пешком."],
        ["They visited the wine-producing region.", "Они посетили винодельческий регион."]
    ],
    "energy": [
        ["She had boundless energy.", "У нее была неиссякаемая энергия."],
        ["He will conserve energy by turning off lights.", "Он экономит энергию, выключая свет."],
        ["They harnessed the energy of the sun.", "Они использовали энергию солнца."]
    ],
    "hunt": [
        ["He went out to hunt for deer.", "Он вышел на охоту за оленем."],
        ["She likes to hunt for mushrooms.", "Ей нравится охотиться за грибами."],
        ["They hunted for treasure in the woods.", "Они искали сокровища в лесу."]
    ],
    "probable": [
        ["It's probable that he will come tomorrow.", "Вероятно, что он придет завтра."],
        ["It's probable that she forgot about the meeting.", "Вероятно, что она забыла о собрании."],
        ["It's probable that they will win the game.", "Вероятно, что они выиграют игру."]
    ],
    "bed": [
        ["She slept in a comfortable bed.", "Она спала в удобной постели."],
        ["He made his bed before leaving the house.", "Он застелил кровать перед выходом из дома."],
        ["They bought a new bed for their bedroom.", "Они купили новую кровать для своей спальни."]
    ],
    "brother": [
        ["She has a younger brother.", "У нее есть младший брат."],
        ["He called his brother to wish him happy birthday.",
         "Он позвонил своему брату, чтобы поздравить его с днем рождения."],
        ["They share a strong bond as brothers.", "У них сильная связь как у братьев."]
    ],
    "egg": [
        ["She boiled an egg for breakfast.", "Она сварила яйцо на завтрак."],
        ["He cracked the egg into the frying pan.", "Он разбил яйцо в сковороду."],
        ["They collected eggs from the chicken coop.", "Они собирали яйца с курятника."]
    ],
    "ride": [
        ["She learned to ride a bike at a young age.", "Она научилась кататься на велосипеде в молодом возрасте."],
        ["He rode a horse through the countryside.", "Он ездил на лошади по сельской местности."],
        ["They took a ride on the roller coaster.", "Они прокатились на американских горках."]
    ],
    "cell": [
        ["She left her phone in the cell.", "Она оставила свой телефон в камере."],
        ["He studied the structure of a cell in biology class.", "Он изучал строение клетки на уроке биологии."],
        ["They examined the cell under the microscope.", "Они рассматривали клетку под микроскопом."]
    ],
    "believe": [
        ["She believes in the power of positive thinking.", "Она верит в силу позитивного мышления."],
        ["He believes that hard work pays off.", "Он верит, что упорный труд окупится."],
        ["They believe in the importance of education.", "Они верят в важность образования."]
    ],
    "fraction": [
        ["She divided the pizza into fractions.", "Она разделила пиццу на части."],
        ["He solved the math problem involving fractions.", "Он решил задачу по математике, включающую дроби."],
        ["They discussed the concept of fractions in class.", "Они обсуждали понятие дробей на уроке."]
    ],
    "forest": [
        ["She took a walk in the forest.", "Она пошла на прогулку в лес."],
        ["He explored the forest with his friends.", "Он исследовал лес со своими друзьями."],
        ["They camped in the forest for the weekend.", "Они походили в лес на выходные."]
    ],
    "sit": [
        ["She likes to sit by the fireplace in the evenings.", "Ей нравится сидеть у камина по вечерам."],
        ["He sat on the bench and watched the sunset.", "Он сидел на скамейке и смотрел на закат."],
        ["They will sit at the front of the classroom.", "Они сядут впереди в классе."]
    ],
    "race": [
        ["She participated in a race for charity.", "Она участвовала в гонке в пользу благотворительности."],
        ["He won first place in the race.", "Он занял первое место в гонке."],
        ["They cheered on the runners during the race.", "Они болели за бегунов во время гонки."]
    ],
    "window": [
        ["She looked out the window and saw a bird.", "Она посмотрела в окно и увидела птицу."],
        ["He opened the window to let in fresh air.", "Он открыл окно, чтобы впустить свежий воздух."],
        ["They closed the window before leaving the house.", "Они закрыли окно перед выходом из дома."]
    ],
    "store": [
        ["She bought groceries at the store.", "Она купила продукты в магазине."],
        ["He works at the hardware store.", "Он работает в хозяйственном магазине."],
        ["They visited the store to pick up some supplies.", "Они посетили магазин, чтобы купить некоторые товары."]
    ],
    "summer": [
        ["She enjoys swimming in the summer.", "Ей нравится купаться летом."],
        ["He spent the summer traveling through Europe.", "Он провел лето в путешествии по Европе."],
        ["They go camping every summer.", "Они ходят в походы каждое лето."]
    ],
    "train": [
        ["She took the train to the city.", "Она поехала в город на поезде."],
        ["He trained for months before the competition.", "Он тренировался месяцами перед соревнованием."],
        ["They watched the train depart from the station.", "Они смотрели, как поезд отправляется со станции."]
    ],
    "sleep": [
        ["She needs to get enough sleep.", "Ей нужно выспаться."],
        ["He slept like a baby after a long day.", "Он спал, как младенец, после долгого дня."],
        ["They decided to sleep under the stars.", "Они решили спать под открытым небом."]
    ],
    "prove": [
        ["She wants to prove her theory.", "Она хочет доказать свою теорию."],
        ["He proved his point with solid evidence.", "Он подтвердил свою точку зрения убедительными доказательствами."],
        ["They hope to prove their innocence in court.", "Они надеются доказать свою невиновность в суде."]
    ],
    "lone": [
        ["She took a walk in the woods all alone.", "Она отправилась прогуляться по лесу совершенно одна."],
        ["He felt lonely in the big city.", "Он чувствовал себя одиноким в большом городе."],
        ["They prefer to live a lone life in the countryside.", "Они предпочитают вести уединенную жизнь за городом."]
    ],
    "leg": [
        ["She broke her leg in a skiing accident.", "Она сломала ногу в аварии на лыжах."],
        ["He injured his leg while playing soccer.", "Он получил травму ноги, играя в футбол."],
        ["They raced each other on one leg.", "Они бросились друг на друга на одной ноге."]
    ],
    "exercise": [
        ["She does yoga for exercise.", "Она занимается йогой для поддержания формы."],
        ["He goes to the gym to exercise regularly.",
         "Он ходит в спортзал, чтобы регулярно заниматься физическими упражнениями."],
        ["They believe in the importance of daily exercise.", "Они верят в важность ежедневных физических упражнений."]
    ],
    "wall": [
        ["She hung a picture on the wall.", "Она повесила картину на стену."],
        ["He painted the wall a bright color.", "Он покрасил стену ярким цветом."],
        ["They built a wall around their garden.", "Они построили стену вокруг своего сада."]
    ],
    "catch": [
        ["She tried to catch the ball.", "Она пыталась поймать мяч."],
        ["He caught a fish in the river.", "Он поймал рыбу в реке."],
        ["They played catch in the park.", "Они играли в ловлю мяча в парке."]
    ],
    "mount": [
        ["She will mount the picture on the wall.", "Она повесит картину на стену."],
        ["He mounted the horse and rode off.", "Он сел на лошадь и ушел."],
        ["They mounted an expedition to the summit.", "Они организовали экспедицию на вершину."]
    ],
    "wish": [
        ["She made a wish upon a shooting star.", "Она загадала желание при увиденной падающей звезде."],
        ["He wished for peace on earth.", "Он загадал желание о мире на земле."],
        ["They wished for good luck in the new year.", "Они загадали желание о счастье в новом году."]
    ],
    "sky": [
        ["She looked up at the clear blue sky.", "Она взглянула вверх на ясное голубое небо."],
        ["He watched the birds fly across the sky.", "Он смотрел, как птицы летают по небу."],
        ["They stargazed under the night sky.", "Они наблюдали за звездами под ночным небом."]
    ],
    "board": [
        ["She wrote her ideas on the white board.", "Она записала свои идеи на белую доску."],
        ["He got on board the train.", "Он сел на поезд."],
        ["They discussed the agenda at the board meeting.", "Они обсуждали повестку дня на заседании совета."]
    ],
    "joy": [
        ["She felt pure joy at the news.", "Она почувствовала чистую радость от новостей."],
        ["He watched with joy as his team won.", "Он смотрел с радостью, как его команда побеждала."],
        ["They celebrated with joy and laughter.", "Они праздновали с радостью и смехом."]
    ],
    "winter": [
        ["She loves to ski in the winter.", "Ей нравится кататься на лыжах зимой."],
        ["He hates driving in the winter.", "Он ненавидит ездить зимой."],
        ["They enjoy cozy nights by the fire in winter.", "Они наслаждаются уютными вечерами у камина зимой."]
    ],
    "sat": [
        ["She sat quietly in the corner.", "Она тихо сидела в уголке."],
        ["He sat on the park bench and watched the world go by.",
         "Он сидел на скамейке в парке и смотрел, как мир проходит мимо."],
        ["They sat together and watched the sunset.", "Они сидели вместе и смотрели на закат."]
    ],
    "written": [
        ["She has written several books.", "Она написала несколько книг."],
        ["He has written a letter to his friend.", "Он написал письмо своему другу."],
        ["They have written their names on the wall.", "Они написали свои имена на стене."]
    ],
    "wild": [
        ["She loves exploring the wild.", "Она любит исследовать дикую природу."],
        ["He grew up in the wild west.", "Он вырос на диком западе."],
        ["They encountered wild animals on their hike.", "Они встретили диких животных во время своего похода."]
    ],
    "instrument": [
        ["She plays the piano and the violin.", "Она играет на пианино и скрипке."],
        ["He studied the violin as his primary instrument.", "Он изучал скрипку как свой основной инструмент."],
        ["They experimented with different musical instruments.",
         "Они экспериментировали с различными музыкальными инструментами."]
    ],
    "kept": [
        ["She kept her promise.", "Она сдержала свое обещание."],
        ["He kept the secret for years.", "Он держал тайну в течение многих лет."],
        ["They kept the tradition alive for generations.", "Они сохраняли традицию в живых на протяжении поколений."]
    ],
    "glass": [
        ["She drank water from a glass.", "Она пила воду из стакана."],
        ["He broke the glass vase by accident.", "Он случайно разбил стеклянную вазу."],
        ["They watched the glassblower create beautiful sculptures.",
         "Они наблюдали, как стеклодув создавал красивые скульптуры."]
    ],
    "grass": [
        ["She lay down in the soft grass.", "Она легла на мягкую траву."],
        ["He mowed the grass in the backyard.", "Он кошил траву во дворе."],
        ["They played soccer on the grass field.", "Они играли в футбол на травяном поле."]
    ],
    "cow": [
        ["She milked the cow every morning.", "Она подоила корову каждое утро."],
        ["He herded the cows into the barn.", "Он загнал коров в амбар."],
        ["They raised cows for dairy production.", "Они разводили коров на молочное производство."]
    ],
    "job": [
        ["She has a full-time job at the hospital.", "У нее полная занятость в больнице."],
        ["He applied for a job at the local restaurant.", "Он подал заявку на работу в местном ресторане."],
        ["They are looking for a summer job.", "Они ищут летнюю работу."]
    ],
    "edge": [
        ["She stood on the edge of the cliff.", "Она стояла на краю обрыва."],
        ["He sharpened the knife's edge.", "Он затачивал лезвие ножа."],
        ["They walked along the edge of the river.", "Они шли вдоль берега реки."]
    ],
    "sign": [
        ["She saw a sign for the exit.", "Она увидела указатель на выход."],
        ["He interpreted the sign as a warning.", "Он толковал знак как предупреждение."],
        ["They followed the sign to the nearest town.", "Они следовали указателю к ближайшему городу."]
    ],
    "visit": [
        ["She plans to visit her grandmother next week.", "Она планирует навестить свою бабушку на следующей неделе."],
        ["He visited the museum on his trip.", "Он посетил музей во время своей поездки."],
        ["They invited friends to visit over the holidays.", "Они пригласили друзей в гости на праздники."]
    ],
    "past": [
        ["She glanced back at her past.", "Она оглянулась на свое прошлое."],
        ["He learned from his past mistakes.", "Он учился на своих прошлых ошибках."],
        ["They discussed events from the past.", "Они обсуждали события из прошлого."]
    ],
    "soft": [
        ["She touched the soft fur of the kitten.", "Она коснулась мягкой шерсти котенка."],
        ["He spoke in a soft voice.", "Он говорил тихим голосом."],
        ["They slept on soft pillows.", "Они спали на мягких подушках."]
    ],
    "fun": [
        ["She had fun at the amusement park.", "Ей весело было в парке аттракционов."],
        ["He likes to have fun with his friends.", "Он любит веселиться с друзьями."],
        ["They organized a fun game for the party.", "Они организовали веселую игру для вечеринки."]
    ],
    "bright": [
        ["She wore a bright red dress.", "Она носила яркое красное платье."],
        ["He has a bright future ahead of him.", "У него предстоит светлое будущее."],
        ["They painted the room in bright colors.", "Они покрасили комнату яркими красками."]
    ],
    "gas": [
        ["She filled up the car with gas.", "Она заправила машину бензином."],
        ["He turned on the gas stove to cook dinner.", "Он включил газовую плиту, чтобы приготовить ужин."],
        ["They use gas for heating their home.", "Они используют газ для отопления своего дома."]
    ],
    "weather": [
        ["She checked the weather forecast before planning the picnic.",
         "Она проверила прогноз погоды перед планированием пикника."],
        ["He likes to talk about the weather.", "Он любит разговаривать о погоде."],
        ["They enjoy sunny weather at the beach.", "Они наслаждаются солнечной погодой на пляже."]
    ],
    "month": [
        ["She marked her birthday month on the calendar.", "Она отметила свой день рождения в календаре."],
        ["He likes to travel during the summer months.", "Он любит путешествовать в летние месяцы."],
        ["They pay the rent each month.", "Они платят арендную плату каждый месяц."]
    ],
    "million": [
        ["She won a million dollars in the lottery.", "Она выиграла миллион долларов в лотерее."],
        ["He dreams of making a million dollars.", "Он мечтает заработать миллион долларов."],
        ["They donated a million dollars to charity.", "Они пожертвовали миллион долларов на благотворительность."]
    ],
    "bear": [
        ["We saw a bear in the forest.", "Мы видели медведя в лесу."],
        ["He decided to bear the burden alone.", "Он решил нести бремя один."],
        ["They went to bear witness to the event.", "Они пошли быть свидетелями события."]
    ],
    "finish": [
        ["She wanted to finish the race.", "Она хотела закончить гонку."],
        ["He will finish the project by Friday.", "Он закончит проект к пятнице."],
        ["They finished eating and left the restaurant.", "Они закончили есть и ушли из ресторана."]
    ],
    "happy": [
        ["She felt happy on her birthday.", "Она чувствовала себя счастливой на свой день рождения."],
        ["He was happy to see his old friends.", "Он был счастлив видеть своих старых друзей."],
        ["They were happy with the results.", "Они были довольны результатами."]
    ],
    "hope": [
        ["She hoped for a better future.", "Она надеялась на лучшее будущее."],
        ["He hoped that she would forgive him.", "Он надеялся, что она простит его."],
        ["They hoped to find a solution soon.", "Они надеялись скоро найти решение."]
    ],
    "flower": [
        ["She picked a flower from the garden.", "Она сорвала цветок из сада."],
        ["He gave her a bouquet of flowers.", "Он подарил ей букет цветов."],
        ["They planted flowers in the backyard.", "Они посадили цветы в заднем дворе."]
    ],
    "clothe": [
        ["She likes to clothe her dolls.", "Ей нравится одевать свои куклы."],
        ["He works in a factory that clothe thousands of people.",
         "Он работает на фабрике, которая облачает тысячи людей."],
        ["They donated clothes to the homeless shelter.", "Они пожертвовали одежду приюту для бездомных."]
    ],
    "strange": [
        ["She saw a strange creature in the woods.", "Она увидела странное существо в лесу."],
        ["He found it strange that no one was home.", "Ему показалось странным, что никого не было дома."],
        ["They had a strange feeling about the place.", "У них было странное чувство по отношению к месту."]
    ],
    "gone": [
        ["She was gone for a week.", "Ее не было неделю."],
        ["He has gone to the store.", "Он пошел в магазин."],
        ["They have gone on vacation.", "Они ушли в отпуск."]
    ],
    "jump": [
        ["She likes to jump rope.", "Ей нравится прыгать на скакалке."],
        ["He can jump over the fence.", "Он может перепрыгнуть через забор."],
        ["They watched the kangaroo jump.", "Они наблюдали, как кенгуру прыгает."]
    ],
    "baby": [
        ["She had a baby last month.", "У нее родился ребенок в прошлом месяце."],
        ["He held the baby in his arms.", "Он держал ребенка на руках."],
        ["They bought baby clothes for the newborn.", "Они купили детскую одежду для новорожденного."]
    ],
    "eight": [
        ["She celebrated her eighth birthday.", "Она отмечала свой восьмой день рождения."],
        ["He arrived at eight o'clock.", "Он прибыл в восемь часов."],
        ["They counted to eight before starting the game.", "Они посчитали до восьми перед началом игры."]
    ],
    "village": [
        ["She grew up in a small village.", "Она выросла в маленькой деревне."],
        ["He visited his grandparents' village.", "Он посетил деревню своих бабушки и дедушки."],
        ["They moved to a village by the sea.", "Они переехали в деревню у моря."]
    ],
    "meet": [
        ["She wants to meet new people.", "Она хочет познакомиться с новыми людьми."],
        ["He will meet with the manager tomorrow.", "Он встретится с менеджером завтра."],
        ["They met at a coffee shop.", "Они встретились в кафе."]
    ],
    "root": [
        ["She dug up the root of the tree.", "Она выкопала корень дерева."],
        ["He traced his family roots.", "Он проследил свои семейные корни."],
        ["They planted the root in the soil.", "Они посадили корень в почву."]
    ],
    "buy": [
        ["She wants to buy a new dress.", "Она хочет купить новое платье."],
        ["He will buy groceries at the store.", "Он купит продукты в магазине."],
        ["They bought tickets for the concert.", "Они купили билеты на концерт."]
    ],
    "raise": [
        ["She wants to raise money for charity.", "Она хочет собрать деньги на благотворительность."],
        ["He will raise his hand to ask a question.", "Он поднимет руку, чтобы задать вопрос."],
        ["They raised their voices in protest.", "Они повысили голоса в знак протеста."]
    ],
    "solve": [
        ["She wants to solve the puzzle.", "Она хочет разгадать головоломку."],
        ["He will solve the math problem.", "Он решит математическую задачу."],
        ["They solved the mystery of the missing keys.", "Они разгадали тайну пропавших ключей."]
    ],
    "metal": [
        ["She collected scrap metal for recycling.", "Она собирала металлолом для переработки."],
        ["He works with metal in his workshop.", "Он работает с металлом в своей мастерской."],
        ["They used metal bars to reinforce the structure.",
         "Они использовали металлические бруски для укрепления конструкции."]
    ],
    "whether": [
        ["She wondered whether to go or stay.", "Она размышляла, идти ли ей или остаться."],
        ["He will check whether the door is locked.", "Он проверит, заперта ли дверь."],
        ["They discussed whether to postpone the meeting.", "Они обсуждали, откладывать ли встречу."]
    ],
    "push": [
        ["She pushed the door open.", "Она толкнула дверь, чтобы открыть ее."],
        ["He will push the cart.", "Он будет толкать тележку."],
        ["They pushed themselves to finish the race.", "Они подтолкнули себя, чтобы закончить гонку."]
    ],
    "seven": [
        ["She counted to seven before jumping.", "Она посчитала до семи перед прыжком."],
        ["He will arrive at seven o'clock.", "Он прибудет в семь часов."],
        ["They took seven days to complete the project.", "Они потратили семь дней на завершение проекта."]
    ],
    "paragraph": [
        ["She wrote a long paragraph.", "Она написала длинный абзац."],
        ["He will read the first paragraph.", "Он прочитает первый абзац."],
        ["They discussed each paragraph in detail.", "Они обсуждали каждый абзац в подробностях."]
    ],
    "third": [
        ["She will be there on the third day.", "Она будет там на третий день."],
        ["He finished third in the race.", "Он финишировал третьим на гонке."],
        ["They will start the third chapter tomorrow.", "Они начнут третью главу завтра."]
    ],
    "shall": [
        ["She shall return by evening.", "Она вернется к вечеру."],
        ["He shall do his best to help.", "Он сделает все возможное, чтобы помочь."],
        ["They shall meet at the usual place.", "Они встретятся в привычном месте."]
    ],
    "held": [
        ["She held her breath underwater.", "Она задержала дыхание под водой."],
        ["He held the door open for her.", "Он удержал дверь, чтобы она прошла."],
        ["They held hands as they walked.", "Они держались за руки, когда шли."]
    ],
    "hair": [
        ["She brushed her hair before bed.", "Она расчесала волосы перед сном."],
        ["He has long hair.", "У него длинные волосы."],
        ["They dyed their hair blonde.", "Они покрасили волосы в блондинку."]
    ],
    "describe": [
        ["She will describe the scene in detail.", "Она опишет сцену подробно."],
        ["He described his experience to the police.", "Он описал свой опыт полиции."],
        ["They described the taste as spicy.", "Они описали вкус как острый."]
    ],
    "cook": [
        ["She likes to cook dinner.", "Она любит готовить ужин."],
        ["He will cook breakfast in the morning.", "Он приготовит завтрак утром."],
        ["They cooked a meal together.", "Они готовили еду вместе."]
    ],
    "floor": [
        ["She swept the floor.", "Она подмела пол."],
        ["He will mop the floor.", "Он вымоет пол."],
        ["They installed hardwood floor in the living room.", "Они установили деревянный пол в гостиной."]
    ],
    "either": [
        ["She can choose either option.", "Она может выбрать любой вариант."],
        ["He doesn't like either candidate.", "Ему не нравится ни один из кандидатов."],
        ["They can come either tomorrow or next week.", "Они могут прийти либо завтра, либо на следующей неделе."]
    ],
    "result": [
        ["She will see the result soon.", "Она увидит результат скоро."],
        ["He hopes for a positive result.", "Он надеется на положительный результат."],
        ["They analyzed the test result.", "Они проанализировали результат теста."]
    ],
    "burn": [
        ["She burned her hand on the stove.", "Она обжегла руку на плите."],
        ["He will burn the leaves in the yard.", "Он сожжет листья на участке."],
        ["They burned candles for atmosphere.", "Они зажгли свечи для атмосферы."]
    ],
    "hill": [
        ["She climbed the hill.", "Она поднялась на холм."],
        ["He will go sledding down the hill.", "Он поедет на санках с горы."],
        ["They built a house on the hilltop.", "Они построили дом на вершине холма."]
    ],
    "safe": [
        ["She felt safe in her home.", "Она чувствовала себя в безопасности дома."],
        ["He will keep the documents safe.", "Он сохранит документы в надежности."],
        ["They arrived safe and sound.", "Они прибыли целыми и невредимыми."]
    ],
    "cat": [
        ["She has a pet cat.", "У нее есть домашний кот."],
        ["He will feed the cat.", "Он покормит кота."],
        ["They adopted a stray cat.", "Они взяли бездомного кота на улице."]
    ],
    "century": [
        ["She studied history of the 18th century.", "Она изучала историю XVIII века."],
        ["He will visit a museum of 20th century art.", "Он посетит музей искусства XX века."],
        ["They discussed innovations of the 21st century.", "Они обсуждали инновации XXI века."]
    ],
    "consider": [
        ["She will consider their offer.", "Она рассмотрит их предложение."],
        ["He considered the consequences of his actions.", "Он обдумывал последствия своих действий."],
        ["They considered him a friend.", "Они считали его другом."]
    ],
    "type": [
        ["She will type the report.", "Она наберет отчет на клавиатуре."],
        ["He can type fast.", "Он может быстро печатать."],
        ["They typed the document in Word.", "Они набрали документ в Word."]
    ],
    "law": [
        ["She studied law at university.", "Она училась на юридическом факультете университета."],
        ["He will consult a lawyer.", "Он обратится к адвокату."],
        ["They discussed changes in the law.", "Они обсуждали изменения в законе."]
    ],
    "bit": [
        ["She ate a bit of cake.", "Она съела кусочек торта."],
        ["He will wait a bit longer.", "Он подождет еще немного."],
        ["They felt a bit tired.", "Они чувствовали себя немного усталыми."]
    ],
    "coast": [
        ["She lives on the coast.", "Она живет на побережье."],
        ["He will drive along the coast.", "Он поедет вдоль побережья."],
        ["They enjoy walks along the coast.", "Они любят гулять по берегу."]
    ],
    "copy": [
        ["She will make a copy of the document.", "Она сделает копию документа."],
        ["He will copy the file to a USB drive.", "Он скопирует файл на USB-накопитель."],
        ["They made a copy for each participant.", "Они сделали копию для каждого участника."]
    ],
    "phrase": [
        ["She repeated the phrase several times.", "Она повторила фразу несколько раз."],
        ["He will learn a new phrase every day.", "Он будет учить новую фразу каждый день."],
        ["They translated the phrase into French.", "Они перевели фразу на французский язык."]
    ],
    "silent": [
        ["She remained silent during the meeting.", "Она молчала на совещании."],
        ["He will keep silent about the incident.", "Он промолчит о происшествии."],
        ["They sat in silent contemplation.", "Они сидели в молчаливом раздумье."]
    ],
    "tall": [
        ["She is tall for her age.", "Она высокая для своего возраста."],
        ["He will plant tall trees in the garden.", "Он посадит высокие деревья в саду."],
        ["They climbed to the top of the tall mountain.", "Они поднялись на вершину высокой горы."]
    ],
    "sand": [
        ["She built a sandcastle on the beach.", "Она построила песочный замок на пляже."],
        ["He will walk barefoot in the sand.", "Он пройдется босиком по песку."],
        ["They collected seashells from the sand.", "Они собрали ракушки с песка."]
    ],
    "soil": [
        ["She planted seeds in the soil.", "Она посадила семена в почву."],
        ["He will fertilize the soil.", "Он удобрит почву."],
        ["They tilled the soil before planting.", "Они вспахали почву перед посадкой."]
    ],
    "roll": [
        ["She will roll the dough for the pie.", "Она раскатает тесто для пирога."],
        ["He will roll the dice.", "Он бросит кости."],
        ["They rolled the carpet out on the floor.", "Они развернули ковер на полу."]
    ],
    "temperature": [
        ["She checked the temperature outside.", "Она проверила температуру на улице."],
        ["He will adjust the temperature of the oven.", "Он отрегулирует температуру печи."],
        ["They measured the temperature of the water.", "Они измерили температуру воды."]
    ],
    "finger": [
        ["She hurt her finger.", "Она поранила палец."],
        ["He will count on his fingers.", "Он будет считать на пальцах."],
        ["They traced their initials in the sand with their fingers.", "Они выписали свои инициалы на песке пальцами."]
    ],
    "industry": [
        ["She works in the automotive industry.", "Она работает в автомобильной промышленности."],
        ["He will study trends in the fashion industry.", "Он будет изучать тенденции в модной индустрии."],
        ["They discussed the future of the tech industry.", "Они обсуждали будущее индустрии высоких технологий."]
    ],
    "value": [
        ["She values honesty above all.", "Она ценит честность выше всего."],
        ["He will appraise the value of the antique.", "Он оценит стоимость антиквариата."],
        ["They discussed the cultural value of art.", "Они обсуждали культурную ценность искусства."]
    ],
    "fight": [
        ["She won the fight.", "Она выиграла бой."],
        ["He will fight for justice.", "Он будет бороться за справедливость."],
        ["They witnessed a fight in the street.", "Они стали свидетелями драки на улице."]
    ],
    "lie": [
        ["She told a white lie.", "Она сказала небольшую ложь."],
        ["He will lie down and rest.", "Он ляжет и отдохнет."],
        ["They caught him in a lie.", "Они поймали его на лжи."]
    ],
    "beat": [
        ["She beat the competition.", "Она обошла конкурентов."],
        ["He will beat the drum.", "Он будет бить в барабан."],
        ["They played cards and beat him at every game.", "Они играли в карты и выиграли у него в каждой игре."]
    ],
    "excite": [
        ["She was excited about the news.", "Она была взволнована новостью."],
        ["He will excite the audience with his performance.", "Он взволнует аудиторию своим выступлением."],
        ["They were excited to visit the amusement park.", "Они с нетерпением ждали посещения парка аттракционов."]
    ],
    "natural": [
        ["She has a natural talent for singing.", "У нее есть естественный талант к пению."],
        ["He will explore natural wonders.", "Он изучит природные чудеса."],
        ["They prefer natural remedies to synthetic drugs.", "Они предпочитают натуральные лекарства синтетическим."]
    ],
    "view": [
        ["She enjoys the view from her balcony.", "Она наслаждается видом с балкона."],
        ["He will take in the view from the mountaintop.", "Он будет наслаждаться видом с вершины горы."],
        ["They have a panoramic view of the city.", "У них панорамный вид на город."]
    ],
    "sense": [
        ["She has a keen sense of smell.", "У нее острое обоняние."],
        ["He will use his common sense.", "Он будет использовать здравый смысл."],
        ["They felt a sense of accomplishment.", "У них возникло чувство достижения."]
    ],
    "ear": [
        ["She whispered in his ear.", "Она шептала ему на ухо."],
        ["He will cover his ears to block out the noise.", "Он закроет уши, чтобы заглушить шум."],
        ["They listened with bated breath and ears pricked.",
         "Они слушали с задержанным дыханием и напряженными ушами."]
    ],
    "else": [
        ["She asked if there was anything else.", "Она спросила, есть ли что-то еще."],
        ["He will do something else instead.", "Он сделает что-то другое вместо этого."],
        ["They have nowhere else to go.", "У них больше некуда идти."]
    ],
    "quite": [
        ["She was quite tired after the long journey.", "Она была довольно усталой после долгого путешествия."],
        ["He will quite enjoy the movie.", "Он вполне насладится фильмом."],
        ["They found the idea quite interesting.", "Они нашли идею довольно интересной."]
    ],
    "broke": [
        ["She broke the vase by accident.", "Она случайно разбила вазу."],
        ["He will fix the window he broke.", "Он починит окно, которое разбил."],
        ["They broke the news gently.", "Они передали новость мягко."]
    ],
    "case": [
        ["She presented her case to the jury.", "Она представила свой случай перед жюри."],
        ["He will study the case files.", "Он изучит файлы дела."],
        ["They discussed various case studies.", "Они обсуждали различные кейс-стади."]
    ],
    "middle": [
        ["She stood in the middle of the room.", "Она стояла посреди комнаты."],
        ["He will meet you in the middle of the bridge.", "Он встретит вас посередине моста."],
        ["They found themselves in the middle of nowhere.", "Они оказались посреди ниоткуда."]
    ],
    "kill": [
        ["She killed the spider with a shoe.", "Она убила паука туфелькой."],
        ["He will hunt to kill.", "Он будет охотиться, чтобы убить."],
        ["They killed time by playing games.", "Они убивали время, играя в игры."]
    ],
    "son": [
        ["She has a son and a daughter.", "У нее есть сын и дочь."],
        ["He will name his son after his father.", "Он назовет сына в честь своего отца."],
        ["They are proud of their son's achievements.", "Они гордятся достижениями своего сына."]
    ],
    "lake": [
        ["She swam in the lake every summer.", "Она купалась в озере каждое лето."],
        ["He will fish at the lake.", "Он будет ловить рыбу на озере."],
        ["They rented a cabin by the lake.", "Они сняли кабину у озера."]
    ],
    "moment": [
        ["She cherished the moment.", "Она хранила момент в сердце."],
        ["He will seize the moment.", "Он воспользуется моментом."],
        ["They captured the perfect moment in a photograph.", "Они запечатали идеальный момент на фотографии."]
    ],
    "scale": [
        ["She measured the scale of the problem.", "Она измерила масштаб проблемы."],
        ["He will weigh the ingredients on the scale.", "Он взвесит ингредиенты на весах."],
        ["They climbed the scale model of the mountain.", "Они взошли на модель горы масштаба."]
    ],
    "loud": [
        ["She spoke loud and clear.", "Она говорила громко и четко."],
        ["He will play the music loud.", "Он включит музыку громко."],
        ["They heard a loud noise outside.", "Они услышали громкий шум на улице."]
    ],
    "spring": [
        ["She planted flowers in the spring.", "Она посадила цветы весной."],
        ["He will clean the house this spring.", "Он уберет дом в эту весну."],
        ["They took a walk in the park in the spring sunshine.", "Они пошли гулять в парке под весенним солнцем."]
    ],
    "observe": [
        ["She liked to observe the stars at night.", "Она любила наблюдать за звездами ночью."],
        ["He will observe the behavior of the animals.", "Он будет наблюдать за поведением животных."],
        ["They were asked to observe silence during the ceremony.",
         "Их попросили соблюдать молчание во время церемонии."]
    ],
    "child": [
        ["She works with child psychology.", "Она работает в области детской психологии."],
        ["He will read a story to the child.", "Он расскажет сказку ребенку."],
        ["They adopted a child from an orphanage.", "Они усыновили ребенка из приюта."]
    ],
    "straight": [
        ["She has straight hair.", "У нее прямые волосы."],
        ["He will walk straight ahead.", "Он пойдет прямо вперед."],
        ["They stood in a straight line.", "Они стояли в стройном ряду."]
    ],
    "consonant": [
        ["She studied vowel and consonant sounds.", "Она изучала гласные и согласные звуки."],
        ["He will learn how to pronounce consonants.", "Он научится произносить согласные звуки."],
        ["They played with consonant blends.", "Они играли со смешанными согласными."]
    ],
    "nation": [
        ["She represented her nation at the Olympics.", "Она представляла свою страну на Олимпийских играх."],
        ["He will sing the national anthem.", "Он исполнит гимн страны."],
        ["They discussed the future of the nation.", "Они обсуждали будущее нации."]
    ],
    "dictionary": [
        ["She looked up the word in the dictionary.", "Она нашла слово в словаре."],
        ["He will buy a bilingual dictionary.", "Он купит двуязычный словарь."],
        ["They consulted the dictionary for the correct spelling.",
         "Они обратились к словарю за правильным написанием."]
    ],
    "milk": [
        ["She poured a glass of milk.", "Она налила стакан молока."],
        ["He will milk the cows in the morning.", "Он подоит коров утром."],
        ["They bought milk from the local dairy.", "Они купили молоко в местной молочной продукции."]
    ],
    "speed": [
        ["She drove at a high speed.", "Она ехала с высокой скоростью."],
        ["He will increase the speed of the treadmill.", "Он увеличит скорость беговой дорожки."],
        ["They measured the speed of the car.", "Они измерили скорость автомобиля."]
    ],
    "method": [
        ["She followed a scientific method.", "Она следовала научному методу."],
        ["He will teach the method to his students.", "Он научит методу своих студентов."],
        ["They developed a new method for testing.", "Они разработали новый метод тестирования."]
    ],
    "organ": [
        ["She plays the organ at church.", "Она играет на органе в церкви."],
        ["He will donate his organs.", "Он пожертвует свои органы."],
        ["They listened to the organ music.", "Они слушали органную музыку."]
    ],
    "pay": [
        ["She will pay the bill.", "Она оплатит счет."],
        ["He will receive his pay at the end of the month.", "Он получит свою зарплату в конце месяца."],
        ["They negotiated the pay for the job.", "Они договорились о оплате за работу."]
    ],
    "age": [
        ["She asked his age.", "Она спросила его возраст."],
        ["He will retire at the age of sixty-five.", "Он выйдет на пенсию в возрасте шестидесяти пяти лет."],
        ["They discussed the aging population.", "Они обсуждали стареющее население."]
    ],
    "section": [
        ["She read the sports section of the newspaper.", "Она читала раздел спорта в газете."],
        ["He will cut the cake into sections.", "Он разрежет торт на куски."],
        ["They sat in the front section of the theater.", "Они сидели в переднем ряду театра."]
    ],
    "dress": [
        ["She wore a beautiful dress to the party.", "Она надела красивое платье на вечеринку."],
        ["He will dress in his best suit.", "Он будет одет в свой лучший костюм."],
        ["They designed the dress for the fashion show.", "Они разработали платье для модного показа."]
    ],
    "cloud": [
        ["She watched the clouds float by.", "Она смотрела, как облака плывут мимо."],
        ["He will cloud the issue with irrelevant details.", "Он затуманит вопрос неважными деталями."],
        ["They predicted rain from the dark clouds.", "Они предсказали дождь по темным облакам."]
    ],
    "surprise": [
        ["She planned a surprise party for his birthday.", "Она организовала сюрприз-вечеринку к его дню рождения."],
        ["He will surprise her with flowers.", "Он удивит ее цветами."],
        ["They gasped in surprise at the announcement.", "Они захватили дыхание от удивления при объявлении."]
    ],
    "quiet": [
        ["She enjoyed the quiet of the countryside.", "Она наслаждалась тишиной загородной местности."],
        ["He will keep quiet about the incident.", "Он промолчит о происшествии."],
        ["They whispered in quiet voices.", "Они шептали тихими голосами."]
    ],
    "stone": [
        ["She skipped stones across the lake.", "Она кидала камни через озеро."],
        ["He will carve his initials into the stone.", "Он вырежет свои инициалы на камне."],
        ["They built the house from local stone.", "Они построили дом из местного камня."]
    ],
    "tiny": [
        ["She found a tiny insect in the garden.", "Она нашла крошечного насекомого в саду."],
        ["He will write his notes in tiny handwriting.", "Он напишет свои заметки крошечным почерком."],
        ["They lived in a tiny apartment.", "Они жили в крошечной квартире."]
    ],
    "climb": [
        ["She likes to climb mountains.", "Она любит восхождения на горы."],
        ["He will climb the ladder to reach the roof.", "Он поднимется по лестнице, чтобы добраться до крыши."],
        ["They climbed the stairs to the top floor.", "Они поднялись по лестнице на верхний этаж."]
    ],
    "cool": [
        ["She felt the cool breeze on her face.", "Она почувствовала прохладный ветер на лице."],
        ["He will cool the drinks in the refrigerator.", "Он охладит напитки в холодильнике."],
        ["They relaxed in the cool shade.", "Они расслабились в прохладной тени."]
    ],
    "design": [
        ["She works as a fashion design.", "Она работает модельером."],
        ["He will design a new logo for the company.", "Он разработает новый логотип для компании."],
        ["They discussed the design of the building.", "Они обсуждали дизайн здания."]
    ],
    "poor": [
        ["She felt sorry for the poor animals.", "Ей было жаль бедных животных."],
        ["He will donate money to help the poor.", "Он пожертвует деньги, чтобы помочь бедным."],
        ["They lived in a poor neighborhood.", "Они жили в бедном районе."]
    ],
    "lot": [
        ["She bought a lot of groceries.", "Она купила много продуктов."],
        ["He will park in the vacant lot.", "Он припаркуется на свободной площадке."],
        ["They have a lot in common.", "У них много общего."]
    ],
    "experiment": [
        ["She conducted an experiment in the laboratory.", "Она провела эксперимент в лаборатории."],
        ["He will design an experiment to test his hypothesis.",
         "Он разработает эксперимент, чтобы проверить свою гипотезу."],
        ["They recorded the results of the experiment.", "Они зафиксировали результаты эксперимента."]
    ],
    "bottom": [
        ["She found the keys at the bottom of her bag.", "Она нашла ключи внизу своей сумки."],
        ["He will hit rock bottom before he starts to improve.", "Он упадет дном, прежде чем начнет улучшаться."],
        ["They explored the bottom of the ocean.", "Они исследовали дно океана."]
    ],
    "key": [
        ["She lost the key to her house.", "Она потеряла ключ от дома."],
        ["He will find the key to success.", "Он найдет ключ к успеху."],
        ["They discussed the key points of the presentation.", "Они обсудили ключевые моменты презентации."]
    ],
    "iron": [
        ["She used an iron to press her clothes.", "Она использовала утюг, чтобы погладить свою одежду."],
        ["He will iron out the wrinkles in the fabric.", "Он разгладит складки на ткани."],
        ["They forged the iron into a horseshoe.", "Они выковали железо в подкову."]
    ],
    "single": [
        ["She is single and looking for love.", "Она одинока и ищет любовь."],
        ["He will single out the best candidate for the job.", "Он выделит лучшего кандидата на работу."],
        ["They live in a single-story house.", "Они живут в одноэтажном доме."]
    ],
    "stick": [
        ["She found a stick to use as a walking aid.",
         "Она нашла палку, чтобы использовать ее в качестве опоры для ходьбы."],
        ["He will stick the pieces together with glue.", "Он склеит кусочки клеем."],
        ["They gathered sticks for the campfire.", "Они собрали ветки для костра."]
    ],
    "flat": [
        ["She lived in a flat in the city.", "Она жила в квартире в городе."],
        ["He will flatten the dough with a rolling pin.", "Он раскатает тесто скалкой."],
        ["They walked across the flat plains.", "Они прошли через равнину."]
    ],
    "twenty": [
        ["She celebrated her twentieth birthday.", "Она отметила свой двадцатый день рождения."],
        ["He will arrive at twenty past seven.", "Он прибудет в двадцать минут семь."],
        ["They counted to twenty.", "Они посчитали до двадцати."]
    ],
    "skin": [
        ["She has sensitive skin.", "У нее чувствительная кожа."],
        ["He will peel the skin from the apple.", "Он снимет кожуру с яблока."],
        ["They felt the sun on their skin.", "Они почувствовали солнце на своей коже."]
    ],
    "smile": [
        ["She greeted him with a smile.", "Она встретила его улыбкой."],
        ["He will smile for the camera.", "Он улыбнется в камеру."],
        ["They smiled at each other.", "Они улыбнулись друг другу."]
    ],
    "crease": [
        ["She ironed out the crease in her shirt.", "Она разгладила складку на своей рубашке."],
        ["He will fold along the crease.", "Он сложит вдоль складки."],
        ["They smoothed the crease with their hands.", "Они разгладили складку руками."]
    ],
    "hole": [
        ["She fell into a deep hole.", "Она упала в глубокую яму."],
        ["He will dig a hole for the plant.", "Он выкопает яму для растения."],
        ["They patched the hole in the wall.", "Они заделали дыру в стене."]
    ],
    "trade": [
        ["She works in the finance trade.", "Она работает в финансовой сфере."],
        ["He will trade his old car for a new one.", "Он обменяет свою старую машину на новую."],
        ["They discussed the terms of the trade.", "Они обсудили условия сделки."]
    ],
    "melody": [
        ["She hummed a familiar melody.", "Она напевала знакомую мелодию."],
        ["He will compose a new melody.", "Он сочинит новую мелодию."],
        ["They danced to the melody of the music.", "Они танцевали под мелодию музыки."]
    ],
    "trip": [
        ["She planned a trip to Europe.", "Она спланировала поездку в Европу."],
        ["He will take a business trip to Japan.", "Он совершит командировку в Японию."],
        ["They went on a hiking trip.", "Они отправились в поход."]
    ],
    "office": [
        ["She works in an office.", "Она работает в офисе."],
        ["He will clean the office.", "Он уберет офис."],
        ["They held a meeting in the office.", "Они провели совещание в офисе."]
    ],
    "receive": [
        ["She will receive a gift for her birthday.", "Она получит подарок к своему дню рождения."],
        ["He will receive a promotion at work.", "Он получит повышение на работе."],
        ["They received a warm welcome.", "Их встретили тепло."]
    ],
    "row": [
        ["She planted seeds in a row.", "Она посадила семена в ряд."],
        ["He will row the boat across the lake.", "Он будет грести лодку через озеро."],
        ["They sat in the front row of the theater.", "Они сидели в переднем ряду театра."]
    ],
    "mouth": [
        ["She covered her mouth when she laughed.", "Она прикрывала рот, когда смеялась."],
        ["He will rinse his mouth with water.", "Он прополощет рот водой."],
        ["They ate with their mouths closed.", "Они ели, закрывая рты."]
    ],
    "exact": [
        ["She gave the exact time.", "Она назвала точное время."],
        ["He will measure with exact precision.", "Он измерит с точной точностью."],
        ["They followed the instructions to the exact letter.", "Они следовали инструкциям буквально."]
    ],
    "symbol": [
        ["She studied the symbol for peace.", "Она изучала символ мира."],
        ["He will use the symbol to represent his idea.", "Он использует символ, чтобы представить свою идею."],
        ["They deciphered the ancient symbols.", "Они разгадали древние символы."]
    ],
    "die": [
        ["She mourned the death of her friend.", "Она оплакивала смерть своего друга."],
        ["He will die his hair black.", "Он покрасит волосы в черный цвет."],
        ["They cut out shapes with a die.", "Они вырезали формы при помощи тиска."]
    ],
    "least": [
        ["She wanted to cause the least amount of trouble.", "Она хотела вызвать как можно меньше проблем."],
        ["He will choose the option that requires the least effort.",
         "Он выберет вариант, требующий минимальных усилий."],
        ["They took the least traveled route.", "Они пошли по меньшей мере проторенному пути."]
    ],
    "trouble": [
        ["She encountered trouble on the road.", "Она столкнулась с проблемой на дороге."],
        ["He will avoid trouble by staying home.", "Он избежит проблем, оставшись дома."],
        ["They faced financial trouble.", "Они столкнулись с финансовыми трудностями."]
    ],
    "shout": [
        ["She shouted for help.", "Она кричала о помощи."],
        ["He will shout to be heard over the noise.", "Он закричит, чтобы быть услышанным на фоне шума."],
        ["They heard a shout from the street.", "Они услышали крик с улицы."]
    ],
    "except": [
        ["She liked all the colors except green.", "Она любила все цвета, кроме зеленого."],
        ["He will accept the offer.", "Он примет предложение."],
        ["They invited everyone except him.", "Они пригласили всех, кроме него."]
    ],
    "wrote": [
        ["She wrote a letter to her grandmother.", "Она написала письмо своей бабушке."],
        ["He will write a novel.", "Он напишет роман."],
        ["They wrote their names on the chalkboard.", "Они написали свои имена на доске."]
    ],
    "seed": [
        ["She planted seeds in the garden.", "Она посадила семена в саду."],
        ["He will save seeds for next year's planting.", "Он сохранит семена для посева на следующий год."],
        ["They watched the seeds sprout.", "Они наблюдали, как прорастают семена."]
    ],
    "tone": [
        ["She spoke in a cheerful tone.", "Она говорила в веселом тоне."],
        ["He will adjust the tone of his speech.", "Он подкорректирует тон своего выступления."],
        ["They detected a sarcastic tone in his voice.", "Они почувствовали саркастический тон в его голосе."]
    ],
    "join": [
        ["She will join the club.", "Она вступит в клуб."],
        ["He will join the conversation.", "Он присоединится к разговору."],
        ["They joined hands.", "Они взялись за руки."]
    ],
    "suggest": [
        ["She suggested a new idea for the project.", "Она предложила новую идею для проекта."],
        ["He will suggest a restaurant for dinner.", "Он порекомендует ресторан на ужин."],
        ["They suggested changes to the plan.", "Они предложили изменения в план."]
    ],
    "clean": [
        ["She likes to keep her house clean.", "Она любит держать свой дом чистым."],
        ["He will clean the windows.", "Он вымоет окна."],
        ["They cleaned the kitchen after dinner.", "Они убрали кухню после ужина."]
    ],
    "break": [
        ["She took a break from work.", "Она взяла перерыв с работы."],
        ["He will break the stick in half.", "Он сломает палку пополам."],
        ["They heard the break of glass.", "Они услышали звук разбитого стекла."]
    ],
    "lady": [
        ["She greeted the old lady with a smile.", "Она встретила старушку улыбкой."],
        ["He will escort the lady to her car.", "Он проводит даму к ее машине."],
        ["They saw a ladybug in the garden.", "Они увидели божью коровку в саду."]
    ],
    "yard": [
        ["She has a large yard behind her house.", "У нее большой двор за домом."],
        ["He will mow the yard.", "Он подстрижет газон."],
        ["They played in the yard.", "Они играли во дворе."]
    ],
    "rise": [
        ["She watched the sun rise.", "Она наблюдала за восходом солнца."],
        ["He will rise early tomorrow.", "Он встанет рано завтра."],
        ["They saw the rise in prices.", "Они заметили повышение цен."]
    ],
    "bad": [
        ["She had a bad day at work.", "У нее был плохой день на работе."],
        ["He will feel bad if he misses the meeting.", "Ему будет плохо, если он опоздает на собрание."],
        ["They avoided the bad neighborhood.", "Они избежали плохого района."]
    ],
    "blow": [
        ["She felt the blow to her ego.", "Она почувствовала удар по своему самолюбию."],
        ["He will blow out the candles.", "Он задует свечи."],
        ["They heard the blow of the horn.", "Они услышали звук сигнала."]
    ],
    "oil": [
        ["She used oil to cook.", "Она использовала масло для приготовления пищи."],
        ["He will change the oil in the car.", "Он поменяет масло в машине."],
        ["They spilled oil on the floor.", "Они пролили масло на пол."]
    ],
    "blood": [
        ["She donated blood.", "Она сдала кровь на анализ."],
        ["He will clean the blood from his shirt.", "Он вымоет кровь со своей рубашки."],
        ["They are related by blood.", "Они родственники."]
    ],
    "touch": [
        ["She felt a gentle touch on her shoulder.", "Она почувствовала легкое прикосновение к своему плечу."],
        ["He will touch up the paint on the wall.", "Он поправит краску на стене."],
        ["They touched the leaves of the plant.", "Они прикоснулись к листьям растения."]
    ],
    "grew": [
        ["She grew tomatoes in her garden.", "Она выращивала помидоры в своем саду."],
        ["He will grew taller than his brother.", "Он вырастет выше своего брата."],
        ["They grew apart over the years.", "Они отдалились друг от друга с годами."]
    ],
    "cent": [
        ["She found a penny on the sidewalk.", "Она нашла пенни на тротуаре."],
        ["He will save every cent.", "Он будет экономить каждый цент."],
        ["They paid fifty cents for the candy.", "Они заплатили пятьдесят центов за конфеты."]
    ],
    "mix": [
        ["She will mix the ingredients in a bowl.", "Она смешает ингредиенты в миске."],
        ["He will mix the colors to create a new shade.", "Он смешает цвета, чтобы создать новый оттенок."],
        ["They mix with different social circles.", "Они общаются с разными социальными кругами."]
    ],
    "team": [
        ["She plays on the basketball team.", "Она играет в баскетбольной команде."],
        ["He will lead the team to victory.", "Он поведет команду к победе."],
        ["They work as a team.", "Они работают в команде."]
    ],
    "wire": [
        ["She cut the wire with scissors.", "Она отрезала провод ножницами."],
        ["He will wire the money to his friend.", "Он переведет деньги своему другу по проводу."],
        ["They installed a wire fence.", "Они установили проволочный забор."]
    ],
    "cost": [
        ["She asked about the cost of the dress.", "Она спросила о стоимости платья."],
        ["He will calculate the cost of the project.", "Он рассчитает стоимость проекта."],
        ["They discussed the cost of living.", "Они обсуждали стоимость жизни."]
    ],
    "lost": [
        ["She lost her keys.", "Она потеряла ключи."],
        ["He will search for the lost dog.", "Он будет искать потерянного пса."],
        ["They got lost in the forest.", "Они заблудились в лесу."]
    ],
    "brown": [
        ["She wore a brown coat.", "Она носила коричневое пальто."],
        ["He will paint the fence brown.", "Он покрасит забор в коричневый цвет."],
        ["They saw a brown bear in the woods.", "Они увидели коричневого медведя в лесу."]
    ],
    "wear": [
        ["She likes to wear dresses.", "Она любит носить платья."],
        ["He will wear a suit to the wedding.", "Он наденет костюм на свадьбу."],
        ["They wear matching shirts.", "Они носят одинаковые рубашки."]
    ],
    "garden": [
        ["She plants flowers in her garden.", "Она сажает цветы в своем саду."],
        ["He will mow the lawn in the garden.", "Он покосит газон в саду."],
        ["They relax in the garden.", "Они отдыхают в саду."]
    ],
    "equal": [
        ["She believes in equal rights.", "Она верит в равные права."],
        ["He will divide the cookies into equal portions.", "Он разделит печенье на равные порции."],
        ["They are equal in skill.", "Они равны в умениях."]
    ],
    "sent": [
        ["She sent a letter to her friend.", "Она отправила письмо своему другу."],
        ["He will be sent to jail.", "Он будет отправлен в тюрьму."],
        ["They sent a package by mail.", "Они отправили посылку по почте."]
    ],
    "choose": [
        ["She will choose the blue dress for the party.", "Она выберет синее платье на вечеринку."],
        ["He will choose his words carefully.", "Он будет внимательно выбирать слова."],
        ["They choose to go on vacation in the mountains.", "Они решили поехать на отдых в горы."]
    ],
    "fell": [
        ["She fell down the stairs.", "Она упала по лестнице."],
        ["He will fell the tree with an axe.", "Он срубит дерево топором."],
        ["They fell in love at first sight.", "Они влюбились с первого взгляда."]
    ],
    "fit": [
        ["She tried on the dress to see if it would fit.", "Она примерила платье, чтобы убедиться, подходит ли оно."],
        ["He will fit all the pieces together.", "Он соединит все детали."],
        ["They are fit and healthy.", "Они в хорошей физической форме."]
    ],
    "flow": [
        ["She watched the river flow.", "Она наблюдала за течением реки."],
        ["He will let his thoughts flow freely.", "Он позволит своим мыслям свободно течь."],
        ["They felt the energy flow through their bodies.", "Они почувствовали энергию, протекающую через их тела."]
    ],
    "fair": [
        ["She thought the decision was fair.", "Она считала решение справедливым."],
        ["He will have a fair chance to win.", "У него будет справедливый шанс на победу."],
        ["They enjoyed the fair in the town square.", "Они наслаждались ярмаркой на городской площади."]
    ],
    "bank": [
        ["She deposited her paycheck at the bank.", "Она внесла свою зарплату в банк."],
        ["He will sit on the bank of the river and fish.", "Он сядет на берегу реки и будет ловить рыбу."],
        ["They saw a duck swimming in the bank of the pond.", "Они увидели утку плавающую в берегу пруда."]
    ],
    "collect": [
        ["She collects stamps as a hobby.", "Она коллекционирует марки в качестве хобби."],
        ["He will collect the data for the research project.", "Он соберет данные для исследовательского проекта."],
        ["They collect donations for charity.", "Они собирают пожертвования на благотворительность."]
    ],
    "save": [
        ["She will save her money for a vacation.", "Она сэкономит свои деньги на отпуск."],
        ["He will save the document before closing the program.", "Он сохранит документ перед закрытием программы."],
        ["They save energy by turning off lights when not in use.",
         "Они экономят энергию, выключая свет, когда его не используют."]
    ],
    "control": [
        ["She needs to control her temper.", "Ей нужно контролировать свой характер."],
        ["He will control the speed of the car.", "Он будет контролировать скорость автомобиля."],
        ["They have control over the situation.", "Они контролируют ситуацию."]
    ],
    "decimal": [
        ["She rounded to the nearest decimal.", "Она округлила до ближайшего десятичного."],
        ["He will add a decimal to the number.", "Он добавит десятичный знак к числу."],
        ["They calculated to the third decimal place.", "Они вычислили до третьего десятичного знака."]
    ],
    "gentle": [
        ["She has a gentle touch.", "У нее нежное прикосновение."],
        ["He will speak in a gentle tone.", "Он будет говорить нежным тоном."],
        ["They were gentle with the injured bird.", "Они обращались бережно с раненой птицей."]
    ],
    "woman": [
        ["She is a strong woman.", "Она сильная женщина."],
        ["He will treat the woman with respect.", "Он будет относиться к женщине с уважением."],
        ["They celebrated International Women's Day.", "Они отметили Международный женский день."]
    ],
    "captain": [
        ["She is the captain of the soccer team.", "Она капитан футбольной команды."],
        ["He will captain the ship.", "Он будет капитаном корабля."],
        ["They elected him as team captain.", "Они выбрали его капитаном команды."]
    ],
    "practice": [
        ["She needs to practice the piano.", "Ей нужно практиковаться на пианино."],
        ["He will practice his speech before the presentation.", "Он практиковать свою речь перед презентацией."],
        ["They practice yoga for relaxation.", "Они занимаются йогой для расслабления."]
    ],
    "separate": [
        ["She will separate the laundry into colors and whites.", "Она разделит белье на цветное и белое."],
        ["He will separate the fighting children.", "Он разделит дерущихся детей."],
        ["They live in separate houses.", "Они живут в разных домах."]
    ],
    "difficult": [
        ["She found the math problem difficult.", "Ей показалась математическая задача сложной."],
        ["He will face difficult decisions.", "Он столкнется с трудными решениями."],
        ["They tackled the difficult terrain.", "Они справились с трудным рельефом."]
    ],
    "doctor": [
        ["She visited the doctor for a check-up.", "Она пошла к врачу на осмотр."],
        ["He will become a doctor.", "Он станет врачом."],
        ["They trust their doctor's advice.", "Они доверяют советам своего врача."]
    ],
    "please": [
        ["She said 'please' when asking for help.", "Она сказала 'пожалуйста', просив о помощи."],
        ["He will try to please everyone.", "Он постарается угодить всем."],
        ["They like to dine at the restaurant, where the service is always pleasing.",
         "Им нравится обедать в ресторане, где обслуживание всегда приятное."]
    ],
    "protect": [
        ["She will protect her children from harm.", "Она будет защищать своих детей от вреда."],
        ["He will protect his privacy.", "Он будет защищать свою конфиденциальность."],
        ["They protect the environment by recycling.", "Они защищают окружающую среду, перерабатывая мусор."]
    ],
    "noon": [
        ["She has lunch at noon.", "Она обедает в полдень."],
        ["He will meet his friend at noon.", "Он встретится со своим другом в полдень."],
        ["They have a noon deadline for the project.", "У них срок до полудня на проект."]
    ],
    "whose": [
        ["She asked whose book it was.", "Она спросила, чья это книга."],
        ["He will find out whose car is parked in front of his house.",
         "Он выяснит, чей автомобиль припаркован перед его домом."],
        ["They discussed whose turn it was next.", "Они обсудили, чья очередь будет следующей."]
    ],
    "locate": [
        ["She needs to locate her keys.", "Ей нужно найти свои ключи."],
        ["He will locate the source of the noise.", "Он обнаружит источник шума."],
        ["They finally located the missing document.", "Они наконец нашли потерянный документ."]
    ],
    "ring": [
        ["She wears a ring on her finger.", "Она носит кольцо на пальце."],
        ["He will ring the doorbell.", "Он позвонит в дверь."],
        ["They heard the telephone ring.", "Они услышали звонок телефона."]
    ],
    "character": [
        ["She has a strong character.", "У нее сильный характер."],
        ["He will develop the character in his novel.", "Он разовьет характер в своем романе."],
        ["They like the main character in the movie.", "Им нравится главный герой в фильме."]
    ],
    "insect": [
        ["She caught an insect in the garden.", "Она поймала насекомое в саду."],
        ["He will study the life cycle of insects.", "Он изучит жизненный цикл насекомых."],
        ["They observed the behavior of insects.", "Они наблюдали за поведением насекомых."]
    ],
    "caught": [
        ["She caught the ball.", "Она поймала мяч."],
        ["He will caught a cold if he doesn't wear a coat.", "Он заболеет, если не наденет пальто."],
        ["They caught the thief in the act.", "Они поймали вора с поличным."]
    ],
    "period": [
        ["She ended the sentence with a period.", "Она закончила предложение точкой."],
        ["He will study the medieval period in history class.", "Он изучит средневековье на уроке истории."],
        ["They discussed the Jurassic period.", "Они обсуждали юрский период."]
    ],
    "indicate": [
        ["She used a map to indicate the location.", "Она использовала карту, чтобы показать местоположение."],
        ["He will indicate his approval with a nod.", "Он покажет свое одобрение кивком."],
        ["They indicate the direction with signs.", "Они указывают направление указателями."]
    ],
    "radio": [
        ["She listens to the radio in the morning.", "Она слушает радио утром."],
        ["He will tune the radio to his favorite station.", "Он настроит радио на свою любимую станцию."],
        ["They broadcast the news on the radio.", "Они транслируют новости по радио."]
    ],
    "spoke": [
        ["She spoke to her friend on the phone.", "Она поговорила с подругой по телефону."],
        ["He will spoke out against injustice.", "Он выступит против несправедливости."],
        ["They spoke about their plans for the future.", "Они говорили о своих планах на будущее."]
    ],
    "atom": [
        ["She studied the structure of the atom.", "Она изучала структуру атома."],
        ["He will break down the molecule into atoms.", "Он разложит молекулу на атомы."],
        ["They discussed the properties of the atom.", "Они обсуждали свойства атома."]
    ],
    "human": [
        ["She believes in the potential of the human mind.", "Она верит в потенциал человеческого разума."],
        ["He will treat every human with dignity.", "Он будет относиться ко всем людям с уважением."],
        ["They explored the human body.", "Они изучали человеческое тело."]
    ],
    "history": [
        ["She enjoys reading about ancient history.", "Она любит читать о древней истории."],
        ["He will study the history of art.", "Он изучит историю искусства."],
        ["They visited historical landmarks.", "Они посетили исторические достопримечательности."]
    ],
    "effect": [
        ["She felt the effect of the medicine.", "Она почувствовала эффект от лекарства."],
        ["He will measure the effect of the advertising campaign.", "Он измерит эффект рекламной кампании."],
        ["They discussed the cause and effect of the problem.", "Они обсудили причину и следствие проблемы."]
    ],
    "electric": [
        ["She uses electric appliances in the kitchen.", "Она использует электрические приборы на кухне."],
        ["He will install an electric fence.", "Он установит электрический забор."],
        ["They power the house with electric energy.", "Они снабжают дом электроэнергией."]
    ],
    "expect": [
        ["She didn't expect to see him there.", "Она не ожидала увидеть его там."],
        ["He will expect a response by tomorrow.", "Он ожидает ответа к завтрашнему дню."],
        ["They expect good weather for the picnic.", "Они ожидают хорошей погоды на пикник."]
    ],
    "crop": [
        ["She planted crops in the field.", "Она посадила урожай на поле."],
        ["He will harvest the crop in the fall.", "Он соберет урожай осенью."],
        ["They rotate crops to maintain soil fertility.", "Они ротируют культуры, чтобы сохранить плодородие почвы."]
    ],
    "modern": [
        ["She prefers modern art.", "Она предпочитает современное искусство."],
        ["He will design a modern building.", "Он разработает современное здание."],
        ["They live in a modern apartment.", "Они живут в современной квартире."]
    ],
    "element": [
        ["She learned about the properties of each element.", "Она узнала о свойствах каждого элемента."],
        ["He will add an element of surprise to the performance.", "Он добавит элемент неожиданности в выступление."],
        ["They discussed the chemical element of water.", "Они обсуждали химический элемент воды."]
    ],
    "hit": [
        ["She hit the ball with a bat.", "Она ударила мяч битой."],
        ["He will hit the target with an arrow.", "Он попадет в цель стрелой."],
        ["They hit the jackpot at the casino.", "Они выиграли джекпот в казино."]
    ],
    "student": [
        ["She is a dedicated student.", "Она преданная ученица."],
        ["He will study hard to become a better student.", "Он учиться усердно, чтобы стать лучшим студентом."],
        ["They help each other with their student projects.", "Они помогают друг другу с проектами студентов."]
    ],
    "corner": [
        ["She found a spider in the corner of the room.", "Она нашла паука в углу комнаты."],
        ["He will turn the corner and continue straight ahead.", "Он повернет за угол и пойдет прямо."],
        ["They sat in the corner of the café.", "Они сидели в углу кафе."]
    ],
    "party": [
        ["She is hosting a party for her birthday.", "Она устраивает вечеринку на свой день рождения."],
        ["He will bring snacks to the party.", "Он принесет закуски на вечеринку."],
        ["They danced all night at the party.", "Они танцевали всю ночь на вечеринке."]
    ],
    "supply": [
        ["She will supply food for the event.", "Она обеспечит едой мероприятие."],
        ["He will supply the necessary tools for the job.", "Он предоставит необходимые инструменты для работы."],
        ["They are in charge of supply management.", "Они ответственны за управление поставками."]
    ],
    "bone": [
        ["She broke a bone in her arm.", "Она сломала кость в руке."],
        ["He will bury the bone in the backyard.", "Он похоронит кость в заднем дворе."],
        ["They found fossilized bones in the desert.", "Они нашли окаменелые кости в пустыне."]
    ],
    "rail": [
        ["She leaned against the rail of the balcony.", "Она оперлась на перила балкона."],
        ["He will ride the train along the rail.", "Он поедет поездом по рельсам."],
        ["They walked along the rail trail.", "Они гуляли по пешеходной тропе вдоль рельсов."]
    ],
    "imagine": [
        ["She can imagine a world without war.", "Она может представить мир без войны."],
        ["He will imagine a different ending to the story.", "Он представит другой конец истории."],
        ["They like to imagine what the future holds.", "Им нравится представлять, что ждет их в будущем."]
    ],
    "provide": [
        ["She will provide all the necessary information.", "Она предоставит всю необходимую информацию."],
        ["He will provide for his family.", "Он будет обеспечивать свою семью."],
        ["They provide shelter for the homeless.", "Они предоставляют укрытие бездомным."]
    ],
    "agree": [
        ["She and her friend always agree.", "Она и ее подруга всегда согласны."],
        ["He will agree to the terms of the contract.", "Он согласится с условиями контракта."],
        ["They agree on the best course of action.", "Они согласны с лучшим вариантом действий."]
    ],
    "thus": [
        ["She worked hard and thus succeeded.", "Она усердно работала, и таким образом достигла успеха."],
        ["He will save money and thus afford a vacation.",
         "Он сэкономит деньги и таким образом сможет себе позволить отпуск."],
        ["They focused on their goals and thus achieved them.",
         "Они сосредоточились на своих целях и таким образом достигли их."]
    ],
    "capital": [
        ["London is the capital of England.", "Лондон - столица Англии."],
        ["Investors are looking for capital to fund the project.",
         "Инвесторы ищут капитал для финансирования проекта."],
        ["The company raised capital through a public offering.",
         "Компания привлекла капитал через публичное размещение."]
    ],
    "won't": [
        ["She won't be able to attend the meeting.", "Она не сможет присутствовать на совещании."],
        ["He won't forget his promise.", "Он не забудет свое обещание."],
        ["They won't finish the project on time.", "Они не закончат проект вовремя."]
    ],
    "chair": [
        ["She sat in the chair by the window.", "Она села в кресло у окна."],
        ["He will lead the meeting from the chairman's chair.", "Он будет вести совещание из кресла председателя."],
        ["They need to buy more chairs for the conference room.", "Им нужно купить больше стульев для конференц-зала."]
    ],
    "danger": [
        ["She warned him of the danger.", "Она предупредила его об опасности."],
        ["He will face danger on his expedition.", "Он столкнется с опасностью в своей экспедиции."],
        ["They escaped from the danger zone.", "Они убежали из зоны опасности."]
    ],
    "fruit": [
        ["She picked apples from the fruit tree.", "Она собирала яблоки с фруктового дерева."],
        ["He will make a fruit salad for dessert.", "Он сделает фруктовый салат на десерт."],
        ["They grow various fruits in their garden.", "Они выращивают различные фрукты в своем саду."]
    ],
    "rich": [
        ["She inherited a fortune and became rich.", "Она унаследовала состояние и стала богатой."],
        ["He will invest in stocks to become rich.", "Он инвестирует в акции, чтобы разбогатеть."],
        ["They live in a rich neighborhood.", "Они живут в богатом районе."]
    ],
    "thick": [
        ["She wore a thick coat in the winter.", "Она носила толстое пальто зимой."],
        ["He will apply a thick layer of paint.", "Он нанесет толстый слой краски."],
        ["They walked through thick fog.", "Они прошли через густой туман."]
    ],
    "soldier": [
        ["She admired the courage of the soldier.", "Она восхищалась мужеством солдата."],
        ["He will serve as a soldier in the army.", "Он будет служить солдатом в армии."],
        ["They honored the fallen soldiers.", "Они почтили память павших солдат."]
    ],
    "process": [
        ["She followed the process step by step.", "Она следовала процессу шаг за шагом."],
        ["He will optimize the manufacturing process.", "Он оптимизирует производственный процесс."],
        ["They need to speed up the approval process.", "Им нужно ускорить процесс утверждения."]
    ],
    "operate": [
        ["She learned to operate the machinery.", "Она научилась управлять механизмами."],
        ["He will operate on the patient tomorrow.", "Завтра он выполнит операцию над пациентом."],
        ["They operate a successful business.", "Они управляют успешным бизнесом."]
    ],
    "guess": [
        ["She guessed the correct answer.", "Она угадала правильный ответ."],
        ["He will take a wild guess.", "Он даст случайный ответ."],
        ["They couldn't even hazard a guess.", "Они даже не могли предположить."]
    ],
    "necessary": [
        ["She considered it necessary to speak up.", "Она считала необходимым высказаться."],
        ["He will provide all the necessary documents.", "Он предоставит все необходимые документы."],
        ["They stressed the importance of necessary precautions.",
         "Они подчеркнули важность необходимых мер предосторожности."]
    ],
    "sharp": [
        ["She sharpened the pencil with a knife.", "Она заточила карандаш ножом."],
        ["He will wear a suit with a sharp cut.", "Он наденет костюм с острым кроем."],
        ["They heard a sharp sound in the distance.", "Они услышали острый звук вдали."]
    ],
    "wing": [
        ["She saw a bird spreading its wings.", "Она увидела птицу, размахивающую крыльями."],
        ["He will design a new wing for the airplane.", "Он разработает новое крыло для самолета."],
        ["They serve chicken wings at the restaurant.", "В ресторане подают куриные крылышки."]
    ],
    "create": [
        ["She likes to create art.", "Она любит создавать произведения искусства."],
        ["He will create a new website.", "Он создаст новый веб-сайт."],
        ["They create innovative solutions to complex problems.",
         "Они разрабатывают инновационные решения сложных проблем."]
    ],
    "neighbor": [
        ["She borrowed sugar from her neighbor.", "Она одолжила сахар у соседа."],
        ["He will introduce himself to the new neighbor.", "Он познакомится с новым соседом."],
        ["They are friendly with their neighbors.", "Они дружат со своими соседями."]
    ],
    "wash": [
        ["She washes her hands before meals.", "Она моет руки перед едой."],
        ["He will wash the car on Saturday.", "В субботу он вымоет машину."],
        ["They need to wash the dishes after dinner.", "Им нужно помыть посуду после обеда."]
    ],
    "bat": [
        ["She swung the bat and hit the ball.", "Она размахнулась битой и попала в мяч."],
        ["He will play baseball with his wooden bat.", "Он сыграет в бейсбол с деревянной битой."],
        ["They watched bats flying at night.", "Они наблюдали за летающими летучими мышами ночью."]
    ],
    "rather": [
        ["She would rather stay home than go out.", "Она предпочла бы остаться дома, чем выйти на улицу."],
        ["He will choose the blue shirt rather than the red one.", "Он выберет синюю рубашку, а не красную."],
        ["They decided to leave early rather than wait.", "Они решили уйти раньше, чем ждать."]
    ],
    "crowd": [
        ["She got lost in the crowd.", "Она потерялась в толпе."],
        ["He will address the crowd from the stage.", "Он обратится к толпе с сцены."],
        ["They joined the crowd at the concert.", "Они присоединились к толпе на концерте."]
    ],
    "corn": [
        ["She harvested ears of corn from the field.", "Она собрала початки кукурузы с поля."],
        ["He will make popcorn from the dried corn.", "Он приготовит попкорн из сушеной кукурузы."],
        ["They planted rows of corn in the spring.", "Они посадили ряды кукурузы весной."]
    ],
    "compare": [
        ["She likes to compare prices before buying.", "Она любит сравнивать цены перед покупкой."],
        ["He will compare the two options before deciding.", "Он сравнит два варианта перед принятием решения."],
        ["They compared their progress with that of their competitors.",
         "Они сравнили свой прогресс с прогрессом своих конкурентов."]
    ],
    "poem": [
        ["She wrote a poem about love.", "Она написала стихотворение о любви."],
        ["He will recite a poem at the poetry reading.", "Он будет читать стихотворение на вечере поэзии."],
        ["They analyzed the structure of the poem.", "Они проанализировали структуру стихотворения."]
    ],
    "string": [
        ["She tied the package with string.", "Она связала пакет ниткой."],
        ["He will play a guitar with nylon strings.", "Он сыграет на гитаре с нейлоновыми струнами."],
        ["They threaded beads onto the string.", "Они нанизали бусины на нить."]
    ],
    "bell": [
        ["She rang the bell to signal the start of class.", "Она звонила в колокол, сигнализируя начало урока."],
        ["He will repair the broken bell.", "Он починит сломанный колокол."],
        ["They heard the church bell toll.", "Они услышали, как звенел колокол в церкви."]
    ],
    "depend": [
        ["She can depend on her friend for support.", "Она может полагаться на поддержку своего друга."],
        ["He will depend on public transportation to get to work.",
         "Он будет полагаться на общественный транспорт, чтобы добраться до работы."],
        ["They depend on each other in times of need.", "Они полагаются друг на друга в трудные моменты."]
    ],
    "meat": [
        ["She bought fresh meat from the butcher.", "Она купила свежее мясо у мясника."],
        ["He will cook meat on the grill.", "Он приготовит мясо на гриле."],
        ["They prefer fish to red meat.", "Они предпочитают рыбу красному мясу."]
    ],
    "rub": [
        ["She rubbed her eyes to clear her vision.", "Она потерла глаза, чтобы прояснить видение."],
        ["He will rub his sore muscles to ease the pain.", "Он потрет больные мышцы, чтобы облегчить боль."],
        ["They rubbed the stain with soap.", "Они потерли пятно мылом."]
    ],
    "tube": [
        ["She squeezed toothpaste from the tube.", "Она выдавила зубную пасту из тюбика."],
        ["He will watch a video on the internet tube.", "Он посмотрит видео на интернет-тюбе."],
        ["They traveled through the tunnel in the subway tube.", "Они проехали через туннель в метро."]
    ],
    "famous": [
        ["She became famous after winning the competition.", "Она стала известной после победы в соревновании."],
        ["He will visit the famous landmarks in the city.", "Он посетит знаменитые достопримечательности города."],
        ["They met a famous actor at the party.", "Они встретили знаменитого актера на вечеринке."]
    ],
    "dollar": [
        ["She paid with a dollar bill.", "Она заплатила долларовой купюрой."],
        ["He will exchange euros for dollars.", "Он обменяет евро на доллары."],
        ["They save a few dollars each week.", "Они откладывают несколько долларов каждую неделю."]
    ],
    "stream": [
        ["She sat by the stream and listened to the water.", "Она сидела у ручья и слушала звук воды."],
        ["He will fish in the stream.", "Он пойдет ловить рыбу в ручье."],
        ["They hiked along the stream in the forest.", "Они гуляли вдоль ручья в лесу."]
    ],
    "fear": [
        ["She overcame her fear of heights.", "Она преодолела свой страх высоты."],
        ["He will face his fear of public speaking.", "Он столкнется со своим страхом публичных выступлений."],
        ["They felt a sense of fear in the dark.", "Они почувствовали чувство страха в темноте."]
    ],
    "sight": [
        ["She lost her sight in a car accident.", "Она потеряла зрение в автомобильной аварии."],
        ["He will see the sights of the city.", "Он посмотрит достопримечательности города."],
        ["They enjoyed the beautiful sight of the sunset.", "Они наслаждались прекрасным видом заката."]
    ],
    "thin": [
        ["She prefers thin crust pizza.", "Она предпочитает пиццу с тонким коржом."],
        ["He will slice the vegetables thin.", "Он нарежет овощи тонкими ломтиками."],
        ["They walked on thin ice.", "Они шли по тонкому льду."]
    ],
    "triangle": [
        ["She drew a triangle on the chalkboard.", "Она нарисовала треугольник на меловой доске."],
        ["He will calculate the area of the triangle.", "Он рассчитает площадь треугольника."],
        ["They built a sandcastle in the shape of a triangle.", "Они построили замок из песка в форме треугольника."]
    ],
    "planet": [
        ["She studied the planets in school.", "Она изучала планеты в школе."],
        ["He will explore the planet Mars.", "Он исследует планету Марс."],
        ["They observed the planet through a telescope.", "Они наблюдали за планетой через телескоп."]
    ],
    "hurry": [
        ["She is in a hurry to catch the bus.", "Она спешит, чтобы успеть на автобус."],
        ["He will hurry to finish the project on time.", "Он поторопится, чтобы закончить проект вовремя."],
        ["They hurried to pack before the trip.", "Они поспешили упаковаться перед поездкой."]
    ],
    "chief": [
        ["She is the chief editor of the magazine.", "Она главный редактор журнала."],
        ["He will meet with the tribal chief.", "Он встретится с вождем племени."],
        ["They elected a new police chief.", "Они избрали нового начальника полиции."]
    ],
    "colony": [
        ["She studied the history of the colonial period.", "Она изучала историю колониального периода."],
        ["He will visit a colony of penguins.", "Он посетит колонию пингвинов."],
        ["They established a colony on the island.", "Они основали колонию на острове."]
    ],
    "clock": [
        ["She glanced at the clock on the wall.", "Она бросила взгляд на часы на стене."],
        ["He will wind the grandfather clock.", "Он заведет настенные часы."],
        ["They synchronized their watches with the clock tower.",
         "Они синхронизировали свои часы со сторожевой башней."]
    ],
    "mine": [
        ["She worked in a coal mine.", "Она работала на угольной шахте."],
        ["He will dig for gold in the mine.", "Он будет копать золото в шахте."],
        ["They explored the abandoned mine.", "Они исследовали заброшенную шахту."]
    ],
    "tie": [
        ["She tied her hair back with a ribbon.", "Она привязала волосы лентой."],
        ["He will wear a tie with his suit.", "Он наденет галстук к своему костюму."],
        ["They use rope to tie the packages.", "Они используют веревку, чтобы завязать пакеты."]
    ],
    "enter": [
        ["She will enter the competition.", "Она будет участвовать в соревновании."],
        ["He will enter the room quietly.", "Он войдет в комнату тихо."],
        ["They need to enter their password to access the system.",
         "Им нужно ввести свой пароль, чтобы получить доступ к системе."]
    ],
    "major": [
        ["She is a major in biology.", "Она специализируется на биологии."],
        ["He will choose his major in college.", "Он выберет свою специализацию в колледже."],
        ["They discussed major issues affecting the economy.", "Они обсудили основные проблемы, влияющие на экономику."]
    ],
    "fresh": [
        ["She bought fresh vegetables from the market.", "Она купила свежие овощи на рынке."],
        ["He will take a shower to feel fresh.", "Он примет душ, чтобы почувствовать себя свежим."],
        ["They enjoy the fresh air in the countryside.", "Им нравится свежий воздух за городом."]
    ],
    "search": [
        ["She will search for her lost keys.", "Она будет искать свои потерянные ключи."],
        ["He will search the internet for information.", "Он будет искать информацию в интернете."],
        ["They conducted a thorough search of the area.", "Они провели тщательный обыск местности."]
    ],
    "send": [
        ["She will send a letter to her friend.", "Она отправит письмо своему другу."],
        ["He will send an email with the instructions.", "Он отправит электронное письмо с инструкциями."],
        ["They will send a package by express delivery.", "Они отправят пакет экспресс-доставкой."]
    ],
    "yellow": [
        ["She painted the walls yellow.", "Она покрасила стены в желтый цвет."],
        ["He will wear a yellow shirt.", "Он наденет желтую рубашку."],
        ["They picked ripe yellow bananas.", "Они собрали спелые желтые бананы."]
    ],
    "gun": [
        ["She aimed the gun at the target.", "Она прицелилась из пистолета в мишень."],
        ["He will clean his gun after hunting.", "Он почистит свой пистолет после охоты."],
        ["They heard gunshots in the distance.", "Они услышали выстрелы вдали."]
    ],
    "allow": [
        ["She will allow her children to play outside.", "Она разрешит своим детям играть на улице."],
        ["He will allow extra time for the project.", "Он выделит дополнительное время для проекта."],
        ["They allow pets in their apartment.", "Они разрешают держать животных в своей квартире."]
    ],
    "print": [
        ["She will print the document for the meeting.", "Она напечатает документ для собрания."],
        ["He printed his boarding pass at the airport.", "Он распечатал посадочный талон в аэропорту."],
        ["They print newspapers daily.", "Они печатают газеты ежедневно."]
    ],
    "dead": [
        ["She found a dead bird in the backyard.", "Она нашла мертвую птицу в заднем дворе."],
        ["He confirmed that the battery was dead.", "Он подтвердил, что батарея разряжена."],
        ["They buried their dead cat in the garden.", "Они похоронили своего мертвого кота в саду."]
    ],
    "spot": [
        ["She noticed a spot on her shirt.", "Она заметила пятно на своей рубашке."],
        ["He will park the car in the empty spot.", "Он припаркует машину на свободном месте."],
        ["They found a good fishing spot by the river.", "Они нашли хорошее место для рыбалки у реки."]
    ],
    "desert": [
        ["She explored the desert on a camel.", "Она исследовала пустыню на верблюде."],
        ["He will cross the desert on foot.", "Он пересечет пустыню пешком."],
        ["They camped in the desert overnight.", "Они разбили лагерь в пустыне на ночь."]
    ],
    "suit": [
        ["She wore a suit to the job interview.", "Она надела костюм на собеседование на работу."],
        ["He will tailor the suit for a perfect fit.", "Он сделает костюм по мерке для идеальной посадки."],
        ["They rented a tuxedo for the formal suit.", "Они арендовали смокинг для официального костюма."]
    ],
    "current": [
        ["She swam against the current.", "Она плыла против течения."],
        ["He will check the current weather forecast.", "Он проверит текущий прогноз погоды."],
        ["They followed the current trends in fashion.", "Они следили за текущими тенденциями в моде."]
    ],
    "lift": [
        ["She asked for help to lift the heavy box.", "Она попросила помощи, чтобы поднять тяжелый ящик."],
        ["He will take the lift to the top floor.", "Он поднимется на лифте на верхний этаж."],
        ["They installed a lift for wheelchair access.", "Они установили лифт для доступа на коляске."]
    ],
    "rose": [
        ["She planted roses in her garden.", "Она посадила розы в своем саду."],
        ["He will give her a bouquet of roses.", "Он подарит ей букет роз."],
        ["They watched the sun rise over the horizon.", "Они наблюдали, как солнце восходит над горизонтом."]
    ],
    "continue": [
        ["She will continue her studies next semester.", "Она продолжит свои учебы в следующем семестре."],
        ["He continued to work despite the interruptions.", "Он продолжал работать, несмотря на прерывания."],
        ["They decided to continue the project despite the challenges.",
         "Они решили продолжить проект, несмотря на сложности."]
    ],
    "block": [
        ["She lives on the next block.", "Она живет на следующем блоке."],
        ["He will block the entrance with a barrier.", "Он заблокирует вход барьером."],
        ["They encountered a road block on the highway.", "Они столкнулись с дорожным блоком на автостраде."]
    ],
    "chart": [
        ["She will create a chart to visualize the data.", "Она создаст диаграмму, чтобы визуализировать данные."],
        ["He analyzed the chart to identify trends.", "Он проанализировал диаграмму, чтобы выявить тенденции."],
        ["They studied a chart of the constellations.", "Они изучали диаграмму созвездий."]
    ],
    "hat": [
        ["She wore a hat to protect her head from the sun.", "Она надела шляпу, чтобы защитить голову от солнца."],
        ["He will buy a new hat for the beach vacation.", "Он купит новую шляпу для пляжного отпуска."],
        ["They hung their hats on the coat rack.", "Они повесили свои шляпы на вешалку для пальто."]
    ],
    "sell": [
        ["She will sell her old clothes at the garage sale.", "Она продаст свою старую одежду на гаражной распродаже."],
        ["He sold his car to buy a new one.", "Он продал свою машину, чтобы купить новую."],
        ["They sell fresh produce at the farmer's market.", "Они продают свежие продукты на фермерском рынке."]
    ],
    "success": [
        ["She celebrated her success with her friends.", "Она отметила свой успех вместе с друзьями."],
        ["He will study the factors contributing to success.", "Он будет изучать факторы, способствующие успеху."],
        ["They achieved great success in their business.", "Они добились большого успеха в своем бизнесе."]
    ],
    "company": [
        ["She works for a software company.", "Она работает в компании по разработке программного обеспечения."],
        ["He will start his own company.", "Он основет свою собственную компанию."],
        ["They formed a partnership to launch the company.", "Они заключили партнерство для запуска компании."]
    ],
    "subtract": [
        ["She needs to subtract expenses from her income.", "Ей нужно вычесть расходы из своего дохода."],
        ["He will subtract the smaller number from the larger one.", "Он вычтет меньшее число из большего."],
        ["They subtracted the tax amount from the total.", "Они вычли сумму налога из общей суммы."]
    ],
    "event": [
        ["She organized a charity event.", "Она организовала благотворительное мероприятие."],
        ["He will attend the cultural event downtown.", "Он посетит культурное мероприятие в центре города."],
        ["They planned the event carefully to ensure its success.",
         "Они тщательно спланировали мероприятие, чтобы обеспечить его успех."]
    ],
    "particular": [
        ["She was very particular about her food preferences.",
         "Она была очень придирчива к своим предпочтениям в еде."],
        ["He will examine the particular details of the contract.", "Он рассмотрит конкретные детали контракта."],
        ["They focused on a particular aspect of the problem.", "Они сосредоточились на конкретном аспекте проблемы."]
    ],
    "deal": [
        ["She made a deal with the car salesman.", "Она заключила сделку с продавцом автомобилей."],
        ["He will negotiate a deal with the supplier.", "Он будет вести переговоры о сделке с поставщиком."],
        ["They sealed the deal with a handshake.", "Они закрыли сделку рукопожатием."]
    ],
    "swim": [
        ["She learned to swim at a young age.", "Она научилась плавать в молодом возрасте."],
        ["He will swim across the lake.", "Он переплывет озеро."],
        ["They enjoyed a swim in the ocean.", "Они наслаждались купанием в океане."]
    ],
    "term": [
        ["She used a medical term to describe the condition.",
         "Она использовала медицинский термин, чтобы описать состояние."],
        ["He will serve a four-year term in office.", "Он отбудет четырехлетний срок в должности."],
        ["They defined the term before starting the discussion.", "Они определили термин перед началом обсуждения."]
    ],
    "opposite": [
        ["She sat on the opposite side of the table.", "Она сидела на противоположной стороне стола."],
        ["He will take the opposite approach to solving the problem.",
         "Он выберет противоположный подход к решению проблемы."],
        ["They have opposite opinions on the matter.", "У них противоположные мнения по этому вопросу."]
    ],
    "wife": [
        ["She is a loving wife and mother.", "Она любящая жена и мать."],
        ["He will surprise his wife with flowers.", "Он удивит свою жену цветами."],
        ["They celebrated their anniversary with their wives.", "Они отметили годовщину своих браков со своими женами."]
    ],
    "shoe": [
        ["She tied her shoe laces.", "Она завязала шнурки на своей обуви."],
        ["He will polish his shoes before the interview.", "Он помоет свою обувь перед собеседованием."],
        ["They bought new shoes for the hiking trip.", "Они купили новую обувь для похода в горы."]
    ],
    "shoulder": [
        ["She leaned on his shoulder for support.", "Она оперлась на его плечо для поддержки."],
        ["He will carry the heavy load on his shoulder.", "Он понесет тяжелую ношу на плече."],
        ["They walked shoulder to shoulder down the street.", "Они шли плечом к плечу по улице."]
    ],
    "spread": [
        ["She spread butter on her toast.", "Она намазала масло на свою тост."],
        ["He will spread the news of their engagement.", "Он распространит новость о их помолвке."],
        ["They spread out the picnic blanket on the grass.", "Они разложили пикниковый плед на траве."]
    ],
    "arrange": [
        ["She will arrange the flowers in a vase.", "Она расставит цветы в вазе."],
        ["He arranged the meeting with the client.", "Он организовал встречу с клиентом."],
        ["They arranged the furniture in the living room.", "Они расставили мебель в гостиной."]
    ],
    "camp": [
        ["She went to summer camp as a child.", "Она ходила в летний лагерь в детстве."],
        ["He will set up camp by the lake.", "Он разберет лагерь у озера."],
        ["They enjoyed campfires during their camping trip.",
         "Они наслаждались кострами во время своего похода по кемпингу."]
    ],
    "invent": [
        ["She will invent a new gadget.", "Она изобретет новое устройство."],
        ["He invented a new method for recycling.", "Он изобрел новый метод переработки."],
        ["They invented a game to play with their friends.", "Они придумали игру, чтобы играть с друзьями."]
    ],
    "cotton": [
        ["She wore a cotton dress in the summer.", "Она носила хлопковое платье летом."],
        ["He will buy cotton sheets for the bed.", "Он купит хлопковые простыни для кровати."],
        ["They harvested the cotton from the fields.", "Они собрали хлопок с полей."]
    ],
    "born": [
        ["She was born in a small town.", "Она родилась в маленьком городке."],
        ["He will celebrate his born day with friends.", "Он отпразднует свой день рождения с друзьями."],
        ["They were born on the same day.", "Они родились в один и тот же день."]
    ],
    "determine": [
        ["She will determine the cause of the problem.", "Она определит причину проблемы."],
        ["He determined the best course of action.", "Он определил наилучший план действий."],
        ["They determined the winner of the competition.", "Они определили победителя соревнования."]
    ],
    "quart": [
        ["She bought a quart of milk from the store.", "Она купила кварту молока в магазине."],
        ["He will measure a quart of water for the recipe.", "Он отмерит кварту воды по рецепту."],
        ["They drank a quart of lemonade at the picnic.", "Они выпили кварту лимонада на пикнике."]
    ],
    "nine": [
        ["She woke up at nine o'clock.", "Она проснулась в девять часов."],
        ["He will turn nine years old next week.", "Он исполнится девять лет на следующей неделе."],
        ["They left at nine in the morning.", "Они ушли в девять утра."]
    ],
    "truck": [
        ["She drove a truck for her job.", "Она водила грузовик на работе."],
        ["He will rent a truck for moving.", "Он арендует грузовик для переезда."],
        ["They loaded the furniture onto the moving truck.", "Они загрузили мебель на грузовик для перевозки."]
    ],
    "noise": [
        ["She heard a strange noise in the attic.", "Она услышала странный шум на чердаке."],
        ["He will reduce the noise level in the office.", "Он снизит уровень шума в офисе."],
        ["They complained about the noise from the construction site.", "Они пожаловались на шум с стройки."]
    ],
    "level": [
        ["She checked the level of the liquid in the container.", "Она проверила уровень жидкости в контейнере."],
        ["He will level the playing field for fair competition.",
         "Он выровняет игровое поле для справедливой конкуренции."],
        ["They reached a higher level of understanding.", "Они достигли более высокого уровня понимания."]
    ],
    "chance": [
        ["She took a chance and applied for the job.", "Она рискнула и подала заявку на работу."],
        ["He will give them a chance to explain.", "Он даст им шанс объясниться."],
        ["They had a chance encounter at the cafe.", "У них была случайная встреча в кафе."]
    ],
    "gather": [
        ["She will gather information for the report.", "Она соберет информацию для отчета."],
        ["He gathered his friends for a birthday party.", "Он собрал своих друзей на день рождения."],
        ["They gathered around the campfire to tell stories.",
         "Они собрались вокруг костра, чтобы рассказывать истории."]
    ],
    "shop": [
        ["She went to the grocery shop for milk.", "Она пошла в продуктовый магазин за молоком."],
        ["He will shop online for a new computer.", "Он купит новый компьютер в интернет-магазине."],
        ["They shopped for souvenirs in the gift shop.", "Они покупали сувениры в магазине сувениров."]
    ],
    "stretch": [
        ["She will stretch her muscles before exercising.", "Она разминет свои мышцы перед занятием спортом."],
        ["He stretched the truth to make himself look better.", "Он исказил правду, чтобы выглядеть лучше."],
        ["They stretched the canvas over the wooden frame.", "Они натянули холст на деревянный каркас."]
    ],
    "throw": [
        ["She will throw the ball to her friend.", "Она бросит мяч своему другу."],
        ["He threw away the old newspapers.", "Он выбросил старые газеты."],
        ["They threw a surprise party for his birthday.", "Они устроили сюрприз-вечеринку на его день рождения."]
    ],
    "shine": [
        ["She polished her shoes until they shone.", "Она полировала свою обувь, пока она не засияла."],
        ["He will shine a light on the dark path.", "Он осветит светом темный путь."],
        ["They watched the sun shine through the clouds.", "Они наблюдали, как солнце светит сквозь облака."]
    ],
    "property": [
        ["She inherited the family property.", "Она унаследовала семейное имущество."],
        ["He will invest in rental property.", "Он вложит деньги в арендное имущество."],
        ["They assessed the value of the property.", "Они оценили стоимость имущества."]
    ],
    "column": [
        ["She wrote a column for the newspaper.", "Она писала колонку для газеты."],
        ["He will add a column to the spreadsheet.", "Он добавит колонку в таблицу."],
        ["They read the gossip column in the magazine.", "Они читали колонку о сплетнях в журнале."]
    ],
    "molecule": [
        ["She studied the structure of a water molecule.", "Она изучала структуру молекулы воды."],
        ["He will analyze the interaction between molecules.", "Он проанализирует взаимодействие между молекулами."],
        ["They discussed the chemical properties of molecules.", "Они обсуждали химические свойства молекул."]
    ],
    "select": [
        ["She will select the best candidate for the job.", "Она выберет лучшего кандидата на работу."],
        ["He selected the items he wanted to purchase.", "Он выбрал товары, которые хотел купить."],
        ["They select the winner of the competition.", "Они выбирают победителя соревнования."]
    ],
    "wrong": [
        ["She admitted she was wrong.", "Она признала, что была неправа."],
        ["He will correct his wrong assumptions.", "Он исправит свои неправильные предположения."],
        ["They acknowledged their wrong decision.", "Они признали свое неправильное решение."]
    ],
    "gray": [
        ["The sky turned gray before the storm.", "Небо покрылось серым перед бурей."],
        ["He prefers to wear gray suits to work.", "Он предпочитает носить серые костюмы на работу."],
        ["The cat had gray fur.", "У кошки была серая шерсть."]
    ],
    "repeat": [
        ["Please repeat after me.", "Пожалуйста, повторите за мной."],
        ["He tends to repeat himself often.", "Он часто повторяется."],
        ["The teacher asked him to repeat his answer.", "Учитель попросил его повторить свой ответ."]
    ],
    "require": [
        ["You require a permit to enter the building.", "Для входа в здание вам нужно разрешение."],
        ["He will require more time to finish the project.", "Ему потребуется больше времени, чтобы завершить проект."],
        ["The job will require a lot of effort.", "Эта работа потребует много усилий."]
    ],
    "broad": [
        ["The road was broad and well-maintained.", "Дорога была широкой и хорошо ухоженной."],
        ["She has broad interests, ranging from art to science.", "У нее широкие интересы, от искусства до науки."],
        ["We need to take a broad view of the situation.", "Мы должны взглянуть на ситуацию широко."]
    ],
    "prepare": [
        ["She needs to prepare for her presentation.", "Ей нужно подготовиться к своему выступлению."],
        ["He prepared dinner for his guests.", "Он приготовил ужин для своих гостей."],
        ["They prepare the stage for the performance.", "Они подготавливают сцену для выступления."]
    ],
    "salt": [
        ["She added a pinch of salt to the soup.", "Она добавила щепотку соли в суп."],
        ["Salt is often used to season food.", "Соль часто используется для приправления еды."],
        ["They spread salt on the icy sidewalk.", "Они посыпали соль на замерзший тротуар."]
    ],
    "nose": [
        ["She touched her nose with her finger.", "Она коснулась своего носа пальцем."],
        ["The dog sniffed with its nose.", "Собака нюхала носом."],
        ["He broke his nose in a sports accident.", "Он сломал нос в спортивной аварии."]
    ],
    "plural": [
        ["The word 'cats' is the plural form of 'cat'.", "Слово 'коты' - множественное число слова 'кот'."],
        ["In English, some nouns have irregular plurals.",
         "В английском языке у некоторых существительных неправильные формы множественного числа."],
        ["They discussed the use of plurals in different languages.",
         "Они обсуждали использование множественного числа в разных языках."]
    ],
    "anger": [
        ["She couldn't hide her anger.", "Она не могла скрыть свой гнев."],
        ["His voice rose with anger.", "Его голос повысился от гнева."],
        ["They expressed their anger through protests.", "Они выразили свой гнев через протесты."]
    ],
    "claim": [
        ["He made a claim for compensation.", "Он предъявил требование о компенсации."],
        ["She disputed his claim of ownership.", "Она оспаривала его заявление о владении."],
        ["They will investigate the validity of the claim.", "Они будут расследовать действительность утверждения."]
    ],
    "continent": [
        ["Africa is the second-largest continent.", "Африка - второй по величине континент."],
        ["She dreams of traveling to every continent.", "Она мечтает побывать на каждом континенте."],
        ["They studied the geography of each continent.", "Они изучали географию каждого континента."]
    ],
    "oxygen": [
        ["Plants produce oxygen during photosynthesis.", "Растения вырабатывают кислород во время фотосинтеза."],
        ["He breathed deeply to get more oxygen.", "Он глубоко дышал, чтобы получить больше кислорода."],
        ["They measure the level of oxygen in the atmosphere.", "Они измеряют уровень кислорода в атмосфере."]
    ],
    "sugar": [
        ["She takes her coffee without sugar.", "Она пьет кофе без сахара."],
        ["Sugar is often used as a sweetener.", "Сахар часто используется в качестве подсластителя."],
        ["They avoid foods high in sugar.", "Они избегают продуктов, богатых сахаром."]
    ],
    "death": [
        ["The death of her grandmother affected her deeply.", "Смерть ее бабушки глубоко повлияла на нее."],
        ["They observed a moment of silence to honor the deaths of soldiers.",
         "Они соблюдали минуту молчания в знак уважения к погибшим солдатам."],
        ["He faced the possibility of death with courage.", "Он столкнулся с возможностью смерти с мужеством."]
    ],
    "pretty": [
        ["She wore a pretty dress to the party.", "Она надела красивое платье на вечеринку."],
        ["The garden looked pretty with all the flowers in bloom.", "Сад выглядел красиво со всеми цветами в цвету."],
        ["He found her pretty, but he was more interested in her personality.",
         "Он нашел ее милой, но его больше интересовал ее характер."]
    ],
    "skill": [
        ["He has excellent cooking skills.", "У него отличные навыки в кулинарии."],
        ["She demonstrated her writing skills in the essay.", "Она продемонстрировала свои навыки письма в эссе."],
        ["They admired his skills as a musician.", "Они восхищались его музыкальными навыками."]
    ],
    "women": [
        ["There were more men than women at the meeting.", "На собрании было больше мужчин, чем женщин."],
        ["Women have made significant contributions to science.", "Женщины внесли значительный вклад в науку."],
        ["She is a strong advocate for women's rights.", "Она является крепким сторонником прав женщин."]
    ],
    "season": [
        ["Spring is my favorite season.", "Весна - мое любимое время года."],
        ["They went skiing during the winter season.", "Они поехали кататься на лыжах в зимний сезон."],
        ["The holiday season is a time for family gatherings.", "Праздничный сезон - это время для семейных собраний."]
    ],
    "solution": [
        ["They found a solution to the math problem.", "Они нашли решение математической задачи."],
        ["She proposed a solution to the ongoing conflict.", "Она предложила решение текущего конфликта."],
        ["We need to find a sustainable solution to the environmental crisis.",
         "Нам нужно найти устойчивое решение экологического кризиса."]
    ],
    "magnet": [
        ["The magnet attracted the metal objects.", "Магнит привлекал металлические предметы."],
        ["She found the poetry of the place to be a magnet for inspiration.",
         "Она считала поэзию места магнитом для вдохновения."],
        ["The city's vibrant culture acts as a magnet for tourists.",
         "Живая культура города выступает в качестве магнита для туристов."]
    ],
    "silver": [
        ["She wore a necklace with a silver pendant.", "Она носила ожерелье с серебряным кулоном."],
        ["The moon shone like silver in the night sky.", "Луна светила, как серебро, на ночном небе."],
        ["They received a silver medal for their performance.", "Они получили серебряную медаль за свое выступление."]
    ],
    "thank": [
        ["She sent a thank-you note after the party.", "Она отправила благодарственную записку после вечеринки."],
        ["He expressed his thankfulness for their help.", "Он выразил свою благодарность за их помощь."],
        ["They thanked him for his generous donation.", "Они поблагодарили его за щедрое пожертвование."]
    ],
    "branch": [
        ["The tree had many branches.", "У дерева было много ветвей."],
        ["She works in the finance branch of the company.", "Она работает в финансовом отделе компании."],
        ["They opened a new branch of the store in the city center.",
         "Они открыли новый филиал магазина в центре города."]
    ],
    "match": [
        ["She lit a match to start the fire.", "Она зажгла спичку, чтобы развести огонь."],
        ["The team won the match with a last-minute goal.", "Команда выиграла матч благодаря голу в последнюю минуту."],
        ["They found a match for the missing sock.", "Они нашли пару для потерянного носка."]
    ],
    "suffix": [
        ["The word 'happiness' has the suffix '-ness'.", "Слово 'счастье' имеет суффикс '-ность'."],
        ["She added the suffix '-able' to the verb.", "Она добавила суффикс '-able' к глаголу."],
        ["They discussed the meaning of various suffixes in linguistics class.",
         "Они обсуждали значение различных суффиксов на уроке лингвистики."]
    ],
    "especially": [
        ["He loves Italian food, especially pizza.", "Он любит итальянскую кухню, особенно пиццу."],
        ["She enjoys outdoor activities, especially hiking.",
         "Она любит активный отдых на природе, особенно пешие походы."],
        ["They made an effort to be especially kind to their guests.",
         "Они приложили усилия, чтобы быть особенно добрыми к своим гостям."]
    ],
    "fig": [
        ["She bought a basket of fresh figs from the market.", "Она купила корзину свежих инжиров на рынке."],
        ["The painting depicted a bowl of ripe figs.", "Картина изображала миску спелых инжиров."],
        ["They used dried figs in the dessert recipe.", "Они использовали сушеные инжиры в рецепте десерта."]
    ],
    "afraid": [
        ["He was afraid of the dark as a child.", "Он боялся темноты в детстве."],
        ["She was afraid to speak in front of the large audience.", "Она боялась выступать перед большой аудиторией."],
        ["They were afraid of what might happen next.", "Они боялись, что может произойти дальше."]
    ],
    "huge": [
        ["The elephant was huge.", "Слон был огромным."],
        ["She received a huge bouquet of flowers.", "Ей подарили огромный букет цветов."],
        ["They made a huge effort to finish the project on time.",
         "Они приложили огромные усилия, чтобы закончить проект в срок."]
    ],
    "sister": [
        ["She has a younger sister.", "У нее есть младшая сестра."],
        ["Her sister lives in another city.", "Ее сестра живет в другом городе."],
        ["They share a close bond as sisters.", "У них крепкая связь как у сестер."]
    ],
    "steel": [
        ["The bridge was made of steel.", "Мост был сделан из стали."],
        ["She sharpened the knife on a steel rod.", "Она затачивала нож на стальном пруте."],
        ["They admired the sleek lines of the steel sculpture.",
         "Они восхищались гладкими линиями стальной скульптуры."]
    ],
    "discuss": [
        ["They need to discuss the terms of the contract.", "Им нужно обсудить условия контракта."],
        ["She discussed her concerns with her supervisor.", "Она обсудила свои опасения со своим надзирателем."],
        ["They will discuss the matter further at the next meeting.",
         "Они еще обсудят этот вопрос на следующем собрании."]
    ],
    "forward": [
        ["She moved forward with her plans.", "Она продвигалась вперед со своими планами."],
        ["He leaned forward to hear better.", "Он наклонился вперед, чтобы лучше слышать."],
        ["They took a step forward in their relationship.", "Они сделали шаг вперед в своих отношениях."]
    ],
    "similar": [
        ["The two paintings are very similar.", "Эти две картины очень похожи."],
        ["She chose a dress similar to her friend's.", "Она выбрала платье, похожее на платье ее подруги."],
        ["They have similar tastes in music.", "У них схожие вкусы в музыке."]
    ],
    "guide": [
        ["The tour guide showed them around the city.", "Экскурсовод показал им город."],
        ["She used a map as a guide for her hike.",
         "Она использовала карту в качестве путеводителя для своего похода."],
        ["They followed the guide's instructions carefully.", "Они внимательно следовали инструкциям гида."]
    ],
    "experience": [
        ["She gained valuable experience from her internship.", "Она получила ценный опыт от своей стажировки."],
        ["He has years of experience in the industry.", "У него многолетний опыт в этой отрасли."],
        ["They offer an unforgettable experience for tourists.", "Они предлагают незабываемый опыт для туристов."]
    ],
    "score": [
        ["She scored the winning goal in the final.", "Она забила победный гол в финале."],
        ["They keep track of the score during the game.", "Они следят за счетом во время игры."],
        ["He achieved a perfect score on the test.", "Он получил идеальный балл на тесте."]
    ],
    "apple": [
        ["She packed an apple in her lunch.", "Она положила яблоко в свой ланч."],
        ["He bit into a crisp apple.", "Он укусил хрустящее яблоко."],
        ["They picked apples at the orchard.", "Они собирали яблоки в саду."]
    ],
    "bought": [
        ["She bought a new dress for the party.", "Она купила новое платье на вечеринку."],
        ["He bought a gift for his sister's birthday.", "Он купил подарок на день рождения своей сестры."],
        ["They bought tickets for the concert online.", "Они купили билеты на концерт в интернете."]
    ],
    "led": [
        ["He led the team to victory.", "Он повел команду к победе."],
        ["She led the discussion at the meeting.", "Она возглавила дискуссию на собрании."],
        ["They followed the path that led to the waterfall.", "Они пошли по тропинке, ведущей к водопаду."]
    ],
    "pitch": [
        ["She pitched the idea to her boss.", "Она представила идею своему начальнику."],
        ["The pitcher threw the ball with great pitch.", "Питчер бросил мяч с большой силой."],
        ["They set up their tent on a flat pitch.", "Они поставили свой палаточный лагерь на ровном участке."]
    ],
    "coat": [
        ["She put on her coat before going outside.", "Она надела пальто, прежде чем выйти на улицу."],
        ["He painted the walls with a fresh coat of paint.", "Он покрасил стены свежим слоем краски."],
        ["They walked along the beach, feeling the sea breeze on their coats.",
         "Они шли по пляжу, ощущая морской бриз на своих пальто."]
    ],
    "mass": [
        ["The spacecraft has a large mass.", "Космический корабль имеет большую массу."],
        ["She felt a mass of emotions after the news.", "Она почувствовала массу эмоций после новостей."],
        ["They studied the effect of mass on gravitational force.", "Они изучали влияние массы на гравитационную силу."]
    ],
    "card": [
        ["She wrote a birthday card for her friend.", "Она написала открытку с днем рождения своей подруге."],
        ["He shuffled the deck of cards.", "Он перетасовал колоду карт."],
        ["They played cards late into the night.", "Они играли в карты до поздней ночи."]
    ],
    "band": [
        ["She wore a rubber band in her hair.", "Она носила резинку для волос на голове."],
        ["He played guitar in a rock band.", "Он играл на гитаре в рок-группе."],
        ["They formed a marching band for the parade.", "Они создали духовой оркестр для парада."]
    ],
    "rope": [
        ["She tied the package with a rope.", "Она привязала пакет веревкой."],
        ["He climbed the mountain with a rope.", "Он поднялся на гору с помощью веревки."],
        ["They used a rope to pull the boat ashore.", "Они использовали веревку, чтобы вытащить лодку на берег."]
    ],
    "slip": [
        ["She almost slipped on the wet floor.", "Она чуть не поскользнулась на мокром полу."],
        ["He wore shoes with a rubber sole to prevent slipping.",
         "Он носил обувь с резиновой подошвой,\nчтобы предотвратить скольжение."],
        ["They watched the boat slip away into the distance.", "Они наблюдали, как лодка удаляется в даль."]
    ],
    "win": [
        ["She won first place in the competition.", "Она заняла первое место в соревновании."],
        ["He won the lottery and became a millionaire.", "Он выиграл в лотерею и стал миллионером."],
        ["They won the game with a last-minute goal.", "Они выиграли игру благодаря голу в последнюю минуту."]
    ],
    "dream": [
        ["She had a vivid dream about flying.", "У нее была яркая мечта о полете."],
        ["He pursued his dream of becoming a musician.", "Он преследовал свою мечту стать музыкантом."],
        ["They shared their dreams for the future.", "Они поделились своими мечтами о будущем."]
    ],
    "evening": [
        ["They went for a walk in the evening.", "Они пошли на прогулку вечером."],
        ["She enjoys reading in the evening.", "Она любит читать вечером."],
        ["They had dinner together in the evening.", "Они поужинали вместе вечером."]
    ],
    "condition": [
        ["The car was in excellent condition.", "Машина была в отличном состоянии."],
        ["She accepted the job offer conditionally.", "Она приняла предложение о работе под определенными условиями."],
        ["They set strict conditions for the agreement.", "Они установили строгие условия для соглашения."]
    ],
    "feed": [
        ["She feeds her cat twice a day.", "Она кормит своего кота дважды в день."],
        ["The farmer feeds the livestock in the morning.", "Фермер кормит скот по утрам."],
        ["They feed on fruits and vegetables.", "Они питаются фруктами и овощами."]
    ],
    "tool": [
        ["He used a hammer as a tool.", "Он использовал молоток в качестве инструмента."],
        ["She has a set of gardening tools.", "У нее есть набор садовых инструментов."],
        ["They need specialized tools for the job.", "Им нужны специализированные инструменты для работы."]
    ],
    "total": [
        ["The total cost of the project was high.", "Общая стоимость проекта была высокой."],
        ["She spent a total of three hours studying.", "Она потратила в общей сложности три часа на учебу."],
        ["They received a total of five complaints.", "Они получили в общей сложности пять жалоб."]
    ],
    "basic": [
        ["She has a basic understanding of the topic.", "У нее есть базовое понимание темы."],
        ["He taught her the basic principles of math.", "Он научил ее основным принципам математики."],
        ["They offer courses in basic computer skills.", "Они предлагают курсы по основным компьютерным навыкам."]
    ],
    "smell": [
        ["She detected a strange smell in the kitchen.", "Она почувствовала странный запах на кухне."],
        ["The flowers had a sweet smell.", "Цветы пахли сладким запахом."],
        ["They noticed a foul smell coming from the garbage.", "Они заметили вонючий запах, исходящий из мусора."]
    ],
    "valley": [
        ["They hiked through the valley.", "Они совершили поход через долину."],
        ["The valley was surrounded by mountains.", "Долина была окружена горами."],
        ["She grew up in a small valley town.", "Она выросла в небольшом городке в долине."]
    ],
    "nor": [
        ["Neither he nor she could solve the puzzle.", "Ни он, ни она не смогли разгадать головоломку."],
        ["He didn't speak, nor did she.", "Он не говорил, и она тоже."],
        ["They found neither the book nor the pen.", "Они не нашли ни книги, ни ручки."]
    ],
    "double": [
        ["She doubled the recipe to make more cookies.", "Она удвоила рецепт, чтобы испечь больше печенья."],
        ["He earns double what I earn.", "Он зарабатывает вдвое больше, чем я."],
        ["The company doubled its profits last year.", "Компания удвоила свою прибыль в прошлом году."]
    ],
    "seat": [
        ["She found a seat near the window.", "Она нашла место рядом с окном."],
        ["He reserved a seat for the concert.", "Он забронировал место на концерт."],
        ["They were seated at the back of the plane.", "Их посадили в задней части самолета."]
    ],
    "arrive": [
        ["They arrive at the airport early.", "Они прибывают в аэропорт рано."],
        ["The train will arrive at 3 PM.", "Поезд прибудет в 15:00."],
        ["She arrived at the conclusion after much thought.", "Она пришла к заключению после долгих размышлений."]
    ],
    "master": [
        ["He is a master of his craft.", "Он мастер своего дела."],
        ["She mastered the art of cooking.", "Она овладела искусством готовки."],
        ["They must master the basics before moving on.", "Они должны овладеть основами, прежде чем идти дальше."]
    ],
    "track": [
        ["They followed the track through the forest.", "Они следовали по тропинке через лес."],
        ["She lost the track of time.", "Она потеряла чувство времени."],
        ["He keeps track of his expenses.", "Он ведет учет своих расходов."]
    ],
    "parent": [
        ["She is a single parent.", "Она мать-одиночка."],
        ["He is a loving parent.", "Он заботливый родитель."],
        ["They attended a meeting with their child's teacher and other parents.",
         "Они посетили собрание с учителем своего ребенка и другими родителями."]
    ],
    "shore": [
        ["They walked along the shore.", "Они гуляли вдоль берега."],
        ["She collected seashells on the shore.", "Она собирала ракушки на берегу."],
        ["They built a sandcastle near the shore.", "Они построили песчаный замок недалеко от берега."]
    ],
    "division": [
        ["The country is divided into states.", "Страна разделена на штаты."],
        ["She heads the marketing division.", "Она возглавляет маркетинговое подразделение."],
        ["They studied long division in math class.", "Они изучали деление с остатком на уроке математики."]
    ],
    "sheet": [
        ["She spread a sheet on the bed.", "Она расстелила простыню на кровати."],
        ["He covered himself with a sheet.", "Он накрыл себя простыней."],
        ["They filled out a balance sheet for the company.", "Они заполнили балансовую ведомость для компании."]
    ],
    "substance": [
        ["The substance of the argument was important.", "Суть аргумента была важной."],
        ["She investigated the chemical substance.", "Она исследовала химическое вещество."],
        ["They discussed the substance of the proposal.", "Они обсудили суть предложения."]
    ],
    "favor": [
        ["He did me a favor by helping.", "Он оказал мне услугу, помогая."],
        ["She asked for a favor from her friend.", "Она попросила одолжения у своего друга."],
        ["They returned the favor with a gift.", "Они отблагодарили подарком."]
    ],
    "connect": [
        ["They connect the dots to reveal the image.", "Они соединяют точки, чтобы раскрыть изображение."],
        ["She needs to connect the printer to the computer.", "Ей нужно подключить принтер к компьютеру."],
        ["He wants to connect with people from different cultures.",
         "Он хочет установить контакт с людьми из разных культур."]
    ],
    "post": [
        ["She wrote a post on social media.", "Она написала пост в социальных сетях."],
        ["He applied for a post at the company.", "Он подал заявку на должность в компании."],
        ["They received a postcard from their friend.", "Они получили открытку от своего друга."]
    ],
    "spend": [
        ["She spends her weekends hiking.", "Она проводит выходные в походах."],
        ["He spends too much money on clothes.", "Он тратит слишком много денег на одежду."],
        ["They spent a week in Paris.", "Они провели неделю в Париже."]
    ],
    "chord": [
        ["She played a beautiful chord on the guitar.", "Она сыграла красивый аккорд на гитаре."],
        ["He studied the chord progression for the song.", "Он изучал последовательность аккордов для песни."],
        ["They heard the chord change in the music.", "Они услышали изменение аккорда в музыке."]
    ],
    "fat": [
        ["She avoided eating fatty foods.", "Она избегала употребления жирной пищи."],
        ["He is trying to lose weight by reducing fat intake.", "Он пытается похудеть, уменьшая потребление жира."],
        ["They used animal fat for cooking.", "Они использовали животный жир для готовки."]
    ],
    "glad": [
        ["She was glad to see her old friend.", "Она была рада увидеть своего старого друга."],
        ["He was glad that the meeting went well.", "Он был рад, что встреча прошла успешно."],
        ["They were glad for the opportunity.", "Они были рады возможности."]
    ],
    "original": [
        ["She owns an original painting by Picasso.", "У нее есть оригинальная картина Пикассо."],
        ["He prefers original music over covers.", "Он предпочитает оригинальную музыку каверам."],
        ["They wanted to keep the original design.", "Они хотели сохранить первоначальный дизайн."]
    ],
    "share": [
        ["She likes to share her experiences with others.", "Она любит делиться своими впечатлениями с другими."],
        ["He received a fair share of the profits.", "Он получил справедливую долю прибыли."],
        ["They share a common goal.", "У них общая цель."]
    ],
    "station": [
        ["They met at the train station.", "Они встретились на железнодорожной станции."],
        ["She works as a radio announcer at the station.", "Она работает ведущей радио на станции."],
        ["He switched off the television at the station break.", "Он выключил телевизор во время перерыва в передаче."]
    ],
    "dad": [
        ["Her dad taught her how to ride a bike.", "Ее отец научил ее кататься на велосипеде."],
        ["He calls his dad every Sunday.", "Он звонит своему отцу каждое воскресенье."],
        ["They celebrated Father's Day with their dad.", "Они отметили День отца с своим папой."]
    ],
    "bread": [
        ["She bought a loaf of bread from the bakery.", "Она купила буханку хлеба в пекарне."],
        ["He likes to make his own bread.", "Он любит печь свой собственный хлеб."],
        ["They spread butter on the bread.", "Они намазали масло на хлеб."]
    ],
    "charge": [
        ["She forgot to charge her phone overnight.", "Она забыла зарядить свой телефон на ночь."],
        ["He will take charge of the project.", "Он возьмет на себя руководство проектом."],
        ["They were arrested on a charge of theft.", "Их арестовали по обвинению в краже."]
    ],
    "proper": [
        ["She followed the proper procedure.", "Она следовала правильной процедуре."],
        ["He wore proper attire for the interview.", "Он надел подходящую одежду на собеседование."],
        ["They need proper equipment for the job.", "Им нужно правильное оборудование для работы."]
    ],
    "bar": [
        ["They went to the bar for drinks.", "Они пошли в бар выпить."],
        ["She passed the bar exam on her first attempt.", "Она сдала экзамен на право практики с первой попытки."],
        ["He installed a security bar on the window.", "Он установил защитные решетки на окна."]
    ],
    "offer": [
        ["She received a job offer from the company.", "Она получила предложение о работе от компании."],
        ["He declined the offer politely.", "Он вежливо отказался от предложения."],
        ["They made an offer to buy the house.", "Они сделали предложение купить дом."]
    ],
    "segment": [
        ["She cut the orange into segments.", "Она разрезала апельсин на дольки."],
        ["He divided the speech into segments.", "Он разделил выступление на сегменты."],
        ["They analyzed each segment of the market.", "Они проанализировали каждый сегмент рынка."]
    ],
    "slave": [
        ["He was forced to work as a slave.", "Его заставили работать как раба."],
        ["She felt like a slave to her job.", "Она чувствовала себя рабыней своей работы."],
        ["They fought to free the slaves.", "Они боролись за освобождение рабов."]
    ],
    "duck": [
        ["They saw a duck swimming in the pond.", "Они увидели утку, плавающую в пруду."],
        ["She ducked to avoid hitting her head.", "Она уклонилась, чтобы не удариться головой."],
        ["He had duck for dinner.", "Он поужинал уткой."]
    ],
    "instant": [
        ["She made instant coffee in the morning.", "Она приготовила растворимый кофе утром."],
        ["He became an instant success.", "Он моментально стал успешным."],
        ["They needed an instant solution to the problem.", "Им нужно было мгновенное решение проблемы."]
    ],
    "market": [
        ["She went to the market to buy fresh vegetables.", "Она пошла на рынок купить свежие овощи."],
        ["He works in the stock market.", "Он работает на фондовом рынке."],
        ["They analyzed the market trends.", "Они проанализировали тенденции рынка."]
    ],
    "degree": [
        ["She earned a degree in psychology.", "Она получила степень в психологии."],
        ["He has a master's degree.", "У него степень магистра."],
        ["They measured the angle in degrees.", "Они измерили угол в градусах."]
    ],
    "populate": [
        ["The island is sparsely populated.", "Остров населен слабо."],
        ["He studied how animals populate different environments.", "Он изучал, как животные населяют разные среды."],
        ["They aimed to populate the database with accurate information.",
         "Они стремились заполнить базу данных точной информацией."]
    ],
    "chick": [
        ["They watched the baby chicks hatch.", "Они наблюдали, как вылуплялись цыплята."],
        ["She found a lost chick in the yard.", "Она нашла потерянного цыпленка на дворе."],
        ["He cooked a delicious chickpea curry.", "Он приготовил вкусное чечевичное карри."]
    ],
    "dear": [
        ["She received a letter from her dear friend.", "Она получила письмо от своего дорогого друга."],
        ["He paid a dear price for his mistake.", "Он заплатил дорогую цену за свою ошибку."],
        ["They hold dear the memories of their childhood.", "Они дорожат воспоминаниями о своем детстве."]
    ],
    "enemy": [
        ["They considered him their enemy.", "Они считали его своим врагом."],
        ["She fought against a common enemy.", "Она боролась против общего врага."],
        ["He made many enemies with his harsh words.", "Он нажил себе много врагов своими резкими словами."]
    ],
    "reply": [
        ["She replied to the email promptly.", "Она ответила на письмо немедленно."],
        ["He waited for a reply to his question.", "Он ждал ответа на свой вопрос."],
        ["They received no reply to their request.", "Они не получили ответа на свою просьбу."]
    ],
    "drink": [
        ["She likes to drink herbal tea before bed.", "Она любит пить травяной чай перед сном."],
        ["He ordered a cold drink at the café.", "Он заказал холодный напиток в кафе."],
        ["They served drinks at the party.", "На вечеринке подавали напитки."]
    ],
    "occur": [
        ["The accident occurred on a rainy day.", "Авария произошла в дождливый день."],
        ["He wondered how the mistake could occur.", "Он удивлялся, как могла произойти ошибка."],
        ["They hoped the meeting would occur without any issues.", "Они надеялись, что встреча пройдет без проблем."]
    ],
    "support": [
        ["She offered her support to the family.", "Она предложила свою поддержку семье."],
        ["He needed emotional support during the difficult time.",
         "Ему нужна была эмоциональная поддержка в трудное время."],
        ["They provided financial support for the project.", "Они предоставили финансовую поддержку проекту."]
    ],
    "speech": [
        ["She gave a moving speech at the ceremony.", "Она произнесла трогательную речь на церемонии."],
        ["He listened to the president's speech.", "Он слушал речь президента."],
        ["They practiced their speeches for the debate.", "Они отрабатывали свои выступления для дебатов."]
    ],
    "nature": [
        ["She enjoys spending time in nature.", "Она любит проводить время на природе."],
        ["He studied the behavior of animals in nature.", "Он изучал поведение животных в природе."],
        ["They appreciate the beauty of nature.", "Они ценят красоту природы."]
    ],
    "range": [
        ["They explored a wide range of options.", "Они исследовали широкий спектр вариантов."],
        ["She has a broad range of interests.", "У нее широкий круг интересов."],
        ["He bought a rifle with a long range.", "Он купил ружье с большим дальнобойным действием."]
    ],
    "steam": [
        ["She cooked vegetables using steam.", "Она готовила овощи на пару."],
        ["He prefers to travel by steam train.", "Он предпочитает путешествовать на паровозе."],
        ["They saw steam rising from the kettle.", "Они увидели, как поднимался пар из чайника."]
    ],
    "motion": [
        ["She detected motion in the bushes.", "Она заметила движение в кустах."],
        ["He studied the laws of motion.", "Он изучал законы движения."],
        ["They recorded the motion of the planets.", "Они записывали движение планет."]
    ],
    "path": [
        ["They walked along the path in the forest.", "Они гуляли по тропинке в лесу."],
        ["She chose a different path in life.", "Она выбрала другой путь в жизни."],
        ["He cleared the path of fallen branches.", "Он расчистил тропинку от упавших веток."]
    ],
    "liquid": [
        ["She spilled the liquid on the table.", "Она пролила жидкость на стол."],
        ["He filled the glass with a clear liquid.", "Он наполнил стакан прозрачной жидкостью."],
        ["They transferred the liquid into containers.", "Они перелили жидкость в контейнеры."]
    ],
    "log": [
        ["They sat on a log by the campfire.", "Они сидели на полено у костра."],
        ["She keeps a log of her workouts.", "Она ведет журнал тренировок."],
        ["He examined the log for signs of termites.", "Он проверил бревно на наличие термитов."]
    ],
    "meant": [
        ["She meant to call, but forgot.", "Она собиралась позвонить, но забыла."],
        ["He realized what she meant by her words.", "Он понял, что она имела в виду своими словами."],
        ["They meant no harm.", "Они не имели в виду никакого вреда."]
    ],
    "quotient": [
        ["She calculated the quotient.", "Она вычислила частное."],
        ["He divided the numbers to find the quotient.", "Он разделил числа, чтобы найти частное."],
        ["They learned about division and quotients in math class.",
         "Они узнали о делении и частных на уроке математики."]
    ],
    "teeth": [
        ["She brushed her teeth before bed.", "Она почистила зубы перед сном."],
        ["He clenched his teeth to stop himself from shouting.", "Он стиснул зубы, чтобы не закричать."],
        ["They counted the teeth on the gear.", "Они посчитали зубцы на шестерне."]
    ],
    "shell": [
        ["She found a seashell on the beach.", "Она нашла морскую раковину на пляже."],
        ["He cracked open the shell to reveal the nut inside.", "Он разбил ракушку, чтобы показать орех внутри."],
        ["They used a shell as a makeshift bowl.", "Они использовали раковину в качестве самодельной миски."]
    ],
    "neck": [
        ["She wore a necklace around her neck.", "Она носила ожерелье на шее."],
        ["He felt a pain in his neck.", "Он почувствовал боль в шее."],
        ["They hugged each other around the neck.", "Они обняли друг друга за шеи."]
    ]
}
json_string = json.dumps(super_dict, ensure_ascii=False, indent=2)

with open('exemples.json', 'w', encoding='utf-8') as json_file:
    json.dump(super_dict, json_file, ensure_ascii=False, indent=2)
