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
import sqlite3
from datetime import datetime, timedelta
from kivy.metrics import dp, sp
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.clock import Clock

Window.size = (432, 768)
Window.title = 'LexiLearn'
client = Client()

# main_font_style = "arial_black.ttf"

main_font_style = "IntroDemo-BlackCAPS.otf"
alt_font_style = "IntroDemoCond-LightCAPS.otf"


class PressableButton(Widget):
    def __init__(self, text="", shadow_height=6, font_size=18, size=(300, 100), color=(0.2, 0.6, 0.8, 1),
                 shadow_color=(0.1, 0.4, 0.6, 1),
                 on_release_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.color = color if len(color) == 4 else self.rgb_to_kivy_color(color)
        self.shadow_color = shadow_color if len(shadow_color) == 4 else self.rgb_to_kivy_color(shadow_color)
        self.text = text
        self.font_size = font_size
        self.shadow_height = shadow_height
        self.on_release_callback = on_release_callback

        # Размеры кнопки
        self.size = kwargs.get("size", size)
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
            font_name=main_font_style,
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
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM words')
        conn.commit()
        conn.close()

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
    def __init__(self, **kwargs):
        super(WordShow, self).__init__(**kwargs)

        # Верхняя панель с кнопкой "Назад"
        self.back_button = Button(text="Назад", size_hint=(None, None), size=(150, 75))
        self.back_button.bind(on_release=self.go_back)

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)
        self.toolbar.add_widget(Label())  # Заполнитель
        self.toolbar.add_widget(self.back_button)

        # Прокручиваемая область (ScrollView)
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=20, padding=10)
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))
        self.scroll_view.add_widget(self.vertical_layout)

        # Основной лейаут экрана
        self.layout = BoxLayout(orientation='vertical', padding=[20])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)

        # Цвет фона
        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def update_content(self, word):
        """Обновляет экран новым словом и примерами."""
        self.vertical_layout.clear_widgets()  # Очищаем старые данные

        # Заголовок (внутри прокрутки!)
        label = Label(
            text=f"\nВаше слово: {word}\n",
            font_size=sp(24),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            font_name=main_font_style
        )
        label.bind(texture_size=self._resize_label)
        self.vertical_layout.add_widget(label)

        # Добавляем примеры предложений
        examples = super_dict.get(word, [])
        if not examples:
            self.vertical_layout.add_widget(Label(text="Примеры предложений отсутствуют.", font_size=18))
            return

        for i in range(min(3, len(examples))):
            example_pair = examples[i]

            # Контейнер с кнопкой и текстом
            horizontal_container = BoxLayout(orientation="horizontal", size_hint=(1, None), spacing=10)

            # Текст примера
            example_label = Label(
                text=f'{example_pair[0]}\n------------------\n{example_pair[1]}',
                size_hint=(1, None),
                font_size=18,
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )
            example_label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            # Кнопка аудио
            image = ImageButton(
                source="audio.png",
                size_hint=(None, None),
                size=(50, 50),
                pos_hint={'center_y': 0.5},
                text=example_pair[0],
                word=word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(example_label)

            # Откладываем пересчет высоты контейнера
            Clock.schedule_once(lambda dt: self.update_container_height(horizontal_container))

            # Добавляем горизонтальный контейнер в вертикальный список
            self.vertical_layout.add_widget(horizontal_container)

        # Принудительно пересчитываем размеры всех контейнеров после добавления
        Clock.schedule_once(lambda dt: self.recalculate_all_heights())

    def update_container_height(self, horizontal_container):
        """Обновляет высоту контейнера на основе максимальной высоты дочерних элементов."""
        max_height = max(child.height for child in horizontal_container.children)
        horizontal_container.height = max_height + 20  # Отступ
        print(f"Updated container height: {horizontal_container.height}")

    def recalculate_all_heights(self, *_):
        """Пересчитывает размеры всех контейнеров после их добавления."""
        for child in self.vertical_layout.children:
            if isinstance(child, BoxLayout):
                max_height = max(grandchild.height for grandchild in child.children)
                child.height = max_height + 20
                print(f"Recalculated container height: {child.height}")

    def _resize_label(self, instance, texture_size):
        """Динамически изменяет высоту текста."""
        instance.height = texture_size[1]

    def go_back(self, *args):
        """Возврат к предыдущему экрану."""
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_words'

    def on_size(self, *args):
        """Обновляет размеры фона и текстовых областей."""
        self.rect.size = self.size
        self.rect.pos = self.pos


class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.text = kwargs.pop('text', '')
        self.word = kwargs.pop('word', '')
        super().__init__(**kwargs)

    def find_sentence_index(self, word, sentence):
        if word in super_dict:
            for index, pair in enumerate(super_dict[word], start=1):
                if pair[0] == sentence:
                    return index
        return None

    def on_press(self):
        wav_file = f'G:\Lexi_voices\{self.word}_{self.find_sentence_index(self.word, self.text)}.wav'

        sample_rate, audio_data = read(wav_file)

        sd.play(audio_data, samplerate=sample_rate)
        sd.wait()


class CloseButton(ButtonBehavior, Image):
    def __init__(self, on_close_callback, **kwargs):
        super().__init__(**kwargs)
        self.source = "Chess_xxt45.svg.png"
        self.on_close_callback = on_close_callback

    def on_press(self):
        if self.on_close_callback:
            self.on_close_callback()


class TheoryScreen(Screen):
    def __init__(self, **kwargs):
        super(TheoryScreen, self).__init__(**kwargs)

        self.close_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(20, 20))

        # # Кнопка "Назад"
        # self.back_button = PressableButton(text="Назад", on_release_callback=lambda: self.go_back())

        # Кнопка "Сгенерировать слово"
        self.next_button = PressableButton(text="СГЕНЕРИРОВАТЬ СЛОВО", font_size=20, size=(200, 75),
                                           on_release_callback=lambda: self.text_load())
        self.next_button.bind(on_release=self.text_load)

        # Кнопка "Добавить в конспект"
        self.jorn_button = PressableButton(text="в 'мои' слова", font_size=16)

        # Кнопка "Больше примеров"
        self.more_ex_button = PressableButton(text="Ещё примеры", on_release_callback=lambda: self.more_w(),
                                              font_size=16)

        # Верхняя панель
        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=20)
        self.toolbar.add_widget(self.close_button)

        # Нижняя панель
        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        self.toolbar2.add_widget(self.next_button)

        # Прокручиваемая область
        self.scroll_view = ScrollView(size_hint=(1, 1))

        # Текстовые метки
        self.label = Label(
            halign='center',
            valign='middle',
            size_hint_y=None,
            text="Нажмите на кнопку 'Сгенирировать слово'\nчтобы мы подобрали вам слово",
            font_size=sp(24),
            font_name=main_font_style
        )
        self.label.bind(texture_size=self._resize_label)

        # Добавляем текстовый лейаут в прокручиваемую область

        # Основной лейаут
        self.main_layout = BoxLayout(orientation='vertical', padding=[20], spacing=20)

        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=20, padding=10)
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))

        self.vertical_layout.add_widget(self.label)

        self.scroll_view.add_widget(self.vertical_layout)

        # Лейаут для дополнительных кнопок
        self.func_layout2 = BoxLayout(size_hint_y=None, height=60, spacing=14)
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

    def add_word_to_database(self, word, db_path='words.db'):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS words (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                word TEXT NOT NULL UNIQUE,
                type1 DATETIME,
                type2 DATETIME,
                type3 DATETIME,
                type4 DATETIME,
                type5 DATETIME,
                type6 DATETIME,
                type7 DATETIME
            )
        ''')
        conn.commit()

        try:
            cursor.execute('''
                INSERT INTO words (word) 
                VALUES (?)
            ''', (word,))
            conn.commit()
            print(f"Слово '{word}' успешно добавлено в базу данных.")
        except sqlite3.IntegrityError:
            print(f"Слово '{word}' уже существует в базе данных.")

        conn.close()

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
        self.label.text_size = (self.width - 40, None)

    def read_csv_as_list(self):
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()
        print(words)

        return words

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

    def text_load(self, *args):
        self.rand_word = self.get_random_word_not_in_csv()

        self.vertical_layout.clear_widgets()

        self.label.text = f"Ваше слово {self.rand_word}"
        self.vertical_layout.add_widget(self.label)

        def update_container_height(horizontal_container):
            """Обновляет высоту контейнера на основе максимальной высоты дочерних элементов."""
            max_height = max(child.height for child in horizontal_container.children)
            horizontal_container.height = max_height + 20  # Добавляем небольшой отступ
            print(f"Updated container height: {horizontal_container.height}")

        for i in range(3):
            horizontal_container = BoxLayout(
                orientation="horizontal",
                size_hint=(1, None),  # Контейнер не растягивается по высоте
                spacing=10
            )

            # Блок текста
            label = Label(
                text=f'{super_dict[self.rand_word][i][0]}\n------------------\n'
                     f'{super_dict[self.rand_word][i][1]}',
                size_hint=(1, None),
                font_size=18,  # Устанавливаем увеличенный шрифт
                halign="left",  # Выравнивание текста по левому краю
                valign="middle",  # Вертикальное выравнивание
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )

            # Привязываем высоту текста к лейблу
            label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            # Добавляем кнопку
            image = ImageButton(
                source="audio.png",  # Указываем путь к изображению
                size_hint=(None, None),
                size=(50, 50),
                pos_hint={'center_y': 0.5},
                text=f'{super_dict[self.rand_word][i][0]}',
                word=self.rand_word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(label)

            # Откладываем пересчет высоты контейнера
            Clock.schedule_once(lambda dt: update_container_height(horizontal_container))

            # Добавляем горизонтальный контейнер в вертикальный список
            self.vertical_layout.add_widget(horizontal_container)

        # Принудительно пересчитываем размеры всех контейнеров после добавления
        def recalculate_all_heights(*_):
            for child in self.vertical_layout.children:
                if isinstance(child, BoxLayout):
                    max_height = max(grandchild.height for grandchild in child.children)
                    child.height = max_height + 20
                    print(f"Recalculated container height: {child.height}")

        Clock.schedule_once(lambda dt: recalculate_all_heights())

        self.next_button.text = 'Следущее слово'
        self.add_word_to_database(self.rand_word)

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


class PracticeScreen(Screen):
    def __init__(self, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)

        # Переменные состояния
        self.current_word = None
        self.correct_answer = None
        self.selected_answer = None
        self.type_question = 0
        self.stand_chanse = [0.5, 0.7, 0.8, 0.9, 0.95, 0.98]

        # Основной лейаут
        self.layout = BoxLayout(orientation='vertical', padding=[20], spacing=10)

        # Верхняя панель с кнопками выбора сложности и "Назад"
        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=75, spacing=10)

        # Spinner для выбора сложности
        self.difficulty_spinner = Spinner(
            text='Легчайший',
            values=('Легчайший', 'Лёгкий', 'Средний', 'Сложный', 'Случайно'),
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
            btn = Button(size_hint=(1, None), height=75, opacity=0)
            btn.bind(on_release=self.select_answer)
            self.answer_buttons.append(btn)
            self.question_layout.add_widget(btn)

        self.audio_butt_lay = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)

        # Добавление всех элементов в основной лейаут
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.center_label)
        self.layout.add_widget(self.audio_butt_lay)
        self.layout.add_widget(self.question_layout)
        self.layout.add_widget(self.bottom_toolbar)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def stop(self, *args):
        self.clear()

        self.center_label.text = f"Выберите уровень сложности и нажимайте на кнопку 'Старт'"

        self.start_button.text = "Старт"
        self.difficulty_spinner.disabled = False

    def on_difficulty_change(self, spinner, text):
        """Обработчик изменения сложности."""
        if text == 'Легчайший':
            self.stand_chanse = [0.5, 0.7, 0.8, 0.9, 0.95, 0.98]
        elif text == 'Лёгкий':
            self.stand_chanse = [0.3, 0.55, 0.65, 0.85, 0.90, 0.96]
        elif text == 'Средний':
            self.stand_chanse = [0.05, 0.25, 0.35, 0.65, 0.85, 0.95]
        elif text == 'Сложный':
            self.stand_chanse = [0.05, 0.06, 0.15, 0.35, 0.65, 0.85]
        elif text == 'Случайно':
            self.stand_chanse = [0.15, 0.30, 0.45, 0.60, 0.75, 0.90]

    def chance_get_main(self, proportions1, proportions2, proportions3, proportions4, proportions5, proportions6):
        chance = random.random()
        print(chance)
        if 0 < chance < proportions1:
            return 0
        elif proportions1 < chance < proportions2:
            return 1
        elif proportions2 < chance < proportions3:
            return 4
        elif proportions3 < chance < proportions4:
            return 2
        elif proportions4 < chance < proportions5:
            return 3
        elif proportions5 < chance < proportions6:
            return 5
        else:
            return 6

    def chance_get_two(self, proportions):
        chance = random.random()
        if chance < proportions:
            return 0
        else:
            return 1

    def read_csv_as_list(self):
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()

        return words

    def get_random_comp_word(self):

        comp_words = self.read_csv_as_list()
        return random.choice(comp_words)

    def get_word_for_task(self, task_type, db_path='words.db'):
        valid_task_columns = {f"type{i}" for i in range(1, 8)}
        if task_type not in valid_task_columns:
            raise ValueError(
                f"Неверное название столбца: {task_type}. Доступные столбцы: {', '.join(valid_task_columns)}")

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        one_week_ago = datetime.now() - timedelta(weeks=1)

        cursor.execute(f'''
            SELECT word 
            FROM words
            WHERE {task_type} IS NULL OR {task_type} < ?
        ''', (one_week_ago,))

        words = [row[0] for row in cursor.fetchall()]

        conn.close()
        print(words)

        return random.choice(words)

    def go_back(self, *args):
        """Возврат на предыдущий экран."""
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = 'main'

    def load_new_question_input(self, q_word):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для слов."""
        self.clear()

        self.current_word = self.translate_to_english(q_word)

        self.center_label.text = f"Переведите: {self.current_word}"

        self.input_field = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод..."
        )
        self.question_layout.add_widget(self.input_field)

    def load_new_question_s_input(self, q_word):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для предложений."""
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

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

    def update_bd_for_word(self, word, type_q, db_path='words.db'):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        current_time = datetime.now()

        cursor.execute(f'''
            UPDATE words
            SET {type_q} = ?
            WHERE word = ?
        ''', (current_time, word))
        conn.commit()

        if cursor.rowcount == 0:
            print(f"Слово '{word}' не найдено в базе данных.")
        else:
            print(f"Для слова '{word}' успешно обновлена дата в task1: {current_time}.")

        conn.close()

    def load_new_question_s_input_audio(self, q_word):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для предложений."""
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]

        btn_audio = Button(text='Прослушать', size_hint_x=0.2, height=75, )  # Изначально кнопки невидимы
        btn_audio.bind(
            on_release=lambda instance: self.play_audio(q_word, self.rand_sent_question_norm_ang))
        self.audio_butt_lay.add_widget(btn_audio)
        btn_audio.disabled = False

        self.center_label.text = f"Напишите предложение на слух"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод...",
        )
        self.question_layout.add_widget(self.input_field_s)

    def load_new_question_s_input_audio_hard(self, q_word):
        """Удаляет кнопки с вариантами ответов и меняет слово, добавляя поле ввода для предложений."""
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]

        self.btn_audio = Button(text='Прослушать', size_hint_x=0.2, height=75)
        self.btn_audio.bind(
            on_release=lambda instance: self.play_one_audio(q_word, self.rand_sent_question_norm_ang))
        self.audio_butt_lay.add_widget(self.btn_audio)
        self.btn_audio.disabled = False

        # print(self.rand_sent_question_norm_ang)

        self.center_label.text = f"Напишите предложение на слух с первого раза"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите перевод...",
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

    def play_one_audio(self, word, sentence):
        self.btn_audio.disabled = True
        wav_file = f'G:\Lexi_voices\{word}_{self.find_sentence_index(word, sentence)}.wav'

        sample_rate, audio_data = read(wav_file)

        sd.play(audio_data, samplerate=sample_rate)
        sd.wait()

    def start_practice(self, *args):
        """Начинает практику."""
        if self.start_button.text == "Старт":

            ch = self.chance_get_main(self.stand_chanse[0], self.stand_chanse[1], self.stand_chanse[2],
                                      self.stand_chanse[3], self.stand_chanse[4], self.stand_chanse[5])
            if ch == 0:
                self.main_word = self.get_word_for_task('type1')
                self.type_question = 0
                self.load_new_question_w_btn(self.main_word)
            elif ch == 1:
                self.main_word = self.get_word_for_task('type2')
                self.type_question = 1
                self.load_new_question_s_btn(self.main_word)
            elif ch == 2:
                self.main_word = self.get_word_for_task('type3')
                self.type_question = 2
                self.load_new_question_input(self.main_word)
            elif ch == 3:
                self.main_word = self.get_word_for_task('type4')
                self.type_question = 3
                self.load_new_question_s_input(self.main_word)
            elif ch == 4:
                self.main_word = self.get_word_for_task('type5')
                self.type_question = 4
                self.load_new_question_s_w_input(self.main_word)
            elif ch == 5:
                self.main_word = self.get_word_for_task('type6')
                self.type_question = 5
                self.load_new_question_s_input_audio(self.main_word)
            elif ch == 6:
                self.main_word = self.get_word_for_task('type7')
                self.type_question = 6
                self.load_new_question_s_input_audio_hard(self.main_word)

            self.start_button.text = "Ответить"
            self.difficulty_spinner.disabled = True
            self.question_layout.height = 2 * 85

            for btn in self.answer_buttons:
                btn.opacity = 1

        elif self.start_button.text == "Ответить":

            if self.type_question == 1:
                self.show_correct_answer_btn_s(self.rand_sent_question_norm_ang, self.rand_sent_question_norm_ru)
            elif self.type_question == 0:
                self.show_correct_answer_btn()
            elif self.type_question == 2:
                self.show_correct_answer_input()
            elif self.type_question == 3:
                self.show_correct_answer_input_s(self.rand_sent_question_norm_ang, self.rand_sent_question_norm_ru)
            elif self.type_question == 4:
                self.show_correct_answer_input_s_w(self.rand_sent_question_norm_ang, self.rand_sent_question_norm_ru)
            elif self.type_question == 5:
                self.show_correct_answer_input_s_audio(self.rand_sent_question_norm_ang,
                                                       self.rand_sent_question_norm_ru)
            elif self.type_question == 6:
                self.show_correct_answer_input_s_audio_hard(self.rand_sent_question_norm_ang,
                                                            self.rand_sent_question_norm_ru)

            self.start_button.text = "Следующее слово"
        elif self.start_button.text == "Следующее слово":

            ch = self.chance_get_main(self.stand_chanse[0], self.stand_chanse[1], self.stand_chanse[2],
                                      self.stand_chanse[3], self.stand_chanse[4], self.stand_chanse[5])
            self.center_label.color = [1, 1, 1, 1]

            if ch == 0:
                self.main_word = self.get_word_for_task('type1')
                self.type_question = 0
                self.load_new_question_w_btn(self.main_word)
            elif ch == 1:
                self.main_word = self.get_word_for_task('type2')
                self.type_question = 1
                self.load_new_question_s_btn(self.main_word)
            elif ch == 2:
                self.main_word = self.get_word_for_task('type3')
                self.type_question = 2
                self.load_new_question_input(self.main_word)
            elif ch == 3:
                self.main_word = self.get_word_for_task('type4')
                self.type_question = 3
                self.load_new_question_s_input(self.main_word)
            elif ch == 4:
                self.main_word = self.get_word_for_task('type5')
                self.type_question = 4
                self.load_new_question_s_w_input(self.main_word)
            elif ch == 5:
                self.main_word = self.get_word_for_task('type6')
                self.type_question = 5
                self.load_new_question_s_input_audio(self.main_word)
            elif ch == 6:
                self.main_word = self.get_word_for_task('type7')
                self.type_question = 6
                self.load_new_question_s_input_audio_hard(self.main_word)

            self.start_button.text = "Ответить"

    def load_new_question_w_btn(self, q_word):
        """Генерация нового вопроса и восстановление кнопок."""
        self.clear()

        if self.chance_get_two(0.7) == 0:
            self.current_word = self.translate_to_english(q_word)
            self.correct_answer = q_word
            other_answers = self.generate_random_ang_words(exclude=[self.correct_answer])
            answers = [self.correct_answer] + other_answers
            random.shuffle(answers)
        else:
            self.current_word = q_word
            self.correct_answer = self.translate_to_english(q_word)
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

    def load_new_question_s_btn(self, q_word):
        """Генерация нового вопроса и восстановление кнопок."""
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)
        self.rand_sent_question = self.replace_word_with_blanks(self.rand_sent[0],
                                                                q_word)
        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        self.current_word = self.translate_to_english(q_word)
        self.correct_answer = q_word
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

        self.center_label.text = f"Вставьте слово: {self.rand_sent_question}"

    def load_new_question_s_w_input(self, q_word):
        """Генерация нового вопроса и восстановление кнопок."""
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)
        self.rand_sent_question = self.replace_word_with_blanks(self.rand_sent[0],
                                                                q_word)
        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        self.current_word = self.translate_to_english(q_word)

        self.input_field_s_w = TextInput(
            size_hint=(1, None),
            height=50,
            multiline=False,
            font_size=24,
            hint_text="Введите слово..."
        )
        self.center_label.text = f"Вставьте слово: {self.rand_sent_question}"
        self.question_layout.add_widget(self.input_field_s_w)

    def clear(self):
        if hasattr(self, 'input_field') and self.input_field:
            self.question_layout.remove_widget(self.input_field)
        if hasattr(self, 'input_field_s') and self.input_field_s:
            self.question_layout.remove_widget(self.input_field_s)
        if hasattr(self, 'input_field_s_w') and self.input_field_s_w:
            self.question_layout.remove_widget(self.input_field_s_w)
        self.question_layout.clear_widgets()
        self.audio_butt_lay.clear_widgets()

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
                self.update_bd_for_word(self.main_word, 'type1')
                btn.background_color = [0, 1, 0, 1]
            else:
                btn.background_color = [1, 0, 0, 1]
            btn.disabled = True

    def show_correct_answer_btn_s(self, ang, ru):
        for btn in self.answer_buttons:
            if btn.text == self.correct_answer:
                btn.background_color = [0, 1, 0, 1]
                self.update_bd_for_word(self.main_word, 'type2')
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
            self.update_bd_for_word(self.main_word, 'type4')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def show_correct_answer_input_s_audio(self, ang, ru):
        if self.calculate_similarity(self.input_field_s.text.lower().strip(),
                                     self.rand_sent_question_norm_ang.lower().strip()) > 80:
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
            self.update_bd_for_word(self.main_word, 'type6')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def show_correct_answer_input_s_audio_hard(self, ang, ru):
        if self.calculate_similarity(self.input_field_s.text.lower().strip(),
                                     self.rand_sent_question_norm_ang.lower().strip()) > 80:
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
            self.update_bd_for_word(self.main_word, 'type7')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def show_correct_answer_input(self):
        """Подсвечивает правильный ответ."""
        if self.input_field.text.strip().lower() == self.main_word.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = 'Правильно!'
            self.update_bd_for_word(self.main_word, 'type3')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно, правильный ответ: {self.main_word}'

    def show_correct_answer_input_s_w(self, ang, ru):
        """Подсвечивает правильный ответ."""
        if self.input_field_s_w.text.strip().lower() == self.main_word.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
            self.update_bd_for_word(self.main_word, 'type5')
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
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()
        print(words)

        return words

    def search_menu(self, screen_manager):
        if not self.manager.has_screen('comp_search_menu'):
            self.comp_search_menu = SearchMenuComp(name='comp_search_menu')
            self.manager.add_widget(self.comp_search_menu)
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_search_menu'

    def word_show(self, screen_manager, word):
        if not screen_manager.has_screen('word_show_window'):
            print("Создаём WordShow...")
            word_show_window = WordShow(name='word_show_window')
            screen_manager.add_widget(word_show_window)
        else:
            print("WordShow уже создан.")

        screen = screen_manager.get_screen('word_show_window')
        print(dir(screen))  # Проверить, какие методы есть у объекта
        screen.update_content(word)

        screen_manager.transition = FadeTransition(duration=0.20)
        screen_manager.current = 'word_show_window'

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
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()
        print(words)

        return words

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

        self.label = Label(text='Lexi\nLearn', font_size=30, font_name=main_font_style)
        self.label2 = Label(halign='center', size_hint_y=0.4)

        self.btn = PressableButton(text='Настройки', font_size=22,
                                   on_release_callback=lambda: self.open_settings(self.screen_manager))
        self.btn3 = PressableButton(text="ТЕОРИЯ", font_size=22,
                                    on_release_callback=lambda: self.open_theory(self.screen_manager))
        self.btn4 = PressableButton(text='ПРАКТИКА', font_size=22,
                                    on_release_callback=lambda: self.open_practice(self.screen_manager))
        self.btn5 = PressableButton(text='БАНК ИЗУЧЕНЫХ СЛОВ', font_size=22,
                                    on_release_callback=lambda: self.open_comp_words_bank(self.screen_manager))
        self.btn6 = PressableButton(text='ОТКРЫТЫЙ БАНК СЛОВ', font_size=22,
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
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()
        print(words)

        return words


if __name__ == '__main__':
    MainWind().run()
