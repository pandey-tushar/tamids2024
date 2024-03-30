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
def interference():
    st.title('Causal interference of the sea level rise')
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
    col3.write("## Sheil")

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
st.set_page_config(page_title="Sea Level Rising and it's impact", page_icon='📊')
st.title('📊 Sea Level Rising and impact')
  
st.subheader('SEA LEVEL CHANGE')


# Sidebar navigation for users -
st.sidebar.header('Navigation tab')
navigation_tab = st.sidebar.selectbox('Choose a tab', ('Home-Page',
 'Publication Analysis','Collaboration potential', 'Grant Analysis',
 'Impact score', 'About the Authors'))

# Displaying pages according to the selection -

# Home page -
if navigation_tab == 'Home-Page':
    home_page()

# First page -
elif navigation_tab == 'Sea Levels on the east coast':
    east_coast()


# Second Page -
elif navigation_tab == 'Causal interference of the sea level rise':
    interference()

# Third Page -
elif navigation_tab == 'Predicting Sea levels':
    predicting_sea_level()

# Fourth Page -
elif navigation_tab == 'Controlling sea level rise':
    control_the_rise()

# About Page -
elif navigation_tab == 'About the Authors':
    authors()

# Load data
# df = pd.read_csv('data/movies_genres_summary.csv')
# df.year = df.year.astype('int')

# # Input widgets
# ## Genres selection
# genres_list = df.genre.unique()
# genres_selection = st.multiselect('Select genres', genres_list, ['Action', 'Adventure', 'Biography', 'Comedy', 'Drama', 'Horror'])

# ## Year selection
# year_list = df.year.unique()
# year_selection = st.slider('Select year duration', 1986, 2006, (2000, 2016))
# year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# df_selection = df[df.genre.isin(genres_selection) & df['year'].isin(year_selection_list)]
# reshaped_df = df_selection.pivot_table(index='year', columns='genre', values='gross', aggfunc='sum', fill_value=0)
# reshaped_df = reshaped_df.sort_values(by='year', ascending=False)


# # Display DataFrame

# df_editor = st.data_editor(reshaped_df, height=212, use_container_width=True,
#                             column_config={"year": st.column_config.TextColumn("Year")},
#                             num_rows="dynamic")
# df_chart = pd.melt(df_editor.reset_index(), id_vars='year', var_name='genre', value_name='gross')

# # Display chart
# chart = alt.Chart(df_chart).mark_line().encode(
#             x=alt.X('year:N', title='Year'),
#             y=alt.Y('gross:Q', title='Gross earnings ($)'),
#             color='genre:N'
#             ).properties(height=320)
# st.altair_chart(chart, use_container_width=True)
