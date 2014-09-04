import unittest
import text

class TestText(unittest.TestCase):

    def setUp(self):
        with open('tsttxt.txt','r') as f:
            t = f.read()

        self.txt = text.Text(t)

    # make sure there's something there
    def test_text(self):
        self.assertTrue(len(str(self.txt)) > 0)



    # make sure the matrix is correct





if __name__ == '__main__':
    unittest.main()



