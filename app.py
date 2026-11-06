import streamlit as st

st.set_page_config(page_title="Мій Супер-Додаток", layout="wide")
st.title("Ласкаво просимо до мого додатку! 🚀")

tab1, tab2 = st.tabs(["👤 Про мене", "🧮 Мій Інструмент"])

with tab1:
    st.header("Знаймство з автором")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=300&q=80", width=200)
    
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюся в Малій Комп'ютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю штучний інтелект.")

        with  st.container():
            st.info("Контакти для зв'язку:")
            st.markdown("- 🐙 GitHub: [Мій Профіль](https://github.com)")
            st.markdown("- 📧 Email: student@itstep.org")

with tab2:
    st.header("Корисний інструмент: Конвертер температури")
    st.info("Цей інструмент допоможе швидко перевести градуси Цельсія у Фаренгейти.")
    c1,c2 = st.columns(2)

    with c1:
        celsius = st.number_input("Введіть температуру в °C:", value=20.0)
    with c2:
        fahrenheit = (celsius*9/5)+32
        st.metric(label="Температура у Фаренгейтах (°F)", value=f'{fahrenheit:.1f}°F')