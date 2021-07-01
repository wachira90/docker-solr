# docker-solr
docker-solr

## start and create core name "gettingstarted"

```
docker run --name solr -p 8983:8983 -t wachira90/solr:8.9.0 solr-precreate gettingstarted
```

## run command for load data to core name "gettingstarted"

```
docker exec -it  solr post -c gettingstarted example/exampledocs/manufacturers.xml
```

## single command demo
```
docker run --name solr_demo -d -p 8983:8983 solr:8 solr-demo
```

## create core
```
docker exec -it solr solr create_core -c gettingstarted

docker exec -it <conatiner_name> <bin_name_in_container> create_core -c gettingstarted

```
