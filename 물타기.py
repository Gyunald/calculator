import streamlit as st
c1,c2 = st.columns([.6,1])
with c1 :
    with st.expander('🎈'):
        try:
            평단 = int(st.text_input('평균단가',0))
            수량 = int(st.text_input('보유수량',0))
            보유금액 = st.text_input('보유금액',f"{평단*수량:,}",disabled=True)
            현재 = int(st.text_input('현재단가',0))                        
            수익률 = (현재 - 평단) / 평단 * 100
            st.warning(f"{평단:,d} ({round(수익률,2):+,}%)")
            매수금액 = 평단 * 수량
            추매수량 = st.number_input('추매수량',min_value=0,step=1)
            보유금액 = st.text_input('추매금액',f"{현재*추매수량:,}",disabled=True)
            추매 = 현재 * 추매수량
            물타기 = (매수금액 + 추매) / (수량 + 추매수량)
            추매수익률 = (현재 - 물타기) / 물타기 * 100
            if 수익률 <= 0 :
                st.info(f"{int(물타기):,d} ({round(추매수익률,2):+,}%)")
            else:
                st.error(f"{int(물타기):,d} ({round(추매수익률,2):+,}%)")
        except ZeroDivisionError:
            st.warning('조건입력')
