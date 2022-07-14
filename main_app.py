import streamlit as st


st.title('Moje prvni appka')



page = st.sidebar.radio('Select page', ['Test', 'Thomson'])

if page == 'Test':
    st.write('Toto je moje prvni aplikace, kteru delam. Dalsi radky budou super COOL!')

if page == 'Thomson':
    st.write('Thomson sampling')
