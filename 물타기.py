import streamlit as st
c1,c2 = st.columns([.6,1])
with c1 :
    with st.expander('🎈'):
        try:
            평단 = st.number_input('평균금액',min_value=0,step=50)
            수량 = st.number_input('보유수량',min_value=0,step=10)
            현재 = st.number_input('현재금액',min_value=0,step=50,value=50)
            매수금액 = 평단 * 수량

            추매수량 = st.number_input("추매수량",min_value=0, step=10)
            추매 = 현재 * 추매수량
            물타기 = (매수금액 + 추매) / (수량 + 추매수량)
            수익률 = (현재 - 평단) / 평단 * 100
            추매수익률 = (현재 - 물타기) / 물타기 * 100
            
            st.warning(f"{평단:,d} ({round(수익률,2):+,}%)")

            if 수익률 <= 0 :
                st.info(f"{int(물타기):,d} ({round(추매수익률,2):+,}%)")
            else:
                st.error(f"{int(물타기):,d} ({round(추매수익률,2):+,}%)")

        except ZeroDivisionError:
            st.warning('조건입력')
