#练习 1：自我介绍
#写一个程序，用 print() 输出以下内容（把你的信息填进去）：
name = "张三"
age = 28
goal = "学会Python配合影刀"

print(f"我叫{name}")
print(f"我今年{age}岁")
print(f"我的目标是{goal}")
print("加油！")

#练习 2：简单计算器
#输入两个数字，打印它们的和、差、积、商。

num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))

print(f"和：{num1 + num2}")
print(f"差：{num1 - num2}")
print(f"积：{num1 * num2}")
print(f"商：{num1 / num2}")

"""
练习 3：购物小票
定义变量：
- 商品名（字符串）
- 单价（小数）
- 数量（整数）
打印出小票格式：

===== 购物小票 =====
苹果 x 3
单价：5.5 元
总价：16.5 元
====================
"""
product_name = "苹果"
price = 5.5
quantity = 3
total = price * quantity

print("===== 购物小票 =====")
print(f"{product_name} x {quantity}")
print(f"单价：{price} 元")
print(f"总价：{total} 元")
print("====================")

"""
练习 4：类型转换猜谜
运行以下代码，先猜输出结果，再实际运行验证：
a = "10"
b = 3
print(a + b)    # 猜猜会怎样？
然后修改它，让程序正确输出 13。
"""

a = 10
b = 3
print(a + b) 

"""
练习 5（挑戦）：找零计算器
小明买了东西，输入总价和付款金额，计算找零。
请输入总价：37.5
请输入付款：50
找零：12.5 元
"""
total = float(input("请输入总价："))
payment = float(input("请输入付款："))

change = payment - total
print(f"找零：{change} 元")