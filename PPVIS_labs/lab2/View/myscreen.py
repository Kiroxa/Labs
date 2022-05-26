import os

from Utility.observer import Observer
import Utility.dialog_windows as window

# kivy
from kivy.properties import ObjectProperty
from kivy.lang import Builder

# kivyMD
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar


class MyScreenView(MDScreen, Observer):
    """ A class that implements the visual presentation `MyScreenModel`. """

    # <Controller.myscreen_controller.MyScreenController object>.
    controller = ObjectProperty()
    # <Model.myscreen.MyScreenModel object>.
    model = ObjectProperty()


    def __init__(self, **kw):
        super().__init__(**kw)
        self.model.add_observer(self)  # register the view as an observer
        self.screen = Screen() 


    def open_dialog(self, mode: str):
        """ Call input, filter and delete windows, save and upload """
        
        if mode == "input":
            self.dialog = window.InputWindow(model=self.model)
        elif mode == "filter":
            self.dialog = window.FilterWindow(model=self.model)
        elif mode == "delete":
            self.dialog = window.DeleteWindow(model=self.model)
        elif mode == "upload":
            self.dialog = window.UploadWindow(model=self.model)
        elif mode == "save":
            self.dialog = window.SaveWindow(model=self.model)

        self.dialog.open()
        self.controller.dialog(mode, self.dialog)
        

    def close_dialog(self, dialog_data: list=[]):
        ''' When you end to edit data in the dialog window, after closing 
            it calls specific dialog window function '''
            
        if self.dialog.mode == "input":
            self.controller.input_student(dialog_data)
        elif self.dialog.mode == "filter":
            self.controller.filter_students(dialog_data)
        elif self.dialog.mode == "delete":
            unlucky = self.controller.delete_students(dialog_data)
            Snackbar(text=f"{unlucky} students are deleted!").open() 
        elif self.dialog.mode == "upload":
            self.controller.upload_from_file(dialog_data)
        elif self.dialog.mode == "save":
            self.controller.save_in_file(dialog_data)
        self.dialog = None 


    def model_is_changed(self, data):
        """ The method is called when the model changes. """

        self.close_dialog(data)
    

    def refresh(self):
        ''' refresh button '''
        
        self.controller.refresh() 


    def build(self):
        ''' Create user interface '''
        
        self.add_widget(self.model.table)
        return self



#load interface from kv file
Builder.load_file(os.path.join(os.path.dirname(__file__), "myscreen.kv"))