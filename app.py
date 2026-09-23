import streamlit as st
import pandas as pd
import joblib

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Credit Default Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LOAD MODEL
# =========================================================

model = joblib.load("model2.pkl")
scaler = joblib.load("scaler.pkl")

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 30px;
}

.section-title {
    font-size: 23px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 15px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    margin-bottom: 20px;
    box-shadow: 0 3px 15px rgba(0,0,0,0.08);
}

.prediction-card {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 10px;
}

.footer {
    text-align: center;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# ENTER KEY NAVIGATION
# =========================================================

st.markdown("""
<script>

document.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        const active = document.activeElement;

        if (
            active.tagName === "INPUT" ||
            active.tagName === "SELECT"
        ) {

            event.preventDefault();

            const elements = Array.from(
                document.querySelectorAll(
                    'input, select, textarea, button'
                )
            );

            const index = elements.indexOf(active);

            if (index >= 0 && index < elements.length - 1) {
                elements[index + 1].focus();
            }
        }
    }

});

</script>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">💳 Credit Card Default Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning powered credit default prediction'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# CUSTOMER INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

with st.container():

    col1, col2 = st.columns(2)

    with col1:

        LIMIT_BAL = st.number_input(
            "Credit Limit",
            min_value=0.0,
            value=None,
            placeholder="Enter credit limit"
        )

        SEX = st.selectbox(
            "SEX",
            ["Select...", "F", "M"]
        )

        EDUCATION = st.selectbox(
            "Education",
            [
                "Select...",
                "University",
                "Graduate school",
                "High School",
                "Other"
            ]
        )

    with col2:

        MARRIAGE = st.selectbox(
            "Marriage Status",
            [
                "Select...",
                "Married",
                "Single",
                "Other"
            ]
        )

        AGE = st.number_input(
            "Age",
            min_value=18,
            max_value=100,
            value=None,
            placeholder="Enter age"
        )


# =========================================================
# REPAYMENT STATUS
# =========================================================

st.markdown(
    '<div class="section-title">📊 Repayment Status</div>',
    unsafe_allow_html=True
)

st.caption(
    "Select the repayment status for each month."
)

pay_values = [
    -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8
]

col1, col2, col3 = st.columns(3)

with col1:

    PAY_0 = st.selectbox(
        "PAY_0 — Most Recent Month",
        ["Select..."] + pay_values
    )

    PAY_2 = st.selectbox(
        "PAY_2 — Previous Month",
        ["Select..."] + pay_values
    )

with col2:

    PAY_3 = st.selectbox(
        "PAY_3 — Month 3",
        ["Select..."] + pay_values
    )

    PAY_4 = st.selectbox(
        "PAY_4 — Month 4",
        ["Select..."] + pay_values
    )

with col3:

    PAY_5 = st.selectbox(
        "PAY_5 — Month 5",
        ["Select..."] + pay_values
    )

    PAY_6 = st.selectbox(
        "PAY_6 — Month 6",
        ["Select..."] + pay_values
    )


# =========================================================
# BILL AMOUNTS
# =========================================================

st.markdown(
    '<div class="section-title">💰 Statement Balance</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    BILL_AMT1 = st.number_input(
        "BILL_AMT1",
        value=None,
        placeholder="Enter amount"
    )

    BILL_AMT2 = st.number_input(
        "BILL_AMT2",
        value=None,
        placeholder="Enter amount"
    )

with col2:

    BILL_AMT3 = st.number_input(
        "BILL_AMT3",
        value=None,
        placeholder="Enter amount"
    )

    BILL_AMT4 = st.number_input(
        "BILL_AMT4",
        value=None,
        placeholder="Enter amount"
    )

with col3:

    BILL_AMT5 = st.number_input(
        "BILL_AMT5",
        value=None,
        placeholder="Enter amount"
    )

    BILL_AMT6 = st.number_input(
        "BILL_AMT6",
        value=None,
        placeholder="Enter amount"
    )


# =========================================================
# PAYMENT AMOUNTS
# =========================================================

st.markdown(
    '<div class="section-title">💵 Payment Amount</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:

    PAY_AMT1 = st.number_input(
        "PAY_AMT1",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )

    PAY_AMT2 = st.number_input(
        "PAY_AMT2",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )

with col2:

    PAY_AMT3 = st.number_input(
        "PAY_AMT3",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )

    PAY_AMT4 = st.number_input(
        "PAY_AMT4",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )

with col3:

    PAY_AMT5 = st.number_input(
        "PAY_AMT5",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )

    PAY_AMT6 = st.number_input(
        "PAY_AMT6",
        min_value=0.0,
        value=None,
        placeholder="Enter payment"
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🔍 Predict Credit Default"
)


# =========================================================
# PREDICTION
# =========================================================

if predict:

    # =====================================================
    # CHECK EMPTY FIELDS
    # =====================================================

    values = [
        LIMIT_BAL,
        SEX,
        EDUCATION,
        MARRIAGE,
        AGE,
        PAY_0,
        PAY_2,
        PAY_3,
        PAY_4,
        PAY_5,
        PAY_6,
        BILL_AMT1,
        BILL_AMT2,
        BILL_AMT3,
        BILL_AMT4,
        BILL_AMT5,
        BILL_AMT6,
        PAY_AMT1,
        PAY_AMT2,
        PAY_AMT3,
        PAY_AMT4,
        PAY_AMT5,
        PAY_AMT6
    ]

    if any(value is None for value in values):

        st.warning(
            "⚠️ Please fill in all fields before making a prediction."
        )

        st.stop()


    # =====================================================
    # CHECK DROPDOWN VALUES
    # =====================================================

    if (
        SEX == "Select..."
        or EDUCATION == "Select..."
        or MARRIAGE == "Select..."
        or PAY_0 == "Select..."
        or PAY_2 == "Select..."
        or PAY_3 == "Select..."
        or PAY_4 == "Select..."
        or PAY_5 == "Select..."
        or PAY_6 == "Select..."
    ):

        st.warning(
            "⚠️ Please select all dropdown values."
        )

        st.stop()


    # =====================================================
    # CREATE INPUT DATAFRAME
    # =====================================================

    input_data = pd.DataFrame([{

        "LIMIT_BAL": LIMIT_BAL,
        "SEX": SEX,
        "EDUCATION": EDUCATION,
        "MARRIAGE": MARRIAGE,
        "AGE": AGE,

        "PAY_0": PAY_0,
        "PAY_2": PAY_2,
        "PAY_3": PAY_3,
        "PAY_4": PAY_4,
        "PAY_5": PAY_5,
        "PAY_6": PAY_6,

        "BILL_AMT1": BILL_AMT1,
        "BILL_AMT2": BILL_AMT2,
        "BILL_AMT3": BILL_AMT3,
        "BILL_AMT4": BILL_AMT4,
        "BILL_AMT5": BILL_AMT5,
        "BILL_AMT6": BILL_AMT6,

        "PAY_AMT1": PAY_AMT1,
        "PAY_AMT2": PAY_AMT2,
        "PAY_AMT3": PAY_AMT3,
        "PAY_AMT4": PAY_AMT4,
        "PAY_AMT5": PAY_AMT5,
        "PAY_AMT6": PAY_AMT6

    }])


    # =====================================================
    # TRANSFORM DATA
    # =====================================================

    input_scaled = scaler.transform(input_data)


    # =====================================================
    # PREDICTION
    # =====================================================

    prediction = model.predict(input_scaled)


    # =====================================================
    # RESULT
    # =====================================================

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction[0] == 1:

        st.error(
            "### ⚠️ DEFAULT\n\n"
            "The customer is predicted to default."
        )

    else:

        st.success(
            "### ✅ NOT DEFAULT\n\n"
            "The customer is predicted not to default."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Credit Card Default Prediction • Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)