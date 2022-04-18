import unittest
import requests
import multiprocessing


class TestEmilienWebCore(unittest.TestCase):
    def test_basic_request(self):
        from EmilienWeb import start
        from EmilienWeb.reponse_generator import generate_response
        process = multiprocessing.Process(target=start,
                                          args=("0.0.0.0", 8080, lambda _: generate_response(200, {}, b"k")))
        process.start()
        r = requests.get("http://0.0.0.0:8080")
        process.terminate()
        self.assertEqual(r.status_code, 200)

    def test_basic_request_with_header(self):
        from EmilienWeb import start
        from EmilienWeb.reponse_generator import generate_response
        process = multiprocessing.Process(target=start,
                                          args=("0.0.0.0", 8080, lambda _:
                                                generate_response(200, {"random": "header"}, b"k")))
        process.start()
        r = requests.get("http://0.0.0.0:8080")
        process.terminate()
        self.assertEqual(r.headers, {"random": "header"})

    def test_basic_request_with_content(self):
        from EmilienWeb import start
        from EmilienWeb.reponse_generator import generate_response
        process = multiprocessing.Process(target=start,
                                          args=("0.0.0.0", 8080, lambda _: generate_response(200, {}, b"k")))
        process.start()
        r = requests.get("http://0.0.0.0:8080")
        process.terminate()
        self.assertEqual(r.text, "k")


if __name__ == '__main__':
    unittest.main()
