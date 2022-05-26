
'''file with classes to create and custom dialog windows for every button '''

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class DialogContent(BoxLayout):
    pass

class InputDialogContent(DialogContent):
    pass

class FilterDialogContent(DialogContent):
    pass

class DeleteDialogContent(DialogContent):
    pass

class UploadDialogContent(DialogContent):
    pass

class SaveDialogContent(DialogContent):
    pass



class DialogWindow(MDDialog):
    def __init__(self, **kwargs):
        super().__init__(
            title=kwargs["title"],
            type="custom",
            content_cls=kwargs["content_cls"],
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.close
                ),
            ],
        )
        self.mode = kwargs["mode"]
        self.model = kwargs["model"]

    def close(self, obj):
        self.dismiss()
        self.model.close_dialog()


class InputWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="New student: ",
                content_cls=InputDialogContent(),
                mode="input",
                model=kwargs["model"], 
        )

    
    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.input_fio.text,
                self.content_cls.ids.input_group.text,
                self.content_cls.ids.input_sick.text,
                self.content_cls.ids.input_skip.text,
                self.content_cls.ids.input_other.text,
            ]
        )


class FilterWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Filter students: ",
                content_cls=FilterDialogContent(),
                mode="filter",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.filter_fio.text,
                self.content_cls.ids.filter_group.text,
                self.content_cls.ids.filter_sick.text,
                self.content_cls.ids.filter_skip.text,
                self.content_cls.ids.filter_other.text,
                self.content_cls.ids.filter_total.text,
            ]
        )


class DeleteWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Delete students: ",
                content_cls=DeleteDialogContent(),
                mode="delete",
                model=kwargs["model"],
        )

    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(
            [
                self.content_cls.ids.delete_fio.text,
                self.content_cls.ids.delete_group.text,
                self.content_cls.ids.delete_sick.text,
                self.content_cls.ids.delete_skip.text,
                self.content_cls.ids.delete_other.text,
                self.content_cls.ids.delete_total.text,
            ]
        )


class SaveWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Saving: ",
                content_cls=SaveDialogContent(),
                mode="save",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(self.content_cls.ids.save_path.text)


class UploadWindow(DialogWindow):
    def __init__(self, **kwargs):
        super().__init__(
                title="Upload: ",
                content_cls=UploadDialogContent(),
                mode="upload",
                model=kwargs["model"],
        )


    def close(self, obj):
        self.dismiss()
        self.model.close_dialog(self.content_cls.ids.upload_path.text)




Builder.load_file(os.path.join(os.path.dirname(__file__), "dialog_windows.kv"))