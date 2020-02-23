#计算个人BMI身体指标

height = eval(input("请输入你的身高:"))
weight = eval(input("请输入你的体重:"))

BMI = weight/pow(height,2)
print("你的BMI指数是:{:.2f}".format(BMI))

zhiBiao = ""
guoJi = ""

if BMI < 18.5:
    zhiBiao = "偏瘦"
elif 18.5 <= BMI <= 24:
    zhiBiao = "正常"
elif 24 <= BMI <= 28:
    zhiBiao = "偏胖"
else:
    zhiBiao = "超重"
#################
if BMI < 18.5:
    guoJi = "偏瘦"
elif 18.5 <= BMI <= 25:
    guoJi = "正常"
elif 25 <= BMI <= 30:
    guoJi = "偏胖"
else:
    guoJi = "超重"

print("您的BMI指数在国内为“{}”的标准".format(zhiBiao))
print("您的BMI指数在国外为“{}”的标准".format(guoJi))
