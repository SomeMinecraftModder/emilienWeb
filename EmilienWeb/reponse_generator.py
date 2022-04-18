def generate_response(code: int, headers: dict, data: bytes) -> bytes:
    response_code = {
        200: "OK",
        404: "NOT FOUND",
        418: "AIN'T A TEAPOT",
        500: "INTERNAL SERVER ERROR",
    }
    fancy_code = response_code.get(code, "200").encode()  # fallback to 200
    code = str(code).encode("utf-8")
    header = ""
    for key, item in list(headers.items()):
        header += f"{key}: {item}\r\n"
    header = header.encode()
    response = b"HTTP/1.0 " + code + b" " + fancy_code + b"\r\n" + header + b"\r\n" + data
    return response
