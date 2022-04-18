from EmilienWeb.request import Request
from EmilienWeb.info import VERSION
from EmilienWeb.reponse_generator import generate_response


def handle_request(request: Request) -> bytes:
    if request.url == "/picture":
        return generate_response(200, {}, open("EmilienWeb/beach.jpg", mode="br").read())
    return generate_response(200, {}, open("EmilienWeb/test_page.html").read().encode() +
                             f"<br>page generated using EmilienWeb {VERSION}".encode())
