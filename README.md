# django-pdd-rest-api
This repository is an interview exercise implemention in DJango.

## Used libraries
- django 3.2.3
- djangorestframework 3.12.4
- requests 2.25.1
- drf-yasg 1.20.0
- mock 4.0.3


## The original description

We would like you to develop a REST API for a fictional client “FooBar Inc”. FooBar Inc need a
REST API for accessing House Price Paid Data (PPD).
The raw data can be found, for free, as a CSV file here:
https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads.

### The Story
As a developer at FooBar Inc.
I want to access house price paid records in JSON format via a REST API
So that I can build an automated system using this data
Acceptance Criteria
- A list of all records is returned in JSON format via the REST API
- A single record is returned in JSON format when its ID is provided
- A list of purchase records made in a specified time range is returned in JSON format
when a date time range is provided

## Solution
This section is aiming to describing the technical analysis of the task. 
 
### Discovery of the source data
Data of House Price Paid records are available in CSV format. From the www.gov.uk we can download the following data:

- Current Monthly subset of PPD ( [link](http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update-new-version.csv) )
- Full year PPD (e.g: 2021 -> [link](http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021.csv) )
- Half year of PPD data ( e.g: 2021 part1 -> [link](http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2021-part1.csv) )
- All the registered PPD data since 2018 ( [link](http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-complete.csv) )

The CSV record field descriptions are available here: https://www.gov.uk/guidance/about-the-price-paid-data?fbclid=IwAR0FxqBOGDmWEYAF4vb106jzuKyKroj419qMkx_YFcmo4MHhn-aP_Nbvdnk

### CSV handling

The available CSV files above are huge, therefore handling them and exposing in REST API required some advanced technical skills.
In this implementation I have solved the CSV handling by evaluating records one by one via Java Streams, and used API response paging described in Paging & HATEOAS section.

## Usage of the PPD API

Swagger and Swagger UI also implemented in the API and available under ``` http://<host>:<port>/swagger/ ```


### Build & Run

You can the API, just like every other Django application by simply executing the following command: 
```
python manage.py runserver <port_of_your_choice>

```

To run the tests run this command: 
```
python manage.py test --settings=house_price_paid_data_search.test_settings
```
It is important to override the settings, otherwise the application will not use the mocked sample data and will produce invalid test results

### Repository options

Based on the source data analysis I have provided two different backend approach.
Please note that both repository requires a valid url (either local or remote) in the ```CSV_DATA_LOCATION``` property the ```settings.py```

1. #### Real-Time CSV proxy: 
   
   With this repository you are able to download and query the csv available www.gov.uk. By default, it is pointing to the latest monthly csv (http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update.txt), but you can specify any other the valid HTTP resource on the ```CSV_DATA_LOCATION```.
   
    For example: 
   ```python
   CSV_DATA_LOCATION = 'http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-monthly-update.txt'
   ```
   
   In case of using real-time repository every API request will download the csv above and do the filtering on the downloaded result. To use Real-Time repository to have to set up the ```PricePaidDataRepository``` Bean like this:
    To use real-time proxy repository to have to specify the full class name in the ```REPOSITORIES``` property in ```settings.py``` like this:
   ```python
   REPOSITORIES = {
        'CSV_REPOSITORY' : 'house_price_paid_data_search.repositories.RealTimeLatestCsvPpdRepository'
   }
   ```
   
2. #### File system cached repository:
    
    This repository is designed to handle big CSV files stored in the local filesystem. To use this repository you have to set the location of the CSV file via the ```data.ppd.localUri```  property.
    In this case the value of ```CSV_DATA_LOCATION``` have to be a valid file path on your local file system. 
   
    For example: 
   ```python
   CSV_DATA_LOCATION = 'C:/Users/oarga/Downloads/pp-complete.csv'
   ```
   With this repository you can download and store all the PPD data available at www.gov.uk.
   To use file system cached repository to have to specify the full class name in the ```REPOSITORIES``` property in ```settings.py``` like this:
   ```python
   REPOSITORIES = {
        'CSV_REPOSITORY' : 'house_price_paid_data_search.repositories.FileSystemCachedCsvPpdRepository'
   }
   ```


### Paging in Response

The CSV database is too big to serve the whole content on the endpoint in one HTTP response. To solve this issue, the API is using giving back only a subset of the CSV (pages) and providing links to the next and previous subsets.
This is behaviour is called paging in this terminology. The paging implementation can be useful to create reactive frontend for the API. For example requesting the all records will give you the following result:

```json
{
    "paging": {
        "page_number": 3,
        "start_record": 1,
        "end_record": 2,
        "next_page": "http://localhost:8000/ppd/?pageNo=2",
        "prev_page": "http://localhost:8000/ppd/?pageNo=4"
    },
    "price_paid_data": [
        {
            "id": "BEF7EBBE-9F40-7A76-E053-6B04A8C092F7",
            "price": "201000.00",
            "date_of_transfer": "2006-07-28 00:00",
            "post_code": "WA16 6DQ",
            "property_type": "T",
            "old_or_new": "N",
            "duration": "F",
            "paon": "3",
            "saon": "",
            "street": "CHURCH VIEW",
            "locality": "",
            "city": "KNUTSFORD",
            "district": "CHESHIRE EAST",
            "county": "CHESHIRE EAST",
            "category": "A",
            "status": "A"
        },
        {
            "id": "BEF7EBBE-C451-7A76-E053-6B04A8C092F7",
            "price": "216000.00",
            "date_of_transfer": "2006-07-26 00:00",
            "post_code": "E1W 3TU",
            "property_type": "F",
            "old_or_new": "N",
            "duration": "L",
            "paon": "11",
            "saon": "FLAT 112",
            "street": "NEW CRANE PLACE",
            "locality": "",
            "city": "LONDON",
            "district": "TOWER HAMLETS",
            "county": "GREATER LONDON",
            "category": "A",
            "status": "A"
        }
    ]
}
```

Size of the pages is 50 record by default, but it you can override via  ```PAGE_SIZE ``` the Django settings file:

    
### Future improvements

- [ ] Repository change wiring to application property
- [ ] Debug logging
- [ ] Maintaining current number of records on CSV
- [ ] Extend with ETL application (via Spring Batch) to keep the filesystem CSV up to date
- [ ] Implement API security (OAuth Client Credentials and/or API-Key & Secret)
- [ ] Integrate CSV handling into the DJango ORM, via model method overrides or custom db driver implementation
- [ ] Implement indexing feature to decrease random access response time

