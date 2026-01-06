import streamlit as st
import time

# 1. إعدادات الصفحة والديزاين (الألوان الفاتحة)
st.set_page_config(page_title="LuxAI Stylist", page_icon="👔", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    .stApp { background-color: #0b120a; color: #f5f5dc; font-family: 'Cairo', sans-serif; }
    
    .lux-header { color: #d4a373; font-size: 4rem; text-align: center; font-weight: bold; margin-bottom: 0; }
    .welcome-text { color: #f5f5dc; text-align: center; font-size: 1.2rem; margin-bottom: 40px; }
    
    /* جعل الخطوط في صندوق الرد فاتحة وواضحة */
    .ai-reply-box {
        background: #1a2619; 
        border: 1px solid #d4a373; 
        border-radius: 25px; 
        padding: 25px; 
        color: #f5f5dc; /* خط فاتح */
        line-height: 1.8;
    }
    .highlight-gold { color: #d4a373; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# ----------------- 2. الواجهة -----------------

st.markdown('<div class="lux-header">LuxAI</div>', unsafe_allow_html=True)
st.markdown('<div class="welcome-text">أهلاً بيك يا فنان في عالم الأناقة.. قولي إيه اللي محيرك؟</div>', unsafe_allow_html=True)

# منطقة السؤال
user_q = st.text_input("إيه اللي محيرك في لبسك؟", placeholder="مثلاً: هودي لونه إيه يمشى مع جينز أزرق؟")

if st.button("نسق لي الطقم 🪄"):
    if user_q:
        with st.spinner('بحلل سؤالك وبراجع داتا الألوان...'):
            time.sleep(1)
            
            # محرك ردود ذكي (صاحبك بجد)
            reply = ""
            q = user_q.lower()
            
            if "جينز ازرق" in q or "بنتلون جينز" in q:
                reply = "بص يا صاحبي، الجينز الأزرق ملك الكاجوال. لو رايح كافيه، الهودي <span class='highlight-gold'>الرمادي الفاتح (Grey)</span> أو <span class='highlight-gold'>الأبيض</span> هيديك لوك نظيف جداً. ولو عايز تبان مميز، جرب هودي <span class='highlight-gold'>هافان أو بيج</span> مع كوتشي أبيض، هتطلع شيك أوي!"
            elif "زيتي" in q:
                reply = "بما إنك سألت عن الزيتي، فالداتا بتقول إن <span class='highlight-gold'>البيج أو الأسود</span> هما اللي بيبرزوا فخامته. جرب تلبس قميص بيج تحت جاكيت زيتي."
            else:
                reply = "سؤالك ذكي! بص يا صاحبي، القاعدة في الموضة هي 'التناسق'. جرب دايماً توازن بين الألوان الغامقة والفاتحة، ولو محتار، <span class='highlight-gold'>الأبيض والرمادي</span> هما الجوكر في أي طقم."

            st.markdown(f"""
                <div class="ai-reply-box">
                    <span style="font-size: 1.3rem;"><b>رد LuxAI:</b></span><br>
                    {reply}
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("يا بطل، قولي محتار في إيه عشان أقدر أساعدك!")

st.write("---")
st.markdown("<p style='text-align:center; opacity:0.5;'>LuxAI - 2026</p>", unsafe_allow_html=True)
