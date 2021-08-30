import csv


def write_into_csv(student_info_list):
  with open('student_info.csv', 'a', newline='') as csv_file:#as this snippet is in loop downwards, every time new fle will be created and data will be entered
   #so we will use "a" as it only appends the new items
    writer = csv.writer(csv_file)

    #writing the header for the file
    if csv_file.tell() == 0:#checks if the file is empty or not

      writer.writerow(["name", "age", "contact", "mail"])

    writer.writerow(student_info_list) #using writerow function we have to put the data in list format

if __name__ == '__main__':


    condition = True
    student_num = 1

    while(condition):
      print("enter student info in following format name , age, contact , mail")
      student_info = input("enter the information of the student #{}".format(student_num))      
      #print("entered information", student_info)
      
      #splitting the string  
      student_info_list = student_info.split()
      #print("entered information is such "  +str(student_info_list))

      #now inserting this into file
      print("\n the entered information is - \n name = {} \n age = {} \n contact_number = {} \n emailid = {}\n ".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
      

      choice_check = input("is the enterd information corrrect ? yes/no")

      if choice_check == "yes":
        write_into_csv(student_info_list)

        check = input("if you want to continue type yes and if no then type no")
        if check == "yes":
          condition = True
          student_num = student_num + 1
        else:
          condition = False

      else:
        print("please re-enter the value")




      
