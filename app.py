import streamlit as st

st.title(":red[Streamlit] Data app :sunglasses:" )
st.snow()

st.header("Data science intern")

st.subheader("feb 2023")

CODE = ''' print("Hello world")'''

st.code(CODE, language="python")


btn_click = st.button("click me")

if btn_click == True:
    st.subheader("you click me :cry:")
