from urlextract import URLExtract
from collections import Counter
import pandas as pd
import matplotlib as plt
extractor = URLExtract()
def fetch_stats(selected_user, df0):

    if selected_user != 'Overall':
        df0 = df0[df0['users'] == selected_user]
    #fetching the number of messages. #
    number_of_messages = df0.shape[0]
    #fetching the number of words in messages, #
    words = []
    for message in df0['messages']:
            words.extend(message.split())
    #fetching the number of media messages. #
    number_of_media_messages = df0[df0['messages'] == '<Media omitted>\n'].shape[0]
    #fetching number of links that are shared. #
    links = []
    for message in df0['messages']:
         links.extend(extractor.find_urls(message))
    
    return number_of_messages, len(words), number_of_media_messages, len(links)

def most_active_users(df0):
    a = df0['users'].value_counts()
    df1 = round((df0['users'].value_counts()/df0.shape[0]*100)).reset_index().rename(columns={'index':'Names', 'users':'percentage'})
    return a, df1

def most_common_words(selected_user, df0):
    if selected_user != 'Overall':
        df0 = df0[df0['users'] == selected_user]

    df2 = df0[df0['users'] != 'Group_notification']
    df2 = df2[df2['messages'] != '<Media omitted>\n']
    
    words = []

    for message in df2['messages']:
        words.extend(message.split())

    
    most_common_words = pd.DataFrame(Counter(words).most_common(20))
    return most_common_words

         
