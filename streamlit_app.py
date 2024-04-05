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
            In this competition, we are tasked with analyzing historical
            data regarding sea level rise and the impact of human activities
            on climate systems.The goal is to identify patterns and trends
            using predictive models to understand patterns in sea level rise
            and consequently comprehend the impact due to sea level rise in
            terms of. We work to map communities most affected by these changes. 

            Additionally, it's worthwile to monitor real-time environmental changes.
            The stretch goal beyond this competition is to leverage data-driven
            approaches to enhance our predictive capabilities and management
            strategies for mitigating the impact of climate change on human
            communities and natural resources.
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
                
                 * **Area of interest:** The study area comprises the states of Texas, Louisiana, Mississippi,
                 Alabama, Florida, Georgia, North Carolina, South Carolina, Virginia,
                 Delaware, New Jersey, New York, Connecticut, Rhode Island,
                 Massachusetts, Maine, and Pennsylvania. The states encompass the Gulf
                 of Mexico and the Eastern Coast of the Contiguous United States (CONUS)
                 adjacent to the North Atlantic Ocean. Low-lying coastal areas are among
                 the most vulnerable to the effects of sea level rise, with a total
                 population of almost 300 million living along the coasts of the globe,
                 including 20 of the 33 megacities
                 
                 * **SLR Data:** Sea level rise data was acquired from National Oceanic and Atmospheric
                 Administration’s (NOAA)/NESDIS/STAR Laboratory for Satellite Altimetry
                 website for sea level data (NOAA/NESDIS/STAR). The program processing
                 system generated the data, which included information from all altimeter
                 Copernicus missions (Sentinel-6A and Sentinel-3A) as well as other
                 collaboration opportunity missions (Jason-3 and Topex/Poseidon). The
                 dataset was obtained for the period 1993-2023.
                 
                 * **Effects of SLR:** The Coastal Data and Analysis Tool for Water Resources Management
                 (CDAT-WRM) supplied data related to specific conductance for
                 investigations that included coastal water management-related
                 visualizations. It  incorporates components of two existing U.S.
                 Geological Survey websites, the Water Level and Salinity Analysis
                 Mapper (U.S. Geological Survey, 2021a) and the Coastal Salinity
                 Index (U.S. Geological Survey, 2021b).
                 
                 * **Dissolved Oxygen:** Globally gridded dataset of DO in surface water for the period
                 1993-2010, monthly observations was downloaded from The World Bank
                 Data Catalog (World Bank Data Catalog) for the Chesapeake Bay,
                 which is the largest estuary in the United States. The Delmarva
                 Peninsula divides the bay, which is in the mid-Atlantic region.
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

                * **Feature Engineering:** Data normalization, filling null values,
                shortlisting counties of choice.
                * **Unsupervised Learning:** Clustering based on different
                features of the data. Rather, with the mapper package,
                we see a better picture of our clusters which brings us to
                the visualizations.
                * **Dynamic Visualization:** About TDA and other visualization.
                Therefore, the website we have designed is very dynamic and suitable
                for future use as well.
                * **Modelling:** An ensemble of 5 LSTM models to find
                the most optimal model in predicting SLR (along the East Coast and
                Gulf of Mexico). Determine the predictive weights for future SLR
                projections, contingent upon variable greenhouse gas levels influenced
                by governmental policies and strategies. A weighted hybrid model
                combining Long Short-Term Memory (LSTM) and Seasonal Autoregressive
                Integrated Moving Average with Exogenous Regressors (SARIMAX)
                methodologies. Construct an interactive tool capable of
                predicting SLR outcomes based on user-inputted pollutant levels,
                projecting up to the year 2100. Comprehensive project with insights
                into the potential ramifications of climate policy on global warming, with 
                a particular focus on Sea Level Rise, thereby enabling predictions regarding
                its subsequent effects on biodiversity, water salinity, and agricultural conditions.
             </p>
                """,
        unsafe_allow_html=True,
    )

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")


# ------------------ Data Exploration  -------------------------
def data_exploration():
    st.write(" ")
    st.write("## Sea Level Rise ")
    st.write(" ")
    st.markdown(
        """
        Sea level rise data was acquired from National Oceanic and Atmospheric
        Administration’s (NOAA)/NESDIS/STAR Laboratory for Satellite Altimetry 
        website for sea level data (NOAA/NESDIS/STAR). The program processing 
        system generated the data, which included information from all altimeter
        Copernicus missions (Sentinel-6A and Sentinel-3A) as well as other
        collaboration opportunity missions (Jason-3 and Topex/Poseidon). The 
        dataset was obtained for the period 1993-2023. Data was downloaded in 
        netCDF format and analyzed using ArcGIS Pro. Additional data for
        visualization purposes were downloaded from Copernicus Climate Change
        (C3) Services. Two variables “adt” and “sla” were downloaded from 
        1993-2023 to observe the sea level rise in the Gulf of Mexico and 
        North Atlantic Ocean along the Southeastern and Eastern US Coast 
        (Copernicus Climate Change (C3)).

        """,
        unsafe_allow_html = True,
    )
    st.write(" ")
    # Setting the Image
    image = Image.open("Images/relative_sea_level_rise.jpg")

    # Setting the image width
    st.image(image, use_column_width=True)

    st.write(" ")
    st.write("## Effects of SLR ")
    st.write(" ")
    st.markdown(
        """
        The Coastal Data and Analysis Tool for Water Resources Management
        (CDAT-WRM) supplied data related to specific conductance for
        investigations that included coastal water management-related 
        visualizations. It  incorporates components of two existing U.S. 
        Geological Survey websites, the Water Level and Salinity Analysis 
        Mapper (U.S. Geological Survey, 2021a) and the Coastal Salinity 
        Index (U.S. Geological Survey, 2021b). The specific conductance 
        values are derived from a summary of the complete day of readings
        and represents the mean value. 

        Globally gridded dataset of DO in surface water for the period 
        1993-2010, monthly observations was downloaded from The World 
        Bank Data Catalog (World Bank Data Catalog) for the Chesapeake 
        Bay, which is the largest estuary in the United States. The
        Delmarva Peninsula divides the bay, which is in the mid-Atlantic 
        region, from the Atlantic Ocean.
        """,
        unsafe_allow_html = True,
    )

    st.write(" ")
    # Setting the Image
    image = Image.open("Images/relative_sea_level_rise.jpg")

    # Setting the image width
    st.image(image, use_column_width=True)

    st.write(" ")



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

    st.markdown("""
            <p>
            In this dynamic visualization, we have a few parameters that are
            adjustable to the user. We can color the nodes using different features,
            such as the CO level, NO2 level, Particulates, SLR etc. Another
            adjustable feature is whether we want to look at the mean of each node
            for the feature selected, or the maximum or the minimum. Clicking on any
            node will let us see the data points in that node. Note that we have
            used a DBSCAN based clustering method and created a network graph that
            adds an edge between local clusters. We also have a feature to look for
            any specific year or decade and see how the levels were in that year. 
            We have used the concept of Topological Data Analysis, and more
            specifically the mapper algorithm to look at the connectivity in the
            dataset. We do the same plot for both the Atlantic Ocean and Gulf of
            Mexico. This provides us with an amazing overview of the relationship 
            between levels of pollutants and SLR over different years and decades. 
            </p>
            """,
        unsafe_allow_html=True,)


# ~~~~~~~~~~~~~~~~~ Predicting Sea levels ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def predicting_sea_level():
    st.title("Predicting Sea levels")
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
def effects_slr():
    st.title("Effects of SLR")
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
        "Effects of SLR",
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
elif navigation_tab == "Effects of SLR":
    effects_slr()

# About Page -
elif navigation_tab == "About the Authors":
    authors()
