import streamlit as st
import matplotlib.pyplot as plt
import preprocessor, helper

st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df0 = preprocessor.preprocessor(data)
    st.dataframe(df0)

    #fetching unique users. #
    users_list = df0['users'].unique().tolist()
    users_list.remove('Group_notification')
    users_list.sort()
    users_list.insert(0, "Overall")

    selected_user = st.sidebar.selectbox("Showing anlysis with respect to ", users_list)

    if st.sidebar.button("Show analysis"):
        number_of_messages, words, number_of_media_messages, number_of_links = helper.fetch_stats(selected_user, df0)

        col1, col2, col3, col4 = st.beta_columns(4)

        with col1:
            st.header("Total messages")
            st.title(number_of_messages)
        with col2:
            st.header("Total words")
            st.title(words)
        with col3:
            st.header('Total media shared')
            st.title(number_of_media_messages)
        with col4:
            st.header("Total number of links shared")
            st.title(number_of_links)

        #fetching the person who was the most active participant on whatsapp. #
        if selected_user == "Overall":
            st.title("Most active Participants")
            a,new_df = helper.most_active_users(df0)
            fig, ax = plt.subplots()
            col1, col2 = st.beta_columns(2)

            with col1:
                ax.bar(a.index, a.values)
                plt.xticks(rotation = 'vertical')
                plt.xlabel('Names')
                plt.ylabel('Most messages')
                st.pyplot(fig)
            with col2:
                st.dataframe(new_df)

            #most common words
            most_common_words = helper.most_common_words(selected_user, df0)
            st.dataframe(most_common_words)
    