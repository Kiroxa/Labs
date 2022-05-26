import xml.dom.minidom as minidom


class DomWriter:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.domtree = minidom.Document()
        self.rows = []

    def create_xml_student(self, data: tuple):
        ''' Decorate students data into xml view and add into file '''
        
        student = self.domtree.createElement("student")

        for value in data:
            temp_child = self.domtree.createElement(value)
            student.appendChild(temp_child)

            node_text = self.domtree.createTextNode(data[value].strip())
            temp_child.appendChild(node_text) 

        self.rows.append(student)
        
    def create_xml_file(self):
        ''' Create an xml file structure '''
        
        pass_table = self.domtree.createElement("pass_table")

        for student in self.rows:
            pass_table.appendChild(student)

        self.domtree.appendChild(pass_table)

        self.domtree.writexml( open(self.file_name, 'w'),
               indent="  ",
               addindent="  ",
               newl='\n')
        self.domtree.unlink()
