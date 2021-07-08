# solr-install load data from database ( ok test )

## 1. edit file location => C:\solr-8.2.0\server\solr\db\conf\solrconfig.xml
```
<requestHandler name="/dataimport" class="org.apache.solr.handler.dataimport.DataImportHandler">
  <lst name="defaults">
    <str name="config">db-data-config.xml</str>
  </lst>
</requestHandler>
```
### add driver connector
```
<lib dir="${solr.install.dir:../../../..}/dist/" regex="solr-dataimporthandler-.*\.jar" />
<lib dir="${solr.install.dir:../../../..}/dist/" regex="mysql-connector-java-5.1.24-bin.jar" />
<lib dir="${solr.install.dir:../../../..}/dist/" regex="postgresql-42.2.22.jar" />
```

## 2. file => C:\solr-8.2.0\server\solr\db\conf\db-data-config.xml

```
<dataConfig>
	<dataSource type="JdbcDataSource" encoding="UTF-8" name="imdb-title-rating" driver="org.postgresql.Driver" url="jdbc:postgresql://192.168.6.150:5432/weightdb" user="postgres" password="postgres" />
	<document>
		<entity pk="id" dataSource="sql" name="post" query="SELECT id, weight, price, card FROM weightdb.public.order;">
			<field column="id" name="id" />
			<field column="weight" name="weight" />
			<field column="price" name="price"/>
			<field column="card" name="card"/>
		</entity>
	</document>
</dataConfig> 
```


## 3. file => C:\solr-8.2.0\server\solr\db\conf\managed-schema
```
<field name="id" type="string" multiValued="false" indexed="true" required="true" stored="true"/>  
<field name="weight" type="string" indexed="true" stored="true"/>
<field name="price" type="string" indexed="true" stored="true"/>
<field name="card" type="string" indexed="true" stored="true"/>

```

## 4. place file connector dist folder

```
C:\solr-8.2.0\dist\postgresql-42.2.22.jar

```


## start service
```
C:\solr-8.2.0>bin\solr start
Java HotSpot(TM) 64-Bit Server VM warning: JVM cannot use large page memory because it does not have enough privilege to lock pages in memory.
Waiting up to 30 to see Solr running on port 8983
Started Solr server on port 8983. Happy searching!
```
## stop service
```
C:\solr-8.2.0>bin\solr stop -all
Stopping Solr process 3084 running on port 8983

Waiting for 0 seconds, press a key to continue ...
```
