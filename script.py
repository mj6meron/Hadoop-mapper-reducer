from pyhadoop import Hadoop

hadoop = Hadoop()

# Set the input and output paths for the job
input_path = 'hdfs://email_dataset/emails.csv'
output_path = 'hdfs://email_dataset/x.txt'

# Set the paths for the mapper and reducer scripts
mapper_path = '/home/hadoop/email_data/mapper.py'
reducer_path = '/home/hadoop/email_data/reducer.py'

# Run the job
hadoop.streaming(input_path, output_path, mapper_path, reducer_path)
