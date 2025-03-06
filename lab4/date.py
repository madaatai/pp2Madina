import datetime 

def FiveDaysAgo():
    today = datetime.date.today()
    five_days_ago = today - datetime.timedelta(days=5)
    return five_days_ago


def YesterdayTodayTomorrow():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    return yesterday, today, tomorrow



def delete_microseconds():
    def drop_microseconds(dt):
        return dt.replace(microsecond=0)

    now = datetime.datetime.now()
    print(f'Original datetime {now}')

    without_microseconds = drop_microseconds(now)
    print(f'Withoud microseconds {without_microseconds}')


def seconds_dif(date1_str, date2_str):
    date_format = '%Y-%m-%d'

    date1 = datetime.datetime.strptime(date1_str, date_format)
    date2 = datetime.datetime.strptime(date2_str, date_format)

    difference = date2 - date1

    return difference.total_seconds()