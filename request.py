import requests
import copy
import requests_cache


url = "https://api.jwstapi.com/all/type/fits?page=1&perPage=10"
api_key = 'e7cc07d4-c546-4895-b734-877fe1e249da'

headers = {
    'X-API-KEY': 'e7cc07d4-c546-4895-b734-877fe1e249da',
}

params = {
    'page':'1',
    'perPage':"100",
}

#session = requests_cache.CachedSession('jwst_cache')

images = []
page = 1
while len(images) <= 100:
    this_params = copy.copy(params)
    this_params['page'] = page
    response = requests.get(url, headers=headers, params=this_params)
    if not response.json()["body"]: break

    for result in response.json()["body"]:
        if result not in images:
            images.append(result["location"])
        page += 1
    


html_image_list = [
    f"""<li>
            <a>
                <img src="{image}">
            </a>
        </li>
    """
    for image in images
]
html_image_list = "\n".join(html_image_list)

html = f"""<!doctype html>
<html><head><meta charset="utf-8">
<title>JWST Images</title>
<style>
ul {{
    list-style: none;
    line-height: 0;
    column-count: 5;
    column-gap: 5px;
}}
li {{
    margin-bottom: 5px;
}}
</style>
</head>
<body>
<ul>
{html_image_list}
</ul>
</body></html>
"""

output_file = f"searchresults.html"
with open(output_file, mode="w", encoding="utf-8") as fp:
    fp.write(html)
print(f"Search results summary written as {output_file}")