#-*- coding:utf-8 -*-
#!/usr/bin/python
'''
美国波斯顿房价预测  决策树回归DTR  回归预测  
'''

#######数据获取#######
# 从sklearn.datasets导入波士顿房价数据读取器
from sklearn.datasets import load_boston
# 从读取房价数据存储在变量boston中
boston = load_boston()
# 输出数据描述
print boston.DESCR

#########数据分割#########
# 从sklearn.cross_validation导入数据分割器
from sklearn.cross_validation import train_test_split
# 导入numpy并重命名为np
X = boston.data       # 数据集
y = boston.target     # 标签
# 随机采样25%的数据构建测试样本，其余作为训练样本
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)

#####数据分析######
# 分析回归目标值的差异
import numpy as np
print "目标值最大值：", np.max(boston.target)  # 最大值
print "目标值最小值：", np.min(boston.target)  # 最小值
print "目标值均值  ：", np.mean(boston.target) # 均值

#####数据处理######
# 从sklearn.preprocessing导入数据标准化模块
from sklearn.preprocessing import StandardScaler
# 分别初始化对特征和目标值的标准化器
ss_X = StandardScaler()
ss_y = StandardScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理
# 注意只接受二维数组 
# 一维数组 array.reshape(-1, 1) 变成单列的二维数组   单个特征 
# array.reshape(1, -1)          变成单行的二维数组   单个样本
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train.reshape(-1,1))
y_test = ss_y.transform(y_test.reshape(-1,1))

######模型训练及预测#################
# 从sklearn.tree中导入DecisionTreeRegressor
from sklearn.tree import DecisionTreeRegressor
# 使用默认配置初始化DecisionTreeRegressor
dtr = DecisionTreeRegressor()
# 用波士顿房价的训练数据构建回归树
dtr.fit(X_train, y_train)
# 使用默认配置的单一回归树对测试数据进行预测，并将预测值存储在变量dtr_y_predict中
dtr_y_predict = dtr.predict(X_test)

###########结果评价###################
###决策树模型###
# 使用uni_knr模型自带的评估模块，并输出评估结果
print '决策树回归模型准确度： ', dtr.score(X_test, y_test)
# 使用R-squared、MSE和MAE指标对三种配置的支持向量机（回归）模型在相同测试集上进行性能评估
# 从sklearn.metrics依次导入r2_score、mean_squared_error以及mean_absoluate_error用于回归性能的评估
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
# 使用r2_score模块，并输出评估结果
print '确定系数 R-squared : ', r2_score(y_test, dtr_y_predict)
# 使用mean_squared_error模块，并输出评估结果
print '均值平方误差 Mean Squared Error: ', mean_squared_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(dtr_y_predict))
# 使用mean_absolute_error模块，并输出评估结果
print '均值绝对误差 Mean Absoluate Error: ', mean_absolute_error(ss_y.inverse_transform(y_test), ss_y.inverse_transform(dtr_y_predict))




