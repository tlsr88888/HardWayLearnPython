cars = 100 # 将100赋予变量cars
space_in_a_car = 4.0 # 将4.0赋予变量space_in_a_car
drivers = 30 # 将30赋予变量drivers
passengers = 90 # 将90赋予变量passengers
cars_not_driven = cars - drivers # 没有driver的cars数量为cars - drivers
cars_driven = drivers # 有drever的cars数量为drevers
carpool_capacity = cars_driven * space_in_a_car # 最大的拼车人数为有driver的数量乘以车坐数量
average_passengers_per_car = passengers / cars_driven #每辆车的乘客数量

print ('There are', cars, 'cars available.')# 车子数量
print ('There are only', drivers, 'drivers available.')# 司机数量
print ('There will be', cars_not_driven, 'empty cars today.')# 不用开的车的数量
print ('We can transport', carpool_capacity, 'people today.')# 开走的人数
print ('We have', passengers, 'to carpool today.')# 乘客总数
print ('We need to put about', average_passengers_per_car, 'in each car.')# 每辆车的乘客数量
