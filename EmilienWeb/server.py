import socket
from EmilienWeb.info import VERSION
from EmilienWeb.parser import parse
from EmilienWeb.default_generator import handle_request
from datetime import datetime


def start(server_host: str, server_port: int, generator=handle_request):
    # Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((server_host, server_port))
    s.listen(1)
    print('Listening on port %s ...' % server_port)
    print(f"EmilienWeb v.{VERSION} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%z')}")
    print(f"On http://{server_host}:{server_port}")
    try:
        while True:
            # Wait for client connections
            client_connection, client_address = s.accept()

            # Get the client request
            current_request = client_connection.recv(1024)

            # Return an HTTP response
            parsed_request = parse(current_request)
            print(
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f%z')} {parsed_request.method} to {parsed_request.url}")
            raw_response = generator(parsed_request)
            client_connection.sendall(raw_response)

            # Close connection
            client_connection.close()

    except KeyboardInterrupt:
        print("Exiting...")
        # Close socket
        s.close()
        exit()
