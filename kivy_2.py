from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, SwapTransition
from kivy.uix.textinput import TextInput
from kivy.uix.recycleview import RecycleView
from kivy.uix.scrollview import ScrollView
import random
from g4f.client import Client
import pandas
import os
import csv
from super_j import super_dict
from kivy.uix.spinner import Spinner
from kivy.graphics import Rectangle, Color, RoundedRectangle
from difflib import SequenceMatcher
from kivy.uix.widget import Widget
from scipy.io.wavfile import read
import sounddevice as sd

Window.size = (432, 768)
Window.title = 'LexiLearn'
client = Client()

filename = "comp_words.csv"


class PressableButton(Widget):
    def __init__(self, text="", font_size=18, color=(0.2, 0.6, 0.8, 1), shadow_color=(0.1, 0.4, 0.6, 1),
                 on_release_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.color = color if len(color) == 4 else self.rgb_to_kivy_color(color)
        self.shadow_color = shadow_color if len(shadow_color) == 4 else self.rgb_to_kivy_color(shadow_color)
        self.text = text
        self.font_size = font_size
        self.shadow_height = 10  # Высота тени
        self.on_release_callback = on_release_callback  # Сохраняем callback для обработки

        # Размеры кнопки
        self.size = kwargs.get("size", (300, 100))
        self.pos = kwargs.get("pos", (100, 200))

        # Рисуем кнопку и тень
        with self.canvas:
            # Тень
            self.shadow_color_instruction = Color(*self.shadow_color)
            self.shadow = RoundedRectangle(size=(self.size[0], self.size[1]),
                                           pos=(self.pos[0], self.pos[1] - self.shadow_height), radius=[20])

            # Кнопка
            self.color_instruction = Color(*self.color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

        # Добавляем текстовый лейбл
        self.label = Label(
            text=self.text,
            halign="center",
            valign="middle",
            size=self.size,
            pos=self.pos,
            font_size=self.font_size,
            font_name="IntroDemo-BlackCAPS.otf",
            color=(1, 1, 1, 1)  # Белый текст
        )
        self.add_widget(self.label)

        # Добавляем обработчики событий
        self.bind(pos=self.update_graphics, size=self.update_graphics)

    @staticmethod
    def rgb_to_kivy_color(rgb, alpha=1.0):
        """Конвертирует цвет из RGB (0-255) в формат Kivy RGBA (0-1)."""
        return tuple(channel / 255 for channel in rgb) + (alpha,)

    def update_graphics(self, *args):
        """Обновление графики при изменении размера или положения."""
        self.shadow.size = self.size
        self.shadow.pos = (self.pos[0], self.pos[1] - self.shadow_height)
        self.rect.size = self.size
        self.rect.pos = self.pos

        # Обновляем текстовый лейбл
        self.label.size = self.size
        self.label.pos = self.pos

    def on_touch_down(self, touch):
        """Обработка нажатия на кнопку."""

        # Проверка попадания в область кнопки с учетом положения
        if self.collide_point(*touch.pos):
            self.pos = (self.pos[0], self.pos[1] - self.shadow_height)  # Опускаем кнопку
            self.shadow_color_instruction.a = 0  # Прячем тень
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        """Обработка отжатия кнопки."""

        # Проверяем, произошло ли отпускание внутри кнопки с учетом положения
        if self.collide_point(*touch.pos):
            self.pos = (self.pos[0], self.pos[1] + self.shadow_height)  # Поднимаем кнопку
            self.shadow_color_instruction.a = 1  # Показываем тень

            # Вызываем callback при отпускании кнопки
            if self.on_release_callback:
                self.on_release_callback()
            return True
        return super().on_touch_up(touch)


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.all_clear = Button(text="Сброс прогресса", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)
        self.all_clear.bind(on_release=self.all_clear_event)

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)
        self.toolbar.add_widget(Label())
        self.toolbar.add_widget(self.back_button)

        self.box_for_clear = BoxLayout(orientation='horizontal', padding=[20])
        self.box_for_clear.add_widget(Label())
        self.box_for_clear.add_widget(self.all_clear)
        self.box_for_clear.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[20])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.box_for_clear)
        self.layout.add_widget(Label())
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def all_clear_event(self, *args):
        with open("comp_words.csv", mode='w', newline='') as file:
            pass

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos


class AllWordsScreen(Screen):
    def __init__(self, **kwargs):
        super(AllWordsScreen, self).__init__(**kwargs)

        # Кнопка "Назад"
        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)

        # Кнопка "Поиск"
        self.search_button = Button(text="Поиск", size_hint=(None, None), size=(150, 75))
        self.search_button.bind(on_release=self.search_proc)

        # Виджет для поиска
        self.search_widget = TextInput(size_hint_y=None, height=75)

        # Заголовок с названием слова
        self.label = Label(
            halign='center',
            valign='middle',
            size_hint_y=None,
            text="\n\nВведите слово для поиска\n\n",
            font_size=24,
        )
        self.label.bind(texture_size=self._resize_label)

        # Виджет для примеров предложений
        self.label2 = Label(
            halign='center',
            valign='top',
            size_hint_y=None,
            font_size=18,
        )
        self.label2.bind(texture_size=self._resize_label)

        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.text_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=[10], spacing=10)
        self.text_layout.bind(minimum_height=self.text_layout.setter('height'))

        self.text_layout.add_widget(self.label)
        self.text_layout.add_widget(self.label2)
        self.scroll_view.add_widget(self.text_layout)

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar.add_widget(self.search_widget)
        self.toolbar.add_widget(self.back_button)

        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar2.add_widget(Label())
        self.toolbar2.add_widget(self.search_button)
        self.toolbar2.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[20])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.toolbar2)
        self.add_widget(self.layout)

        self.bind(width=self._update_text_sizes)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет высоту виджета в зависимости от его содержания."""
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        """Обновляет размеры текстовых областей."""
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)

    def go_back(self, *args):
        """Возврат к предыдущему экрану."""
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def search_proc(self, *args):
        """Поиск слова и отображение примеров."""
        self.word = self.search_widget.text
        if self.word in super_dict.keys():
            # Формирование текста с примерами предложений
            text_ex = "Примеры предложений:\n\n"
            for example_pair in super_dict[self.word]:
                text_ex += f"{example_pair[0]}\n{example_pair[1]}\n\n"

            self.label.text = f"\n\nВаше слово: {self.word}\n\n"
            self.label2.text = text_ex
        elif self.word == '':
            self.label.text = f"Введите слово в поле выше"
            self.label2.text = ''
        else:
            self.label.text = f"Слово не найдено"
            self.label2.text = 'Проверьте правильность написания слова\n\n' \
                               'Если не помогло, то слова нет в базе\n' \
                               ' из 1000 самых используемых слов в английском языке'

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label2.text_size = (self.width - 40, None)


class WordShow(Screen):
    def __init__(self, word, **kwargs):
        super(WordShow, self).__init__(**kwargs)

        # Кнопка "Назад"
        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)

        # Заголовок с названием слова
        self.label = Label(
            halign='center',
            valign='middle',
            size_hint_y=None,
            text=f"Ваше слово: {word}",
            font_size=24,  # Увеличение шрифта заголовка
        )
        self.label.bind(texture_size=self._resize_label)

        # Виджет для примеров предложений
        self.label2 = Label(
            halign='center',
            valign='top',
            size_hint_y=None,
            text_size=(self.width - 40, None),  # Автоматический перенос текста
            font_size=18,  # Размер шрифта для текста примеров
        )
        self.label2.bind(texture_size=self._resize_label)

        # Прокручиваемая область для длинного текста
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.text_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=[10])
        self.text_layout.bind(minimum_height=self.text_layout.setter('height'))

        self.text_layout.add_widget(self.label)  # Добавляем заголовок
        self.text_layout.add_widget(self.label2)  # Добавляем примеры
        self.scroll_view.add_widget(self.text_layout)

        # Верхняя панель
        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar.add_widget(Label())
        self.toolbar.add_widget(self.back_button)

        # Основной лейаут
        self.layout = BoxLayout(orientation='vertical', padding=[20])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)

        # Обновляем содержимое
        self.update_content(word)

        # Цвет фона
        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет высоту виджета в зависимости от его содержания."""
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def update_content(self, word):
        """Обновляет содержимое для нового слова."""
        self.label.text = f"\n\nВаше слово: {word}\n\n"
        self.label2.text = self._get_examples(word)

    def _get_examples(self, word):
        """Формирует текст с примерами предложений для слова."""
        examples = super_dict.get(word, [])
        if not examples:
            return "Примеры предложений отсутствуют."

        # Форматирование примеров предложений
        text_ex = "Примеры предложений:\n\n"
        for example_pair in examples:
            text_ex += f"{example_pair[0]}\n{example_pair[1]}\n\n"
        return text_ex

    def go_back(self, *args):
        """Возврат к предыдущему экрану."""
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_words'

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label2.text_size = (self.width - 40, None)


class TheoryScreen(Screen):
    def __init__(self, **kwargs):
        super(TheoryScreen, self).__init__(**kwargs)

        # Кнопка "Назад"
        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)

        # Кнопка "Озвучка слов"
        self.vol_button = Button(text="Озвучка слов", size_hint=(None, None), size=(150, 75))

        # Кнопка "Сгенерировать слово"
        self.next_button = Button(text="Сгенирировать слово", size_hint=(None, None), size=(200, 75))
        self.next_button.bind(on_release=self.text_load)

        # Кнопка "Добавить в конспект"
        self.jorn_button = Button(text="Добавить в конспект", size_hint=(1, None), height=60)

        # Кнопка "Больше примеров"
        self.more_ex_button = Button(text="Больше примеров", size_hint=(1, None), height=60)
        self.more_ex_button.bind(on_release=self.more_w)

        # Верхняя панель
        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)
        self.toolbar.add_widget(self.vol_button)
        self.toolbar.add_widget(Label())
        self.toolbar.add_widget(self.back_button)

        # Нижняя панель
        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=100)
        self.toolbar2.add_widget(Label())
        self.toolbar2.add_widget(self.next_button)
        self.toolbar2.add_widget(Label())

        # Прокручиваемая область
        self.scroll_view = ScrollView(size_hint=(1, 1))

        # Лейаут для текста внутри ScrollView
        self.text_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=[10], spacing=10)
        self.text_layout.bind(minimum_height=self.text_layout.setter('height'))

        # Текстовые метки
        self.label = Label(
            halign='center',
            valign='middle',
            size_hint_y=None,
            text="\nНажмите на кнопку 'Сгенирировать слово'\nчтобы мы подобрали вам слово",
            font_size=24,
        )
        self.label.bind(texture_size=self._resize_label)

        self.label2 = Label(
            halign='center',
            valign='top',
            size_hint_y=None,
            font_size=18,
        )
        self.label2.bind(texture_size=self._resize_label)

        # Добавляем метки в текстовый лейаут
        self.text_layout.add_widget(self.label)
        self.text_layout.add_widget(self.label2)

        # Добавляем текстовый лейаут в прокручиваемую область
        self.scroll_view.add_widget(self.text_layout)

        # Основной лейаут
        self.main_layout = BoxLayout(orientation='vertical', padding=[20])

        # Лейаут для дополнительных кнопок
        self.func_layout2 = BoxLayout(size_hint_y=None, height=75)
        self.func_layout2.add_widget(self.jorn_button)
        self.func_layout2.add_widget(self.more_ex_button)

        # Добавляем все элементы в основной лейаут
        self.main_layout.add_widget(self.toolbar)
        self.main_layout.add_widget(self.scroll_view)  # ScrollView занимает всё оставшееся пространство
        self.main_layout.add_widget(self.func_layout2)
        self.main_layout.add_widget(self.toolbar2)

        self.add_widget(self.main_layout)
        self.bind(width=self._update_text_sizes)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def go_back(self, *args):
        """Возврат к предыдущему экрану."""
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет высоту виджета в зависимости от его содержания."""
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        """Обновляет размеры текстовых областей."""
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)

    def read_csv_as_list(self):
        """Чтение CSV файла."""
        filename = "comp_words.csv"
        data_list = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.extend(row)
            file.close()
        return data_list

    def get_random_word_not_in_csv(self):
        """Получение случайного слова, отсутствующего в CSV."""
        comp_words = self.read_csv_as_list()

        with open("1-1000.txt", "r") as file:
            text_words = file.read().split()
            file.close()

        available_words = [word for word in text_words if word not in comp_words]

        if available_words:
            random_word = random.choice(available_words)
            return random_word
        else:
            return None

    def csv_write(self, rand_word):
        """Запись слова в CSV."""
        filename = "comp_words.csv"
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([rand_word])
            file.close()

    def text_load(self, *args):
        """Загрузка случайного слова и примеров предложений."""
        self.rand_word = self.get_random_word_not_in_csv()
        self.csv_write(self.rand_word)
        self.text_ex = f'Примеры предложений:\n\n{super_dict[self.rand_word][0][0]}\n' \
                       f'{super_dict[self.rand_word][0][1]}\n\n{super_dict[self.rand_word][1][0]}\n' \
                       f'{super_dict[self.rand_word][1][1]}\n\n{super_dict[self.rand_word][2][0]}\n' \
                       f'{super_dict[self.rand_word][2][1]}\n\n'
        self.label.text = f"\n\nВаше слово {self.rand_word}\n\n"
        self.label2.text = self.text_ex
        self.next_button.text = 'Следущее слово'

    def more_w(self, *args):
        """Генерация дополнительных примеров предложений."""
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user",
                           "content": f"make 3 examples of sentences in English using the word {self.rand_word}"
                                      " After each sentence, put a ' / ' sign and write a translation into Russian."
                                      " Do not keep the numbering of "
                                      "sentences. Sample sentences should be no longer than 65 characters. "
                                      "Example of formatting: Не admitted that he was lost. / Он признал, что заблудился."}])
            text = response.choices[0].message.content
            self.final_gen = str()
            text_list_form = [i.split(' / ') for i in text.split('\n') if i.strip()]
            for i in text_list_form:
                self.final_gen += f'{i[0]}\n{i[1]}\n\n'
            self.label2.text += self.final_gen
        except Exception as e:
            self.label2.text += 'Функция доп. примеров\nвременно недоступна'

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label2.text_size = (self.width - 40, None)


class PracticeScreen(Screen):
    def __init__(self, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)

        # Переменные состояния
        self.current_word = None
        self.correct_answer = None
        self.selected_answer = None
        self.type_question = 0
        self.stand_chanse = [0.5, 0.8, 0.95]

        # Основной лейаут
        self.layout = BoxLayout(orientation='vertical', padding=[20], spacing=10)

        # Верхняя панель с кнопками выбора сложности и "Назад"
        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)

        # Spinner для выбора сложности
        self.difficulty_spinner = Spinner(
            text='Легчайший',
            values=('Легчайший', 'Лёгкий', 'Средний'),
            size_hint=(1, None),
            height=75
        )
        self.difficulty_spinner.bind(text=self.on_difficulty_change)
        self.toolbar.add_widget(self.difficulty_spinner)

        self.stop_button = Button(text="Завершить", size_hint=(1, None), height=75)
        self.stop_button.bind(on_release=self.stop)
        self.toolbar.add_widget(self.stop_button)

        # Кнопка "Назад"
        self.back_button = Button(text="Назад", size_hint=(1, None), height=75)
        self.back_button.bind(on_release=self.go_back)
        self.toolbar.add_widget(self.back_button)

        # Текстовое поле по центру
        self.center_label = Label(
            text="Выберите уровень сложности и нажимайте на кнопку 'Старт'",
            font_size=32, halign='center', valign='middle'
        )
        self.center_label.bind(texture_size=self._resize_label)

        # Нижняя панель с кнопкой "Старт"
        self.bottom_toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)
        self.start_button = Button(text="Старт", size_hint=(1, None), height=75)
        self.start_button.bind(on_release=self.start_practice)
        self.bottom_toolbar.add_widget(self.start_button)

        # Виджеты для вопросов и вариантов ответа (в сетке 2x3)
        self.question_layout = GridLayout(cols=3, spacing=10, padding=[0, 10], size_hint_y=None, height=0)
        self.answer_buttons = []
        for _ in range(6):  # Создаём 6 кнопок
            btn = Button(size_hint=(1, None), height=75, opacity=0)  # Изначально кнопки невидимы
            btn.bind(on_release=self.select_answer)
            self.answer_buttons.append(btn)
            self.question_layout.add_widget(btn)

        # Добавление всех элементов в основной лейаут
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.center_label)
        self.layout.add_widget(self.question_layout)
        self.layout.add_widget(self.bottom_toolbar)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def stop(self, *args):
        self.question_layout.clear_widgets()
        if hasattr(self, 'input_field') and self.input_field:
            self.question_layout.remove_widget(self.input_field)
        if hasattr(self, 'input_field_s') and self.input_field_s:
            self.question_layout.remove_widget(self.input_field_s)

        self.center_label.text = f"Выберите уровень сложности и нажимайте на кнопку 'Старт'"

        self.start_button.text = "Старт"
        self.difficulty_spinner.disabled = False

    def on_difficulty_change(self, spinner, text):
        """Обработчик изменения сложности."""
        if text == 'Легчайший':
            self.stand_chanse = [0.5, 0.8, 0.95]
        elif text == 'Лёгкий':
            self.stand_chanse = [0.3, 0.7, 0.9]
        elif text == 'Средний':
            self.stand_chanse = [0.05, 0.40, 0.75]

    def chance_get_main(self, proportions1, proportions2, proportions3):
        chance = random.random()
        if 0 < chance < proportions1:
            return 0
        elif proportions1 < chance < proportions2:
            return 1
        elif proportions2 < chance < proportions3:
            return 2
        else:
            return 3

    def chance_get_two(self, proportions):
        chance = random.random()
        if chance < proportions:
            return 0
        else:
            return 1

    def read_csv_as_list(self):
        """Чтение CSV файла."""
        filename = "comp_words.csv"
        data_list = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.extend(row)
            file.close()
        return data_list

    def get_random_comp_word(self):
        """Получение случайного слова."""
        comp_words = self.read_csv_as_list()
        return random.choice(comp_words)

    def go_back(self, *args):
        """Возврат на предыдущий экран."""
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = 'main'

    def load_new_question_input(self):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для слов."""
        self.question_layout.clear_widgets()

        self.rand_word_question = self.get_random_comp_word()
        self.current_word = self.translate_to_english(self.rand_word_question)

        self.center_label.text = f"Переведите: {self.current_word}"

        self.input_field = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод..."
        )
        self.question_layout.add_widget(self.input_field)

    def load_new_question_s_input(self):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для предложений."""
        self.question_layout.clear_widgets()

        self.rand_word_question = self.get_random_comp_word()
        self.rand_sent = self.get_random_sent(self.rand_word_question)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        print(self.rand_sent_question_norm_ang)

        self.center_label.text = f"Переведите: {self.rand_sent[1]}"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод..."
        )
        self.question_layout.add_widget(self.input_field_s)

    def load_new_question_s_input_audio(self):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для предложений."""
        self.clear()

        self.rand_word_question = self.get_random_comp_word()
        self.rand_sent = self.get_random_sent(self.rand_word_question)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]

        btn_audio = Button(text='Прослушать', size_hint_x=0.2, height=75)  # Изначально кнопки невидимы
        btn_audio.bind(
            on_release=lambda instance: self.play_audio(self.rand_word_question, self.rand_sent_question_norm_ang))
        self.audio_butt_lay.add_widget(btn_audio)

        # print(self.rand_sent_question_norm_ang)

        self.center_label.text = f"Напишите предложение на слух"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод..."
        )
        self.question_layout.add_widget(self.input_field_s)

    def find_sentence_index(self, word, sentence):
        if word in super_dict:
            for index, pair in enumerate(super_dict[word], start=1):
                if pair[0] == sentence:
                    return index
        return None

    def play_audio(self, word, sentence):
        wav_file = f'G:\Lexi_voices\{word}_{self.find_sentence_index(word, sentence)}.wav'

        sample_rate, audio_data = read(wav_file)

        sd.play(audio_data, samplerate=sample_rate)
        sd.wait()

    def start_practice(self, *args):
        """Начинает практику."""
        if self.start_button.text == "Старт":

            ch = self.chance_get_main(self.stand_chanse[0], self.stand_chanse[1], self.stand_chanse[2])

            if ch == 2:
                self.type_question = 0
                self.load_new_question_input()
            elif ch == 0:
                self.type_question = 1
                self.load_new_question_w_btn()
            elif ch == 1:
                self.type_question = 2
                self.load_new_question_s_btn()
            elif ch == 3:
                self.type_question = 3
                self.load_new_question_s_input()

            self.start_button.text = "Ответить"
            self.difficulty_spinner.disabled = True
            self.question_layout.height = 2 * 85

            for btn in self.answer_buttons:
                btn.opacity = 1

        elif self.start_button.text == "Ответить":

            if self.type_question == 1:
                self.show_correct_answer_btn()
            elif self.type_question == 0:
                self.show_correct_answer_input()
            elif self.type_question == 2:
                self.show_correct_answer_btn_s(self.rand_sent_question_norm_ang, self.rand_sent_question_norm_ru)
            elif self.type_question == 3:
                self.show_correct_answer_input_s(self.rand_sent_question_norm_ang, self.rand_sent_question_norm_ru)

            self.start_button.text = "Следующее слово"
        elif self.start_button.text == "Следующее слово":

            ch = self.chance_get_main(self.stand_chanse[0], self.stand_chanse[1], self.stand_chanse[2])
            self.center_label.color = [1, 1, 1, 1]

            if ch == 2:
                self.type_question = 0
                self.load_new_question_input()
            elif ch == 0:
                self.type_question = 1
                self.load_new_question_w_btn()
            elif ch == 1:
                self.type_question = 2
                self.load_new_question_s_btn()
            elif ch == 3:
                self.type_question = 3
                self.load_new_question_s_input()

            self.start_button.text = "Ответить"

    def load_new_question_w_btn(self):
        """Генерация нового вопроса и восстановление кнопок."""
        if hasattr(self, 'input_field') and self.input_field:
            self.question_layout.remove_widget(self.input_field)
        if hasattr(self, 'input_field_s') and self.input_field_s:
            self.question_layout.remove_widget(self.input_field_s)

        if self.chance_get_two(0.7) == 0:
            self.rand_word_question = self.get_random_comp_word()
            self.current_word = self.translate_to_english(self.rand_word_question)
            self.correct_answer = self.rand_word_question
            other_answers = self.generate_random_ang_words(exclude=[self.correct_answer])
            answers = [self.correct_answer] + other_answers
            random.shuffle(answers)
        else:
            self.rand_word_question = self.get_random_comp_word()
            self.current_word = self.rand_word_question
            self.correct_answer = self.translate_to_english(self.rand_word_question)
            other_answers = self.generate_random_rus_words(exclude=[self.correct_answer])
            answers = [self.correct_answer] + other_answers
            random.shuffle(answers)

        for btn in self.answer_buttons:
            self.question_layout.remove_widget(btn)

        for btn, answer in zip(self.answer_buttons, answers):
            btn.text = answer
            btn.background_color = [1, 1, 1, 1]
            btn.disabled = False
            self.question_layout.add_widget(btn)

        self.center_label.text = f"Переведите: {self.current_word}"

    def get_random_sent(self, word):
        return super_dict[word][random.randint(0, 2)]

    def replace_word_with_blanks(self, sentence, target_word):
        """Заменяет слово в предложении на подчёркивания, если слово содержится в элементе."""
        words = sentence.split()
        modified_words = [
            "_" * len(word) if target_word.lower() in word.lower() else word
            for word in words
        ]
        return " ".join(modified_words)

    def load_new_question_s_btn(self):
        """Генерация нового вопроса и восстановление кнопок."""
        if hasattr(self, 'input_field') and self.input_field:
            self.question_layout.remove_widget(self.input_field)
        if hasattr(self, 'input_field_s') and self.input_field_s:
            self.question_layout.remove_widget(self.input_field_s)

        self.rand_word_question = self.get_random_comp_word()
        self.rand_sent = self.get_random_sent(self.rand_word_question)
        self.rand_sent_question = self.replace_word_with_blanks(self.rand_sent[0],
                                                                self.rand_word_question)
        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        self.current_word = self.translate_to_english(self.rand_word_question)
        self.correct_answer = self.rand_word_question
        other_answers = self.generate_random_ang_words(exclude=[self.correct_answer])
        answers = [self.correct_answer] + other_answers
        random.shuffle(answers)

        for btn in self.answer_buttons:
            self.question_layout.remove_widget(btn)

        for btn, answer in zip(self.answer_buttons, answers):
            btn.text = answer
            btn.background_color = [1, 1, 1, 1]
            btn.disabled = False
            self.question_layout.add_widget(btn)

        self.center_label.text = f"Переведите: {self.rand_sent_question}"

    def load_new_question_s_w_input(self):
        """Генерация нового вопроса и восстановление кнопок."""
        self.clear()

        self.rand_word_question = self.get_random_comp_word()
        self.rand_sent = self.get_random_sent(self.rand_word_question)
        self.rand_sent_question = self.replace_word_with_blanks(self.rand_sent[0],
                                                                self.rand_word_question)
        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        self.current_word = self.translate_to_english(self.rand_word_question)

        self.input_field_s_w = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите слово..."
        )
        self.center_label.text = f"Вставьте слово: {self.rand_sent_question}"
        self.question_layout.add_widget(self.input_field_s_w)

    def select_answer(self, instance):
        """Выбор варианта ответа."""
        self.selected_answer = instance.text
        for btn in self.answer_buttons:
            btn.background_color = [0.8, 0.8, 0.8, 1]
        instance.background_color = [0.6, 0.6, 0.6, 1]

    def show_correct_answer_btn(self):
        """Подсвечивает правильный ответ."""
        for btn in self.answer_buttons:
            if btn.text == self.correct_answer:
                btn.background_color = [0, 1, 0, 1]
            else:
                btn.background_color = [1, 0, 0, 1]
            btn.disabled = True

    def show_correct_answer_btn_s(self, ang, ru):
        for btn in self.answer_buttons:
            if btn.text == self.correct_answer:
                btn.background_color = [0, 1, 0, 1]
            else:
                btn.background_color = [1, 0, 0, 1]
            btn.disabled = True

        self.center_label.text = f"{ang}\n\n{ru}"

    def calculate_similarity(self, user_input, correct_answer):
        similarity_ratio = SequenceMatcher(None, user_input, correct_answer).ratio()

        return round(similarity_ratio * 100, 2)

    def show_correct_answer_input_s(self, ang, ru):
        if self.calculate_similarity(self.input_field_s.text.lower().strip(),
                                     self.rand_sent_question_norm_ang.lower().strip()) > 80:
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def show_correct_answer_input(self):
        """Подсвечивает правильный ответ."""
        if self.input_field.text.strip().lower() == self.rand_word_question.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = 'Правильно!'
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно, правильный ответ: {self.rand_word_question}'

    def show_correct_answer_input_s_w(self, ang, ru):
        """Подсвечивает правильный ответ."""
        if self.input_field_s_w.text.strip().lower() == self.rand_word_question.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def translate_to_english(self, word):
        """Перевод слова на английский (заглушка)."""
        with open("1-1000.txt", "r") as file:
            text_words = file.read().split('\n')
            file.close()

        with open("1-1000 ru.txt", "r", encoding='windows-1251') as file1:
            text_words_trans = file1.read().split('\n')
            file1.close()

        return text_words_trans[text_words.index(word)]

    def generate_random_ang_words(self, exclude=None):
        exclude = exclude or []
        all_words = []
        for i in range(6):
            word = self.get_random_comp_word()
            if word not in all_words:
                all_words.append(word)
        return [word for word in all_words if word not in exclude][:5]

    def generate_random_rus_words(self, exclude=None):
        exclude = exclude or []
        all_words = []
        for i in range(6):
            word = self.get_random_comp_word()
            if word not in all_words:
                all_words.append(self.translate_to_english(word))
        return [word for word in all_words if word not in exclude][:5]

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет размеры текста."""
        instance.size = instance.texture_size
        instance.text_size = (self.width - 40, None)


class CompWordsScreen(Screen):
    def __init__(self, **kwargs):
        super(CompWordsScreen, self).__init__(**kwargs)

        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.search_button = Button(text="Поиск", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)
        self.search_button.bind(on_release=lambda instance: self.search_menu(self.manager))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)
        self.toolbar.add_widget(self.search_button)
        self.toolbar.add_widget(Label())
        self.toolbar.add_widget(self.back_button)

        self.scroll_view = ScrollView()

        self.layout = GridLayout(cols=2, spacing=10, size_hint_y=None)

        self.scroll_view.add_widget(self.layout)

        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.main_layout = BoxLayout(orientation='vertical', padding=[20], spacing=10)
        self.main_layout.add_widget(self.toolbar)
        self.main_layout.add_widget(self.scroll_view)
        self.add_widget(self.main_layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def on_pre_enter(self, *args):
        self.layout.clear_widgets()

        for i in self.read_csv_as_list():
            btn = Button(text=f'{i}', size_hint=(1, None))
            btn.bind(on_release=lambda instance, text=i: self.word_show(self.manager, text))
            self.layout.add_widget(btn)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def read_csv_as_list(self):
        data_list = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.extend(row)
            file.close()
        return data_list[::-1]

    def search_menu(self, screen_manager):
        if not self.manager.has_screen('comp_search_menu'):
            self.comp_search_menu = SearchMenuComp(name='comp_search_menu')
            self.manager.add_widget(self.comp_search_menu)
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_search_menu'

    def word_show(self, screen_manager, word):
        if not self.manager.has_screen('word_show_window'):
            self.word_show_window = WordShow(word, name='word_show_window')
            self.manager.add_widget(self.word_show_window)

        self.manager.get_screen('word_show_window').update_content(word)
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'word_show_window'

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos


class SearchMenuComp(Screen):
    def __init__(self, **kwargs):
        super(SearchMenuComp, self).__init__(**kwargs)

        self.label = Label(
            halign='center',
            valign='middle',
            size_hint=(1, None),
            text='\n\nМожно просматривать только те слова, которые\nбыли раннее изучены в разделе "теория"',
            font_size=24,
        )
        self.label.bind(texture_size=self._resize_label)

        self.label2 = Label(
            halign='center',
            valign='top',
            size_hint=(1, None),
            font_size=18,
        )
        self.label2.bind(texture_size=self._resize_label)

        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.text_layout = BoxLayout(orientation='vertical', size_hint_y=None, padding=[10], spacing=10)
        self.text_layout.bind(minimum_height=self.text_layout.setter('height'))

        self.text_layout.add_widget(self.label)
        self.text_layout.add_widget(self.label2)
        self.scroll_view.add_widget(self.text_layout)

        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)
        self.search_button = Button(text="Поиск", size_hint=(None, None), size=(150, 75))
        self.search_button.bind(on_release=self.search_proc)

        self.search_widget = TextInput()

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar.add_widget(self.search_widget)
        self.toolbar.add_widget(self.back_button)

        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar2.add_widget(Label())
        self.toolbar2.add_widget(self.search_button)
        self.toolbar2.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[20])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.toolbar2)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_words'

    def read_csv_as_list(self):
        data_list = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.extend(row)
            file.close()
        print(data_list)
        return data_list

    def search_proc(self, *args):
        self.word = self.search_widget.text
        if self.word in self.read_csv_as_list():
            self.text_ex = f'Примеры предложений:\n\n{super_dict[self.word][0][0]}\n' \
                           f'{super_dict[self.word][0][1]}\n\n{super_dict[self.word][1][0]}\n' \
                           f'{super_dict[self.word][1][1]}\n\n{super_dict[self.word][2][0]}\n' \
                           f'{super_dict[self.word][2][1]}\n\n'
            self.label.text = f"\n\nВаше слово {self.word}\n\n"
            self.label2.text = self.text_ex
        elif self.word in super_dict.keys() and not (self.word in self.read_csv_as_list()):
            self.label.text = f"Слово ещё не изучено"
            self.label2.text = 'Чтобы просмотреть любое слово из базы\nобратитесь к разделу "открытый банк слов"'
        elif self.word == '':
            self.label.text = f"Введите слово в поле выше"
        else:
            self.label.text = f"Слово не найдено"
            self.label2.text = 'Проверьте правильность написания слова\n\n' \
                               'Если не помогло, то слова нет в базе\n' \
                               'из 1000 самых используемых слов в английском языке'

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет высоту виджета в зависимости от его содержания."""
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        """Обновляет размеры текстовых областей."""
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)


class MainWind(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.settings_screen = SettingsScreen(name='settings')
        self.main_screen = Screen(name='main')

        with self.main_screen.canvas.before:
            Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.main_screen.size, pos=self.main_screen.pos)

        self.box1 = BoxLayout(size_hint_y=None, height=75, spacing=10)
        self.box2 = BoxLayout(orientation='vertical', spacing=25)
        self.box_main = BoxLayout(orientation='vertical', padding=[20], spacing=40)

        self.label = Label(text='Lexi\nLearn', font_size=30, font_name="IntroDemo-BlackCAPS.otf")
        self.label2 = Label(halign='center', size_hint_y=0.4)

        self.btn = PressableButton(text='Настройки', font_size=22,
                                   on_release_callback=lambda: self.open_settings(self.screen_manager))
        self.btn3 = PressableButton(text="ТЕОРИЯ", font_size=28,
                                    on_release_callback=lambda: self.open_theory(self.screen_manager))
        self.btn4 = PressableButton(text='ПРАКТИКА', font_size=28,
                                    on_release_callback=lambda: self.open_practice(self.screen_manager))
        self.btn5 = PressableButton(text='БАНК ИЗУЧЕНЫХ СЛОВ', font_size=28,
                                    on_release_callback=lambda: self.open_comp_words_bank(self.screen_manager))
        self.btn6 = PressableButton(text='ОТКРЫТЫЙ БАНК СЛОВ', font_size=28,
                                    on_release_callback=lambda: self.open_all_words_bank(self.screen_manager))

        self.box1.add_widget(self.label)
        self.box1.add_widget(self.btn)
        self.box2.add_widget(self.btn3)
        self.box2.add_widget(self.btn4)
        self.box2.add_widget(self.btn5)
        self.box2.add_widget(self.btn6)
        self.box_main.add_widget(self.box1)
        self.box_main.add_widget(self.box2)
        self.box_main.add_widget(self.label2)
        self.main_screen.add_widget(self.box_main)

        self.screen_manager.add_widget(self.main_screen)
        self.screen_manager.add_widget(self.settings_screen)

        self.main_screen.bind(on_pre_enter=self.update_statistics)

        self.update_statistics()

        self.main_screen.bind(size=self.update_rect, pos=self.update_rect)

        return self.screen_manager

    def update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def update_statistics(self, *args):
        studied_words = len(self.read_csv_as_list())
        remaining_percentage = round(((1000 - studied_words) / 1000) * 100, 2)
        self.label2.text = f'Статистика:\nИзучено слов: {studied_words}\nОсталось {remaining_percentage}%'

    def open_settings(self, screen_manager):
        self.screen_manager.transition = FadeTransition(duration=0.20)
        self.screen_manager.current = 'settings'

    def open_theory(self, screen_manager):
        if not self.screen_manager.has_screen('theory'):
            self.theory_screen = TheoryScreen(name='theory')
            self.screen_manager.add_widget(self.theory_screen)
        self.screen_manager.transition = FadeTransition(duration=0.20)
        self.screen_manager.current = 'theory'

    def open_practice(self, screen_manager):
        if not self.screen_manager.has_screen('practice'):
            self.practice_screen = PracticeScreen(name='practice')
            self.screen_manager.add_widget(self.practice_screen)
        self.screen_manager.transition = FadeTransition(duration=0.20)
        self.screen_manager.current = 'practice'

    def open_comp_words_bank(self, screen_manager):
        if not self.screen_manager.has_screen('comp_words'):
            self.comp_words_screen = CompWordsScreen(name='comp_words')
            self.screen_manager.add_widget(self.comp_words_screen)
        self.screen_manager.transition = FadeTransition(duration=0.20)
        self.screen_manager.current = 'comp_words'

    def open_all_words_bank(self, screen_manager):
        if not self.screen_manager.has_screen('all_words'):
            self.words_screen = AllWordsScreen(name='all_words')
            self.screen_manager.add_widget(self.words_screen)
        self.screen_manager.transition = FadeTransition(duration=0.20)
        self.screen_manager.current = 'all_words'

    def read_csv_as_list(self):
        filename = "comp_words.csv"
        data_list = []
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.extend(row)
            file.close()
        return data_list


if __name__ == '__main__':
    MainWind().run()
