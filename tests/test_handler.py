import unittest
import json
from noises.handler import Handler


class HandlerTest(unittest.TestCase):

    @unittest.skip("annoyance")
    def test_it_handles_status_failure(self):
        # Given
        handler = Handler()
        with open('./example-payloads/status.json') as json_file:
            data = json.load(json_file)

            # When
            handler.status(data)

    @unittest.skip("annoyance")
    def test_it_handles_status_success(self):
        # Given
        handler = Handler()
        with open('./example-payloads/status_success.json') as json_file:
            data = json.load(json_file)

            # When
            handler.status(data)







if __name__ == '__main__':
    unittest.main()
