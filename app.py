import streamlit as st
import math
# Custom CSS for red input boxes in rows 14 and 15
st.markdown("""
<style>
.qqq-price-right {
    text-align: right !important;
    display: block;
}
.qqq-price-left {
    text-align: left !important;
    display: block;
}
.qqq-price-darkred {
    background-color: #222 !important;
    color: #ff2222 !important;
    padding: 0.5em 1em;
    border-radius: 0.25em;
    display: inline-block;
    font-weight: inherit;
    font-size: inherit;
    font-family: inherit;
    font-style: inherit;
    text-align: center;
}
.qqq-price-red {
    color: #ff2222 !important;
    font-weight: inherit;
    font-size: inherit;
    font-family: inherit;
    font-style: inherit;
}
.qqq-price-darkmatch {
    background-color: #222 !important;
    color: inherit !important;
    padding: 0.5em 1em;
    border-radius: 0.25em;
    display: inline-block;
    font-weight: inherit;
    font-size: inherit;
    font-family: inherit;
    font-style: inherit;
    text-align: center;
}
.qqq-price-darkgreen-right {
    background-color: #222 !important;
    color: #00c853 !important;
    padding: 0.5em 1em;
    border-radius: 0.25em;
    display: block;
    text-align: right;
    font-weight: inherit;
    font-size: 0.8rem !important;
    font-family: inherit;
    font-style: inherit;
}
.qqq-price-darkgreen-left {
    background-color: #222 !important;
    color: #00c853 !important;
    padding: 0.5em 1em;
    border-radius: 0.25em;
    display: block;
    text-align: left;
    font-weight: inherit;
    font-size: 0.9rem !important;
    font-family: inherit;
    font-style: inherit;
}
/* Force all column rows to stay on one line and shrink on mobile */
[data-testid="stHorizontalBlock"] {
    flex-wrap: nowrap !important;
    gap: 0.25rem !important;
    overflow-x: auto !important;
}
[data-testid="stColumn"] {
    min-width: 0 !important;
    overflow: hidden !important;
}
/* Shrink text and inputs inside columns */
[data-testid="stColumn"] p,
[data-testid="stColumn"] span,
[data-testid="stColumn"] div,
[data-testid="stColumn"] pre {
    font-size: 0.78rem !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}
[data-testid="stColumn"] input[type="number"] {
    font-size: 0.78rem !important;
    padding: 0.2rem 0.3rem !important;
    min-width: 0 !important;
    width: 100% !important;
}
[data-testid="stColumn"] [data-testid="stNumberInput"] > div {
    padding: 0 !important;
    gap: 0 !important;
}
[data-testid="stColumn"] [data-testid="stNumberInput"] button {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Options Calc", layout="wide")

# --- Title & Subtitle ---
st.title("Options Calc")
st.subheader("Sell Iron Condor - Stable Profit")

# --- Input Parameters ---
col1, col2, col3 = st.columns(3)
with col1:
    contracts_per_lot = st.number_input("每張合約（股）", value=100, disabled=True)
    down_spread = st.number_input("向下Spread (-)", value=20, step=1, min_value=1)
with col2:
    spread_width = st.number_input("Spread 寬度", value=2, step=1, min_value=1)
    up_spread = st.number_input("向上Spread (+)", value=15, step=1, min_value=1)
with col3:
    num_contracts = st.number_input("多少張合約", value=1, step=1, min_value=1)
    qqq_price = st.number_input("QQQ 現價", value=600, step=1)

st.markdown("---")

# ===================== Options Table =====================
COL = [3, 1.5, 1.5, 2, 2.5]

# Header row
h = st.columns(COL)
for i, title in enumerate(["Item", "DTE", "QQQ Price", "期權金", "平倉位"]):
    h[i].markdown(f"**{title}**")


# --- Row 11: 60DTE Long Put (insurance leg) ---
row11_qqq = qqq_price - down_spread - spread_width - 14
c = st.columns(COL)
c[0].write("long put (Buy)↓P")
c[1].write("(60DTE)")
c[2].markdown(f'<div class="qqq-price-darkgreen-right">{row11_qqq}</div>', unsafe_allow_html=True)
row11_premium = c[3].number_input(
    "premium_60dte_put", value=18.52, step=0.1, format="%.2f",
    key="premium_60dte_put",
    label_visibility="collapsed",
)
c[4].text("< " + str(math.ceil(row11_qqq - row11_premium - 3)))

# BR
st.markdown("<br>", unsafe_allow_html=True)


# --- Row 13: 2DTE Long Put ---
row13_qqq = qqq_price - down_spread - spread_width
c = st.columns(COL)
c[0].write("long put (Buy)↓P")
c[1].write("(2DTE)")
c[2].markdown(f'<div class="qqq-price-darkgreen-right">{row13_qqq}</div>', unsafe_allow_html=True)
c[3].number_input(
    "premium_2dte_lp", value=1.30, step=0.1, format="%.2f",
    key="premium_2dte_lp",
    label_visibility="collapsed",
)
c[4].write("")


# --- Row 14: 2DTE Short Put ---
row14_qqq = qqq_price - down_spread
c = st.columns(COL)
c[0].write("short put (Sell)↓P")
c[1].write("(2DTE)")
c[2].markdown(f'<span class="qqq-price-right qqq-price-red">{row14_qqq}</span>', unsafe_allow_html=True)
c[3].number_input(
    "premium_2dte_sp", value=1.49, step=0.1, format="%.2f",
    key="premium_2dte_sp",
    label_visibility="collapsed",
)
c[4].write(qqq_price - down_spread + 1)


# --- Row 15: 2DTE Short Call ---
row15_qqq = qqq_price + up_spread
c = st.columns(COL)
c[0].write("short call (Sell)↓C")
c[1].write("(2DTE)")
c[2].markdown(f'<span class="qqq-price-red">{row15_qqq}</span>', unsafe_allow_html=True)
c[3].number_input(
    "premium_2dte_sc", value=0.93, step=0.1, format="%.2f",
    key="premium_2dte_sc",
    label_visibility="collapsed",
)
c[4].write(qqq_price + up_spread - 1)


# --- Row 16: 2DTE Long Call ---
row16_qqq = qqq_price + up_spread + spread_width
c = st.columns(COL)
c[0].write("long call (Buy)↑C")
c[1].write("(2DTE)")
c[2].markdown(f'<div class="qqq-price-darkgreen-left">{row16_qqq}</div>', unsafe_allow_html=True)
c[3].number_input(
    "premium_2dte_lc", value=0.63, step=0.1, format="%.2f",
    key="premium_2dte_lc",
    label_visibility="collapsed",
)
c[4].write("")

# BR
st.markdown("<br>", unsafe_allow_html=True)


# --- Row 18: 60DTE Long Call (insurance leg) ---
row18_qqq = qqq_price + up_spread + spread_width + 14
c = st.columns(COL)
c[0].write("long call (Buy)↑C")
c[1].write("(60DTE)")
c[2].markdown(f'<div class="qqq-price-darkgreen-left">{row18_qqq}</div>', unsafe_allow_html=True)
row18_premium = c[3].number_input(
    "premium_60dte_call", value=18.35, step=0.1, format="%.2f",
    key="premium_60dte_call",
    label_visibility="collapsed",
)
c[4].text("> " + str(math.ceil(row18_qqq + row18_premium + 3)))

st.markdown("---")

# ===================== Calculations =====================
# Get premium values from session state
row14_premium = st.session_state["premium_2dte_sp"]
row15_premium = st.session_state["premium_2dte_sc"]
row13_premium = st.session_state["premium_2dte_lp"]
row16_premium = st.session_state["premium_2dte_lc"]
row11_premium = st.session_state["premium_60dte_put"]
row18_premium = st.session_state["premium_60dte_call"]
net_credit = (row14_premium + row15_premium - row13_premium - row16_premium) * num_contracts
net_credit_x100 = (contracts_per_lot * net_credit) - 10.5
potential_loss = (contracts_per_lot * spread_width * num_contracts) - net_credit_x100
insurance_cost = (row11_premium + row18_premium) * num_contracts

st.markdown(f"**Net Credit:** {net_credit:.2f}")
st.markdown(
    f"**Net Credit x 100 - Transaction Fee:** {net_credit_x100:.2f} USD"
)
st.markdown(f"**Potential Loss:** {potential_loss:.2f} USD")

st.markdown("---")

st.markdown(f"**長期 OTM 保險腿成本:** {insurance_cost:.2f} USD")
