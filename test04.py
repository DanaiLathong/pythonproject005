#รับข้อมูลจำนวนเต็ม 5 จากจำนวนผู้ใช้ และคำนวนหาผลรวมและค่าเฉลี่ยของข้อมูลที่รับเข้ามาเป็นเท่าใด แล้วแสดงผลทางหน้าจอ
#ขอ 4 ฟังก์ชั่น ดังนั้นหาให้ได้ 4 Feature
#=================================
#   Program Average 5 Number
#=================================
#Enter number 1 : <input>
#Enter number 2 : <input>
#Enter number 3 : <input>
#Enter number 4 : <input>
#Enter number 5 : <input>
#=================================
#Sum of 5 number is : <output>
#Average of 5 number is : <output> (ขอทศนิยม 4 ตำแหน่ง)
#=================================
def input_value():
    num_1 = int(input("Enter Number 1 : "))
    num_2 = int(input("Enter Number 2 : "))
    num_3 = int(input("Enter Number 3 : "))
    num_4 = int(input("Enter Number 4 : "))
    num_5 = int(input("Enter Number 5 : "))
    return num_1 , num_2 , num_3 , num_4, num_5

def sum_5_number ( num_1 , num_2 , num_3 , num_4 , num_5 ):
    sumnumber = num_1 + num_2 + num_3 + num_4 + num_5
    return sumnumber

def average_number ( sumnumber ):
    average_5_number = sumnumber / 5
    return average_5_number

def output_5_number ( sumnumber , average_5_number):
    print (f"Sum of 5 Number is : {sumnumber}")
    print (f"Average of 5 Number is : {average_5_number:.4f}") 
    return sumnumber , average_5_number

print ("-----------------------------------")
print ("---- PROGRAM AVERAGE 5 NUMBER -----")
print ("-----------------------------------")
num_1 , num_2 , num_3 , num_4 , num_5 = input_value()
print ("-----------------------------------")
output_5_number ( sum_5_number ( num_1 , num_2 , num_3 , num_4 , num_5 ) , average_number ( sum_5_number ( num_1 , num_2 , num_3 , num_4 , num_5 ) ))
print ("-----------------------------------")