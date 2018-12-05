from lxml import objectify
import pandas as pd

col = ['genid', 'rge', 'is_block_power_on_off']
# df = pd.DataFrame(columns=('target_date', 'hour', 'genid', 'rge', 'is_block_power_on_off'))
data = []
# df = pd.DataFrame(columns=col)
# print(df)

path = 'c:\load_xml\ego_st.xml'
xml = objectify.parse(open(path))
root = xml.getroot()
print(root.attrib)
for a in root.getchildren():
    print(a.attrib)
    for b in a.getchildren():
        print(b.attrib)
        data.append(b.attrib)
         # df = df.append(b.attrib)

print(data)
df = pd.DataFrame(data, columns=col)
df.to_excel('xml.xlsx')
print(df)