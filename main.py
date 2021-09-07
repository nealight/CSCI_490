import twint
import pandas

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Configure
    c = twint.Config()
    c.Search = ("td OR technical debt")
    c.Limit = 1000
    c.Pandas = True
    c.Pandas_clean = True
    c.Store_csv = True
    c.Output = "./td_dataset.csv"

    twint.run.Search(c)
    tweets_df = twint.storage.panda.Tweets_df

    # print(tweets_df)

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
