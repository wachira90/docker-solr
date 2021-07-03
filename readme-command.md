# solr

## url 
```
http://localhost:8983/solr/
```

## start
```
bin\solr.cmd start 

bin\solr status

```

## Start Solr with a Specific Bundled Example "techproducts"
```
bin/solr -e techproducts
```

## create core
```
bin/solr create -c <name>
bin\solr config -c <name> -p 8983 -action set-user-property -property update.autoCreateFields -value false
```



## You can increase the memory by doing the following:
```
1. Open the {INSTALLDIR}\bin\solr\solr.in.cmd file in a text editor of your choice
2. Search for the following REM set SOLR_JAVA_MEM=-Xms512m -Xmx512m
3. You can copy paste the line or just remove the REM portion to allow a new value to be set
4. Replace the -Xms512m -Xmx512m value with the value you want (1GB would be -Xms1g -Xmx1g, 10GB would be -Xms10g -Xmx10g, etc)
5. Save the file and restart your Solr service for the new size to be applied.


or

SOLR_JAVA_MEM="-Xms10g -Xmx10g"

https://jdbc.postgresql.org/download/postgresql-42.2.2.jar

"contrib/dataimporthandler/lib"

```
