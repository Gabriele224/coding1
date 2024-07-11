import os
import math
import  streamlit as st

st.title("Calcolatrice")
num1= st.number_input("Numero:\n",key="first")
num2=st.number_input("Numero:\n",key="second")

operbox1=['Add','Sott','Molti','Divi','sqrt']
ope=st.selectbox("Calc:",operbox1)
if ope=='Add':
    result=num1+num2
    st.write(result)
elif ope=='Sott':
    result=num1-num2
    st.write(result)
elif ope=='Molti':
    result=num1*num2
    st.write(result)
elif ope=='Divi':
    if num2 !=0:
        result=(num1/num2)
        st.write(result)
    else:
        st.error("divisione non consentita")
elif ope=='sqrt':
    result =math.sqrt(num2)
    st.write(result)
else:
    st.write("Inserisci numeri validi")