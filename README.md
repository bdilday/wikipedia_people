# wikipedia_people

A Python script to collect data on influential people from wikipedia. The purpose is to programmatically generate a
data set similar to the one used in this Wait But Why blog post (horizontal history):

http://waitbutwhy.com/2016/01/horizontal-history.html

Currently it collects length of a persons wikipedia entry, the number of links that point to their page, and the year of their demise. A possible next step is to parse the categories in more detail, i.e. artist, scientist, politician, etc... or to apply PageRank, similar to this http://arxiv.org/abs/1405.7183

The data are written as csv files in the data directory. Each file is named by the year of birth, i.e.,
wiki_XXXX.csv, where XXXX is the year of birth for each person listed in the file. I did not include a header in the data
files in order to simplify
concatenation of the files.
There is an example header provided in the header.txt file in the data directory.

__Note:__ The name field sometime contains commas and double quotes which may cause probelsm with importing the csv files. I removed the extra commas in the all.csv file and am working on removing both commas and quotation marks from the individual year files.
  
`length,linkshere,pagelinkshere,year_birth,year_demise,name`

The column meanings are:
```
length: length of the article. Specifically, the page size property exposed by the wikipedia API.
linkshere: count of the wikipedia API property linkshere.
pagelinkshere: count of the wikipedia API property linkshere, filtered to include only other wikipedia pages.
               Some pages have lots of links from Talk or User pages, which are less relevant for determining
               cultural and historical significance, and this measure removes those.
year_birth: name says it all
year_demise:
name: title of the page. Usually this is the persons name, but sometimes has addition information, e.g.,
      William Smith (lexicographer)
```

The best way to assess cultural and historical significance from these data is debatable, but `pagelinkshere` is a reasonable default metric to use.
You can run the shell script `top10.sh` to get a list of the top 10, over all years, sorted by `pagelinkshere`, e.g.,
```
$ ./top10.sh
1889 1945 Adolf Hitler
1707 1778 Carl Linnaeus
1809 1865 Abraham Lincoln
1882 1945 Franklin D. Roosevelt
1874 1965 Winston Churchill
1819 1901 Queen Victoria
1732 1799 George Washington
1769 1821 Napoleon
1859 1926 Sidney Lee
1878 1953 Joseph Stalin
```

Optionally you may include the command line argument N to list the top N, e.g.,

```
$ ./top10.sh 20
1889 1945 Adolf Hitler
1707 1778 Carl Linnaeus
1809 1865 Abraham Lincoln
1882 1945 Franklin D. Roosevelt
1874 1965 Winston Churchill
1819 1901 Queen Victoria
1732 1799 George Washington
1769 1821 Napoleon
1859 1926 Sidney Lee
1878 1953 Joseph Stalin
1858 1919 Theodore Roosevelt
1890 1969 Dwight D. Eisenhower
1743 1826 Thomas Jefferson
1902 1983 Nikolaus Pevsner
1908 1973 Lyndon B. Johnson
1856 1924 Woodrow Wilson
1756 1791 Wolfgang Amadeus Mozart
1869 1948 Mahatma Gandhi
1685 1750 Johann Sebastian Bach
1818 1883 Karl Marx
```
