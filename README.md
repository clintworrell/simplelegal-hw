# Running the project  
`git clone git@github.com:clintworrell/simplelegal-hw.git`  
`cd simplelegal-hw/simplelegalhw`  
`python manage.py runserver`  

Browse to http://localhost:8000/simplelegal/invoices/ (replace localhost:8000 with the correct address and port if your development server is running at a different location)

# Description of the project

* Once visiting the URL above you will see a list of all invoices that were retrieved from the invoices API endpoint and loaded into the local SQLite database.
* You'll notice that a reasonable, but somewhat arbitrary list of fields from the invoices are displayed.
* Using the "Search within results..." input you are able to search across all displayed fields to filter for the content you're looking for. The invoice list will dynamically update based on the search criteria. The total at the bottom of the Amount column will also dynamically update based on the same.
* You'll notice that 4 decimal places are displayed in the Amount column. When creating the Invoice model I chose 4 decimal places for some of the fields because some of the dollar amounts returned from the API had 4 decimal places (ie. the total amount for invoice number 198459150629). Not being familiar with the nature of your data I took that as my guideline.
* The entries in the Invoice Number column link to a view of the line items for that specific invoice number.
* Again, a reasonable, but somewhat arbitrary list of fields from the line items are displayed in that view.
