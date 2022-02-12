import csv
import mysql.connector
import pandas as pd



# f = open("C:\rishi it field job\sachin dada dataset\comma-seperated-values-file-1" , 'r')
# f.read()






conn = mysql.connector.connect(user='root', password='intel', database='csv_db')
db = conn.cursor()
if conn.is_connected() :
    print("database condnected")
else:
    print("not connected")



file = open("usgov.csv")
csvfile = pd.read_csv("usgov.csv")
df = pd.DataFrame(csvfile)
for row in df.itertuples():
    print(row)

insert_into_ds = 'insert into tbl_csv_new (Project ,emp_year,cft, srf, HaleCP,HaleWP,ACE,AMM,AMO,NAO,SOI,N34,SST_caran,SST_carac,DaysHUR,AverTemp_Oct_thr_Sep,AverTemp_Dec_thr_Feb,DaysMinTemp_eq0,TotalPpt_Oct_thr_Sep,TotalPpt_Aug_thr_Dec,EAI,ed_Year,SRF_progression,Yr_Sequence,CFT_Reconstruction,ot_year,CFT_Projection,th_Year,SOI_laung,fo_Year,January,February,March,April,May,June,July,August,September,October,November,December)
                values
                '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    db.execute('''
                Insert into tbl_csv_new (Project ,emp_year,cft, srf, HaleCP,HaleWP,	ACE,AMM,AMO,NAO,SOI,N34,SST_caran,SST_carac,DaysHUR,
                 AverTemp_Oct_thr_Sep,AverTemp_Dec_thr_Feb,DaysMinTemp_eq0,TotalPpt_Oct_thr_Sep,TotalPpt_Aug_thr_Dec,EAI,ed_Year,
                 SRF_progression,Yr_Sequence,CFT_Reconstruction,ot_year,CFT_Projection,th_Year,SOI_laung,fo_Year,January,February,
                 March,April,May,June,July,August,September,October,November,December)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                 ''',(
                row.Project,
                row.emp_year,
                row.cft,
                row.srf,
                row.HaleCP,
                row.HaleWP,
                row.ACE,
                row.AMM,
                row.AMO,
                row.NAO,
                row.SOI,
                row.N34,
                row.SST_caran,
                row.SST_carac,
                row.DaysHUR,
                row.AverTemp_Oct_thr_Sep,
                row.AverTemp_Dec_thr_Feb,
                row.DaysMinTemp_eq0,
                row.TotalPpt_Oct_thr_Sep,
                row.TotalPpt_Aug_thr_Dec,
                row.EAI,
                row.ed_Year,
                row.SRF_progression,
                row.Yr_Sequence,
                row.CFT_Reconstruction,
                row.ot_year,
                row.CFT_Projection,
                row.th_Year,
                row.SOI_laung,
                row.fo_Year,
                row.January,
                row.February,
                row.March,
                row.April,
                row.May,
                row.June,
                row.July,
                row.August,
                row.September,
                row.October,
                row.November,
                row.December
                    )

# content = csv.reader(df)
# insert_records = (  "Insert into tbl_csv (Project,Year,CFT, SRF, HaleCP,HaleWP,	ACE,AMM,AMO,,NAO,SOI,N34,SST_caran,SST_carac,DaysHUR,"
#                  "AverTemp_Oct_thr_Sep,AverTemp_Dec_thr_Feb,DaysMinTemp_eq0,TotalPpt_Oct_thr_Sep,TotalPpt_Aug_thr_Dec,EAI,ed_Year," \
#                  "SRF_progression,Yr_Sequence,CFT_Reconstruction,ot_year,CFT_Projection,th_Year,SOI_laung,fo_Year,January,February," \
#                  "March,April,May,June,July,August,September,October,November,December)values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?")
#
#
conn.commit()



