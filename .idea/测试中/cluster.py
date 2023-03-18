# conda update conda
# conda update anaconda
# conda update --all
# !conda update --all 加感叹号，强制按照命令行，本身notebook是按shell
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import warnings
warnings.filterwarnings('ignore')
import os
os.chdir(r'C:\Data\Jupyter_file\机器学习')

df= pd.read_csv('profile_bank.csv')
data = df.iloc[:,1:-1]
#数据标准化
from sklearn import preprocessing
std_data= preprocessing.scale(data)
#主成分分析 PCA 确定需要几个主成分
from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(std_data)
#查看方差特征
pca.explained_variance_
#查看方差比率
pca.explained_variance_ratio_
sum(pca.explained_variance_ratio_)
#因子分析
from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting
#实例化
fa=FactorAnalysis.load_data_samples(
    std_data,
    preproc_demean=True,
    preproc_scale=True
)
fa.extract_components()
#设定提取主成分的方法
fa.find_comps_to_retain(method='top_n',num_keep=3)
#最大方差拉升旋转,看数据 的变异方向
fa.rotate_components(method='varimax')
#因子的载荷矩阵（权重距阵）
# print(fa.comps['rot'])  #表示两个主要因子的权重系数
#输出 因子得分
score = fa.get_component_scores(std_data)
score = pd.DataFrame(score,columns=['POS','TBM','CSC'])
#Kmeans-异常识别
var = ['TBM','POS','CSC']
#求偏度
skew_var={}
for i in var:
    skew_var[i]=score[i].skew()
# skew_var #》右偏； 《0 左偏
#进行Kmeans聚类
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
result = kmeans.fit(score)
#pip install GraphhViz 决策树
from sklearn import tree
#分类树
clf=tree.DecisionTreeClassifier(criterion="gini",
                                max_depth=3,
                                min_samples_split=100,
                                min_samples_leaf=100,
                                random_state=12345)
clf.fit(df,result.labels_)
#pydotplus
# pip install pydotplus
#画决策树图。对分类结果进行解读
import pydotplus
from IPython.display import Image
import sklearn.tree as tree
dot_data=tree.export_graphviz(clf,
                              out_file=None,
                              feature_names=df.columns,
                              class_names=["0","1","2"],
                              filled=True)
graph=pydotplus.graph_from_dot_data(dot_data)
print(Image(graph.create_png()))
#保存图像到pdf文件
# graph.write_pdf('决策树.pdf')