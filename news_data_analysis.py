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
        order by count desc
        limit 1;
        '''

        print("\nSecond report: Who are the most popular"
              " article authors of all time?")
        result = self.fetch(query)
        print("%s - %s Views" % (result[0][0], str(result[0][1])))

    def over_one_percent_request_error_date(self):
        """This Function call the fetch function with query to find out
        On which days did more than 1% of requests lead to errors
        """
        query = '''select date(log.time) as DayDate,
        count(*) as NumRequest,
        log.status as status
        from   log
        group by (DayDate, status)
        order by DayDate;'''
        result = self.fetch(query)

        """
        loop on the results rows to count :
        1- number of good requests
        2- number of bad requests
        then count add them to get the total requests at that date
        finally get the error persentage by multiply the bad requests with 100
        then divided over the total number of requests

        check if it is over 1 we print that date and the error persentage

        """

        for counter in range(0, len(result), 2):
            goodRequest = result[counter]
            badRequest = result[counter + 1]
            numGoodRequests = goodRequest[1]
            numBadRequests = badRequest[1]
            totalRequests = numGoodRequests + numBadRequests
            badRequestsPrecentage = (numBadRequests * 100.0 / totalRequests)
            if badRequestsPrecentage > 1:
                print(
                    "\nThird report: On which days did more than 1%"
                    "of requests lead to errors?")
                print("%s - %s%% errors" % (result[counter][0].strftime(
                    "%b %d, %Y"), str(round(badRequestsPrecentage, 2))))


news_data_analysis = News_Data_Analysis()

news_data_analysis.most_three_popular_articles()

news_data_analysis.most_popular_authors()

news_data_analysis.over_one_percent_request_error_date()
