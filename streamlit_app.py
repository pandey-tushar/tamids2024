import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import streamlit.components.v1 as components
import webbrowser


# ~~~~~~~~~~~~~~~~~~~~~~~~ Home Page ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def home_page():

    # Desription -
    st.markdown("""
                <p style='text-align: justify;'>
                The 2024 TAMIDS Data Science Competition is about sea level rising and its impact.
                </p>
                """, unsafe_allow_html=True)

    # Problem Statement -
    st.write("""
             ## Problem Statement
             """)
    st.markdown("""
                <p style='text-align: justify;'>
            Prob stat
             </p>
                """, unsafe_allow_html=True)

    # Data Collection and Pre-processing -
    st.write("""
             ## Data Collection and Pre-processing
             """)
    st.markdown("""
                <p style='text-align: justify;'>
                 Data collec + prepro
                 </p>
                """, unsafe_allow_html=True)
    
    
    
    st.markdown("""
                <p style='text-align: justify;'>
             New para
             </p>
                """, unsafe_allow_html=True)
    st.markdown("""
                <p style='text-align: justify;'>
             new paragraph
             </p>
                """, unsafe_allow_html=True)

    
    # Overview -
    st.write("""
             ## Methodology
             """)
    st.markdown("""
                <p style='text-align: justify;'>
                New parag
             </p>
                """, unsafe_allow_html=True)

    # Navigation -
    st.write("")
    st.info("Please navigate using the select box in the sidebar on the left.")




#------------------ Sea Levels on the east coast  -------------------------
def east_coast():
    st.title('Sea Levels on the east coast')
    st.write(" ")




#~~~~~~~~~~~~~~~~~~ Causal interference of the sea level rise ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def network_analysis():
    st.title('Relationship between different green house gas emissions and sea level rise')
    st.write(" ")
    st.write("""
            We can go to the network analysis page by clicking
            on the link. Below is a snapshot of the green house emissions and the sea level rise 
            in the guld of Mexico""")

    #To access the network analysis, press the button below.

    st.write("")
    col1, col2, col3 = st.columns((1,1,1))
    link = '[Green House emissions and sea level rise in Gulf of Mexico](https://pandey-tushar.github.io/tamids2024/)'
    col2.markdown(link, unsafe_allow_html=True)

    st.write(" ")
    #Setting the Image
    image = Image.open('Images/gulf_of_mexico_TDA.jpg')

    #Setting the image width
    st.image(image, use_column_width = True)

    st.write(" ")



#~~~~~~~~~~~~~~~~~ Predicting Sea levels ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def predicting_sea_level():
    st.title('Predicting Sea levels')
    st.write(" ")
    


#~~~~~~~~~~~~~~~~~~ Controlling sea level rise ~~~~~~~~~~~~~~~~~~~~~~~
def control_the_rise():
    st.title('Controlling sea level rise')
    st.write(" ")
    




#------------------ About the Authors -------------------------
def authors():
    # Setting the title -
    st.title("About the Authors")
    st.write(" ")


    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # # Setting the image -
    # image = Image.open('Images/tushar.png')

    # # Setting the image width -
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Tushar Pandey")

    # About section -
    col3.write("""
               Research Area: Quantum Topology

               * **University:** Texas A&M University (Department of Mathematics)
               * **Degree:** PhD Student (2024)
               * **Email:** tusharp@tamu.edu
               * **LinkedIn:** [linkedin.com/in/tushar-pandey1612/](https://www.linkedin.com/in/tushar-pandey1612/)
               * **Github:** [github.com/pandey-tushar](https://github.com/pandey-tushar)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # # Setting the image -
    # image = Image.open('Images/sambandh.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Ritesh Singh Suhag -
    col3.write("## Sambandh Dhal")

    # About section -
    col3.write("""
               Research Area: Error Estimation and Machine Learning.

               * **University:** Texas A&M University (Department of Electrical and Computer Engineering)
               * **Degree:** PhD Student (Computer Engineering)
               * **Email:** sambandh@tamu.edu
               * **LinkedIn:** [linkedin.com/in/sambandh-dhal9163/](https://www.linkedin.com/in/sambandh-dhal9163/)
               * **Github:** [github.com/Sambandh](https://github.com/Sambandh)
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # Setting the image -
    # image = Image.open('Images/Abhijeet.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Vivek -
    col3.write("## Vivek")

    # About section -
    col3.write("""
               Research Area: 

               * **University:** Texas A&M University ()
               * **Degree:** PhD Student (Engineering)
               * **Email:** 
               * **LinkedIn:** []()
               * **Github:** []()
               """)
    st.write("")
    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # # Setting the image -
    # image = Image.open('Images/swarnabha.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Rishabh -
    col3.write("## Rishabh")

    # About section -
    col3.write("""
               Research Area: .

               * **University:** Texas A&M University ()
               * **Degree:** PhD Student ( Engineering)
               * **Email:** 
               * **LinkedIn:** []()
               * **Github:** []()
               """)
    st.write("")

    # Dividing screen into 2 parts -
    col1, col2, col3 = st.columns((0.75,0.1,2))

    # # Setting the image -
    # image = Image.open('Images/dd.png')

    # # Setting the image width -
    # col1.write("")
    # col1.write("")
    # col1.image(image, use_column_width=True)

    # Sheil -
    col3.write("## Sheel")

    # About section -
    col3.write("""
               Research Area: 

               * **University:** Texas A&M University ()
               * **Degree:** PhD Student ( Engineering)
               * **Email:** 
               * **LinkedIn:** []()
               * **Github:** []()
               """)
    st.write("")


# Page title
st.set_page_config(layout='wide', page_title="Sea Level Rising and it's impact", page_icon='🌊')
st.set_option('deprecation.showPyplotGlobalUse', False)



# Sidebar navigation for users -
st.sidebar.header('Navigation tab')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page',
 'Sea Levels on the east coast','Green house emissions and sea level rise', 'Predicting Sea levels',
 'Controlling sea level rise', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Sea Levels on the east coast':
    east_coast()


# Second Page -
elif navigation_tab == 'Green house emissions and sea level rise':
    network_analysis()

# Third Page -
elif navigation_tab == 'Predicting Sea levels':
    predicting_sea_level()

# Fourth Page -
elif navigation_tab == 'Controlling sea level rise':
    control_the_rise()

# About Page -
elif navigation_tab == 'About the Authors':
    authors()

