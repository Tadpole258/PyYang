import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

# 加载波士顿房价数据集作
X, y = datasets.load_boston(return_X_y=True)

# 训练随机森林回归预测模型
reg2 = RandomForestRegressor(random_state=1, n_estimators=10)
reg2.fit(X, y)

xt = X[:20]

plt.figure()
plt.plot(reg2.predict(xt), 'b^', label='RandomForestRegressor')
plt.tick_params(axis='x', which='both', bottom=False, top=False,
                labelbottom=False)
plt.ylabel('predicted')
plt.xlabel('training samples')
plt.legend(loc="best")
plt.title('RandomForestRegressor predictions')
plt.show()