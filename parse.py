from lxml import objectify
import pandas as pd
import sqlalchemy as sa
import config as cfg
# Подключение к БД
ora = sa.create_engine('oracle://'+cfg.user_db+':'+cfg.pass_db+'@'+cfg.db)
conn = ora.connect()
col = ('targetdate', 'hour', 'genid', 'rge', 'is_block_power_on_off')
data = []

path = 'c:\load_xml\ego_st.xml'
xml = objectify.parse(open(path))
root = xml.getroot()
for a in root.getchildren():
    for b in a.getchildren():
        q = {**root.attrib, **a.attrib, **b.attrib}
        data.append(q)

df = pd.DataFrame(data, columns=col)

# df['targetdate'] = pd.to_datetime(df['targetdate'])
df.to_excel('c:\load_xml\pxml.xlsx', index=False)
print(df)
print(df.dtypes)
df.to_sql('ego', conn, if_exists='replace', index=False)
