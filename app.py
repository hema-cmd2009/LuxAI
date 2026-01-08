import streamlit as st
import random

# إعدادات الهوية - our goal study
st.set_page_config(page_title="our goal study", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000; color: #ffffff !important; font-family: 'Cairo', sans-serif; }
    .logo-text { font-size: 3.5rem; color: #D4AF37; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state: st.session_state.page = "login"

# --- واجهة الدخول بالتليجرام ---
if st.session_state.page == "login":
    st.markdown("<p class='logo-text'>our goal study</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;'>سجل دخولك عبر التليجرام لتبدأ رحلة النجاح 🚀</p>", unsafe_allow_html=True)
    
    # استبدل YOUR_BOT_USERNAME باسم بوتك اللي عملته في BotFather
    telegram_widget = """
    <div style="text-align: center;">
        <script async src="https://telegram.org/js/telegram-widget.js?22" 
                data-telegram-login="YOUR_BOT_USERNAME" 
                data-size="large" data-userpic="true" data-request-access="write"></script>
    </div>
    """
    st.components.v1.html(telegram_widget, height=100)
    
    # زر مؤقت للدخول لو لسه معملتش البوت
    if st.button("🚀 دخول كضيف (مؤقت)"):
        st.session_state.user_name = "بطل_مكافح"
        st.session_state.page = "waiting"; st.rerun()

# --- باقي التطبيق (الروم والجدول) ---
elif st.session_state.page == "waiting":
    st.markdown("## نورت يا وحش! جاهز توصل لهدفك؟")
    st.write("هنا هنعرض جدول المذاكرة والتحكم في الروم.")
