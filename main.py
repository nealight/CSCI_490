import scrape
import analyzer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tweet_scrapper = scrape.Scrape()
    df = tweet_scrapper.scrape_data(2020, 2021)

    tweet_analyzer = analyzer.Analyzer(df)
    tweet_analyzer.analyze()



    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
