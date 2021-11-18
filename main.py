import scrape
import analyzer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tweet_scrapper = scrape.Scrape()
    df = tweet_scrapper.scrape_data(2010, 2021, True)

    # tweet_analyzer = analyzer.Analyzer(df)
    # tweet_analyzer.analyze()

    test_alpha = [0.01, 0.25, 0.5, 1.0, 2.0, 5.0, 'symmetric', 'asymmetric', 'auto']
    test_beta = [0.01, 0.25, 0.5, 1.0, 2.0, 5.0, 'symmetric', 'auto']

    for a in test_alpha:
        for b in test_beta:    
            tweet_analyzer = analyzer.Analyzer(df, "_alpha"+ str(a) + "_beta" + str(b))
            tweet_analyzer.analyze(a, b)

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
