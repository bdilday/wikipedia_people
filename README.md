# wikipedia_people

A Python script to collect data on influential people from wikipedia. The purpose is to programatically generate a data set similatr to the one used in this Wait But Why blog post (horizontal history):
 http://waitbutwhy.com/2016/01/horizontal-history.html

Currently it collects length of a persons wikipedia entry, the number of links that point to their page, and the year of their demise. A possible next step is to parse the categories in more detail, i.e. artist, scientist, politician, etc... or to apply PageRank, similar to this http://arxiv.org/abs/1405.7183

The data are written as csv files with out a header, and columns length of article, number of links to the article, number of links to article originating from a page (i.e not a forum, etc...), year of birth, year of demise, title of article (i.e. name or description of person)

An example bash command to take top 10 by inward links:

```
$ cat data/*csv | sed 's/,/ /g' | awk '{print $3, $0}' | sort -nr | head -10
```
