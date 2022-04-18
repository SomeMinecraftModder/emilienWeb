from EmilienWeb.request import Request


def parse(raw_data: bytes) -> Request:
    raw_data_split = raw_data.split(b"\r\n")
    method = raw_data_split[0].split(b" ")[0].decode()
    try:
        url = raw_data_split[0].split(b" ")[1].decode()
    except IndexError:
        url = "/"
    headers = {k: v.strip() for k, v in [line.split(":", 1)
                                         for line in raw_data.decode().splitlines() if ":" in line]}
    try:
        data = raw_data.split(b"\r\n\r\n")[1].split(b"\r\n")  # noice
    except IndexError:
        data = ""
    return Request(raw_data, headers, method, url, data)
