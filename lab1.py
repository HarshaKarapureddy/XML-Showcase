import xml.etree.ElementTree as ET

class tempConv:
    def c_to_f(self, c):
        answer = 9/5 * c + 32
        return answer

class forecast_xml:
    def __init__(self):
        self.conv = tempConv()
        self.tree = ET.parse('forecast.xml')
        self.root = self.tree.getroot()

    def parse(self):
        for i in self.root:
            c = i[1].text
            print(i[0].text+ ": " + c + " Celcius, " + str(self.conv.c_to_f(int(c))) + " Fahrenheit")

app = forecast_xml()
app.parse()