import os
import csv

voterid = []
county = []
candidate =[]
totalvotes = 0
khanvotes = 0
Correy = 0
Li = 0
OTooley = 0
file_to_output = os.path.join("Resources", "poll_data_reformatted2.csv")
csvpath = os.path.join("Resources",'election_data.csv')
with open(csvpath,newline="")as csvfile:
    assign = csv.reader(csvfile,delimiter=',')
    header = next(assign)

    for row in assign:
        voterid = voterid + [row[0]]
        candidate = candidate + [row[2]]
        if row[2] == "Khan":
            khanvotes = khanvotes + 1        
        elif row[2] == "Correy" :
            Correy = Correy + 1
        elif row[2] == "Li":
            Li = Li + 1
        elif row[2] ==  "O'Tooley":
            OTooley = OTooley + 1
       
      
totalvotes = len(voterid)    
khanP = (khanvotes/totalvotes )
CorreyP = (Correy/totalvotes)
Lip =(Li/totalvotes)
OTooleyP = (OTooley/totalvotes)
Polldb = (totalvotes,khanvotes,Correy,Li,OTooley)
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Tot Votes", "Khan Votes", "Li Votes","Correy Votes"
                     , "OTooley Votes", ])
    writer.writerow(Polldb)
print("------------------------------------------------------------")
print("Total Votes:",totalvotes)
print("------------------------------------------------------------")
print(f"Khan: {khanP:.3%} ({(khanvotes)})")
print(f"Li: {Lip:.3%} ({Li})")
print(f"Correy: {CorreyP:.3%} ({Correy}) ")
print(f"OTooley: {OTooleyP:.3%} ({OTooley})")
print("-------------------------------------------------------------")
print("Winner: Khan")