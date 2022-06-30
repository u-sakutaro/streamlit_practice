import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('streamlit入門')

st.write('dataflame')

df = pd.DataFrame({
    '1列目':[1, 2, 3, 4],
    '2列目':[10, 20, 30, 40],
})

st.dataframe(df.style.highlight_max(axis=0), width=300, height=200)


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
シングルクォーテーションではなくバッククォーテーション

"""


df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

#折れ線グラフ
st.line_chart(df)

#折線の中身を塗ったグラフ
st.area_chart(df)

#新宿付近のマッピング
df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

# 画像を表示する
if st.checkbox('Show Image'):
    img = Image.open('kyne.jpeg')
    st.image(img, caption='Kyne', use_column_width=True)

#セレクトボックス
option = st.selectbox(
    'あなたの好きな数字を選んでください',
    list(range(1, 11))
)
'your favorite number is', option, '.'

# テキストボックス
st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えてください')
'your hobby is', text, '.'

#スライダー
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'調子は', condition


# サイドバーに表示する。
st.write('Interactive Widgets')
text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

'your hobby is', text, '.'
'調子は', condition


# ツーカラムレイアウト
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむ')

#エキスパンダー
expander = st.expander('お問合せ')
expander.write('お問合せ回答を書く')

st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えてください')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)

'your hobby is', text, '.'
'調子は', condition


# プログレスバーの表示
'Start'
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
'Done!!!'
