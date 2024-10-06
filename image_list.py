html_image_list = [
    f"""<li>
            <a href="{image["pageURL"]}">
                <img src="{image['thumbnail']}" alt="{image["tags"]}">
            </a>
        </li>
    """
    for image in images # type: ignore
]
html_image_list = "\n".join(html_image_list)