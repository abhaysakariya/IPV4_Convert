import time

print("WELCOME TO THE PROGRAM CREATED BY ABHAY SAKARIYA. THIS PROGRAM WILL DO IPV4 BINARY-DECIMAL AND DECIMAL-BINARY CONVERSION")

print("******************************")

print("What Type Conversion You Want To Do:-")

print("1. Binary To Decimal")

print("2. Decimal To Binary")

choice = int(input("Enter Your Choice : "))

print("LOADING...... pls wait")

time.sleep(5)

if choice == 1:

  print("******Binary To Decimal Conversion Started.******")

  binary_list = []

  decimal_list = []

  print("Enter Binary Code :")

  n_iterate = 4

  for i in range(0,n_iterate):

    ele = input()

    check_len = len(ele)

    if check_len < 8 or check_len > 8:

      print("ERROR!! \n YOUR ARE ENTERING WRONG LENGTH OF AN BINARY CODE . YOU NEED 8 OF LENGTH EG. 11001100")

    else:  

    

      binary_list.append(ele)

  if len(binary_list) < 4:

    diff_list = len(binary_list)

    rem_list_no = 4 - diff_list

    for i in range(0,rem_list_no):

      ele = input()

      check_len = len(ele)

      if check_len < 8 or check_len > 8:

        print("ERROR!! \n YOUR ARE ENTERING WRONG LENGTH OF AN BINARY CODE . YOU NEED 8 OF LENGTH EG. 11001100")

      else:  

    

        binary_list.append(ele)

  for i in range(0,n_iterate):

    calculate_1 = 0

    if binary_list[i][0] == '1':

      calculate_1 += 128

    if binary_list[i][1] == '1':

      calculate_1 += 64

    if binary_list[i][2] == '1':

      calculate_1 += 32

    if binary_list[i][3] == '1':

      calculate_1 += 16

    if binary_list[i][4] == '1':

      calculate_1 += 8

    if binary_list[i][5] == '1':

      calculate_1 += 4

    if binary_list[i][6] == '1':

      calculate_1 += 2

    if binary_list[i][7] == '1':

      calculate_1 += 1 

    decimal_list.append(calculate_1)

  print("\n Calculating Answer For Binary To Decinal Conversion In IPV4 address Type.\n")

  time.sleep(8)

  print("Answer Is : {}.{}.{}.{}".format(decimal_list[0],decimal_list[1],decimal_list[2],decimal_list[3]))

  

elif choice == 2:

  print("******Decimal To Binary Conversion Started******\n")

  decimal_list_1 = []

  binary_list_1 = []

  n_iterate = 4

  print("Enter Decimal Code : ")

  for i in range(0,n_iterate):

    ele = input()

    if len(ele) > 3 and int(ele) > 255:

      print("ERROR!!! required Only 3 digit eg. 192")

      

    else:

      decimal_list_1.append(ele)

  if len(decimal_list_1) < 3 :

    diff = len(decimal_list_1)

    rem = 4 - diff

    for i in range(0,rem):

      ele = input()

      if len(ele) > 3 and int(ele) > 255:

        print("ERROR!!! Required only 3 digit eg. 192.")

    

      else:

        decimal_list_1.append(ele)

  

  cal_bin = ""

  for i in range(0,n_iterate):

    calculate = int(decimal_list_1[i])

    if int(decimal_list_1[i]) - 128 >= 0:

      calculate -= 128

      cal_bin += "1"

    else :

      cal_bin += "0"

    if calculate - 64 >= 0:

      cal_bin += "1"

      calculate -= 64

    else :

      cal_bin += "0"

    if calculate - 32 >= 0:

      cal_bin += "1"

      calculate -= 32

    else :

      cal_bin += "0"

    if calculate - 16 >= 0:

      cal_bin += "1"

      calculate -= 16

    else :

      cal_bin += "0"

    if calculate - 8 >= 0:

      cal_bin += "1"

      calculate -= 8

    else :

      cal_bin += "0"

    if calculate - 4 >= 0:

      cal_bin += "1"

      calculate -= 4

    else :

      cal_bin += "0"

    if calculate - 2 >= 0:

      cal_bin += "1"

      calculate -= 2

    else :

      cal_bin += "0"

    if calculate - 1 >= 0:

      cal_bin += "1"

      calculate -= 1

    else :

      cal_bin += "0"

    binary_list_1.append(cal_bin)

    cal_bin = ""

  print("\n Calculating The Conversion Pls Wait!!\n")

  time.sleep(8)

  print("answer is : {}.{}.{}.{}".format(binary_list_1[0],binary_list_1[1],binary_list_1[2],binary_list_1[3]))

else:

  print("WRONG INPUT!!! THANKS FOR USING")

