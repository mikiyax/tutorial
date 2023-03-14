import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlit for Very Beginer")
st.write("プログレスバー")

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(10):
    latest_iteration.text(f"iteration{i+1}")
    bar.progress((i+1)**2)
    time.sleep(0.1)
"Completed"

# left_column,right_column = st.columns(2)
# boton = left_column.button("右に文字を表示")
# if boton:
#     right_column.write("ここは右からむ")
# expander = st.expander("問い合わせ")
# expander.write("お問い合わせ内容1")
# expander.write("お問い合わせ内容2")
# c = st.checkbox("HideImage")
# option = st.selectbox(
#     "好きな数字を選択",
#     list(range(1,11))
# )
# age = st.slider("How old are you",0,100,10)
# option2 = st.text_input("趣味")

# st.write("趣味:",option2)
# "年齢:",age
# "あなたの好きな数字は",option,"です"
# if c == False:
#     img = Image.open("sample.jpg")
#     st.image(img,caption = "carcass", use_column_width=True)
