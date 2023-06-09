import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import Test_thuong.test_function_dangnhap


def nhom_nsx_thanhcong(br):
        btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']")
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']/option[2]")
        cbb1.click()
        time.sleep(1)

        cbb_hangsx = br.find_element(By.XPATH,
                                     "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlMan']")
        if not cbb_hangsx:
            print("Case 3 fail - combo nsx rong")
            return False

        cbb_hangsx.click()
        time.sleep(1)

        nsx = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlMan']/option[3]")
        nsx.click()
        time.sleep(1)

        cbb_model = br.find_element(By.XPATH,
                                "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']")
        cbb_model.click()
        time.sleep(1)
        c = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']/option[3]")
        c.click()
        time.sleep(1)

        txt_tenSp = br.find_element(By.XPATH,
                                    "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[4]/div/input")
        txt_tenSp.send_keys("HT0101")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                                   "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[5]/div/input")
        txt_maSp.send_keys("Nhãn")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[6]/div/input")
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[9]/div/input")
        txt_sl.send_keys("100")
        time.sleep(1)

        # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                                  "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[10]/div/input")
        txt_stt.send_keys("2")
        time.sleep(1)

        # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[11]/div/table/tbody/tr/td[1]/input")
        rd_conHang.click()
        time.sleep(1)

        # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[12]/div/div/input")
        click_calendar.click()
        time.sleep(1)

        # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                         "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[13]/div/input")
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 3 pass")
            return True
        else:
            print("Case 3 fail")
            return False
def nhom_nsx_derong(br):
        btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
        btn_ChonThem.click()

        cbb_nhomSp = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']")
        cbb_nhomSp.click()

        cbb1 = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlForder']/option[2]")
        cbb1.click()
        time.sleep(1)

        cbb_model = br.find_element(By.XPATH,
                                "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']")
        cbb_model.click()
        time.sleep(1)
        c = br.find_element(By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_ucLoadControl_ctl00_ddlModel']/option[3]")
        c.click()
        time.sleep(1)

        txt_tenSp = br.find_element(By.XPATH,
                                "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[4]/div/input")
        txt_tenSp.send_keys("HT0101")
        time.sleep(1)
        txt_maSp = br.find_element(By.XPATH,
                               "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[5]/div/input")
        txt_maSp.send_keys("Nhãn")
        time.sleep(1)

        txt_bh = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[6]/div/input")
        txt_bh.send_keys("10")
        time.sleep(1)

        txt_sl = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[9]/div/input")
        txt_sl.send_keys("100")
        time.sleep(1)

    # Nhap thu tu
        txt_stt = br.find_element(By.XPATH,
                              "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[10]/div/input")
        txt_stt.send_keys("2")
        time.sleep(1)

    # Chọn còn hàng
        rd_conHang = br.find_element(By.XPATH,
                                 "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[11]/div/table/tbody/tr/td[1]/input")
        rd_conHang.click()
        time.sleep(1)

    # Click calendar
        click_calendar = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[12]/div/div/input")
        click_calendar.click()
        time.sleep(1)

    # Click checkbox
        click_checkBox = br.find_element(By.XPATH,
                                     "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[1]/div/div[13]/div/input")
        click_checkBox.click()
        time.sleep(1)

        btn_capNhat = br.find_element(By.XPATH, "/html/body/form/div[4]/div[3]/div/div/div/div[2]/div[9]/div/div/a[1]")
        btn_capNhat.click()
        time.sleep(1)

        if br.current_url == "http://1.hoctestertop.com/admin-product/list.aspx":
            print("Case 4 pass")
            return True
        else:
            print("Case 4 fail")
            return False
        time.sleep(1)
def them(br):
    btn_ThemSP = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/a")
    btn_ThemSP.click()
    btn_ChonThem = br.find_element(By.XPATH, "//*[@id='sidebar']/div/div[1]/ul/li[4]/ul/li[1]/a")
    btn_ChonThem.click()
    time.sleep(2)
    return

if __name__ == '__main__':
    br = webdriver.Chrome()
    br.get("http://1.hoctestertop.com/control.panel/")
    Test_thuong.DangNhap.thanh_cong(br)
    them(br)
    nhom_nsx_thanhcong(br)
    nhom_nsx_derong(br)
    time.sleep(2)
