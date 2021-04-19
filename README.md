# End To End Analytics Pipeline using AWS & Einstein Analytics
 
**Overview**

This series is aimed at providing a comprehensive view on  **building**  ,**designing**  and  **developing**  an  **analytics\AI data pipeline**  for stack overflow using the  **AWS stack**  and finally build a dashboard in  **Einstein Analytics**.

Pipelines are the  **heart of analytics**  and ML and quite often this is the hardest part of an  **analytics or ML problem**. If you have a  **well designed pipeline,**  then half your battle is over.

1.  **_Introduction to Stack Overflow and Business Requirements._**
2.  [**_Technical Design Architecture For an Analytics Pipeline_**](https://medium.com/p/fe14643c67fd)**_._**
3.  [**_Data Ingestion using Kinesis Firehose and boto3._**](https://medium.com/p/5fec529f2a51)
4.  [**_ETL and Data Processing Using Apache Spark on AWS EMR._**](https://medium.com/p/3e889784ba70)
5.  [**_Data Storage in Redshift._**](https://medium.com/p/6fd649f25854)
6.  [**_Einstein Analytics Data Prep & Dashboards_**](https://medium.com/p/18b4a5aa135b)**_._**

**Motivation**

End to End Analytics solutions are always a challenge. It's easier to build a dashboard from a CSV file. But building a live dashboard by streaming data and transforming it to the relevant form is quite difficult to achieve.
There are many technical considerations to be taken into account.

**Goal**

My Goal was to map out the thought process involved in creation of a full fledged analytical solution using AWS and Einstein Analytics.

**Tools Used**

* S3  as a data lake.
* Kinesis to stream stack over flow data.
* Apache Spark to process the data
* Redshift as a datawarehouse to store to transformed data.
* Einstein Analytics for Data Visualization.

**Technical Design Architecture**

-   **Kinesis Firehose**  is chosen to stream the data from stack api and output it to  **S3 bucket folder.**
-   **Spark** will batch process the streams from S3 on a daily basis and output the transformed data back to  **Redshift- This will be a script scheduled on ec2 once every day.**
-   **Einstein Analytics**  will use it native  **S3 connector**  to sync the data and display it in the  **dashboards- Dashboards will be refreshed everyday with the data of yesterday’s**

**Blog** 

Full Blog Post can be read here :

(https://medium.com/analytics-vidhya/building-an-end-to-end-analytics-pipeline-using-einstein-analytics-kinesis-spark-and-redshift-6d9fe1feb3c3)
