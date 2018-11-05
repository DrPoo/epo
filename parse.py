import xml.etree.ElementTree as ET 
import os, csv, base64
import pandas as pd

xmldir = r'C:\xml'
abdir = r'C:\abstracts'
aidir = r'C:\Users\rhynes\Google Drive\UCD\3 - Research\EPO Project'

data = {}

for file in os.listdir(xmldir):
	#print(file)
	tree = ET.parse(xmldir+'\\'+file)
	root = tree.getroot()
	docid = root.attrib.get('id')
	abelement = root.find('abstract')
	if abelement:
		abstract = "".join(abelement.itertext())
		#print(abstract.tostring)
		data[docid]=abstract
	else:
		print('no abstract')

non_ai_df = pd.DataFrame.from_dict(data, orient='index')

# NOTE: Assuming that all these are non-responsive. Probably a bad assumption.
non_ai_df['ai']=0
#s = pd.Series(data)
#print(non_ai_df)

ai_df = pd.read_excel(aidir+'\\ABSTRACT.xlsx', index_col=0, usecols=[0,1])

ai_df['ai']=1

df = non_ai_df.append(ai_df)
df = df.drop(0, axis=1)
#print(df)
df.to_pickle(aidir+'\\abstracts.pkl')
