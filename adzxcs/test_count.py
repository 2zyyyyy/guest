"""
2018/08/28
2zyyyyy
单元测试用例--加减乘除
"""
import unittest
from adzxcs.count import Calculator


class CountTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        print('完事儿~~')
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEquals(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEquals(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEquals(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEquals(result, 2)


if __name__ == "__main__":
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(CountTest.test_add())
    suite.addTest(CountTest.test_sub())
    suite.addTest(CountTest.test_mul())
    suite.addTest(CountTest.test_div())
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
