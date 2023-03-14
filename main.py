import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit for Very Beginer")

st.write("Dataframe")
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
df2 = pd.DataFrame(
    np.random.rand(100,2)/[30,30] + [35.69,139.70],
    columns=["lat","lon"]
)

st.write(df)
st.bar_chart(df)

st.map(df2)

st.write("Display_image")
img = Image.open("sample.jpg")
st.image(img,caption = "carcass", use_column_width=True)

"""
# 章
## 節
### 項
$exp(-x^2)$
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""