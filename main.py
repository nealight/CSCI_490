import twint
import pandas

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for year in range(2005, 2022):
        # Configure
        c = twint.Config()
        c.Search = (f"td OR technical debt")
        c.Year = year
        c.Limit = 1000
        c.Pandas = True
        c.Pandas_clean = True
        c.Store_csv = True
        c.Output = f"./td_dataset_{year}.csv"

        twint.run.Search(c)
        tweets_df = twint.storage.panda.Tweets_df

    # print(tweets_df)

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
