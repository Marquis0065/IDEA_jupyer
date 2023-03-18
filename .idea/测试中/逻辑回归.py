import os
os.__file__
import sys
# sys.executable
# dir()

# 分割测试集训练集
from sklearn.model_selection import train_test_split
# 模型评估（召回率），选择0.5为阈值
from sklearn.metrics import classification_report
import numpy as np
from scipy import stats
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
os.chdir(r'C:\Users\fzh00\Desktop\文件\python资料\Python数据清洗基础\data\2_逻辑回归案例')
data = pd.read_excel('客户列表.xls')
# data.head()
#‘成交意向度’为系统输出，这里不需要
data.drop('成交意向度', axis=1, inplace=True)
data.rename(columns={'客户ID':'ID', '对话时长(总时长/对话数量)':'对话时长', '互动次数(总次数/对话数量)':'互动次数',
                     '是否已成交(1已成交0未成交)':'是否成交'}, inplace=True)
# 去掉变量ID
data.drop('ID', axis=1, inplace=True)
train,test = train_test_split(data,test_size=0.3,random_state=6)


#拟合模型
formula = '是否成交~对话数量+对话时长+互动次数+销售说话时长占比+销售最长讲述+客户最长讲述+对话得分'
model = smf.logit(formula,train) #实例化
model = model.fit() #拟合数据
model.summary() #输出结果
#输出预测概率
pre = model.predict(test.iloc[:,:-1])
#预测标签
label = (pre>0.5).astype('int')
#输出 分类报告,Y的真实值 和预测标签
print(classification_report(test.iloc[:,-1],label))

#下面是模型调优
#SMOTE,处理不平衡数据的方法
# train['是否成交'].value_counts()
# SMOTE过采样:对训练集进行过采
from imblearn.over_sampling import SMOTE

#过采样（SMOTE）
smote = SMOTE(random_state=42)   #实例化
Xtrain_sm,  Ytrain_sm= smote.fit_resample(train.iloc[:,:-1], train.iloc[:,-1])   #过采样
#合并过采样后的自变量与因变量
train_sm = pd.concat([Xtrain_sm, Ytrain_sm], axis=1)
#重新拟合模型
formula2='是否成交~对话数量+对话时长+互动次数+销售说话时长占比+销售最长讲述+客户最长讲述+对话得分'
model_sm = smf.logit(formula=formula2, data=train_sm)   #实例化
model_sm = model_sm.fit()   #拟合数据
model_sm.summary()
#预测
pre_sm = model_sm.predict(test.iloc[:,:-1])
# (pre_sm>0.5).sum()
#输出 分类报告,Y的真实值 和预测标签
print(classification_report(test.iloc[:,-1],(pre_sm>0.5).astype('int')))
#混淆矩阵，默认阈值0.5
# model_sm.pred_table()
#改进方法BorderlineSMOTE1
from imblearn.over_sampling import BorderlineSMOTE
smote_b1 = BorderlineSMOTE(random_state=123)
Xtrain_sm_1,Ytrain_sm_1 = smote_b1.fit_resample(train.iloc[:,:-1],train.iloc[:,-1])
train_sm_1 = pd.concat([Xtrain_sm_1, Ytrain_sm_1],axis=1)
# train_sm_1.shape
formula3='是否成交~对话数量+对话时长+互动次数+销售说话时长占比+销售最长讲述+客户最长讲述+对话得分'
model_sm_1 = smf.logit(formula=formula3, data=train_sm_1).fit()
model_sm_1.summary()
pre_label_sm_1= (model_sm_1.predict(test) > 0.5).astype("int")   # 生成预测值
print(classification_report(test.iloc[:,-1], pre_label_sm_1))   # Y的真实值，Y的预测值

#改进方法BorderlineSMOTE2
smote_b2 = BorderlineSMOTE(random_state=123, kind='borderline-2') #默认SMOTE1
Xtrain_sm_2,Ytrain_sm_2 = smote_b2.fit_resample(train.iloc[:,:-1],train.iloc[:,-1])
train_sm_2 = pd.concat([Xtrain_sm_2, Ytrain_sm_2],axis=1)
formula4='是否成交~对话数量+对话时长+互动次数+销售说话时长占比+销售最长讲述+客户最长讲述+对话得分'
model_sm_2 = smf.logit(formula=formula4, data=train_sm_2).fit()
# model_sm_2.summary()

pre_label_sm_2= (model_sm_2.predict(test) > 0.5).astype("int")   # 生成预测值
print(classification_report(test.iloc[:,-1], pre_label_sm_2))   # Y的真实值，Y的预测值

#预测出来的标签的结果，用于得到分类报告的
pre_sm_1 = model_sm_1.predict(test)
pre_sm_2 = model_sm_2.predict(test)

#模型评估
from sklearn import metrics
#将真实的标签值与预测出来的为1的概率值传入metrics.roc_curve（），返回的是一系列的tpr、fpr、阈值的取值情况
fpr, tpr, th = metrics.roc_curve(test.iloc[:,-1], pre)
fpr_sm, tpr_sm, th_sm = metrics.roc_curve(test.iloc[:,-1], pre_sm)
fpr_sm_1, tpr_sm_1, th_sm_1 = metrics.roc_curve(test.iloc[:,-1], pre_sm_1)
fpr_sm_2, tpr_sm_2, th_sm_2 = metrics.roc_curve(test.iloc[:,-1], pre_sm_2)

#绘图
plt.figure(figsize=[5, 5])
plt.plot(fpr, tpr, 'b', label='AUC = %.4f' %metrics.auc(fpr, tpr))
plt.plot(fpr_sm, tpr_sm, 'r', label='AUC_sm = %.4f' %metrics.auc(fpr_sm, tpr_sm))
plt.plot(fpr_sm_1, tpr_sm_1, 'g', label='AUC_sm_1 = %.4f' %metrics.auc(fpr_sm_1, tpr_sm_1))
plt.plot(fpr_sm_2, tpr_sm_2, 'y', label='AUC_sm_2 = %.4f' %metrics.auc(fpr_sm_2, tpr_sm_2))


plt.legend(loc = 'lower right')
plt.title('ROC curve')
print(sys.executable)
plt.show();







