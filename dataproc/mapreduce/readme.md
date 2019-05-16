## MapReduce on DataProc

### Getting started

Lets run a simple mapreduce:

1. Get a cluster running, regular with one master and two data nodes
2. SSH into master node to inspect it
3. Change som firewall rules, open ports 8080, 8088 and 9870
4. Check out the master node on those ports. It should give us some familiar
   hadoop dashboards
5. Create a bucket for scripts and one for (input)data
6. Put the mapper and reduce scripts into the scripts bucket and data into
   input_data bucket. The input data is called itemData.txt here and contains
   columns `time, store, item, price, payment` seperated by spaces (which the
   mapper will split on)
7. Run the hadoop command on the master node:
```
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files gs://peakbreaker-tmp-data/mapr_scripts/mapper.py,gs://peakbreaker-tmp-data/mapr_scripts/reducer.py \
    -mapper 'python mapper.py' \
    -reducer 'python reducer.py' \
    -input gs://peakbreaker-tmp-data/mapr_data/itemData.txt \
    -output gs://peakbreaker-tmp-data/mapr_output
```

Each line of the input file is then read, the data is split into its parts and
a KV pair of interest is spit into stdout (i.e. printed out)
