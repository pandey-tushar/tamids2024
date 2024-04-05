import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import altair as alt
import streamlit.components.v1 as components
import webbrowser
from PIL import Image


# ~~~~~~~~~~~~~~~~~~~~~~~~ Home Page ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def home_page():
    # Setting the title -
    # st.title("TAMIDS Data Science Competition 2024")

    # Desription -
    st.markdown(
        """
                <p style='text-align: justify;'>
                The 2024 TAMIDS Data Science Competition is about finding the
                impact of sea level rise, the factors affecting sea level rise
                and data driven solutions to restrict the negative impacts.
                </p>
                """,
        unsafe_allow_html=True,
    )

    # Problem Statement -
    st.write(
        """
             ## Problem Statement
             """
    )
    st.markdown(
        """
                <p style='text-align: justify;'>
            We’re tackling the challenge of using data-driven research to predict
            and mitigate sea level rise (SLR). We aim to analyze the impacted
            areas and provide actionable insights to guide decision-makers,
            balancing precision with clear communication.
             </p>
                """,
        unsafe_allow_html=True,
    )

    # Data Collection and Pre-processing -
    st.write(
        """
             ## Data Collection and Pre-processing
             """
    )
    st.markdown(
        """
                <p style='text-align: justify;'>
                 The analysis has been made on SLR and
                 impacts of SLR. This also includes
                 the factors affecting climate change
                 as well as SLR impacts like the 
                 Greenhouse gases
                 <ul>
                 <li> list item 1
                 <li> list item 2 </ul>
                 </p>
                """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
                <p style='text-align: justify;'>
             The abstract keywords per department were calculated by using NLP algorithms on the dataset containing the 
             abstracts of the publications using unigram, bigram and trigram to find the most frequently occurring sequential tokens. 
             From the sequential tokens, the generic words were removed to formulate a clean corpus which was used to compute the four 
             types of scores defined above.
             </p>
                """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
                <p style='text-align: justify;'>
             In order to have a better understanding of these metrics, a graphical representation per department was plotted which 
             has been included in our website and a few of these plots have been shown below.
             </p>
                """,
        unsafe_allow_html=True,
    )

    # Overview -
    st.write(
        """
             ## Methodology
             """
    )
    st.markdown(
        """
                <p style='text-align: justify;'>

                * **Feature Engineering:** Data normalization explained
                * **Unsupervised Learning:** Clustering based on different features of the data. Rather, with the mapper package, we see a better picture of our clusters which brings us to the visualizations.
                * **Dynamic Visualization:** About TDA and other visualization. Therefore, the website we have designed is very dynamic and suitable for everyone.
             </p>
                """,
        unsafe_allow_html=True,
    )

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")


# ------------------ Sea Levels on the east coast  -------------------------
def data_exploration():
    st.title("Sea Levels on the east coast")
    st.write(" ")
    st.write(
        """Below is the sea level rise estimates averaged
            over first few months of a year after using LSTM and SARIMAX model to
            predict the future values until the year 2103.
            """
    )
    # Getting the graph
    HtmlFile = open(f"HTML/SLR_predictions.html", "r", encoding="utf-8")
    source_code_2 = HtmlFile.read()
    components.html(source_code_2, height=500)
    st.write(" ")

    st.write(
        """
            We can see that not only the sea levels are going to rise over
            the years, but it's also going up substantially. Here, we have predicted
            the sea level averaged over the month of Jan, Feb, March, Apr, May. 

            It's worth noting that in the first three months, the sea levels are
            relatively lower than the levels in spring and summer. Therefore, 
            one can expect the highest level in the summer to be at least 3 times
            the value we have on the graph.

            !! This is very concerning !!
            """
    )


# ~~~~~~~~~~~~~~~~~~ Causal interference of the sea level rise ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def network_analysis():
    st.title(
        "Relationship between different green house gas emissions and sea level rise"
    )
    st.write(" ")
    st.write(
        """
            We can go to the network analysis page by clicking
            on the link. Below is a snapshot of the green house emissions and the sea level rise 
            in the gulf of Mexico"""
    )

    # To access the network analysis, press the button below.

    st.write("")
    col1, col2, col3 = st.columns((1, 1, 1))
    link = "[Green House emissions and sea level rise in Gulf of Mexico](https://pandey-tushar.github.io/tamids2024/)"
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    # Setting the Image
    image = Image.open("Images/gulf_of_mexico_TDA.jpg")

    # Setting the image width
    st.image(image, use_column_width=True)

    st.write(" ")

    st.write(
        """
            We can go to the network analysis page of the green house emissions and the sea level
            rise in the Atlantic ocean as well.
            """
    )
    # To access the network analysis, press the button below.

    st.write("")
    col1, col2, col3 = st.columns((1, 1, 1))
    link = "[Green House emissions and sea level rise in Atlantic Ocean](https://pandey-tushar.github.io/tamids24/)"
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    # Setting the Image
    image = Image.open("Images/atlantic_TDA.jpg")

    # Setting the image width
    st.image(image, use_column_width=True)

    st.write(" ")


# ~~~~~~~~~~~~~~~~~ Predicting Sea levels ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def predicting_sea_level():

    st.title("Predicting Sea levels")
    st.write(" ")

    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    st.write("""## Gulf of Mexico""")
    # model_gom = load_model("models/model_gom_3.hdf5")

    key_co_gom, key_no2_gom, key_pm10_gom, key_so2_gom = (
        "key_co_gom",
        "key_no2_gom",
        "key_pm10_gom",
        "key_so2_gom",
    )

    co_gom = st.text_input(label="Carbon Monoxide (CO)", key=key_co_gom)
    no2_gom = st.text_input(label="Nitrogen Dioxide (NO2)", key=key_no2_gom)
    pm10_gom = st.text_input(label="Particulate Matter 10mm (PM-10)", key=key_pm10_gom)
    so2_gom = st.text_input(label="Sulphur Dioxide (SO2)", key=key_so2_gom)

    # # Normalize the predictors
    # scaler = MinMaxScaler()
    # predictors = np.array([[so2_gom, co_gom, pm10_gom, no2_gom]])
    # predictors_scaled = scaler.fit_transform(predictors)

    if st.button(label="Predict", key="predict_gom"):
        # output_gom = model_gom.predict(predictors_scaled)
        output_gom = 150
        st.success(f"Sea level is {output_gom} mm.")

    st.write("""## East Coast""")
    # model_na = load_model("models/model_na_3.hdf5")

    key_co_na, key_no2_na, key_pm10_na, key_so2_na = (
        "key_co_na",
        "key_no2_na",
        "key_pm10_na",
        "key_so2_na",
    )

    co_na = st.text_input(label="Carbon Monoxide (CO)", key=key_co_na)
    no2_na = st.text_input(label="Nitrogen Dioxide (NO2)", key=key_no2_na)
    pm10_na = st.text_input(label="Particulate Matter 10mm (PM-10)", key=key_pm10_na)
    so2_na = st.text_input(label="Sulphur Dioxide (SO2)", key=key_so2_na)

    # # Normalize the predictors
    # scaler = MinMaxScaler()
    # predictors = np.array([[pm10_na, co_na, so2_na, no2_na]])
    # predictors_scaled = scaler.fit_transform(predictors)

    if st.button("Predict", key="predict_na"):
        # output_na = model_na.predict(predictors_scaled)
        output_na = 150
        st.success(f"Sea level is {output_na} mm.")


# ~~~~~~~~~~~~~~~~~~ Controlling sea level rise ~~~~~~~~~~~~~~~~~~~~~~~
def control_the_rise():
    st.title("Controlling sea level rise")
    st.write(" ")


# ------------------ About the Authors -------------------------
def authors():
    # Setting the title -
    st.title("About the Authors")
    st.write(" ")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75, 0.1, 2))

    # # Setting the image -
    # image = Image.open('Images/tushar.png')

    # # Setting the image width -
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Tushar Pandey")

    # About section -
    col3.write(
        """
               Research Area: Quantum Topology

               * **University:** Texas A&M University (Department of Mathematics)
               * **Degree:** PhD Student (2024)
               * **Email:** tusharp@tamu.edu
               * **LinkedIn:** [linkedin.com/in/tushar-pandey1612/](https://www.linkedin.com/in/tpmath/)
               * **Github:** [github.com/pandey-tushar](https://github.com/pandey-tushar)
               """
    )
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75, 0.1, 2))

    # # Setting the image -
    # image = Image.open('Images/sambandh.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")

    # About section -
    col3.write(
        """
               Research Area: Error Estimation and Machine Learning.

               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering)
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/Sambandh](https://github.com/Sambandh)
               """
    )
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75, 0.1, 2))

    # Setting the image -
    # image = Image.open('Images/Abhijeet.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Vivek -
    col3.write("## Vivekvardhan Kesireddy")

    # About section -
    col3.write(
        """
               Research Area: Drilling Automation

               * **University:** Texas A&M University
               * **Degree:** PhD Student (Petroleum Engineering)
               * **Email:** vkesireddy@tamu.edu
               * **LinkedIn:** [linkedin.com/in/vivekkesireddy/](https://www.linkedin.com/in/vivekkesireddy/)
               * **Github:** [github.com/vivekkesireddy](https://github.com/vivekkesireddy)
               """
    )
    st.write("")
    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75, 0.1, 2))

    # # Setting the image -
    # image = Image.open('Images/swarnabha.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Rishabh -
    col3.write("## Rishabh Singh")

    # About section -
    col3.write(
        """
               Research Area: Soil carbon, Climate smart agriculture

               * **University:** Texas A&M University ()
               * **Degree:** PhD Student (Biological and Agricultural Engineering)
               * **Email:** irishabh1996@tamu.edu
               * **LinkedIn:** [www.linkedin.com/in/rishabh2996/](https://www.linkedin.com/in/rishabh2996/)
               * **Github:** [github.com/irishabh-96](https://github.com/irishabh-96)
               """
    )
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75, 0.1, 2))

    # # Setting the image -
    # image = Image.open('Images/dd.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Sheil -
    col3.write("## Sheelabhadra Dey")

    # About section -
    col3.write(
        """
               Research Area: Reinforcement Learning

               * **University:** Texas A&M University
               * **Degree:** PhD Student (Computer Science)
               * **Email:** sheelabhadra@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sheelabhadra/](https://www.linkedin.com/in/sheelabhadra/)
               * **Github:** [github.com/sheelabhadra](https://github.com/sheelabhadra)
               """
    )
    st.write("")


# Page title
st.set_page_config(
    layout="wide", page_title="Sea Level Rising and it's impact", page_icon="🌊"
)
st.set_option("deprecation.showPyplotGlobalUse", False)


# Sidebar navigation for users -
st.sidebar.header("Navigation tab")
navigation_tab = st.sidebar.selectbox(
    "Choose a tab",
    (
        "Home-Page",
        "Exploring the data",
        "Green house emissions and sea level rise",
        "Predicting Sea levels",
        "Controlling sea level rise",
        "About the Authors",
    ),
)

# Displaying pages according to the selection -

# Home page -
if navigation_tab == "Home-Page":
    home_page()

# First page -
elif navigation_tab == "Exploring the data":
    data_exploration()


# Second Page -
elif navigation_tab == "Green house emissions and sea level rise":
    network_analysis()

# Third Page -
elif navigation_tab == "Predicting Sea levels":
    predicting_sea_level()

# Fourth Page -
elif navigation_tab == "Controlling sea level rise":
    control_the_rise()

# About Page -
elif navigation_tab == "About the Authors":
    authors()
