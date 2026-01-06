import streamlit as st
import time
import random

# 1. إعدادات الهوية البصرية (LuxAI - Olive & Beige)
st.set_page_config(page_title="LuxAI | لكس أي", page_icon="👔", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* الخلفية والخطوط */
    .stApp {
        background-color: #0b120a;
        color: #f5f5dc;
        font-family: 'Cairo', sans-serif;
    }

    /* الهيدر الحديث (كلام صحاب) */
    .hero-section {
        background: linear-gradient(135deg, rgba(212, 163, 115, 0.1) 0%, rgba(11, 18, 10, 1) 100%);
        border: 1px solid #d4a373;
        border-radius: 50px;
        padding: 40px;
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 1.5s ease;
    }

    @keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }

    /* فقاعة الرد (صاحبك الستايليست) */
    .chat-bubble {
        background: #1a2619;
        border-right: 6px solid #d4a373;
        border-radius: 25px;
        padding: 25px;
        margin-top: 20px;
        font-size: 1.1rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    /* التصميم البيضاوي للحقول والأزرار */
    .stTextInput>div>div>input {
        border-radius: 50px !important;
        border: 2px solid #d4a373 !important;
        background: #1a2619 !important;
        color: #f5f5dc !important;
        padding: 12px 25px !important;
    }

    .stButton>button {
        background: linear-gradient(90deg, #d4a373, #a98467) !important;
        color: #0b120a !important;
        font-weight: bold !important;
        border-radius: 50px !important;
        height: 55px !important;
        width: 100% !important;
        border: none !important;
        transition: 0.3s ease;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 0 20px rgba(212, 163, 115, 0.4); }

    /* كروت المعرض */
    .gallery-card {
        background: #1a2619;
        border-radius: 30px;
        padding: 15px;
        border: 1px solid #d4a373;
        text-align: center;
        transition: 0.4s;
    }
    .gallery-card:hover { transform: translateY(-10px); }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 2. المحتوى الرئيسي -----------------

# رسالة الترحيب
st.markdown("""
    <div class="hero-section">
        <h1 style='color:#d4a373; font-size: 3.5rem;'>LuxAI</h1>
        <p style='font-size:1.3rem;'>أهلاً بيك في <b>لكس أي</b>.. ستايليست شخصي وصاحبك الجدع اللي بيفهم في الأصول.</p>
        <p style='opacity:0.8;'>عندنا داتا ضخمة عشان نخليك دايماً شيك بالزيتي والبيج وكل الألوان اللي تحبها.</p>
    </div>
    """, unsafe_allow_html=True)

# المنسق الذكي (المركز الأول)
st.markdown("### 🪄 المنسق الذكي (اسأل LuxAI)")
col_in, col_analyze = st.columns([3, 1])

with col_in:
    user_q = st.text_input("إيه اللي محيرك في لبسك؟", placeholder="مثلاً: ألبس إيه طرحة على دريس زيتي؟ / إيه أحسن جزمة للبيج؟")

with col_analyze:
    st.write("##") # موازنة المسافة
    btn = st.button("نسق لي الطقم")

if btn:
    if user_query := user_q:
        with st.spinner('براجع داتا الموضة عشانك...'):
            time.sleep(1.5)
            st.markdown(f"""
                <div class="chat-bubble">
                    <b>بص يا صاحبي بخصوص "{user_query}":</b><br>
                    بناءً على الداتا اللي عندي، التنسيق ده محتاج لمسة "هدوء". 
                    لو اللبس زيتي، خليك في البيج الكريمي أو "الأوف وايت" عشان الوش ينور. 
                    ولو بتدور على شياكة زايدة، ساعة بجلد بني هي اللي هتكمل اللوحة.
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
    else:
        st.warning("يا بطل، قولي محتار في إيه عشان أقدر أساعدك!")

st.write("---")

# معرض المجتمع (المركز الثاني)
st.markdown("### 👥 ملهمين من مجتمع LuxAI")
c1, c2, c3, c4 = st.columns(4)

# داتا تجريبية للمعرض
gallery_items = [
    {"img": "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?q=80&w=400", "t": "كاجوال رائق"},
    {"img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?q=80&w=400", "t": "أناقة الحجاب"},
    {"img": "https://images.unsplash.com/photo-1516762689617-e1cffcef479d?q=80&w=400", "t": "فورمال فخم"},
    {"img": "https://images.unsplash.com/photo-1520975954732-35dd2229969e?q=80&w=400", "t": "ستايل شتوي"}
]

for i, col in enumerate([c1, c2, c3, c4]):
    with col:
        st.markdown(f"""
            <div class="gallery-card">
                <img src="{gallery_items[i]['img']}" style="width:100%; border-radius:20px; margin-bottom:10px;">
                <p style="color:#d4a373; font-weight:bold;">{gallery_items[i]['t']}</p>
            </div>
        """, unsafe_allow_html=True)

st.write("##")
st.markdown("<p style='text-align:center; opacity:0.5;'>LuxAI - 2026 | All Rights Reserved</p>", unsafe_allow_html=True)
