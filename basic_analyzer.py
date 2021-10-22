import csv
def analyse(year):  
    
    filename = "td_dataset_" + year +".csv"
    fields = []
    rows = []
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            rows.append(row)
        
    user_id_col = fields.index('user_id')
    lang = fields.index('language')
    mention = fields.index('mentions')
    url = fields.index('urls')
    photo = fields.index('photos')
    reply = fields.index('replies_count')
    retweet = fields.index('retweets_count')
    like = fields.index('likes_count')
    hashtag = fields.index('hashtags')

    unique_user = set()
    unique_lang = set()
    total_mention = 0
    ave_mention = 0.0
    with_mention = 0
    total_url = 0
    ave_url = 0.0
    with_url = 0 
    with_photo = 0
    replies = 0
    with_reply = 0
    retweets = 0
    with_retweet = 0
    likes = 0
    with_like = 0
    hashtags = 0
    with_hashtag = 0
    for row in rows:
        unique_user.add(row[user_id_col])
        unique_lang.add(row[lang])
        c = row[mention].count('screen_name')
        total_mention += c
        with_mention += 1 if c > 0 else 0
        c = row[url].count('http')
        total_url += c
        with_url += 1 if c > 0 else 0
        with_photo += 1 if row[photo].count('http') > 0 else 0
        r = int(row[reply])
        replies += r
        with_reply += 1 if r > 0 else 0
        r = int(row[retweet])
        retweets += r
        with_retweet += 1 if r > 0 else 0
        r = int(row[like])
        likes += r
        with_like += 1 if r > 0 else 0
        hashtags += len(row[hashtag].split(',')) if len(row[hashtag]) > 2 else 0
        with_hashtag += 1 if len(row[hashtag]) > 2 else 0
    ave_mention = float(total_mention)/float(len(rows))
    ave_url = float(total_url)/float(len(rows))

    # print(len(unique_user), len(unique_lang), total_mention, ave_mention, with_mention, total_url, ave_url, with_url, with_photo, with_reply, with_retweet, with_like, with_hashtag)

    # import csv
    # writer.writerow([len(unique_user), len(unique_lang), total_mention, ave_mention, with_mention, total_url, ave_url, with_url, with_photo, with_reply, with_retweet, with_like, with_hashtag])      
    output_name = 'combined_exploratory_analysis.csv'
    with open(output_name, mode='a') as explore_file:
        writer = csv.writer(explore_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([year, len(rows), len(unique_user), len(unique_lang), total_mention, ave_mention, with_mention, total_url, ave_url, with_url, with_photo, with_reply, with_retweet, with_like, with_hashtag])
  
output_name = 'combined_exploratory_analysis.csv'
with open(output_name, mode='w') as explore_file:
    writer = csv.writer(explore_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['year','# of tweets','# of unique users', '# of unique languages', 'total # of mentions', 'average mentions/tweet', '# of tweets with mentions', 'total # of urls', 'average urls/tweet', '# of tweets with urls', '# of tweet with photots', '# of tweet with replies', '# of tweet with retweets', '# of tweet with likes', '# of tweet with hashtags'])
        
for year in ['2008', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']:
    analyse(year)
