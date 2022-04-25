# MLR,Multiple Linear Regression
from cache import basic
import statsmodels.api as sm
basic.warnings.filterwarnings('ignore')


def alg_MLR(limit):
    cols = list(data.columns)[1:]
    for i in range(len(cols)):
        ivar = data[cols]
        x = sm.add_constant(ivar)  # 生成自变量
        y = data["交易金额"]  # 生成因变量
        model = sm.OLS(y, x)  # 生成模型
        mod = model.fit()  # 模型拟合
        p_values = mod.pvalues  # 得到结果中所有P值
        p_values.drop('const', inplace=True)  # 把const取得
        p_max = max(p_values)  # 选出最大的P值
        if p_max > limit:
            ind = p_values.idxmax()  # 找出最大P值的index
            cols.remove(ind)  # 把这个index从cols中删除
        else:
            return mod


if __name__ == '__main__':
    files = r"./MLR-data.xlsx"
    data = basic.pd.read_excel(files)
    result = alg_MLR(0.01)
    print(result.summary())
