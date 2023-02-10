
import pandas as pd
import streamlit as st

     
 # https://discuss.streamlit.io/t/change-font-size-and-font-color/12377/2
new_title = '<p style="font-family:calibre; color:Green; font-size: 32px;">Curcumin Chalcone Derivatives Database (CCDD)</p>'
st.markdown(new_title, unsafe_allow_html=True)


# https://discuss.streamlit.io/t/loading-our-own-datasets/7118/2


df = pd.read_csv("ChaCur_NCdb.csv")
st.title("Dataframe with Descriptors      📚       ")  ##st.w#

#st.write(df)

#filter-rows-pandas
st.sidebar.header('Select _Filters')
MW = st.sidebar.slider(
    label="Molecular Weight:",
    min_value=00.0,
    max_value=900.0,
    value=0.0,
   step=10.0,
)
LogP= st.sidebar.slider(
    label="LogP:",
    min_value=0.0,
    max_value=12.0,
    value=0.0,
   step=1.0,
)

NumHDonors= st.sidebar.slider(
    label="HBD:",
    min_value=0,
    max_value=9,
    value=0,
    step=1,
)

NumHAcceptors= st.sidebar.slider(
    label="HBA:",
    min_value=0,
    max_value=17,
    value=0,
   step=1,
)
#result = df[(df['MW'] > MW) & (df['LogP'] > LogP) & (df['NumHDonors'] > NumHDonors)& (df['NumHAcceptors'] > NumHAcceptors)]
result = df[(df['MW'] >= MW) & (df['LogP'] >=LogP) & (df['NumHDonors'] >=NumHDonors)& (df['NumHAcceptors'] >= NumHAcceptors)]
st.write(result)



# https://docs.streamlit.io/knowledge-base/using-streamlit/how-download-pandas-dataframe-csv
@st.cache
def convert_df(result):
   return result.to_csv().encode('utf-8')


csv = convert_df(result)

st.download_button(
   "   📥   Get Compounds ",
   csv,
   "selected.csv",
  
   key='download-csv'
)
 #Vizualization of S
st.title(' Visualisation of Structures 🔍           ')


#2D

import streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw




compound_smiles=st.text_input('SMILES please','C1=CC=C(C=C1)O')
#compound_smiles = 'c1cc(C(=O)O)c(OC(=O)C)cc1'
m = Chem.MolFromSmiles(compound_smiles)
im=Draw.MolToImage(m)

#st.image(im)


new_title = '<p style="font-family:sans-serif; color:Green; font-size: 25px;">2D structure</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.image(im, channels="BGR")


st.title(' 🔦   Sorting by Rows      ')
a= dict([(key, value) for (key, value) in df.groupby("smiles")])
#st.write(a)
smiles = st.text_input (" Kindly Enter Valid Smiles",  "CO" )
if smiles in a.keys():
        st.write(a[smiles])
else :
        st.write("Sorry!! No smiles found")
        

st.header('For Questions :')
st.write("Please contact: shailima.rampogu@gmail.com, dhanaj8@gmail.com, joonhwa@gnu.ac.kr ")


