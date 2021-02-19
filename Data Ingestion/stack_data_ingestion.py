from stackapi import StackAPI
import setup
import boto3
import json


class Kinesis(object):
    def __init__(self, StreamName=None):
        self.StreamName = StreamName
        self.session = boto3.Session(profile_name='bigdata_demo')
        self.client = self.session.client('firehose', region_name='us-east-1')

    def get_kinesis_records(self):
        SITE = StackAPI('stackoverflow')
        key = setup.client_id
        SITE.page_size = 100
        SITE.max_pages =500
        questions = SITE.fetch('questions',order='desc')
        for quest in questions['items']:
            payload_lst = {'question_id': str(quest['question_id']),
                           'is_answered': str(quest['is_answered']),
                           'view_count': quest['view_count'],
                           'answer_count': quest['answer_count'],
                           'score': quest['score'],
                           'last_activity_date': quest['last_activity_date'],
                           'creation_date': quest['creation_date'],
                           }
            json_payload = json.dumps(payload_lst)
            json_payload_encode = json_payload.encode("utf-8")
            kinesis_record = {
                'DeliveryStreamName' : self.StreamName,
                'Record' : {
                    'Data': json_payload_encode
                            }

            }
            response = self.client.put_record(**kinesis_record )
            return response



def main():
    kinesis_helper = Kinesis(StreamName='stack-firehose-stream')
    aws_response =kinesis_helper.get_kinesis_records()
    print(aws_response)

if __name__ == "__main__":
    main()

