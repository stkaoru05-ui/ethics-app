import streamlit as st
import pandas as pd

# CSV読み込み
df = pd.read_csv("questions.csv")

# リストに変換
questions = df["question"].tolist()

st.title("倫理質問テスト")

# 表示
for i, q in enumerate(questions):
    st.write(f"Q{i+1}. {q}")

answers = []

for i, q in enumerate(questions):
    ans = st.slider(f"Q{i+1}. {q}", 1, 5, 3)
    answers.append(ans)

st.write("回答:", answers)

U = [1,1,1]   # 今は質問3つなので3つだけ
D = [-1,1,0]
V = [0,0,1]

def calc_score(answers, weights):
    return sum(a * w for a, w in zip(answers, weights))

def normalize(score, weights):#正規化の関数
    max_score = sum(5 * abs(w) for w in weights)
    min_score = sum(1 * -abs(w) for w in weights)
    
    if max_score == min_score:
        return 0.5
    
    return (score - min_score) / (max_score - min_score)

if st.button("結果を見る"):

    u = calc_score(answers, U)
    d = calc_score(answers, D)
    v = calc_score(answers, V)

    u_n = normalize(u, U)
    d_n = normalize(d, D)
    v_n = normalize(v, V)

    

    st.write("### 結果")
    st.write(f"功利主義: {u_n:.2f}")
    st.write(f"義務論: {d_n:.2f}")
    st.write(f"徳倫理: {v_n:.2f}")

    scores = {
    "功利主義": u_n,
    "義務論": d_n,
    "徳倫理": v_n
}

    result = max(scores, key=scores.get)
    st.write("### あなたの倫理タイプ")
    st.write(f"👉 {result}")
    
    # ======================
    # 棒グラフ
    # ======================
    chart_data = pd.DataFrame({
        "倫理タイプ": ["功利主義", "義務論", "徳倫理"],
        "スコア": [u_n, d_n, v_n]
    })

    st.bar_chart(chart_data.set_index("倫理タイプ"))



#venv\Scripts\activate streamlit run app.py