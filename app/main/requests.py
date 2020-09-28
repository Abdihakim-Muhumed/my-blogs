import urllib.request,json
from ..models import Quote

get_quote_url=""
def configure_request(app):
    get_quote_url=app.config['QUOTES_URL']

def get_quote():
    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)

        quote_results =None
        if get_quote_response["quote"]:
            quote_results_list = get_quote_response["quote"]
            quote_results = process_quote_results(quote_results_list)


    return  quote_results

def process_quote_results(quote_list):
    '''function to process results and create Quote object
    '''
    quote_results = []
    for  quote in  quote_list:
        id =  quote.get('id')
        quote =  quote.get('quote')
        author =  quote.get('author')

        quote_object =  Quote(id,quote,author)
        quote_results.append( quote_object)


    return  quote_results