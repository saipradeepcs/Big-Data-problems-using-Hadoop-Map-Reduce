 #!/bin/bash
 hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -D mapred.reduce.tasks=50 -input /data/1gram -output $1 -file *.py -mapper wordcountmapper.py -reducer wordcountreducer.py
