import xml.etree.ElementTree as ET

shop = ET.Element('shop')
category = ET.SubElement(shop, 'category', {'name' : 'Vegan Products'})

product_GMS = ET.SubElement(category, 'product', {'name' : 'Good Morning Sunshine'})
type_GMS =  ET.SubElement(product_GMS, 'type')
type_GMS.text = "cereals"
producer_GMS = ET.SubElement(product_GMS, "producer")
producer_GMS.text = "OpenEDG Testing Service"
price_GMS = ET.SubElement(product_GMS, "price")
price_GMS.text = "9.90"
currency_GMS = ET.SubElement(product_GMS, "currency")
currency_GMS.text = "USD"

product_SV = ET.SubElement(category, 'product', {'name' : 'Spaghetti Veganietto'})
type_SV =  ET.SubElement(product_SV, 'type')
type_SV.text = "pasta"
producer_SV = ET.SubElement(product_SV, "producer")
producer_SV.text = "Programmers Eat Pasta"
price_SV = ET.SubElement(product_SV, "price")
price_SV.text = "15.49"
currency_SV = ET.SubElement(product_SV, "currency")
currency_SV.text = "EUR"

product_FAM = ET.SubElement(category, 'product', {'name' : 'Fantastic Almond Milk'})
type_FAM =  ET.SubElement(product_FAM, 'type')
type_FAM.text = "beverages"
producer_FAM = ET.SubElement(product_FAM, "producer")
producer_FAM.text = "Drinks4Coders Inc."
price_FAM = ET.SubElement(product_FAM, "price")
price_FAM.text = "19.75"
currency_FAM = ET.SubElement(product_FAM, "currency")
currency_FAM.text = "USD"

ET.dump(shop)

tree = ET.ElementTree(shop)
tree.write('shop.xml', 'UTF-8', True)