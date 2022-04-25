# from sklearn.model_selection import GridSearchCV # 通过网格方式来搜索参数
# from sklearn import datasets
# from sklearn.neighbors import KNeighborsClassifier
#
# # 导入iris是数据
# iris = datasets.load_iris()
# X = iris.data
# y = iris.target
#
# # 设置需要搜索的K值， 'n_neighbors'是sklearn中KNN的参数
# parameters = {'n_neighbors':[1,3,5,7,9,11,13,15]}
# knn = KNeighborsClassifier()  # 注意：在这里不用指定参数
#
# # 通过GridSearchCV来搜索最好的K值。 这个模块的内部其实
# # 就是对于每一个K值做了评估
# clf = GridSearchCV(knn, parameters, cv=5)
# clf.fit(X, y)
#
# # 输出最好的参数以及对应的准确率
# print ("best score is: %.2f"%clf.best_score_, "  best param: ",clf.best_params_)



#加载红酒数据集
from sklearn.datasets import load_wine
#KNN分类算法
from sklearn.neighbors import KNeighborsClassifier
#分割训练集与测试集
from sklearn.model_selection import train_test_split
#导入numpy
import numpy as np
#加载数据集
wine_dataset=load_wine()
#查看数据集对应的键
print("红酒数据集的键:\n{}".format(wine_dataset.keys()))
print("数据集描述:\n{}".format(wine_dataset['data'].shape))

# data 为数据集数据;target 为样本标签
#分割数据集，比例为 训练集：测试集 = 8:2
X_train,X_test,y_train,y_test=train_test_split(wine_dataset['data'],wine_dataset['target'],test_size=0.2,random_state=0)

#构建knn分类模型，并指定 k 值
KNN=KNeighborsClassifier(n_neighbors=10)

#使用训练集训练模型
KNN.fit(X_train,y_train)

#评估模型的得分
score=KNN.score(X_test,y_test)
print(score)
#给出一组数据对酒进行分类
X_wine_test=np.array([[11.8,4.39,2.39,29,82,2.86,3.53,0.21,2.85,2.8,.75,3.78,490]])
predict_result=KNN.predict(X_wine_test)
print(predict_result)
print("分类结果：{}".format(wine_dataset['target_names'][predict_result]))