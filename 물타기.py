import streamlit as st
c1,c2 = st.columns([.6,1])
with c1 :
    with st.expander('🎈'):
        try:
            평단 = st.number_input('매입금액',step=50)
            수량 = st.number_input('보유수량',step=10)
            현재 = st.number_input('추매금액',step=50,value=평단)
            매수금액 = 평단 * 수량

            추매수량 = st.number_input("추매수량", step=10)
            추매 = 현재 * 추매수량
            물타기 = (매수금액 + 추매) / (수량 + 추매수량)
            추매수익률 = (현재 - 물타기) / 물타기 * 100

            st.write('####', int(물타기))
            st.write('####', round(추매수익률,2))

        except ZeroDivisionError:
            st.warning('🎈 조건입력')
