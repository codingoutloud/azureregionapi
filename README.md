# Azure Region API #

Simple API that returns the Windows Azure Region name associated with a provided IP address.

## Main Site ##

https://azureregionapi.azurewebsites.net

## API Usage ##

### GET Request: ###

https://azureregionapi.azurewebsites.net/regions/__*<ip-address\>*__

### Response if Found (HTTP 200, application/json): ###

{ region: '__*region name*__' }

### Response if Not Found (HTTP 404, application/json): ###

{ region: '<unknown\>' }

## API Example ##

### Request: ###

https://azureregionapi.azurewebsites.net/regions/137.116.184.4

### Response (HTTP 200, application/json): ###

{ region: 'uswest' }

