from random import randint
from parsers.dom_writer import DomWriter

import names


class XMLGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_xml_files(files_count, students_count):
        ''' Generate a numbers of unknown students'''
        
        for i in range(files_count):
            path = f"xml/{str(i)}.xml"
            data_dict = {}
            with open(path, 'w') as f:
                dom = DomWriter(path)
                for _ in range(students_count):
                    data_dict["name"] = names.get_full_name()
                    data_dict["group"] = str(randint(100000, 999999))
                    data_dict["sick"] = str(randint(0, 50))
                    data_dict["skip"] = str(randint(0, 50))
                    data_dict["other"] = str(randint(0, 50))

                    dom.create_xml_student(data_dict)
            dom.create_xml_file()


def main():
    XMLGenerator.generate_xml_files(files_count=10, students_count=50)


if __name__ == "__main__":
    main()