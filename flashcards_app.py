import streamlit as st

# Tạo danh sách từ vựng
vocab_list = [
    ("音読", "おんどく"), ("放送", "ほうそう"), ("詩人", "しじん"), ("左右", "さゆう"),
    ("遠方", "えんぽう"), ("消息", "しょうそく"), ("解決", "かいけつ"), ("破竹", "はちく"),
    ("時局", "じきょく"), ("関係", "かんけい"), ("電池", "でんち"), ("銀行", "ぎんこう"),
    ("登録", "とうろく"), ("丸薬", "がんやく"), ("首席", "しゅせき"), ("慣習", "かんしゅう"),
    ("終止", "しゅうし"), ("遺族", "いぞく"), ("返答", "へんとう"), ("秋祭り", "あきまつり"),
    ("細分", "さいぶん"), ("急速", "きゅうそく"), ("和紙", "わし"), ("内申", "ないしん"),
    ("友好", "ゆうこう"), ("幸福", "こうふく"), ("星雲", "せいうん"), ("羽毛", "うもう"),
    ("待機", "たいき"), ("険悪", "けんあく"), ("整理", "せいり"), ("順番", "じゅんばん"),
    ("君子", "くんし"), ("冬季", "とうき")
]

st.title("📚 Japanese Flashcards")

# Tùy chọn ẩn/hiện Kanji hoặc Hiragana
show_kanji = st.checkbox("Hiện Kanji", value=True)
show_hiragana = st.checkbox("Hiện Hiragana", value=False)

# Flashcard từng dòng
for i, (kanji, hiragana) in enumerate(vocab_list):
    with st.expander(f"Từ {i + 1}"):
        if show_kanji:
            st.markdown(f"**Kanji**: {kanji}")
        if show_hiragana:
            st.markdown(f"**Hiragana**: {hiragana}")
