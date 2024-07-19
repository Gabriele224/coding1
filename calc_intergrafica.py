import os
import math
import  streamlit as st

st.title("Calcolatrice")
num1= st.number_input("Numero:\n",key="first")
num2=st.number_input("Numero:\n",key="second")

operbox1=['+','-','x','/','sqrt']
ope=st.selectbox("Calc:",operbox1)
if ope=='+':
    result=num1+num2
    st.write(result)
elif ope=='-':
    result=num1-num2
    st.write(result)
elif ope=='x':
    result=num1*num2
    st.write(result)
elif ope=='/':
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

st.title("Radicali algebrici")
radice=st.number_input("radice\n")
radice_box=['2radice','3radice','4radice','5radice','6radice','7radice','8radice','9radice','10radice']
eseradice=st.selectbox("Radice\n",radice_box)
if st.button("Radice"):
    if eseradice =='2radice':
        calc=math.sqrt(radice)
        st.write(calc)
    elif eseradice=='3radice':
        calc=radice**(1/3)
        st.write(calc)
    elif eseradice=='4radice':
        calc=radice**(1/4)
        st.write(calc)
    elif eseradice=='5radice':
        calc=radice**(1/5)
        st.write(calc)
    elif eseradice=='6radice':
        calc=radice**(1/6)
        st.write(calc)
    elif eseradice=='7radice':
        calc=radice**(1/7)
        st.write(calc)
    elif eseradice=='8radice':
        calc=radice**(1/8)
        st.write(calc)
    elif eseradice=='9radice':
        calc=radice**(1/9)
        st.write(calc)
    elif eseradice=='10radice':
        calc=radice**(1/10)
        st.write(calc)
    else:
        st.write("inserisci il numero valido")

st.title("Equazioni di primo grado1")
num_eq=st.number_input("numero con la x\n")
num_eq1=st.number_input("numero intero\n")
st.write(f"{num_eq}x + {num_eq1} =0")
num_eq1=-(num_eq1)
st.write(f"{num_eq}x = {num_eq1}")
st.write(f"x = {num_eq} / {num_eq1}")

st.title("Equazioni di primo grado")
st.write("primo membro")
num_eq=st.number_input("numero con la x\n",key="second_numbe")
num_eq1=st.number_input("numero intero\n",key="second_n")
st.write("secondo membro")
num_eq2=st.number_input("numero con la x\n",key="second_title")
num_eq3=st.number_input("numero intero")

st.write(f"{num_eq}x + {num_eq1} = {num_eq2}x - {num_eq3}")
calc_num_eq= num_eq - num_eq2
calc_num_eq=-(calc_num_eq)
calc_num_eq_intero=-(num_eq1)-(num_eq3)
calc_num_eq_intero=-(calc_num_eq_intero)

st.write(f"{calc_num_eq}x = {calc_num_eq_intero}")
    
