from kivy.lang import Builder
from kivymd.app import MDApp

root_kv = """
FloatLayout:
    size_hint: 1,1
    AnchorLayout:
        anchor_x: "center"
        anchor_y: "top"
        MDToolbar:
            id: toolbar
            title: "KivyMD DEMO Home Page"
            md_bg_color: app.theme_cls.primary_color
            size_hint_y: None
            size: self.width, 100

    MDLabel:
        id: label
        pos_hint: {"center_x":.5, "center_y":.5}
        text: "You have pushed the button this many times:"
        halign: "center"
        color: .2,.2,.2,1
    MDLabel:
        id: counter
        pos: 0, -75
        pos_hint: {"center_x":.5}
        color: .4,.4,.4,1
        size: self.width, 64
        halign: "center"
        text: "0"
        font_size: 64

    MDFloatingActionButton:
        #pos_hint: None, None
        pos: root.width - 160, 50
        md_bg_color: app.theme_cls.primary_color
        icon: "plus"
        on_press: app.press()
        



"""


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "KivyMD DEMO Home Page"
        self.count = 0
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(root_kv)
        self.root.ids.toolbar.ids.label_title.halign = "center"
        self.root.ids.toolbar.ids.label_title.font_size = 32
        #self.root.ids.counter.pos = (0, self.root.ids.label.pos[1])
        #self.root.ids.counter.pos = (0, 0)

    def press(self):
        self.count += 1
        self.root.ids.counter.text = str(self.count)
        print("pressed")


if __name__ == "__main__":
    MainApp().run()
