# using python 2.7
# conforms to PEP8

# the news_data_analysis class is working
# on newsdata.sql Database to analyse the huge data
# to smaller reports which is easy to read,
# the news_data_analysis contains three methods
# 1 - most_three_popular_articles
# 2 - most_popular_authors
# 3 - over_one_percent_request_error_date

import psycopg2
import datetime


class News_Data_Analysis:
    # store the database name as class atribute
    Database_Name = "news"

    def fetch(self, query):
        """This function connect to the DB, execute the query, and returns the results
        Arguments:
            query {String} -- the query should be executed
        Returns:
            [array] -- [the array of fetching rows]
        """

        news_database = psycopg2.connect(database=self.Database_Name)
        database_cursor = news_database.cursor()
        database_cursor.execute(query)
        result = database_cursor.fetchall()
        news_database.close()
        return result

    def most_three_popular_articles(self):
        """This Function call the fetch function with query to find out
        the most popular three articles of all time
        """
        query = '''select articles.title as Article_Name , count(*) as Views_Count
        from log
        right join articles on log.path = concat('/article/', articles.slug)
        where log.status = '200 OK'
        group by articles.title
        order by count(*) desc
        limit 3;'''

        print("\nFirst report: What are the most popular"
              " three articles of all time?")

        result = self.fetch(query)
        for record in result:
            print("\" %s \" - %s Views" % (record[0], str(record[1])))

    def most_popular_authors(self):
        """This Function call the fetch function with query to find out
        Who are the most popular article authors of all time
        """
        query = '''select authors.name, count(*)
        from log, articles, authors
        where log.status = '200 OK' and log.path = concat('/article/',
        articles.slug) and articles.author = authors.id
        group by authors.name
        order by count desc;
        '''

        print("\nSecond report: Who are the most popular"
              " article authors of all time?")
        result = self.fetch(query)
        # print("%s - %s Views" % (result[0][0], str(result[0][1])))
        for record in result:
            print("%s - %s Views" % (record[0], str(record[1])))

    def over_one_percent_request_error_date(self):
        """This Function call the fetch function with query to find out
        On which days did more than 1% of requests lead to errors
        """
        query = '''select date(log.time) as DayDate,
        count(*) as NumRequest,
        SUM(CASE WHEN log.status = '200 OK' THEN 1 ELSE 0 END) as good,
        SUM(CASE WHEN log.status = '200 OK' THEN 0 ELSE 1 END) as error,
        100.0*(SUM(CASE WHEN log.status = '200 OK' THEN 0 ELSE 1 END))/count(*)
        as ratio
        from log
        group by (DayDate)
        order by DayDate'''

        query = '''select DayDate,ratio
        from   ('''+query+''') as v
        where ratio >   1 '''
        results = self.fetch(query)
        print(
                    "\nThird report: On which days did more than 1%"
                    "of requests lead to errors?")

        for result in results:
            # print("Error in day ",result[0], "is", result[1])
            print("%s - %s%% errors" % (result[0].strftime(
                    "%b %d, %Y"), str(round(result[1], 2))))

news_data_analysis = News_Data_Analysis()

news_data_analysis.most_three_popular_articles()

news_data_analysis.most_popular_authors()

news_data_analysis.over_one_percent_request_error_date()
