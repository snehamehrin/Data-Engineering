

from pyspark.sql import SQLContext
from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import unix_timestamp, to_date, date_format, month, year, dayofyear, dayofweek, col
from pyspark.sql.types import TimestampType

from pyspark.sql import functions as F
from pyspark.sql import SparkSession
from pyspark.sql.functions import unix_timestamp, to_date, date_format, month, year, dayofyear, dayofweek, col
from pyspark.sql.types import TimestampType
from pyspark.sql.types import DateType
from datetime import datetime
from datetime import timedelta



def get_latest_file_name():
    """
    This function connects to s3 and get the latest file from the s3 bucket
    """
    Previous_Date = datetime.today() -timedelta(days=1)
    year=Previous_Date.strftime ('%Y')
    month=Previous_Date.strftime ('%m')
    day=Previous_Date.strftime ('%d')
    file_folder="s3://stack-overflow-bucket/StackOverFlow/year="+'{}'.format(year)+"/month="+'{:0>2}'.format(month)+"/day="+'{:0>2}'.format(day)+"*"
    return file_folder



spark = SparkSession.builder.appName('Stack Overflow ML').getOrCreate()
print('Session created')

sc = spark.sparkContext
sc._jsc.hadoopConfiguration().set("fs.s3n.awsAccessKeyId", )
sc._jsc.hadoopConfiguration().set("fs.s3n.awsSecretAccessKey", )

#Get the latest file from s3
filename=get_latest_file_name()
stack = sc.textFile(filename)
stack.take(5)
#Convert it into a dataframe
df = spark.read.json(stack)
df.show(5)



# %%
#Drop any duplicates if any
df_duplicates=df.dropDuplicates(['questionid'])
#Convert the UnixTimesStamp into time stamp
df_duplicates=df_duplicates.withColumn("creation_date", F.from_unixtime("creation_date", "yyyy-mm-dd"))


df_duplicates.write.format("com.databricks.spark.redshift")\
.option("url", "jdbc:redshift://redshift-cluster-1.c9lgtyzxfycf.us-east-1.redshift.amazonaws.com:5439/dev?user=&password=")\
.option("dbtable", "stackoverflow")\
.option("forward_spark_s3_credentials","true")\
.option("tempdir", "s3n://stack-overflow-bucket")\
.mode("append")\
.save()

++++