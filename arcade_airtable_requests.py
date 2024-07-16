import requests
from nanoid import generate

cookies = {
    "X-Is-Automation": "Yes"
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://airtable.com/appOKDJk2ALKSisEM/shriBhjoCj83rYCGT',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '',
    'tracestate': '',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 UnofficialAirtableHack/1.0',
    'x-airtable-application-id': 'appOKDJk2ALKSisEM',
    'x-airtable-client-queue-time': '3.7999999970197678',
    'x-airtable-inter-service-client': 'webClient',
    'x-airtable-inter-service-client-code-version': '795bf53f3b63b1f1ad2535441463128959fd0e38',
    'x-airtable-page-load-id': 'pgl7G6QawhhAofZdZ',
    'x-requested-with': 'XMLHttpRequest',
    'x-time-zone': 'America/Los_Angeles',
    'x-user-locale': 'en',
}

params = {
    'stringifiedObjectParams': '{"includeDataForPageId":"pagQ2kSrE1T0wzxH4","shouldIncludeSchemaChecksum":true,"expectedPageLayoutSchemaVersion":23,"shouldPreloadQueries":true,"shouldPreloadAllPossibleContainerElementQueries":true,"urlSearch":"","includeDataForExpandedRowPageFromQueryContainer":true,"includeDataForAllReferencedExpandedRowPagesInLayout":true,"navigationMode":"view"}',
    'requestId': 'req' + str(generate(size = 14, alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")), # a bit cursed yes
    'accessPolicy': '{"allowedActions":[{"modelClassName":"page","modelIdSelector":"pagQ2kSrE1T0wzxH4","action":"read"},{"modelClassName":"application","modelIdSelector":"appOKDJk2ALKSisEM","action":"readForSharedPages"}],"shareId":"shriBhjoCj83rYCGT","applicationId":"appOKDJk2ALKSisEM","generationNumber":0,"expires":"2024-08-01T00:00:00.000Z","signature":"b6d599bf8cb40f7f9aac46dd3bfddeaaf76168d4a325b1ebac6db19d664352d3"}',
}

default_session = requests.session()
def download_table(session: requests.Session = default_session, raw = False):
    response = session.get(
        'https://airtable.com/v0.3/application/appOKDJk2ALKSisEM/readForSharedPages',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    if raw == True:
        return response
    return response.json()

if __name__ == "__main__":
    response = download_table(default_session, raw = True)
    print(response.status_code, len(response.text))