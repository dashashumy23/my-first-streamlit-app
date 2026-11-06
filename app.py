import streamlit as st

st.set_page_config(page_title="Мій Супер-Додаток", layout="wide")
st.title("Ласкаво просимо до мого додатку! 🚀")

tab1, tab2, tab3 = st.tabs(["👤 Про мене", 
                            "🧮 Калькулятор градусів",
                            "Калькілятор ваги"])

with tab1:
    st.header("Знаймство з автором")

    col1, col2 = st.columns([1,2])

    with col1:
        st.image("https://images.unsplash.com/photo-1535713875002-d1d0cf377fde?auto=format&fit=crop&w=300&q=80", width=200)
    
    with col2:
        st.subheader("Привіт, я майбутній Python Developer!")
        st.write("Я навчаюся в Малій Комп'ютерній Академії IT STEP. Створюю круті веб-додатки та вивчаю штучний інтелект.")

        st.markdown("### Мої інтереси:")
        st.write("🎮 Розробка ігор | 🤖 Штучний інтелект | 🌐 Веб-дизайн")
        

        with  st.container():
            st.write('---')
            st.info("Контакти для зв'язку:")
            st.markdown("- 🐙 GitHub: [Мій Профіль](https://github.com/dashashumy23)")
            st.markdown("- [📧 Надіслати Email](mailto:dasha.shumy.23.09@gmail.com)")
       
        with st.container():
            my_app_url = "https://my-first-app-app-esgdg4vnfsmenqgshw4nxx.streamlit.app/p"
            qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={my_app_url}"
            
            with col1:
                st.write("Скануй мене:")
                st.image(qr_api_url, caption="QR-код мого додатка")

with tab2:
    st.header("Корисний інструмент: Конвертер температури")
    st.info("Цей інструмент допоможе швидко перевести градуси Цельсія у Фаренгейти.")
    c1,c2 = st.columns(2)

    with c1:
        celsius = st.number_input("Введіть температуру в °C:", value=20.0)
    with c2:
        fahrenheit = (celsius*9/5)+32
        st.metric(label="Температура у Фаренгейтах (°F)", value=f'{fahrenheit:.1f}°F')

with tab3:
    st.header("Калькулятор Індексу Маси Тіла (ІМТ)")
    st.write("Дізнайтеся, чи в нормі ваша вага за допомогою швидкого підрахунку!")
    
    col_inputs, col_results = st.columns(2)

    with col_inputs:
        weight = st.number_input("Введіть вашу вагу (в кг):", min_value=10.0, max_value=200.0, value=50.0, step=0.5)
        height_cm = st.number_input("Введіть ваш зріст (в см):", min_value=50.0, max_value=250.0, value=150.0, step=1.0)
    with col_results:
        height_m = height_cm/100
        bmi=weight/(height_m**2)
        st.subheader("Ваш результат:")
        st.metric(label="Індекс маси тіла (ІМТ)", value=f"{bmi:.1f}")
        
        if bmi<18.5:
            st.warning("Категорія: Недостатня вага 🥦")
        elif 18.5 <= bmi < 25.0:
            st.success("Категорія: Нормальна вага 👍")
        else:
            st.error("Категорія: Надмірна вага 🏃‍♂️")

    
