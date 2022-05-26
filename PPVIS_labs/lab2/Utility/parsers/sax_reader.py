import xml.sax as sax


class SaxReader(sax.ContentHandler):
    def __init__(self) -> None:
        super().__init__()
        self.table_datas = []
        self.student_data = []
        self.parser = sax.make_parser()

    def startElement(self, name, attrs):
        ''' When start to read '''
        
        self.current = name
        if name == "student":
            pass

    def characters(self, content):
        ''' Fields of every student '''
        if self.current == "name":
            self.name = content
        elif self.current == "group":
            self.group = content
        elif self.current == "sick":
            self.sick = content
        elif self.current == "skip":
            self.skip = content
        elif self.current == "other":
            self.other = content

    def endElement(self, name):
        ''' Then end to read '''
        
        if self.current == "name":
            self.student_data.append(self.name)
        elif self.current == "group":
            self.student_data.append(self.group)
        elif self.current == "sick":
            self.student_data.append(self.sick)
        elif self.current == "skip":
            self.student_data.append(self.skip)
        elif self.current == "other":
            self.student_data.append(self.other)

        if len(self.student_data) == 5:
            self.table_datas.append(tuple(self.student_data))
            self.student_data = []

        self.current = ""
