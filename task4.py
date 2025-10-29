# извлечение данных
import xml.etree.ElementTree as ET


tree = ET.parse('currency.xml')
root = tree.getroot()

charcod_vector = []
valute_vector = []

for valute in root.findall('Valute'):  
    if valute.find('Nominal').text == "10":
        charcod_vector.append(valute.find('CharCode').text)
    if valute.find('Nominal').text == "100":
        charcod_vector.append(valute.find('CharCode').text

print("CharCode:", charcod_vector)
