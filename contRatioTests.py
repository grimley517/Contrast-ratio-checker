import unittest
import contRatio as cr

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test1(self):
        '''checks that that appropriate errors in hexstring input are caught and 
        that componentise function splits out an 
        input hex colour string into its RGB components
        also checks that return value is a list of strings
        
        '''
        falseIns = ["11","1111","11111","1111111","#1111", "#111111111"]
        for inputValue in falseIns:
           self.assertRaises(ValueError, cr.componentise, inputValue)
        trueIns = ["#123","123","#112233","112233"]
        answers = [['11','22','33'],['11','22','33'],['11','22','33'],['11','22','33']]
        for i in range(len(trueIns)):
            self.assertEqual(cr.componentise(trueIns[i]),answers[i], 
            msg ="Something went wrong with the {0}th item".format(i+1))
    
    def test2(self):
        '''Checks hexVal funtion takes in a hex string and 
        returns the right integer
        '''
        inputs = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        for i in range(len(inputs)):
            self.assertEqual(cr.hexVal(inputs[i]),i, 
            msg="{0} converted to {1}".format(inputs[i], cr.hexVal(inputs[i])))
    
    def test3(self):
        ''' tests the unitise funtion'''
        self.assertAlmostEqual(cr.unitise(255), 1.0, msg="255 does not unitise to 1")
        self.assertAlmostEqual(cr.unitise(0),0.0, msg= "0 does not unitise to 0")
        self.assertAlmostEqual(cr.unitise(51), 0.2, msg = "51 does not unitise to 0.2")
        
    def test4(self):
        '''tests the final contrast ratios are within the bounds'''
        background = "#000000"
        for fg in range(2^24):
            foreground = "{0:x}".format(fg)
            while len(foreground)<6:
                foreground = "0"+foreground
            
            self.assertGreaterEqual(cr.ratio(background, foreground), 1.0, 
            msg = "{0} has a Contrast ratio of less than 1".format(foreground))
            
            self.assertLessEqual(cr.ratio(background, foreground), 21.0, 
            msg = "{0} has a Contrast ratio of greater than 21".format(foreground))
            
    def test5(self):
        tColours = ['000','111','222','333','444','555','666','777','888','999',
        'aaa','bbb','ccc','ddd','eee','fff']
        tExpected = [0.0, 
        0.0056054,
        0.0159963, 
        0.0331048, 
        0.0578054, 
        0.0908417,
        0.1328683,
        0.1844750,
        0.2462013,
        0.3185468,
        0.4019778,
        0.4969330,
        0.6038273,
        0.7230551,
        0.8549926,
        1.0]
        for i in range(len(tColours)):
            self.assertAlmostEqual(cr.relLuminance(tColours[i]),tExpected[i], 
                            places=7,
                            msg = "{0} does not have the expected relative luminance {1}".format(tColours[i], tExpected[i]))
            
    

if __name__ == '__main__':
    unittest.main(verbosity = 3)
