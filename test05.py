#คำนวณหาภาษีที่ต้องจ่าย และเงินเดือนสุทธิของพนักงานแล้วแสดงผลทางหน้าจอ โดยรับค่ารหัสพนักงาน ชื่อพนักงานและเงินเดือนปกติของพนักงานนั้นจะต้องหักค่าภาษีและเบี้ยประกันสังคมออกจากเงินเดือนปกติเสียก่อน
#โดยที่พนักงานต้องเสียภาษี 7% ของเงินเดือนปกติดและจ่ายค่าเบี้ยประกันสังคม 500 บาท

#ขอ 5 ฟังก์ชั่น ดังนั้นต้องหาให้ได้ 5 feature
#====================================
#         คำนวณเงินเดือนพนักงาน
#====================================
#ป้อนรหัสพนักงาน : <input>
#ป้อนชื่อพนักงาน : <input>
#ป้อนเงินเดือนปกติ : <input> บาท
#====================================
# ภาษีเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
# เงินเดือนสุทธิเป็นเงิน : <output> บาท (ขอทศนิยม 2 ตำแหน่ง)
#====================================
def inputdata ():
    user_password = int(input("ป้อนรหัสพนักงาน : "))
    user_name = str(input("ป้อนชื่อพนักงาน : "))
    user_money = int(input("ป้อนเงินเดือนพนักงาน : "))
    return user_money , user_name , user_password
def addtax_money (user_money):
    Additional_taxes = user_money * 0.07
    return Additional_taxes
def sso_money (user_money):
    have_user = user_money - 500 
    return have_user
def vat_user (have_user , Additional_taxes):
    use_money = have_user - Additional_taxes
    return use_money
def output_vat (Additional_taxes ,vat_user):
    print (f"ภาษีเป็นเงิน : {Additional_taxes:.2f} บาท")
    print (f"เงินเดือนสุทธิเป็นเงิน : {vat_user:.2f} บาท")

print ("--------------------------------------------")
print ("--------------คำนวณเงินเดือนพนักงาน------------")
print ("--------------------------------------------")
user_money , user_name , user_password = inputdata ()
print ("--------------------------------------------")
output_vat (addtax_money (user_money) ,vat_user (sso_money (user_money), addtax_money (user_money)))
print ("--------------------------------------------")