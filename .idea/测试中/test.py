# import numpy as np
# import pandas as pd
# import warnings
# warnings.filterwarnings("ignore")
# from  sklearn.metrics.pairwise import cosine_similarity
# import os
# os.chdir('C:\Data\Jupyter_file\机器学习')
# df=pd.read_csv("example.txt",header=None,names=["user_id","product_id","score"])
# #转换成我们需要的那种数据结构 透视表
# up_matrix=df.pivot_table(index="user_id",columns="product_id",values="score")
# #填充0
# up_matrix=up_matrix.fillna(0)
# similar_matrix=pd.DataFrame(cosine_similarity(up_matrix),index=up_matrix.index,columns=up_matrix.index)
# #待要推荐的用户是谁
# #选定你前几个朋友
# #推荐前几个商品
# k=2
# user_id=2
# item_id=2
# #找出最相似的前K个用户
# similar_k_users=similar_matrix.loc[user_id,:].sort_values(ascending=False)[1:k+1].sort_index()
# print(similar_k_users)

# import numpy as np
# import matplotlib.pylab as plt
#
# x, y = [], []
# for sample in open(r'..\_Data\prices.txt', "r"):
#     xx, yy = sample.split(",")
#     x.append(float(xx))
#     y.append(float(yy))
# x, y = np.array(x), np.array(y)
# # Perform normalization
# x = (x - x.mean()) / x.std()
# # Scatter dataset
# plt.figure()
# plt.scatter(x, y, c="g", s=20)
# plt.show()

print(input('请输入：'))



