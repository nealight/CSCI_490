import twint
import pandas
import os
import glob

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

        extension = 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
        # combine all files in the list
        combined_csv = pandas.concat([pandas.read_csv(f) for f in all_filenames])
        # export to csv
        combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

        return tweets_df

        # print(tweets_df)