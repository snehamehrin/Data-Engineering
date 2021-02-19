

spark-submit --jars RedshiftJDBC42-no-awssdk-1.2.20.1043.jar --packages org.apache.spark:spark-avro_2.11:2.4.3,com.databricks:spark-redshift_2.11:2.0.1  stack-processing.py