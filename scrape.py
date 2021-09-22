import twint
import pandas

class Scrape:

    def scrape_data(self, start:int, end:int) -> pandas.DataFrame:
        for year in range(start, end):
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

        return tweets_df

        # print(tweets_df)