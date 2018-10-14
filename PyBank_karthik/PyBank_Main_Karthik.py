
import os
import csv

second = []
months = []
newlist = []
list2 = []
third=[]
i = 0
x=0
total = 0
tot=0
list3 = []
Average = 0

file_to_output = os.path.join("Resources", "bank_data.txt")
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath,newline="")as csvfile:
    assign = csv.reader(csvfile,delimiter=',')
    header = next(assign)

    for row in assign:
        months = months +[row[0]]
        second = second + [row[1]]
    for sm in second:
        total += int(sm)
        
    while( i<=84):
        list1 = [second[i]]+[second[i+1]]
        list2 = [int(y)-int(x) for x, y in zip (list1, list1[1:])]
        list3.extend(list2)
        newlist.append(list2)
        i+=1
    for add in list3:
        tot+= int(add)
    
    a = len(months)
    Average = tot/a


print("Total Months:" , a)
print("Total:",total)
print("Average Change",Average)
#print(list3)
#print("sum of {0}".format(sum(newlist[0:85])))
print("Greatest Increase in Profits:  {0}".format(max(list3)))
print("Greatest Decrease in Profits:  {0}".format(min(list3)))

with open(file_to_output, "w", newline="") as file:
    text_file.writelines("Total Months:"str(a))
    text_file.writelines(print("Total:"+str(total)))
    text_file.writelines(print("Average Change",Average))
    text_file.writelines(print("Greatest Increase in Profits: Feb-2012 {0}".format(max(list3))))
    text_file.writelines(print("Greatest Decrease in Profits: Sep-2013 {0}".format(min(list3))))


