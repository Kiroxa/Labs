import re

# parsers
from Utility.parsers.dom_writer import DomWriter
from Utility.parsers.sax_reader import SaxReader


class MyScreenModel:
    """
    The MyScreenModel class is a data model implementation.The model provides an
    interface through which to work with stored values. The model contains
    methods for registration, deletion and notification observers.
    """

    # list of row data that are hidden
    _not_filtered = []


    def __init__(self, table):
        self.table = table
        self.dialog = None
        self._observers = []


    def add_observer(self, observer):
        self._observers.append(observer)


    def remove_observer(self, observer):
        self._observers.remove(observer)


    def notify_observers(self, data):
        for x in self._observers:
            x.model_is_changed(data)


    def read_data_from_file(self, path):
        ''' Read a students from xml and add it in the table '''
        
        try:
            handler = SaxReader()
            handler.parser.setContentHandler(handler)
            handler.parser.parse("xml/"+path)

            # print(handler.table_datas)
            for data in handler.table_datas:
                self.add_new_student_in_table(data)
        except Exception as e:
            pass 


    @staticmethod
    def create_empty_file(path):
        try:
            with open(path, 'w'):
                pass
            return True
        except Exception as e:
            return False 


    def write_data_in_file(self, path: str):
        ''' Save students from table to xml file '''
        
        path = "xml/"+path
        if self.create_empty_file(path):
            dom = DomWriter(path)
            data_dict = {}
            for row in self.table.row_data:
                data_dict["name"] = row[0]
                data_dict["group"] = row[1]
                data_dict["sick"] = row[2]
                data_dict["skip"] = row[3]
                data_dict["other"] = row[4]

                dom.create_xml_student(data_dict)
            dom.create_xml_file()


    def add_new_student_in_table(self, row):
        try:
            self.table.row_data.insert(
                len(self.table.row_data),
                (
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    str( int(row[2]) + int(row[3]) + int(row[4]) )
                    )
                )
        except ValueError as v:
            pass

    @staticmethod
    def get_surname(fio: str):
        return fio.split()[1]


    def refresh_students_in_table(self):
        ''' When press a refresh button '''
        
        try:
            self.table.row_data += self._not_filtered
        except ValueError as v:
            pass
        self._not_filtered = []


    def select_students_by_filters(self, filters: list):
        ''' Select students by:
            - surname
            - group
            - diapason
            and put their in the list
        '''
        
        # this list
        selected_students = []

        for row in self.table.row_data:
            # wave 1
            if filters[0]: # fio
                fio = self.get_surname(row[0])
                filter_fio = filters[0]
                if fio != filter_fio:
                    selected_students.append(tuple(row))
                    continue
            # wave 2
            if filters[1] and row[1] != filters[1]: # group
                    selected_students.append(tuple(row))
                    continue
            # wave 3
            for i in range(2, len(filters)):
                if filters[i]: # sick, skip, other, total
                    if re.match(r'^\d+-\d+$', filters[i]):
                        start, end = filters[i].split('-')
                        if int(row[i]) not in range(int(start), int(end)+1):
                            selected_students.append(tuple(row))
                            continue
                    elif int(row[i]) != int(filters[i]):
                        selected_students.append(tuple(row))
                        continue 
        return selected_students


    def filter_students_in_table(self, filters: list):
        ''' filter a student in Table according to filters parameters '''
        
        self._not_filtered = self.select_students_by_filters(filters=filters)
        for row in self._not_filtered:
            try:
                self.table.row_data.remove(row)
            except Exception as e:
                # print(e.__str__())
                pass
    
    @staticmethod
    def empty_filters(filters):
        ''' Check if we won't apply some filter in the dialog item '''
        
        for filt in filters:
            if filt != '':
                return False
        return True


    def delete_students_from_table(self, filters):
        ''' delete a students that are in _not_filtered list '''
        
        unlucky_count = 0
        if self.empty_filters(filters):
            return unlucky_count
        lucky_students = self.select_students_by_filters(filters=filters)
        for row in self.table.row_data[:]:
            if row not in lucky_students:
                try:
                    self.table.row_data.remove(row)
                    unlucky_count += 1
                except Exception as e:
                    pass
        return unlucky_count


    def open_dialog(self, dialog, mode):
        ''' Get dialog window to collet input data '''
        self.dialog = dialog 


    def close_dialog(self, dialog_data: list=[]):
        ''' Return dialog window  '''
        
        data = dialog_data
        self.notify_observers(data)
        self.dialog = None     