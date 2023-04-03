import pandas as pd
import re
def preprocessor(data):
    pattern = "\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s"
    messages = re.split(pattern, data)[1:]
    dates = re.findall(pattern, data)

    df0 = pd.DataFrame({'users_messages':messages, 'messages_date': dates})
    #convert dates into date_type #
    df0['messages_date'] = pd.to_datetime(df0['messages_date'], format = '%d/%m/%Y, %H:%M - ')
    df0.rename(columns={'messages_date':'date'}, inplace=True)

    users = []
    messages = []
    for message in df0['users_messages']:
       entry = re.split('([\w\W]+?):\s', message)
       if entry[1:]:
         users.append(entry[1])
         messages.append(entry[2])
       else:
         users.append('Group_notification')
         messages.append(entry[0])
        
    df0['users'] = users
    df0['messages'] = messages
    df0.drop(columns = {'users_messages'}, inplace=True)
    df0.head(5)

    df0['year'] = df0['date'].dt.year
    df0['month'] = df0['date'].dt.month_name()
    df0['day'] = df0['date'].dt.day
    df0['hour'] = df0['date'].dt.hour
    df0['minutes'] = df0['date'].dt.minute
    
    return df0