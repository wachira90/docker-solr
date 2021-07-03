# solr data import from database 

1. Update solrconfig.xml to create the “dataimport" request handler, and enable Solr to read custom JARs posted in contrib/dataimporthandler/lib folder.
Add following tags under the <config> tag so that Solr picks up the Custom JARs

```

<lib dir="${solr.install.dir:../../../..}/contrib/dataimporthandler/lib" regex=".*\.jar" />
<lib dir="${solr.install.dir:../../../..}/dist/" regex="solr-dataimporthandler-.*\.jar" />

```

Define /dataimport request handler

```
<!– A request handler for data import handler –>
<requestHandler name="/dataimport" class="org.apache.solr.handler.dataimport.DataImportHandler">
  <lst name="defaults">
    <str name="config">data-config.xml</str>
  </lst>
</requestHandler>
```

2. Create data-config.xml file in the same folder as solrconfig.xml, this file will contain the connection string, the query to get data, and the details about incoming fields.

```
<dataConfig>
  <dataSource type="JdbcDataSource" name="imdb-title-rating" driver="org.postgresql.Driver" url="jdbc:postgresql://127.0.0.1:5432/imdb" user="postgrestest" password="test" />
  <document name="title_rating">
    <entity name="rating" query="SELECT * FROM title_ratings;">
      <field column="tconst" name="tconst" />
      <field column="averagerating" name="averageRating" />
      <field column="numvotes" name="numVotes" />
    </entity>
  </document>
</dataConfig>
```

3. Edit managed-schema file, or if it doesn’t exist, then create schema.xml file. The incoming fields defined in Step 2 need to be made recognizable by Solr. Every incoming field needs to be map it to the Solr   recognizable datatype, so that it can parse the data.

When editing managed-schema file, then add the fields defined above –
```
<field name="tconst" type="string" indexed="true" stored="true" />
<field name="averageRating" type="tint" indexed="true" stored="true" />
<field name="numVotes" type="int" indexed="true" stored="true" />
<field name="id" type="string" indexed="true" stored="true" multiValued="false" />
```


4.Download and copy jdbc driver jar for postgres to “contrib/dataimporthandler/lib" folder

```
https://jdbc.postgresql.org/download/postgresql-42.2.22.jar
  
https://jdbc.postgresql.org/download/postgresql-42.2.2.jar
```
  
  
****
TIP :
  
Only Windows Server 2003 supports large page memory. In order to use it, the administrator must first assign additional privilege to the user who will be running the application:
  
1. select Control Panel -> Administrative Tools -> Local Security Policy 
2. select Local Policies -> User Rights Assignment 
3. double click "Lock pages in memory", add users and/or groups 
4. reboot the machine
  
****
