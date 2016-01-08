import unittest
from instructions_decoder import cmd_decoder


class TestInstructionDecoder(unittest.TestCase):

    def test_hlt(self):
        self.assertEqual(cmd_decoder(0x76), ("HLT", None, None))

if __name__ == "__main__":
    unittest.main()

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestGetBit)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestGetBits)
    #unittest.TextTestRunner(verbosity=2).run(suite)