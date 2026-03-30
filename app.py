import streamlit as st
import pandas as pd

# ======================
# ページ設定
# ======================
st.set_page_config(
    page_title="倫理診断",
    page_icon="🧠",
    layout="wide"
)

# ======================
# CSS（全体デザイン）
# ======================
st.markdown("""
<style>
/* 全体背景 */
.stApp {
    background: linear-gradient(180deg, #fefcf8 0%, #fff8f1 45%, #f8fbff 100%);
}

/* タイトル */
.main-title {
    font-size: 2.4rem;
    font-weight: 800;
    color: #2c3e50;
    margin-bottom: 0.3rem;
}

.sub-title {
    font-size: 1.05rem;
    color: #5f6b7a;
    margin-bottom: 1.2rem;
}

/* 質問カード */
.question-card {
    background: rgba(255,255,255,0.92);
    border: 1px solid #e9eef5;
    border-radius: 20px;
    padding: 20px 22px 14px 22px;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
}

/* 質問番号 */
.q-number {
    font-size: 0.92rem;
    font-weight: 700;
    color: #ff8a65;
    margin-bottom: 8px;
}

/* 質問文 */
.q-text {
    font-size: 1.16rem;
    font-weight: 700;
    color: #273444;
    line-height: 1.7;
    margin-bottom: 12px;
}

/* 補足 */
.q-caption {
    font-size: 0.92rem;
    color: #6b7280;
    margin-bottom: 8px;
}

/* 結果カード */
.result-card {
    background: rgba(255,255,255,0.95);
    border: 1px solid #e9eef5;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.06);
    margin-bottom: 18px;
}

/* タイプ詳細カード */
.type-card {
    background: rgba(255,255,255,0.96);
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 24px;
    line-height: 1.95;
    font-size: 15.5px;
    color: #1f2937;
    box-shadow: 0 8px 24px rgba(0,0,0,0.05);
    margin-top: 10px;
    margin-bottom: 18px;
}

/* セクション見出し */
.section-title {
    font-size: 1.45rem;
    font-weight: 800;
    color: #2c3e50;
    margin-top: 1.2rem;
    margin-bottom: 0.8rem;
}

/* 小見出し */
.mini-title {
    font-size: 1.12rem;
    font-weight: 800;
    color: #374151;
    margin-top: 0.5rem;
    margin-bottom: 0.4rem;
}

/* トップタイプ表示 */
.top-type {
    font-size: 1.5rem;
    font-weight: 800;
    color: #1d4ed8;
    margin-top: 6px;
}

/* キャッチコピー */
.catch-copy {
    font-size: 1.12rem;
    font-weight: 700;
    color: #7c3aed;
    margin-top: 4px;
    margin-bottom: 14px;
}

/* 注目質問カード */
.impact-card {
    background: rgba(255,255,255,0.88);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 20px;
    padding: 18px 20px;
    margin: 14px 0;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
}

.impact-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 12px;
    gap: 12px;
    flex-wrap: wrap;
}

.impact-rank {
    display: inline-block;
    background: linear-gradient(135deg, #ffd166, #ffb703);
    color: #3a2a00;
    font-weight: 800;
    font-size: 0.95rem;
    padding: 6px 12px;
    border-radius: 999px;
}

.impact-qnum {
    display: inline-block;
    background: rgba(255,255,255,0.7);
    color: #333;
    font-weight: 700;
    font-size: 0.92rem;
    padding: 6px 12px;
    border-radius: 999px;
    border: 1px solid rgba(0,0,0,0.06);
}

.impact-question {
    font-size: 1.08rem;
    font-weight: 700;
    line-height: 1.8;
    color: #222;
    margin-bottom: 14px;
}

.impact-meta {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 6px;
}

.impact-badge-plus {
    display: inline-block;
    background: rgba(56, 176, 0, 0.14);
    color: #1f7a1f;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 0.92rem;
    border: 1px solid rgba(56, 176, 0, 0.18);
}

.impact-badge-minus {
    display: inline-block;
    background: rgba(214, 40, 40, 0.12);
    color: #b42318;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 0.92rem;
    border: 1px solid rgba(214, 40, 40, 0.18);
}

.impact-score {
    display: inline-block;
    background: rgba(0,0,0,0.05);
    color: #333;
    font-weight: 700;
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 0.92rem;
}

@media (prefers-color-scheme: dark) {
    .impact-card {
        background: rgba(28, 28, 35, 0.88);
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: 0 8px 24px rgba(0,0,0,0.28);
    }

    .impact-qnum {
        background: rgba(255,255,255,0.06);
        color: #f5f5f5;
        border: 1px solid rgba(255,255,255,0.08);
    }

    .impact-question {
        color: #f7f7f7;
    }

    .impact-score {
        background: rgba(255,255,255,0.08);
        color: #f5f5f5;
    }

    .impact-badge-plus {
        background: rgba(80, 200, 120, 0.14);
        color: #9ef0ae;
        border: 1px solid rgba(80, 200, 120, 0.18);
    }

    .impact-badge-minus {
        background: rgba(255, 90, 90, 0.12);
        color: #ffb3b3;
        border: 1px solid rgba(255, 90, 90, 0.18);
    }
}

/* ダークモード対策 */
@media (prefers-color-scheme: dark) {
    .question-card, .result-card, .type-card, .impact-card {
        background: rgba(30, 41, 59, 0.92) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        color: #f3f4f6 !important;
    }
    .main-title, .section-title, .mini-title, .q-text, .top-type {
        color: #f8fafc !important;
    }
    .sub-title, .q-caption, .q-number, .catch-copy {
        color: #d1d5db !important;
    }
    .type-card b {
        color: #ffffff !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ======================
# タイトル
# ======================
st.markdown('<div class="main-title">🧠 あなたの倫理観診断</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">30問からあなたの価値観を分析します。あまり考え込みすぎず、直感で答えてください。</div>', unsafe_allow_html=True)

st.divider()

# ======================
# CSV読み込み
# ======================
df = pd.read_csv("questions.csv", encoding="utf-8-sig")
questions = df["question"].tolist()

# ======================
# 質問表示
# ======================
st.markdown('<div class="section-title">📋 質問</div>', unsafe_allow_html=True)

answers = []
for i, q in enumerate(questions):
    st.markdown(f"""
    <div class="question-card">
        <div class="q-number">Q{i+1}</div>
        <div class="q-text">{q}</div>
        <div class="q-caption">1 = 全くそう思わない / 5 = とてもそう思う</div>
    </div>
    """, unsafe_allow_html=True)

    ans = st.slider(
        label=f"Q{i+1}",
        min_value=1,
        max_value=5,
        value=3,
        key=f"q_{i}",
        label_visibility="collapsed"
    )
    answers.append(ans)

st.divider()

# ======================
# 重み（完全版）
# ======================
U = [ 2,0,0,-2,0,0,0,1,2,0,0,0,0,0,0,1,2,0,0,0,0,0,0,1,2,0,0,0,0,0]
D = [ 0,2,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,2,0,0,0,0]
V = [ 0,0,2,0,1,0,0,0,0,0,2,0,1,0,0,0,0,0,2,0,1,0,0,0,0,0,2,0,0,0]
R = [-2,0,0,2,0,0,0,0,-1,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,-2,0,0,2,0,0]
C = [ 0,0,1,0,2,0,0,0,0,0,1,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,1,0,2,0]
S = [ 0,1,0,0,0,2,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,2,0,0,0,1,0,0,0,2]
Com=[ 0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0]
E = [ 0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,0,0,0,0,0,0]

types = {
    "功利主義": U,
    "義務論": D,
    "徳倫理": V,
    "権利論": R,
    "ケア倫理": C,
    "契約主義": S,
    "共同体主義": Com,
    "利己主義": E
}

# ======================
# タイプ詳細（descriptions完全廃止）
# ======================
type_details = {
    "功利主義": {
        "catch": "👉「みんなにとって一番いい結果は？」で考える人",
        "text": """
<b>■ 特徴</b><br>
最大多数の幸福を重視し、「結果としてどれだけ多くの人が幸せになるか」で判断する傾向があります。ベンサムやJ.S.ミルに代表される立場です。<br><br>

<b>■ 👍 良い傾向</b><br>
学校やサークル、アルバイト先などで「全体として最も良い選択は何か」を考えやすく、感情論ではなく合理的に物事を整理できます。多数の人が関わる意思決定で強みを発揮します。<br><br>

<b>■ ⚠️ 注意点</b><br>
一方で、「全体の利益」のために少数の不利益を見落としやすい面もあります。たとえば、一人だけが不公平に損をしていても「仕方ない」と処理してしまうことがあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この選択で、最も多くの人が納得・利益・幸福を得るのはどれか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>義務論</b>：結果よりも「ルールそのものの正しさ」を優先するため、衝突しやすいです。
"""
    },

    "義務論": {
        "catch": "👉「それはルールとして正しいか？」で考える人",
        "text": """
<b>■ 特徴</b><br>
結果よりも、「その行為自体が正しいかどうか」を重視する傾向があります。代表的なのはカントです。<br><br>

<b>■ 👍 良い傾向</b><br>
約束、誠実さ、公平なルールを大切にしやすく、周囲から「筋を通す人」と見られやすいです。不正やごまかしを嫌い、信頼を得やすいタイプです。<br><br>

<b>■ ⚠️ 注意点</b><br>
一方で、状況に応じた柔軟さが不足し、「正しいけれど冷たい」判断になることがあります。例外を認めにくく、人間関係がぎくしゃくすることもあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「もし誰もが同じ行動をしたら、それは許されるルールになるか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>功利主義</b>：結果を優先してルールを破る発想に違和感を覚えやすいです。
"""
    },

    "徳倫理": {
        "catch": "👉「自分はどういう人でありたいか」で考える人",
        "text": """
<b>■ 特徴</b><br>
何が正しいかを「行為」だけでなく、「どのような人格・習慣を育てるか」から考える傾向があります。代表的なのはアリストテレスです。<br><br>

<b>■ 👍 良い傾向</b><br>
礼儀、勇気、節度、誠実さなどをバランスよく考えやすく、長い目で見て「信頼される人間であること」を重視します。日常の振る舞いを丁寧に整える力があります。<br><br>

<b>■ ⚠️ 注意点</b><br>
一方で、判断が抽象的になりやすく、「結局どうすべきか」が曖昧になることがあります。具体的なルールや結果の比較が必要な場面では迷いやすいです。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この行動は、自分が目指したい人間像にふさわしいか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>契約主義</b>：形式的なルールや合意より、人としての成熟を重視するためズレが出やすいです。
"""
    },

    "権利論": {
        "catch": "👉「その人の権利は守られているか？」で考える人",
        "text": """
<b>■ 特徴</b><br>
個人の自由、尊厳、権利の保護を重視する傾向があります。ロックなどに代表される発想です。<br><br>

<b>■ 👍 良い傾向</b><br>
「少数派だから」「立場が弱いから」といって不利益を押しつけることに敏感で、人の尊厳を守ろうとします。いじめや不当な扱いに強い違和感を持ちやすいタイプです。<br><br>

<b>■ ⚠️ 注意点</b><br>
ただし、全員の権利を同時に守るのは難しいことも多く、現実の調整が必要な場面で硬直しやすい面があります。「正しいけれど前に進まない」こともあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この判断で、誰かの自由や尊厳が不当に踏みにじられていないか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>功利主義</b>：全体の利益のために個人の権利を後回しにする発想とぶつかりやすいです。
"""
    },

    "ケア倫理": {
        "catch": "👉「その人をちゃんと大切にできているか？」で考える人",
        "text": """
<b>■ 特徴</b><br>
抽象的なルールよりも、関係性・思いやり・具体的な相手への配慮を重視する傾向があります。ギリガンなどに代表される立場です。<br><br>

<b>■ 👍 良い傾向</b><br>
友人、家族、身近な人が本当に困っているときに、形式よりも「今この人に必要なこと」を考えやすいです。対人場面での温かさと気配りが大きな強みです。<br><br>

<b>■ ⚠️ 注意点</b><br>
一方で、近しい人に肩入れしすぎて、公平さを欠くことがあります。関係性を重視するあまり、線引きが難しくなることもあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この選択で、目の前の人は本当に大切に扱われているか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>契約主義</b>：感情や関係性より、形式的な公平性を重視する発想とズレやすいです。
"""
    },

    "契約主義": {
        "catch": "👉「みんなが納得できるルールか？」で考える人",
        "text": """
<b>■ 特徴</b><br>
公平な合意、ルール、制度の正当性を重視する傾向があります。ロールズ的な発想に近いです。<br><br>

<b>■ 👍 良い傾向</b><br>
「特定の人だけが得をしないか」「誰にとってもフェアか」を考えやすく、集団のルール作りや調整に向いています。冷静で社会的な視点を持ちやすいです。<br><br>

<b>■ ⚠️ 注意点</b><br>
ただし、現実の人間関係や感情の複雑さをやや切り捨ててしまうことがあります。「公平ではあるが冷たい」と見られることもあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「立場が入れ替わっても、自分はこのルールに納得できるか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>ケア倫理</b>：個別の事情や関係性を優先する発想と衝突しやすいです。
"""
    },

    "共同体主義": {
        "catch": "👉「社会や文化にとって良いか？」で考える人",
        "text": """
<b>■ 特徴</b><br>
個人だけでなく、共同体・文化・伝統・社会のつながりを重視する傾向があります。サンデルなどの議論に近い発想です。<br><br>

<b>■ 👍 良い傾向</b><br>
「自分だけが良ければいい」ではなく、所属する集団や社会全体の秩序・継続性を考えられるのが強みです。責任感や公共心につながりやすいです。<br><br>

<b>■ ⚠️ 注意点</b><br>
その反面、同調圧力や慣習を正当化しやすく、個人の自由を抑えてしまう危険もあります。「昔からこうだから」で止まりやすい面もあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この選択は、私たちの社会や関係をより良いものにするか？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>利己主義</b>：自分の利益を最優先する発想と真っ向からぶつかりやすいです。
"""
    },

    "利己主義": {
        "catch": "👉「自分にとって得か？」で考える人",
        "text": """
<b>■ 特徴</b><br>
自分の利益、損得、自己保存を重視する傾向があります。日常ではかなり自然な発想でもあります。<br><br>

<b>■ 👍 良い傾向</b><br>
自分の限界やリソースを把握しやすく、「無理して他人に合わせすぎない」現実感があります。自己防衛や合理性という点では強みになります。<br><br>

<b>■ ⚠️ 注意点</b><br>
ただし、短期的な得を優先しすぎると信頼関係を壊しやすく、長期的には不利益になることもあります。協力や配慮が不足すると孤立につながることもあります。<br><br>

<b>■ 💡 あなたに向いている問い方</b><br>
「この選択は、短期だけでなく長期的に見ても自分にとって本当に得か？」<br><br>

<b>■ ⚔️ あなたが対立しやすいタイプ</b><br>
<b>共同体主義</b>：個人より共同体を優先する発想とぶつかりやすいです。
"""
    }
}

# ======================
# スコア計算
# ======================
def calc_score(answers, weights):
    score = 0
    contribs = []
    for a, w in zip(answers, weights):
        centered = a - 3
        c = centered * w
        score += c
        contribs.append(c)
    return score, contribs

def normalize(score, weights):
    max_score = sum(2 * abs(w) for w in weights)
    min_score = sum(-2 * abs(w) for w in weights)

    if max_score == min_score:
        return 0.5

    return (score - min_score) / (max_score - min_score)

# ======================
# 実行
# ======================
if st.button("🔍 診断結果を見る", use_container_width=True):

    scores = {}
    all_contribs = {}

    for name, weights in types.items():
        raw, contribs = calc_score(answers, weights)
        norm = normalize(raw, weights)

        scores[name] = norm
        all_contribs[name] = contribs

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    top1 = sorted_scores[0]
    top2 = sorted_scores[1]
    top3 = sorted_scores[2]

    result = top1[0]
    detail = type_details[result]

    # ======================
    # 結果表示
    # ======================
    st.markdown('<div class="section-title">📊 診断結果</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-card">
        <div class="mini-title">あなたのタイプ</div>
        <div class="top-type">🧠 {top1[0]}</div>
        <div class="catch-copy">{detail['catch']}</div>
        <div style="font-size:1rem; color:#6b7280;">
            🥈 2番目に近いタイプ：<b>{top2[0]}</b><br>
            🥉 3番目に近いタイプ：<b>{top3[0]}</b>
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ======================
    # 詳細解説
    # ======================
    st.markdown('<div class="section-title">📝 詳細解説</div>', unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="type-card">
            {detail['text']}
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # グラフ
    st.markdown('<div class="section-title">📈 タイプ別スコア</div>', unsafe_allow_html=True)

    chart_data = pd.DataFrame({
        "倫理タイプ": list(scores.keys()),
        "スコア": list(scores.values())
    })
    st.bar_chart(chart_data.set_index("倫理タイプ"))

    st.divider()

    # ======================
    # 影響の大きい質問
    # ======================
    st.markdown('<div class="section-title">🔍 あなたの結果に特に影響した質問 TOP5</div>', unsafe_allow_html=True)

    contribs = all_contribs[result]

    impact_df = pd.DataFrame({
        "質問": questions,
        "影響": contribs
    })

    impact_df["絶対値"] = impact_df["影響"].abs()
    impact_df = impact_df.sort_values(by="絶対値", ascending=False).head(5).reset_index(drop=True)

    for rank, row in impact_df.iterrows():
        q_num = questions.index(row["質問"]) + 1
        impact_value = round(row["影響"], 2)

        if row["影響"] > 0:
            direction_badge = f'<span class="impact-badge-plus">このタイプを強めた</span>'
        elif row["影響"] < 0:
            direction_badge = f'<span class="impact-badge-minus">このタイプを弱めた</span>'
        else:
            direction_badge = f'<span class="impact-score">影響は中立</span>'

        st.html(f"""
        <div class="impact-card">
            <div class="impact-top">
                <span class="impact-rank">#{rank + 1}</span>
                <span class="impact-qnum">Q{q_num}</span>
            </div>

            <div class="impact-question">
                {row["質問"]}
            </div>

            <div class="impact-meta">
                {direction_badge}
                <span class="impact-score">影響スコア：{impact_value}</span>
            </div>
        </div>
        """)

