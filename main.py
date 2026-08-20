from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MedlinkApp(App):

    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=40,
            spacing=20
        )

        titre = Label(
            text="MEDLINK",
            font_size=40,
            bold=True
        )

        sous_titre = Label(
            text="La santé connectée au Mali",
            font_size=20
        )

        bouton = Button(
            text="COMMENCER",
            size_hint=(1, 0.25),
            font_size=20
        )

        layout.add_widget(titre)
        layout.add_widget(sous_titre)
        layout.add_widget(bouton)

        return layout


if __name__ == "__main__":
    MedlinkApp().run()
