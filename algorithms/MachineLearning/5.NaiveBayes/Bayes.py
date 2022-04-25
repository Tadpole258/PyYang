########### Gaussian Naive Bayes ~#############

#鸢尾花数据集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
#导入朴素贝叶斯模型，这里选用高斯分布下的朴素贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
# 除此之外，还有多项式分布下的朴素贝叶斯，伯努利分布下的朴素贝叶斯，补集朴素贝叶斯
# MultinomialNB,BernoulliNB,ComplementNB

#载入数据集
X, y = load_iris(return_X_y=True)
# 训练集、测试集拆分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
# 模型训练，分类模型预测
y_pred = gnb.fit(X_train, y_train).predict(X_test)

# 输出结果
print("Number of mislabeled points out of a total %d points : %d"
      % (X_test.shape[0], (y_test != y_pred).sum()))
