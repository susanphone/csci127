import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import interactive

enrollments = r"/home/susan/CSCI127/Labs/Lab12/MSU College Enrollments.csv"
faculty = r"/home/susan/CSCI127/Labs/Lab12/CS Faculty.csv"

df_enrollments = pd.read_csv(enrollments)
df_faculty = pd.read_csv(faculty)

print(df_enrollments)
print(df_faculty)

sort_enroll = df_enrollments.sort_values(['College Enrollment'])
sort_fac = df_faculty.sort_values(['Years at MSU'])

print(sort_enroll)
print(sort_fac)
figures = [sort_enroll, sort_fac]
# enrollment2 = pd.DataFrame({'College Name': 'College Enrollment'})
# faculty2 = pd.DataFrame({'CS Faculty': 'Years at MSU'})

sort_enroll.plot(x='College Name', y='College Enrollment', kind='bar')
plt.show()
sort_fac.plot(x='CS Professor', y='Years at MSU', kind='bar')
plt.show()