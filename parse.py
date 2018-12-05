from lxml import objectify
import pandas as pd

col = ('targetdate', 'hour', 'genid', 'rge', 'is_block_power_on_off')
data = []

path = 'c:\load_xml\ego_st.xml'
xml = objectify.parse(open(path))
root = xml.getroot()
for a in root.getchildren():
    for b in a.getchildren():
        q = {**a.attrib, **b.attrib}
        data.append(q)

df = pd.DataFrame(data, columns=col)
df.to_excel('c:\load_xml\pxml.xlsx', index=False)
print(df)

