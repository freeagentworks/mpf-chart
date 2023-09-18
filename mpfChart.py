import yfinance as yf
import mplfinance as mpf
import streamlit as st


st.title("株価チャートMplfinance")
#st.subheader("Mpfを使ってチャートを表示します")

st.text("ティッカー、証券コードを入力してくだい\n" +
        "例）AAPL,7203.T,^N225")

col1, col2 = st.columns(2)
with col1:
    ticker = st.text_input("ティッカーコード:",'^N225')
with col2:
    dsp_days = st.text_input("表示日数", 150)
    #submit_btn = st.button("送信")

st.markdown("---")


st.sidebar.subheader("設定項目")
st.sidebar.caption("設定項目を入力してください")

with st.sidebar.form("settings_form"):
    show_volume = st.checkbox('出来高表示',False)
    
    chart_types = [
        'candle', 'ohlc', 'line', 'renko', 'pnf'
    ]
    chart_type = st.selectbox('チャートタイプ', options=chart_types, index=chart_types.index('candle'))

    chart_styles = [
        'default', 'binance', 'blueskies', 'brasil', 
        'charles', 'checkers', 'classic', 'yahoo',
        'mike', 'nightclouds', 'sas', 'starsandstripes'
    ]
    chart_style = st.selectbox('チャートスタイル', options=chart_styles, index=chart_styles.index('yahoo'))

    marketcolors = [
        'default', 'binance', 'blueskies', 'brasil', 
        'charles', 'checkers', 'classic', 'yahoo',
        'mike', 'nightclouds', 'sas', 'starsandstripes'        
    ]
    market_color = st.selectbox('マーケットカラー', options=marketcolors, index=chart_styles.index('yahoo')) 
    
    st.text("移動平均線")
    sma1 = int(st.text_input("短期", 5))
    sma2 = int(st.text_input("中期", 20))
    sma3 = int(st.text_input("長期", 60))
    
    
    st.form_submit_button("表示")
    

    
def show_chart(ticker,df):
   df = yf.download(ticker).tail(int(dsp_days))
   fig, ax = mpf.plot(
       df,
        title=ticker,
        style=chart_style,
        type=chart_type,
        figsize=(20,10),
        volume=show_volume,
        mav = (sma1, sma2, sma3),
        returnfig=True
    ) 
   st.pyplot(fig)
   
if ticker:
    df = yf.download(ticker).tail(int(dsp_days))
    show_chart(ticker,df)


#st.dataframe(df)
    
