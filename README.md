# django-pdd-rest-api
This repository is an interview exercise implemention in DJango.

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

