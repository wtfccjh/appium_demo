from appium import webdriver
import time
import HTMLTestRunner
import unittest


class Dttest(unittest.TestCase):
    @classmethod
    def setUp(self):
        print('start setup')
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4' #版本号 与使用的AVD相同
        desired_caps['deviceName'] = 'Custom Phone' #可在appium中设定 不设定的话随便取
        desired_caps['app'] = 'C:\\Users\YR\\Desktop\\20161010-qy-yyb.apk' #apk所在位置 注意要使用\\
        desired_caps['appPackage'] = 'com.yr.browser' #包名可在cmd中使用aapt 或者 直接在appium中查看
        desired_caps['appActivity'] = 'com.yr.browser.views.activitys.LoadingActivity'

        self.driver=webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print('tearDown')

    def test_clicktap(self):
        self.driver.swipe(800,200,20,200,1000) #滑动屏幕（X1，Y1，X2，Y2 ，滑动时间）
        time.sleep(5)
        self.driver.swipe(800,200,20,200,1000)
        time.sleep(5)
        self.driver.swipe(800,200,20,200,1000)
        time.sleep(5)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        time.sleep(5)
        print('click pass')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Dttest('test_clicktap'))
    #timestr = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
    filename = 'F:\\result.html'   # 'Users/YR/PycharmProjects/tryspy/.idea/report/'+timestr+ '.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='result',
        description='report'
    )
    runner.run(suite)
    fp.close()