import unittest
from instructions_decoder import cmd_decoder

from commands import *
from registers import A, B, C, D, E, H, L


class TestInstructionDecoder(unittest.TestCase):

    def test_inr(self):
        self.assertEqual(cmd_decoder(0b00000100), (inr, B, None))
        self.assertEqual(cmd_decoder(0b00001100), (inr, C, None))
        self.assertEqual(cmd_decoder(0b00010100), (inr, D, None))
        self.assertEqual(cmd_decoder(0b00011100), (inr, E, None))
        self.assertEqual(cmd_decoder(0b00100100), (inr, H, None))
        self.assertEqual(cmd_decoder(0b00101100), (inr, L, None))
        self.assertEqual(cmd_decoder(0b00111100), (inr, A, None))

    def test_dcr(self):
        self.assertEqual(cmd_decoder(0b10000001), (inr, B, None))
        self.assertEqual(cmd_decoder(0b10000101), (inr, C, None))
        self.assertEqual(cmd_decoder(0b10001001), (inr, D, None))
        self.assertEqual(cmd_decoder(0b10001101), (inr, E, None))
        self.assertEqual(cmd_decoder(0b10010001), (inr, H, None))
        self.assertEqual(cmd_decoder(0b10010101), (inr, L, None))
        self.assertEqual(cmd_decoder(0b10011101), (inr, A, None))

    def test_cma(self):
        self.assertEqual(cmd_decoder(0x2F), (cma, None, None))

    def test_daa(self):
        self.assertEqual(cmd_decoder(0x27), (daa, None, None))

    def test_nop(self):
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_mov(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_stax(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_ldax(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_add(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_adc(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_sub(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_sbb(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_ana(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_xra(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_ora(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_cmp(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_rlc(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_rrc(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_ral(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))

    def test_rar(self):#TODO
        self.assertEqual(cmd_decoder(0x00), (nop, None, None))







    def test_hlt(self):
        self.assertEqual(cmd_decoder(0x76), ("HLT", None, None))

if __name__ == "__main__":
    unittest.main()

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestGetBit)
    #unittest.TextTestRunner(verbosity=2).run(suite)

    #suite = unittest.TestLoader().loadTestsFromTestCase(TestGetBits)
    #unittest.TextTestRunner(verbosity=2).run(suite)