
import streamlit as st
import pandas as pd
import joblib

# Load trained ML model
model = joblib.load("titanic_model.pkl")

# Page configuration
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="wide"
)

# Custom Dashboard Styling

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #172554,
        #312e81
    );
    color: white;
}

/* Main Content Width */
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main Heading */
h1 {
    color: #ffffff !important;
    font-size: 42px !important;
    font-weight: 800 !important;
}

/* Section Headings */
h2, h3 {
    color: #93c5fd !important;
    font-weight: 700 !important;
}

/* Paragraph and Labels */
p, label, [data-testid="stWidgetLabel"] {
    color: #e2e8f0 !important;
}

/* Input Fields */
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background-color: #1e293b;
    border: 1px solid #475569;
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 25px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

/* Button Hover */
.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #7c3aed,
        #2563eb
    );
    color: white;
    border: 1px solid #93c5fd;
}

/* Divider */
hr {
    border-color: #475569;
}

/* Input Text - White */
.stApp input {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* Selectbox Text - White */
.stApp [data-baseweb="select"] {
    color: #ffffff !important;
}

.stApp [data-baseweb="select"] div {
    color: #ffffff !important;
}

/* Number Input Background */
.stApp [data-baseweb="input"] {
    background-color: #1e293b !important;
}

/* Number Input Buttons */
.stApp [data-testid="stNumberInput"] button {
    background-color: #1e293b !important;
    color: #ffffff !important;
    border-color: #475569 !important;
}

/* Placeholder Text */
.stApp input::placeholder {
    color: #cbd5e1 !important;
}

</style>
""", unsafe_allow_html=True)

# Main heading
st.title("🚢 Titanic Survival Prediction")
st.subheader("Machine Learning Based Prediction Dashboard")

st.write(
    "This application predicts whether a passenger "
    "would survive the Titanic disaster."
)



#[ Passenger Details Section]

st.header("👤 Enter Passenger Details")

col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "Passenger Class",
        [1, 2, 3]
    )

    sex = st.selectbox(
        "Gender",
        ["male", "female"]
    )

    age = st.number_input(
        "Age",
        min_value=0.0,
        max_value=100.0,
        value=25.0
    )

    sibsp = st.number_input(
        "Number of Siblings/Spouses",
        min_value=0,
        max_value=10,
        value=0
    )

with col2:
    parch = st.number_input(
        "Number of Parents/Children",
        min_value=0,
        max_value=10,
        value=0
    )

    fare = st.number_input(
        "Ticket Fare",
        min_value=0.0,
        value=32.0
    )
    embarked_options = {
    "Southampton": "S",
    "Cherbourg": "C",
    "Queenstown": "Q"
}

selected_port = st.selectbox(
    "Port of Embarkation",
    options=list(embarked_options.keys())
)

embarked = embarked_options[selected_port]



# Prediction Button

st.divider()

if st.button("🔍 Predict Survival", use_container_width=True):

    # Create input DataFrame
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked': [embarked]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.success("🎉 The passenger is predicted to SURVIVE!")
    else:
        st.error("The passenger is predicted NOT TO SURVIVE.")

