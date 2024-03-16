import streamlit as st
from pages.finance_tracker_data.finance import PersonalFinance
import pages.finance_tracker_data.markdown as md
from csv import writer
from datetime import datetime
df = PersonalFinance()
 
PAGE_CONFIG = {"page_title":"Personal Finance", 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)   

st.sidebar.markdown("## Options")
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'Window 1', 'Window 2', 'Window 3'])
 
if sidebar_main == 'Home' : 
    st.title('Personal Finance Dashboard')

    banner = md.headerSection()
    st.markdown(banner,unsafe_allow_html=True)
    
    st.markdown("""
    ## Enter Expense :  
    """)
    #item_date = st.date_input("Enter date of expense : ")
    now = datetime.now()
    item_date = now.strftime("%m/%d/%Y")
    print(item_date)
    
    option = st.selectbox(
     'Choose type of expense: ',
     ('Charity', 'Clothes', 'Food','Medicine','Study Materials','Travel',"Utilities","Wants"))
    item_title = st.text_input("Enter name of expense : ")
    item_price = st.number_input("Enter cost of expense : ")
    submit = st.button("Submit")
    L = [item_date,option,item_title,item_price]
    print(L)

    if submit:
        with open('pages/data/data  - item.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(L)
            f_object.close()
            print("Written da data")
        


 
elif sidebar_main == 'Window 1' : 
    st.title('Expense dashboard')
    sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category', 'boxplot', 'total expenses', 'treemap'])
    
    data = df.preprocess_dataframe().tail()

    st.markdown(
            """
            ##### After preprocessing the data looks like this
            """
        )
    st.dataframe(data.head())
    if sidebar_sub == 'Window 2' : 

        st.markdown(
            """
            ##### Check the expenses 
            """
        ) 
        
        col1, col2 = st.columns(2)
        with col1 : 
            daily = st.button('Daily') 

        with col2 :  
            monthly = st.button('Monthly')
        
        if monthly : 
            st.plotly_chart(df.plot_expenses('month')[0])
            percent = df.plot_expenses('month')[1]

            if percent > 0 : 
                st.write('which is ',percent,'%',' higher than prev month')
            else : 
                st.write('which is ',abs(percent),'%',' lower than prev month')

        else : 
            st.plotly_chart(df.plot_expenses('date'))

    elif sidebar_sub == 'Category' :
        st.markdown(
            """
            ##### Category wise expenses 
            """
        ) 
        st.plotly_chart(df.share_of_category())

    elif sidebar_sub == 'boxplot' : 
        st.markdown(
            """
            ##### Category wise boxplot 
            """
        ) 
        col1, col2, col3 = st.columns(3)
        with col1 : 
            food = st.button('food') 

        with col2 :  
            travel = st.button('travel')
        
        with col3 :  
            wants = st.button('wants')

        if travel :
            st.plotly_chart(df.plot_boxplot('travel'))
        if wants :
            st.plotly_chart(df.plot_boxplot('wants'))
        else: 
            st.plotly_chart(df.plot_boxplot('food'))

    elif sidebar_sub == 'total expenses' : 
        st.markdown(
            """
            ##### Total Expenses 
            """
        ) 
        st.plotly_chart(df.total_spending()[0])
        st.write('Total amount spent is ',df.total_spending()[1])

    else : 
        st.markdown(
            """
            ##### Spending on items 
            """
        ) 
        st.plotly_chart(df.plot_treemap())

elif sidebar_main == 'Window 3' : 
    st.markdown(
            md.aboutpage()
        ) 

else : 
    # dropdown
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on food :')
    with col2 :
        check = st.button('check', key = 1)
    
    if check : 
        st.write('I ate ', df.find_max('food')[0], ' on ', df.find_max('food')[2].date(), ' with ', df.find_max('food')[1])
    
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on travel :')
    with col2 :
        check = st.button('check', key = 2)
    
    if check : 
        st.write('I used ', df.find_max('travel')[0], ' on ', df.find_max('travel')[2].date(), ' for ', df.find_max('travel')[1])

    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on wants :')
    with col2 :
        check = st.button('check', key = 3)
    
    if check : 
        st.write('I have spent on ', df.find_max('wants')[0], ' on ', df.find_max('wants')[2].date(), ' for ', df.find_max('wants')[1])

footer = md.footerSection()
st.markdown(footer,unsafe_allow_html=True) 