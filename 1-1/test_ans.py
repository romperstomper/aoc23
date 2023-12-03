import unittest
import ans

class Testing(unittest.TestCase):
    def test_getleft(self):
      #self.assertEqual(ans.getleft('twoone'), 2)
      self.assertEqual(ans.getleft('73'), 7)
      self.assertEqual(ans.getleft('treb7uchet'), 7)
      self.assertEqual(ans.getleft('1qcbszfgonedjcqj66929'), 1)

    @unittest.skip
    def test_getright(self):
      #self.assertEqual(ans.getright('twoone')), 1)
      self.assertEqual(ans.getright('73'), 3)
      self.assertEqual(ans.getright('treb7uchet'), 7)
      self.assertEqual(ans.getright('1qcbszfgonedjcqj66929'), 9)

    def test_combo(self):
      self.assertEqual(ans.combo('56'), 56)
      self.assertEqual(ans.combo('3four'), 33)
      self.assertEqual(ans.combo('seven8'), 88)
      self.assertEqual(ans.combo('73'), 73)
      self.assertEqual(ans.combo('6kvfn'), 66)
      self.assertEqual(ans.combo('treb7uchet'), 77)
      self.assertEqual(ans.combo('jjfvnnlfivejj1'), 11)
      self.assertEqual(ans.combo('6fourfour'), 66)
      self.assertEqual(ans.combo('ninevbmltwo69'), 69)
      self.assertEqual(ans.combo('pcg91vqrfpxxzzzoneightzt'), 91)
      self.assertEqual(ans.combo('jpprthxgjfive3one1qckhrptpqdc'), 31)
      self.assertEqual(ans.combo('mxphxfnffninethreetdj5jgknqfrxmhxfivexcxqv'), 55)
      self.assertEqual(ans.combo('three7pktwo4279z'), 79)
      self.assertEqual(ans.combo('1qcbszfgonedjcqj66929'), 19)
      self.assertEqual(ans.combo('fivesixthreeptcqjnkzgdfgzspmlvmmhn3'), 33)
      self.assertEqual(ans.combo('vm2sixseven'), 22)
      self.assertEqual(ans.combo('1nine6oneeightnine5lfrzmzh7'), 17)
      self.assertEqual(ans.combo('7onevsffj78ninejcnnvgn65'), 75)
      self.assertEqual(ans.combo('qstwonepcd3twosixrmcnxhfzv'), 33)
      self.assertEqual(ans.combo('3bnjfrfourseventwo'), 33)
      self.assertEqual(ans.combo('zpcdmvmktlrrq8sixgjtxxjpt8fcstt1'), 81)
      self.assertEqual(ans.combo('nine1gkmptbfsix87'), 17)
      self.assertEqual(ans.combo('9ldmlbchvnvgfivesixnine7zrt'), 97)
      self.assertEqual(ans.combo('45mjmblfqjvf9'), 49)
      self.assertEqual(ans.combo('onehcpgmvd837sgzgsqqrtseven'), 87)
      self.assertEqual(ans.combo('rhjfvkznjdvlgv9one8'), 98)
      self.assertEqual(ans.combo('22xkkdsvfvfourhdpchs'), 22)
      self.assertEqual(ans.combo('sixzjx5kvjbcfgcsrjndznkrtf6'), 56)
      self.assertEqual(ans.combo('1fourmk8three3seven'), 13)
      self.assertEqual(ans.combo('4716lpzhdcbone6seventwo'), 46)
      self.assertEqual(ans.combo('443two27'), 47)
      self.assertEqual(ans.combo('9sgtwoseven6'), 96)
      self.assertEqual(ans.combo('pjtbhxchqfseven18tznxpbsppk'), 18)
      self.assertEqual(ans.combo('9eightwonkt'), 99)
      self.assertEqual(ans.combo('htsgxmrfsevenone8qjxhjsixnbsvcf5'), 85)
      self.assertEqual(ans.combo('5jmnjnnfsfoursevenprtjzdxmxj7six'), 57)
      self.assertEqual(ans.combo('dthreenrzonefourcxfrzsvtfz9xb'), 99)
      self.assertEqual(ans.combo('6kvfn'), 66)
      self.assertEqual(ans.combo('vlfbzpbpseven8tspgqfdzkmfivefourzjzdbxgtvx'), 88)

if __name__ == '__main__':
    unittest.main()
