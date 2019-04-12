# the news_data_analysis class is working 
# on newsdata.sql Database to analyse the huge data 
# to smaller reports which is easy to read,
# the news_data_analysis contains three methods 
# 1 -
# 2 -
# 3 -


import psycopg2

class News_Data_Analysis:
      
      Database_Name = "dbname=news"
      
      def most_three_popular_articles(self):
          news_database = psycopg2.connect(database= self.Database_Name)
          database_cursor = news_database.cursor()
          database_cursor.execute("select content, time from posts order by time desc")
          most_three_popular_articles = database_cursor.fetchall()
          news_database.close()
          return most_three_popular_articles

      def most_popular_authors(self):
          news_database = psycopg2.connect(database= self.Database_Name)
          database_cursor = news_database.cursor()
          database_cursor.execute("select content, time from posts order by time desc")
          most_popular_authors = database_cursor.fetchall()
          news_database.close()
          return most_popular_authors   
      
      def over_one_percent_request_error_date(self):
          news_database = psycopg2.connect(database= self.Database_Name)
          database_cursor = news_database.cursor()
          database_cursor.execute("select content, time from posts order by time desc")
          over_one_percent_request_error_date = database_cursor.fetchall()
          news_database.close()
          return over_one_percent_request_error_date

news_data_analysis = News_Data_Analysis()

print(news_data_analysis.most_three_popular_articles()) 

            
    