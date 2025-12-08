import pandas as pd
data = pd.read_excel('data.xlsx')
data.rename(columns={'행정구역(시군구)별':'year'}, inplace=True)
data.iat[0,0] = "population"
data = data.set_index("year")

data.replace("총인구수 (명)","total", inplace=True)
data.replace("남자인구수 (명)","male", inplace=True)
data.replace("여자인구수 (명)","female", inplace=True)

data_T = data.transpose()
print(data_T)


x_value = data_T.index[data_T['population']=="female"]
y_value1 = data_T['경기도'][data_T['population']=="female"]
y_value2 = data_T['서울특별시'][data_T['population']=="female"]
y_value3 = data_T['전국'][data_T['population']=="female"]
#
import matplotlib.pyplot as plt

plt.figure(num="population")
plt.title("total")
# ax = plt.gca()

plt.plot(x_value, y_value1, marker='o', color='red')
plt.plot(x_value, y_value2, marker='o', color='blue')
plt.plot(x_value, y_value3, marker='o', color='green')
plt.show()


