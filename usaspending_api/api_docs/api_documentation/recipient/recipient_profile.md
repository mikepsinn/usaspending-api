FORMAT: 1A
HOST: https://api.usaspending.gov

# Recipient Profile

These endpoints are used to power USAspending.gov's recipient profile pages. This data can be used to visualize the government spending that pertains to a specific recipient.

# Group Profile Page

These endpoints support the individual Recipient Profile pages that display data for a specific DUNS.

## Recipient Overview [/api/v2/recipient/duns/{recipient_id}/{?year}]

This endpoint returns a high-level overview of a specific recipient, given its id.

+ Parameters
    + `recipient_id`: `0036a0cb-0d88-2db3-59e0-0f9af8ffef57-C` (required, string)
        A unique identifier for the recipient at a specific level (parent, child, or neither). Note that the `recipient_id` must include a `recipient_level` suffix (i.e. `-C`, `-P`, `-R`)
    + year: `2017` (optional, string)
        The fiscal year you would like data for. Use `all` to view all time or `latest` to view the latest 12 months.

### Get Recipient Overview [GET]

+ Sample Request: `/api/v2/recipient/duns/543ee6af-9096-f32a-abaa-834106bead6a-P/?year=latest`

+ Response 200 (application/json)
    + Attributes (RecipientOverview)
    
## Recipient Children [/api/v2/recipient/children/{duns}/{?year}]

This endpoint returns a list of child recipients belonging to the given parent recipient DUNS.

+ Parameters
    + duns: `001006360` (required, string)
        Parent recipient's DUNS.
    + year: `2017` (optional, string)
        The fiscal year you would like data for. Use `all` to view all time or `latest` to view the latest 12 months.

### Get Recipient Children [GET]

+ Sample Request: `/api/v2/recipient/children/004027553/?year=all`

+ Response 200 (application/json)
    + Attributes (array[ChildRecipient], fixed-type)

# Data Structures

## RecipientOverview (object)
+ name: The ABC Corporation (required, string, nullable)
    Name of the recipient. `null` when the name is not provided.
+ duns: `001006360` (required, string, nullable)
    Recipient's DUNS (Data Universal Numbering System) number. `null` when no DUNS is provided.
+ `recipient_id`: `0036a0cb-0d88-2db3-59e0-0f9af8ffef57-C` (required, string)
    A unique identifier for the recipient.
+ `parent_name`: The XYZ Corporation (required, string, nullable)
    Parent recipient's name. `null` if the recipient does not have a parent recipient.
+ `parent_duns`: `001006361` (required, string, nullable)
    Parent recipient's DUNS number. `null` if the recipient does not have a parent recipient, or the parent recipient's DUNS is not provided.
+ `parent_id`: `0036a0cb-0d88-2db3-59e0-0f9af8ffef57-P` (required, string, nullable)
    A unique identifier for the parent recipient. `null` if the recipient does not have a parent recipient.
+ location: (required, RecipientLocation, fixed-type)
+ `business_types`: `minority_owned_business`, `for_profit_organization` (required, array[string], fixed-type)
    An array of business type field names used to categorize recipients.
+ `total_transaction_amount`: 30020000000 (required, number)
    The aggregate monetary value of all transactions associated with this recipient for the given time period.
+ `total_transactions`: 327721 (required, number)
    The number of transactions associated with this recipient for the given time period.
+ `recipient_level`: C (required, string)
    A letter representing the recipient level. `R` for neither parent nor child, `P` for Parent Recipient, or `C` for child recipient. 
    + Members
        + R
        + P
        + C

## RecipientLocation (object)
+ `address_line1`: 123 Sesame St (required, string, nullable)
    The first line of the recipient's street address. 
+ `address_line2`: (required, string, nullable)
    Second line of the recipient's street address. 
+ `address_line3`: (required, string, nullable)
    Third line of the recipient's street address. 
+ `foreign_province`: (required, string, nullable)
    Name of the province in which the recipient is located, if it is outside the United States.
+ `city_name`: McLean (required, string, nullable)
    Name of the city in which the recipient is located.
+ `county_name`: (required, string, nullable)
    Name of the county in which the recipient is located.
+ `state_code`: VA (required, string, nullable)
    Code for the state in which the recipient is located. 
+ zip: `22102` (required, string, nullable)
    Recipient's zip code (5 digits)
+ zip4: (required, string, nullable)
    Recipient's zip code (4 digits)
+ `foreign_postal_code`: (required, string, nullable)
    Recipient's postal code, if it is outside the United States.
+ `country_name`: (required, string, nullable)
     Name of the country in which the recipient is located.
+ `country_code`: USA (required, string, nullable)
     Code for the country in which the recipient is located.
+ `congressional_code`: `05` (required, string, nullable)
    Number for the recipient's congressional district. 
 
## ChildRecipient (object)
+ name: Child of ABC Corporation (required, string, nullable)
    Name of the child recipient. `null` if the child recipient's name is not provided.
+ duns: `001006360` (required, string, nullable)
    Child recipient's DUNS. `null` if the child recipient's DUNS is not provided.
+ `recipient_id`: `0036a0cb-0d88-2db3-59e0-0f9af8ffef57-C` (required, string)
    A unique identifier for the child recipient.
+ `state_province`: New Jersey (required, string, nullable)
    The state or province in which the child recipient is located.
+ amount: 300200000 (required, number)
    The aggregate monetary value of transactions associated with this child recipient for the selected time period.