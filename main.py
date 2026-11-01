from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class RomanticApp(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=24,
            spacing=20
        )
        title = Label(
            text="عالم الحب والرومانسية",
            font_size="26sp",
            color=(1, 0.2, 0.5, 1),
            size_hint_y=None,
            height="70dp"
        )
        poem = Label(
            text="عيناكِ غابتا نخيلٍ ساعةَ السحر...\n"
                 "أو شرفتان راح يثنيهما القمر\n"
                 "حبكِ عاصفةٌ تسري في الروحِ وتستقر",
            font_size="20sp",
            color=(0.9, 0.9, 0.9, 1),
            halign="center",
            valign="middle"
        )
        poem.bind(size=lambda instance, value: setattr(instance, "text_size", value))
        layout.add_widget(title)
        layout.add_widget(poem)
        return layout

if __name__ == "__main__":
    RomanticApp().run()
