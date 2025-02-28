from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, FadeTransition, SwapTransition
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import random
from g4f.client import Client
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
import threading
from openai import OpenAI
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

Window.size = (432, 768)
Window.title = 'LexiLearn'
client = OpenAI(
    api_key=os.environ.get('API'),
    base_url="https://api.proxyapi.ru/openai/v1",
)

print("Current DPI:", Window.dpi)

# main_font_style = "arial_black.ttf"

main_font_style = "IntroDemo-BlackCAPS.otf"
alt_font_style = "IntroDemoCond-LightCAPS.otf"


class PressableButton(Widget):
    def __init__(self, text="", shadow_height=6, font_size=18, size=(300, 100), color=(0.2, 0.6, 0.8, 1),
                 shadow_color=(0.1, 0.4, 0.6, 1), on_release_callback=None, disabled=False, **kwargs):
        super().__init__(**kwargs)
        self.default_color = color
        self.default_shadow_color = shadow_color
        self.disabled_color = (0.5, 0.5, 0.5, 1)
        self.text_color = (1, 1, 1, 1)
        self.disabled_text_color = (0.7, 0.7, 0.7, 1)
        self.shadow_height = dp(shadow_height)
        self.on_release_callback = on_release_callback
        self.size = kwargs.get("size", size)
        self.pos = kwargs.get("pos", (100, 200))
        self.disabled = disabled
        self.text = text
        self.font_size = font_size

        self.color = self.disabled_color if self.disabled else self.default_color
        self.shadow_color = self.default_shadow_color if not self.disabled else self.disabled_color

        with self.canvas:
            self.shadow_color_instruction = Color(*self.shadow_color)
            self.shadow = RoundedRectangle(size=self.size, pos=(self.pos[0], self.pos[1] - self.shadow_height),
                                           radius=[20])

            self.color_instruction = Color(*self.color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

        self.label = Label(
            text=self.text,
            halign="center",
            valign="middle",
            size=self.size,
            pos=self.pos,
            font_size=sp(self.font_size),
            color=self.disabled_text_color if self.disabled else self.text_color,
            font_name=main_font_style
        )
        self.add_widget(self.label)

        self.bind(pos=self.update_graphics, size=self.update_graphics)

    def update_graphics(self, *args):
        self.shadow.size = self.size
        self.shadow.pos = (self.pos[0], self.pos[1] - self.shadow_height)
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label.size = self.size
        self.label.pos = self.pos

    def on_touch_down(self, touch):
        if self.disabled:
            return False
        if self.collide_point(*touch.pos):
            self.rect.pos = (self.pos[0], self.pos[1] - self.shadow_height)
            self.label.pos = (self.pos[0], self.pos[1] - self.shadow_height)
            self.shadow_color_instruction.a = 0
            return True
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self.disabled:
            return False
        if self.collide_point(*touch.pos):
            self.rect.pos = self.pos
            self.label.pos = self.pos
            self.shadow_color_instruction.a = 1
            if self.on_release_callback:
                self.on_release_callback()
            return True
        return super().on_touch_up(touch)

    def set_disabled(self, state=True):
        self.disabled = state
        self.color = self.disabled_color if self.disabled else self.default_color
        self.color_instruction.rgba = self.color
        self.shadow_color_instruction.rgba = self.disabled_color if self.disabled else self.default_shadow_color
        self.label.color = self.disabled_text_color if self.disabled else self.text_color

    def set_text(self, new_text):
        self.text = new_text
        self.label.text = new_text


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)

        self.back_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)))
        self.all_clear = PressableButton(text="Сброс прогресса",
                                         on_release_callback=lambda: self.all_clear_event())

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(20))
        self.toolbar.add_widget(self.back_button)
        self.toolbar.add_widget(Label())

        self.box_for_clear = BoxLayout(orientation='vertical', padding=[dp(20)])
        self.box_for_clear.add_widget(Label())
        self.box_for_clear.add_widget(self.all_clear)
        self.box_for_clear.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[dp(20)])
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
        self.rect.size = self.size
        self.rect.pos = self.pos


class AllWordsScreen(Screen):
    def __init__(self, **kwargs):
        super(AllWordsScreen, self).__init__(**kwargs)

        self.label = Label(
            halign='center',
            valign='middle',
            size_hint=(1, None),
            text='Введите слово в поле выше',
            font_size=sp(24),
            font_name=main_font_style
        )
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(20), padding=dp(10))
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))
        self.vertical_layout.add_widget(self.label)
        self.scroll_view.add_widget(self.vertical_layout)

        self.back_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)),
                                       pos_hint={'top': 1})
        self.search_button = PressableButton(text="Поиск", size_hint=(None, None), size=(dp(300), dp(70)),
                                             on_release_callback=lambda: self.search_proc())

        self.search_widget = TextInput(size_hint_y=None, height=dp(60), font_size=sp(32))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30), spacing=dp(10))
        self.toolbar.add_widget(self.back_button)

        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(75), spacing=dp(10))
        self.toolbar2.add_widget(Label())
        self.toolbar2.add_widget(self.search_button)
        self.toolbar2.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[dp(20)])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.search_widget)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.toolbar2)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def read_csv_as_list(self):
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('SELECT word FROM words')
        words = [row[0] for row in cursor.fetchall()]

        conn.close()

        return words

    def text_gen(self, word):
        self.vertical_layout.clear_widgets()

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

        examples = super_dict.get(word, [])
        if not examples:
            self.vertical_layout.add_widget(Label(text="Примеры предложений отсутствуют.", font_size=sp(18)))
            return

        for i in range(min(3, len(examples))):
            example_pair = examples[i]

            horizontal_container = BoxLayout(orientation="horizontal", size_hint=(1, None), spacing=dp(10))

            example_label = Label(
                text=f'{example_pair[0]}\n------------------\n{example_pair[1]}',
                size_hint=(1, None),
                font_size=sp(18),
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )
            example_label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            image = ImageButton(
                source="audio.png",
                size_hint=(None, None),
                size=(dp(50), dp(50)),
                pos_hint={'center_y': 0.5},
                text=example_pair[0],
                word=word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(example_label)

            Clock.schedule_once(lambda dt: self.update_container_height(horizontal_container))

            self.vertical_layout.add_widget(horizontal_container)

        Clock.schedule_once(lambda dt: self.recalculate_all_heights())

    def no_word(self, word):
        self.vertical_layout.clear_widgets()

        label = Label(
            text=f'Слово не добавлено в\nраздел "мои слова"',
            font_size=sp(24),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            font_name=main_font_style
        )
        label.bind(texture_size=self._resize_label)
        self.vertical_layout.add_widget(label)

    def no_input(self, word):
        self.vertical_layout.clear_widgets()

        label = Label(
            text=f'Введите слово в поле выше',
            font_size=sp(24),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            font_name=main_font_style
        )
        label.bind(texture_size=self._resize_label)
        self.vertical_layout.add_widget(label)

    def search_proc(self, *args):
        self.word = self.search_widget.text.strip()
        if self.word in self.read_csv_as_list():
            self.text_gen(self.word)
        elif self.word in super_dict.keys() and not (self.word in self.read_csv_as_list()):
            self.label.text = f'Слово ещё не изучено'
        elif self.word == '':
            self.label.text = f"Введите слово в поле выше"
        else:
            self.label.text = f"Слово не найдено в базе"

    def update_container_height(self, horizontal_container):
        max_height = max(child.height for child in horizontal_container.children)
        horizontal_container.height = max_height + 20
        print(f"Updated container height: {horizontal_container.height}")

    def recalculate_all_heights(self, *_):
        for child in self.vertical_layout.children:
            if isinstance(child, BoxLayout):
                max_height = max(grandchild.height for grandchild in child.children)
                child.height = max_height + 20
                print(f"Recalculated container height: {child.height}")

    def _resize_label(self, instance, texture_size):
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)

    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label.text_size = (self.width - 40, None)


class WordShow(Screen):
    def __init__(self, **kwargs):
        super(WordShow, self).__init__(**kwargs)

        self.back_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(20))
        self.toolbar.add_widget(self.back_button)

        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(20), padding=dp(10))
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))
        self.scroll_view.add_widget(self.vertical_layout)

        self.layout = BoxLayout(orientation='vertical', padding=[dp(20)])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.scroll_view)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def update_content(self, word):
        self.vertical_layout.clear_widgets()

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

        examples = super_dict.get(word, [])
        if not examples:
            self.vertical_layout.add_widget(Label(text="Примеры предложений отсутствуют.", font_size=sp(18)))
            return

        for i in range(min(3, len(examples))):
            example_pair = examples[i]

            horizontal_container = BoxLayout(orientation="horizontal", size_hint=(1, None), spacing=dp(10))

            example_label = Label(
                text=f'{example_pair[0]}\n------------------\n{example_pair[1]}',
                size_hint=(1, None),
                font_size=sp(18),
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )
            example_label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            image = ImageButton(
                source="audio.png",
                size_hint=(None, None),
                size=(dp(50), dp(50)),
                pos_hint={'center_y': 0.5},
                text=example_pair[0],
                word=word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(example_label)

            Clock.schedule_once(lambda dt: self.update_container_height(horizontal_container))

            self.vertical_layout.add_widget(horizontal_container)

        Clock.schedule_once(lambda dt: self.recalculate_all_heights())

    def update_container_height(self, horizontal_container):
        max_height = max(child.height for child in horizontal_container.children)
        horizontal_container.height = max_height + 20
        print(f"Updated container height: {horizontal_container.height}")

    def recalculate_all_heights(self, *_):
        for child in self.vertical_layout.children:
            if isinstance(child, BoxLayout):
                max_height = max(grandchild.height for grandchild in child.children)
                child.height = max_height + 20
                print(f"Recalculated container height: {child.height}")

    def _resize_label(self, instance, texture_size):
        instance.height = texture_size[1]

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_words'

    def on_size(self, *args):
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
        def audio_thread():
            wav_file = f'G:\Lexi_voices\{self.word}_{self.find_sentence_index(self.word, self.text)}.wav'

            sample_rate, audio_data = read(wav_file)

            sd.play(audio_data, samplerate=sample_rate)
            sd.wait()

        thread = threading.Thread(target=audio_thread, daemon=True)
        thread.start()


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

        self.close_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)))

        self.next_button = PressableButton(text="СГЕНЕРИРОВАТЬ СЛОВО", font_size=20, size=(dp(200), dp(75)),
                                           on_release_callback=lambda: self.text_load())

        self.jorn_button = PressableButton(text="в 'мои' слова", font_size=16,
                                           on_release_callback=lambda: self.add_to_my_words())

        self.more_ex_button = PressableButton(text="Ещё примеры", on_release_callback=lambda: self.more_w(),
                                              font_size=16)

        self.jorn_button.set_disabled(True)
        self.more_ex_button.set_disabled(True)

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(20))
        self.toolbar.add_widget(self.close_button)

        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        self.toolbar2.add_widget(self.next_button)

        self.scroll_view = ScrollView(size_hint=(1, 1))

        self.label = Label(
            halign='center',
            valign='middle',
            size_hint_y=None,
            text="Нажмите на кнопку 'Сгенирировать слово'\nчтобы мы подобрали вам слово",
            font_size=sp(24),
            font_name=main_font_style
        )
        self.label.bind(texture_size=self._resize_label)

        self.main_layout = BoxLayout(orientation='vertical', padding=[dp(20)], spacing=dp(20))

        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(20), padding=dp(10))
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))

        self.vertical_layout.add_widget(self.label)

        self.scroll_view.add_widget(self.vertical_layout)

        self.func_layout2 = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(14))
        self.func_layout2.add_widget(self.jorn_button)
        self.func_layout2.add_widget(self.more_ex_button)

        self.main_layout.add_widget(self.toolbar)
        self.main_layout.add_widget(self.scroll_view)
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
                type7 DATETIME,
                is_my INT
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

    def add_to_my_words(self, *args):
        print(11)
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('''
                UPDATE words
                SET is_my = 1
                WHERE word = ?
            ''', (self.rand_word,))

        if cursor.rowcount == 0:
            print(f"Слово '{self.rand_word}' не найдено в базе данных.")
        else:
            print(f"Слово '{self.rand_word}' помечено как 'моё'.")

        conn.commit()
        conn.close()

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def _resize_label(self, instance, texture_size):
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        self.label.text_size = (self.width - 40, None)

    def read_csv_as_list(self):
        try:
            conn = sqlite3.connect('words.db')
            cursor = conn.cursor()

            cursor.execute('SELECT word FROM words')
            words = [row[0] for row in cursor.fetchall()]

            conn.close()
            print(words)
        except Exception as e:
            words = []

        return words

    def get_random_word_not_in_csv(self):
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
        self.jorn_button.set_disabled(False)
        self.more_ex_button.set_disabled(False)
        self.rand_word = self.get_random_word_not_in_csv()

        self.vertical_layout.clear_widgets()

        self.label.text = f"Ваше слово {self.rand_word}"
        self.vertical_layout.add_widget(self.label)

        def update_container_height(horizontal_container):
            max_height = max(child.height for child in horizontal_container.children)
            horizontal_container.height = max_height + 20
            print(f"Updated container height: {dp(horizontal_container.height)}")

        for i in range(3):
            horizontal_container = BoxLayout(
                orientation="horizontal",
                size_hint=(1, None),
                spacing=dp(10)
            )

            label = Label(
                text=f'{super_dict[self.rand_word][i][0]}\n------------------\n'
                     f'{super_dict[self.rand_word][i][1]}',
                size_hint=(1, None),
                font_size=sp(18),
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )

            label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            image = ImageButton(
                source="audio.png",
                size_hint=(None, None),
                size=(dp(50), dp(50)),
                pos_hint={'center_y': 0.5},
                text=f'{super_dict[self.rand_word][i][0]}',
                word=self.rand_word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(label)

            Clock.schedule_once(lambda dt: update_container_height(horizontal_container))

            self.vertical_layout.add_widget(horizontal_container)

        def recalculate_all_heights(*_):
            for child in self.vertical_layout.children:
                if isinstance(child, BoxLayout):
                    max_height = max(grandchild.height for grandchild in child.children)
                    child.height = max_height + 20
                    print(f"Recalculated container height: {dp(child.height)}")

        Clock.schedule_once(lambda dt: recalculate_all_heights())

        self.next_button.set_text('Следующее слово')
        self.add_word_to_database(self.rand_word)

    def more_w(self, *args):
        if not hasattr(self, "rand_word") or not self.rand_word:
            print("Слово ещё не сгенерировано.")
            return

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user",
                           "content": f"Give one example sentence in English using the word '{self.rand_word}'. "
                                      "After the sentence, put a ' / ' sign and provide a Russian translation. "
                                      "Example: He admitted that he was lost. / Он признал, что заблудился."}]
            )

            new_example = response.choices[0].message.content.strip()
            print(new_example)
            example_parts = new_example.split(' / ')

            if len(example_parts) < 2:
                print("Ошибка API: Получен некорректный формат ответа.")
                return

            english_sentence = example_parts[0].strip()
            russian_translation = example_parts[1].strip()

            horizontal_container = BoxLayout(
                orientation="horizontal",
                size_hint=(1, None),
                spacing=dp(10),
                height=dp(70)
            )

            label = Label(
                text=f"{english_sentence}\n------------------\n{russian_translation}",
                size_hint=(1, None),
                font_size=sp(18),
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )

            label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            empty_widget = Widget(size_hint=(None, None), size=(dp(50), dp(50)))

            horizontal_container.add_widget(empty_widget)
            horizontal_container.add_widget(label)

            def update_height(*_):
                max_height = max(child.height for child in horizontal_container.children)
                horizontal_container.height = max_height + dp(10)
                print(f"Updated example block height: {horizontal_container.height}")

            Clock.schedule_once(update_height)

            self.vertical_layout.add_widget(horizontal_container)

        except Exception as e:
            print(f"Ошибка при запросе к API: {e}")
            error_label = Label(
                text="Ошибка загрузки примера...",
                font_size=sp(18),
                color=(1, 0, 0, 1)
            )
            self.vertical_layout.add_widget(error_label)

    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos


class PracticeScreen(Screen):
    def __init__(self, **kwargs):
        super(PracticeScreen, self).__init__(**kwargs)

        self.current_word = None
        self.correct_answer = None
        self.selected_answer = None
        self.type_question = 0
        self.stand_chanse = [0.5, 0.7, 0.8, 0.9, 0.95, 0.98]

        self.layout = BoxLayout(orientation='vertical', padding=[dp(20)], spacing=dp(10))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(75), spacing=dp(10))

        self.difficulty_spinner = Spinner(
            text='Легчайший',
            values=('Легчайший', 'Лёгкий', 'Средний', 'Сложный', 'Случайно'),
            size_hint=(1, None),
            height=dp(75)
        )
        self.difficulty_spinner.bind(text=self.on_difficulty_change)
        self.toolbar.add_widget(self.difficulty_spinner)

        self.stop_button = Button(text="Завершить", size_hint=(1, None), height=dp(75))
        self.stop_button.bind(on_release=self.stop)
        self.toolbar.add_widget(self.stop_button)

        self.back_button = Button(text="Назад", size_hint=(1, None), height=dp(75))
        self.back_button.bind(on_release=self.go_back)
        self.toolbar.add_widget(self.back_button)

        self.center_label = Label(
            text="Выберите уровень сложности и нажимайте на кнопку 'Старт'",
            font_size=32, halign='center', valign='middle'
        )
        self.center_label.bind(texture_size=self._resize_label)

        self.bottom_toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(75))
        self.start_button = Button(text="Старт", size_hint=(1, None), height=dp(75))
        self.start_button.bind(on_release=self.start_practice)
        self.bottom_toolbar.add_widget(self.start_button)

        self.question_layout = GridLayout(cols=3, spacing=dp(10), padding=[0, dp(10)], size_hint_y=None, height=0)
        self.answer_buttons = []
        for _ in range(6):
            btn = Button(size_hint=(1, None), height=dp(75), opacity=0)
            btn.bind(on_release=self.select_answer)
            self.answer_buttons.append(btn)
            self.question_layout.add_widget(btn)

        self.audio_butt_lay = BoxLayout(orientation='horizontal', size_hint_y=None, height=75)

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
        self.manager.transition = FadeTransition(duration=0.2)
        self.manager.current = 'main'

    def load_new_question_input(self, q_word):
        self.clear()

        self.current_word = self.translate_to_english(q_word)

        self.center_label.text = f"Переведите: {self.current_word}"

        self.input_field = TextInput(
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            font_size=sp(24),
            hint_text="Введите перевод..."
        )
        self.question_layout.add_widget(self.input_field)

    def load_new_question_s_input(self, q_word):
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        print(self.rand_sent_question_norm_ang)

        self.center_label.text = f"Переведите: {self.rand_sent[1]}"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            font_size=sp(24),
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
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]

        btn_audio = Button(text='Прослушать', size_hint_x=0.2, height=dp(75))  # Изначально кнопки невидимы
        btn_audio.bind(
            on_release=lambda instance: self.play_audio(q_word, self.rand_sent_question_norm_ang))
        self.audio_butt_lay.add_widget(btn_audio)
        btn_audio.disabled = False

        self.center_label.text = f"Напишите предложение на слух"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            font_size=sp(24),
            hint_text="Введите перевод...",
        )
        self.question_layout.add_widget(self.input_field_s)

    def load_new_question_s_input_audio_hard(self, q_word):
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)

        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]

        self.btn_audio = Button(text='Прослушать', size_hint_x=0.2, height=dp(75))
        self.btn_audio.bind(
            on_release=lambda instance: self.play_one_audio(q_word, self.rand_sent_question_norm_ang))
        self.audio_butt_lay.add_widget(self.btn_audio)
        self.btn_audio.disabled = False

        # print(self.rand_sent_question_norm_ang)

        self.center_label.text = f"Напишите предложение на слух с первого раза"

        self.input_field_s = TextInput(
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            font_size=sp(24),
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
        def audio_thread():
            wav_file = f'G:\Lexi_voices\{word}_{self.find_sentence_index(word, sentence)}.wav'

            sample_rate, audio_data = read(wav_file)

            sd.play(audio_data, samplerate=sample_rate)
            sd.wait()

        thread = threading.Thread(target=audio_thread, daemon=True)
        thread.start()

    def play_one_audio(self, word, sentence):
        self.btn_audio.disabled = True

        def audio_thread():
            wav_file = f'G:\Lexi_voices\{word}_{self.find_sentence_index(word, sentence)}.wav'

            sample_rate, audio_data = read(wav_file)

            sd.play(audio_data, samplerate=sample_rate)
            sd.wait()

        thread = threading.Thread(target=audio_thread, daemon=True)
        thread.start()

    def start_practice(self, *args):
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
            self.question_layout.height = dp(2 * 85)

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
        words = sentence.split()
        modified_words = [
            "_" * len(word) if target_word.lower() in word.lower() else word
            for word in words
        ]
        return " ".join(modified_words)

    def load_new_question_s_btn(self, q_word):
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
        self.clear()

        self.rand_sent = self.get_random_sent(q_word)
        self.rand_sent_question = self.replace_word_with_blanks(self.rand_sent[0],
                                                                q_word)
        self.rand_sent_question_norm_ang = self.rand_sent[0]
        self.rand_sent_question_norm_ru = self.rand_sent[1]
        self.current_word = self.translate_to_english(q_word)

        self.input_field_s_w = TextInput(
            size_hint=(1, None),
            height=dp(50),
            multiline=False,
            font_size=sp(24),
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
        self.selected_answer = instance.text
        for btn in self.answer_buttons:
            btn.background_color = [0.8, 0.8, 0.8, 1]
        instance.background_color = [0.6, 0.6, 0.6, 1]

    def show_correct_answer_btn(self):
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
        if self.input_field.text.strip().lower() == self.main_word.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = 'Правильно!'
            self.update_bd_for_word(self.main_word, 'type3')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно, правильный ответ: {self.main_word}'

    def show_correct_answer_input_s_w(self, ang, ru):
        if self.input_field_s_w.text.strip().lower() == self.main_word.strip().lower():
            self.center_label.color = [0, 1, 0, 1]
            self.center_label.text = f'Правильно!\n\n{ang}\n\n{ru}'
            self.update_bd_for_word(self.main_word, 'type5')
        else:
            self.center_label.color = [1, 0, 0, 1]
            self.center_label.text = f'Неправильно\n\n{ang}\n\n{ru}'

    def translate_to_english(self, word):
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
        self.rect.size = self.size
        self.rect.pos = self.pos

    def _resize_label(self, instance, texture_size):
        instance.size = instance.texture_size
        instance.text_size = (self.width - 40, None)


class CompWordsScreen(Screen):
    def __init__(self, **kwargs):
        super(CompWordsScreen, self).__init__(**kwargs)

        self.back_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)),
                                       pos_hint={'top': 1})
        self.search_button = PressableButton(text="Поиск", size_hint=(None, None), size=(dp(150), dp(70)),
                                             pos_hint={'top': 1},
                                             on_release_callback=lambda: self.search_menu(self.manager))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(76))
        self.toolbar.add_widget(self.back_button)
        self.toolbar.add_widget(Label())
        self.toolbar.add_widget(self.search_button)

        self.scroll_view = ScrollView()

        self.layout = GridLayout(cols=2, spacing=dp(20), size_hint_y=None)

        self.scroll_view.add_widget(self.layout)

        self.layout.bind(minimum_height=self.layout.setter('height'))

        self.main_layout = BoxLayout(orientation='vertical', padding=[dp(20)], spacing=dp(10))
        self.main_layout.add_widget(self.toolbar)
        self.main_layout.add_widget(self.scroll_view)
        self.add_widget(self.main_layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def on_pre_enter(self, *args):
        self.layout.clear_widgets()

        for i in self.read_csv_as_list():
            btn = PressableButton(text=f'{i}', size_hint=(1, None), size=(dp(150), dp(70)),
                                  on_release_callback=lambda text=i: self.word_show(self.manager, text))
            self.layout.add_widget(btn)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'main'

    def read_csv_as_list(self):
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('''
                SELECT word FROM words
                WHERE is_my = 1
            ''')

        words = [row[0] for row in cursor.fetchall()]
        conn.close()
        return words

    def search_menu(self, screen_manager):
        if not self.manager.has_screen('comp_search_menu'):
            self.comp_search_menu = SearchMenuComp(name='comp_search_menu')
            self.manager.add_widget(self.comp_search_menu)
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_search_menu'

    def word_show(self, screen_manager, word):
        print(1)
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
        self.rect.size = self.size
        self.rect.pos = self.pos


class SearchMenuComp(Screen):
    def __init__(self, **kwargs):
        super(SearchMenuComp, self).__init__(**kwargs)

        self.label = Label(
            halign='center',
            valign='middle',
            size_hint=(1, None),
            text='Введите слово в поле выше',
            font_size=sp(24),
            font_name=main_font_style
        )
        self.scroll_view = ScrollView(size_hint=(1, 1))
        self.vertical_layout = BoxLayout(orientation="vertical", size_hint_y=None, spacing=dp(20), padding=dp(10))
        self.vertical_layout.bind(minimum_height=self.vertical_layout.setter('height'))
        self.vertical_layout.add_widget(self.label)
        self.scroll_view.add_widget(self.vertical_layout)

        self.back_button = CloseButton(on_close_callback=self.go_back, size_hint=(None, None), size=(dp(20), dp(20)),
                                       pos_hint={'top': 1})
        self.search_button = PressableButton(text="Поиск", size_hint=(None, None), size=(dp(300), dp(70)),
                                             on_release_callback=lambda: self.search_proc())

        self.search_widget = TextInput(size_hint_y=None, height=dp(60), font_size=sp(32))

        self.toolbar = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30), spacing=dp(10))
        self.toolbar.add_widget(self.back_button)

        self.toolbar2 = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(75), spacing=dp(10))
        self.toolbar2.add_widget(Label())
        self.toolbar2.add_widget(self.search_button)
        self.toolbar2.add_widget(Label())

        self.layout = BoxLayout(orientation='vertical', padding=[dp(20)])
        self.layout.add_widget(self.toolbar)
        self.layout.add_widget(self.search_widget)
        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(self.toolbar2)
        self.add_widget(self.layout)

        with self.canvas.before:
            self.color_rect = Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

    def go_back(self, *args):
        self.manager.transition = FadeTransition(duration=0.20)
        self.manager.current = 'comp_words'

    def get_my_words(self):
        conn = sqlite3.connect('words.db')
        cursor = conn.cursor()

        cursor.execute('''
                        SELECT word FROM words
                        WHERE is_my = 1
                    ''')

        words = [row[0] for row in cursor.fetchall()]
        conn.close()
        return words

    def text_gen(self, word):
        self.vertical_layout.clear_widgets()

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

        examples = super_dict.get(word, [])
        if not examples:
            self.vertical_layout.add_widget(Label(text="Примеры предложений отсутствуют.", font_size=sp(18)))
            return

        for i in range(min(3, len(examples))):
            example_pair = examples[i]

            horizontal_container = BoxLayout(orientation="horizontal", size_hint=(1, None), spacing=dp(10))

            example_label = Label(
                text=f'{example_pair[0]}\n------------------\n{example_pair[1]}',
                size_hint=(1, None),
                font_size=sp(18),
                halign="left",
                valign="middle",
                text_size=(0, None),
                font_name="IntroDemo-BlackCAPS.otf"
            )
            example_label.bind(
                width=lambda s, w: s.setter('text_size')(s, (w, None)),
                texture_size=lambda s, t: s.setter('height')(s, t[1])
            )

            image = ImageButton(
                source="audio.png",
                size_hint=(None, None),
                size=(dp(50), dp(50)),
                pos_hint={'center_y': 0.5},
                text=example_pair[0],
                word=word
            )

            horizontal_container.add_widget(image)
            horizontal_container.add_widget(example_label)

            Clock.schedule_once(lambda dt: self.update_container_height(horizontal_container))

            self.vertical_layout.add_widget(horizontal_container)

        Clock.schedule_once(lambda dt: self.recalculate_all_heights())

    def no_word(self, word):
        self.vertical_layout.clear_widgets()

        label = Label(
            text=f'Слово не добавлено в\nраздел "мои слова"',
            font_size=sp(24),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            font_name=main_font_style
        )
        label.bind(texture_size=self._resize_label)
        self.vertical_layout.add_widget(label)

    def no_input(self, word):
        self.vertical_layout.clear_widgets()

        label = Label(
            text=f'Введите слово в поле выше',
            font_size=sp(24),
            halign="center",
            valign="middle",
            size_hint=(1, None),
            font_name=main_font_style
        )
        label.bind(texture_size=self._resize_label)
        self.vertical_layout.add_widget(label)

    def search_proc(self, *args):
        self.word = self.search_widget.text.strip()
        if self.word in self.get_my_words():
            self.text_gen(self.word)
        elif self.word in super_dict.keys() and not (self.word in self.get_my_words()):
            self.label.text = f'Слово не добавлено в раздел "мои слова"'
        elif self.word == '':
            self.label.text = f"Введите слово в поле выше"
        else:
            self.label.text = f"Слово не найдено"

    def update_container_height(self, horizontal_container):
        max_height = max(child.height for child in horizontal_container.children)
        horizontal_container.height = max_height + 20
        print(f"Updated container height: {horizontal_container.height}")

    def recalculate_all_heights(self, *_):
        for child in self.vertical_layout.children:
            if isinstance(child, BoxLayout):
                max_height = max(grandchild.height for grandchild in child.children)
                child.height = max_height + 20
                print(f"Recalculated container height: {child.height}")

    def _resize_label(self, instance, texture_size):
        instance.height = instance.texture_size[1]
        instance.size_hint_y = None

    def _update_text_sizes(self, *args):
        self.label2.text_size = (self.width - 40, None)
        self.label.text_size = (self.width - 40, None)

    def on_size(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.label.text_size = (self.width - 40, None)


class MainWind(App):
    def build(self):
        self.screen_manager = ScreenManager()
        self.settings_screen = SettingsScreen(name='settings')
        self.main_screen = Screen(name='main')

        with self.main_screen.canvas.before:
            Color(0.23, 0.14, 0.4, 1)
            self.rect = Rectangle(size=self.main_screen.size, pos=self.main_screen.pos)

        self.box1 = BoxLayout(size_hint_y=None, height=dp(75))
        self.box2 = BoxLayout(orientation='vertical', spacing=dp(25))
        self.box_main = BoxLayout(orientation='vertical', padding=[dp(20)], spacing=dp(40))

        self.label = Label(text='Lexi\nLearn', font_size=sp(30), font_name=main_font_style)
        self.label2 = Label(halign='center', size_hint_y=0.4, font_size=sp(20), font_name=main_font_style)

        self.btn = PressableButton(text='Настройки', font_size=22,
                                   on_release_callback=lambda: self.open_settings(self.screen_manager))
        self.btn3 = PressableButton(text="ТЕОРИЯ", font_size=22,
                                    on_release_callback=lambda: self.open_theory(self.screen_manager))
        self.btn4 = PressableButton(text='ПРАКТИКА', font_size=22,
                                    on_release_callback=lambda: self.open_practice(self.screen_manager))
        self.btn5 = PressableButton(text='"МОИ" СЛОВА', font_size=22,
                                    on_release_callback=lambda: self.open_comp_words_bank(self.screen_manager))
        self.btn6 = PressableButton(text='БАНК ИЗУЧЕННЫХ СЛОВ', font_size=22,
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
        self.label2.text = f'Статистика\n\nИзучено слов: {studied_words}\nОсталось {remaining_percentage}%'

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
        try:
            conn = sqlite3.connect('words.db')
            cursor = conn.cursor()

            cursor.execute('SELECT word FROM words')
            words = [row[0] for row in cursor.fetchall()]

            conn.close()
            print(words)
        except Exception as e:
            words = []

        return words


if __name__ == '__main__':
    MainWind().run()
