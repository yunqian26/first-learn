import numpy as np

class LinearRegression:
    """
    多元线性回归模型，使用最小二乘法求解。
    """
    def __init__(self, fit_intercept=True):
        """
        初始化线性回归模型。
        :param fit_intercept: 是否拟合截距项，默认为 True。
        """
        self.fit_intercept = fit_intercept
        self.coefficients = None  # 回归系数
        self.intercept = None  # 截距项

    def fit(self, X, y):
        """
        拟合线性回归模型。
        :param X: 特征矩阵，形状为 (n_samples, n_features)
        :param y: 目标值，形状为 (n_samples,)
        """
        # 检查输入数据的形状
        X = np.asarray(X)
        y = np.asarray(y)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array")
        if y.ndim != 1:
            raise ValueError("y must be a 1D array")
        if X.shape[0] != y.shape[0]:
            raise ValueError("The number of samples in X and y must match")

        # 添加截距项（如果需要）
        if self.fit_intercept:
            X = np.hstack([np.ones((X.shape[0], 1)), X])

        # 使用最小二乘法求解回归系数
        try:
            # 计算 (X^T X)^(-1) X^T y
            coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
        except np.linalg.LinAlgError:
            raise ValueError("X^T X is singular. Try setting fit_intercept=False or check your data.")

        # 分离截距项和回归系数
        if self.fit_intercept:
            self.intercept = coefficients[0]
            self.coefficients = coefficients[1:]
        else:
            self.coefficients = coefficients
            self.intercept = 0.0

    def predict(self, X):
        """
        使用拟合好的模型进行预测。
        :param X: 特征矩阵，形状为 (n_samples, n_features)
        :return: 预测值，形状为 (n_samples,)
        """
        X = np.asarray(X)
        if X.ndim != 2:
            raise ValueError("X must be a 2D array")
        if X.shape[1] != self.coefficients.shape[0]:
            raise ValueError("The number of features in X does not match the model")

        # 计算预测值 y = X * coefficients + intercept
        return X @ self.coefficients + self.intercept

    def score(self, X, y):
        """
        计算模型的 R² 值。
        :param X: 特征矩阵
        :param y: 真实目标值
        :return: R² 值
        """
        y_pred = self.predict(X)
        y_mean = np.mean(y)
        ss_tot = np.sum((y - y_mean) ** 2)
        ss_res = np.sum((y - y_pred) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2

    def get_params(self, deep=False):
        """
        获取模型参数。
        :param deep: 是否递归获取参数（与 scikit-learn 兼容）
        :return: 参数字典
        """
        return {"fit_intercept": self.fit_intercept}

    def set_params(self, **params):
        """
        设置模型参数。
        :param params: 参数字典
        """
        if "fit_intercept" in params:
            self.fit_intercept = params["fit_intercept"]
        return self

    def __repr__(self):
        return f"LinearRegression(fit_intercept={self.fit_intercept}, coefficients={self.coefficients}, intercept={self.intercept})"


# 示例：使用多元线性回归
if __name__ == "__main__":
    # 生成模拟数据
    np.random.seed(42)
    X = np.random.rand(100, 2)  # 100个样本，2个特征
    y = 3 * X[:, 0] + 2 * X[:, 1] + 1 + np.random.randn(100) * 0.5  # 真实关系：y = 3x1 + 2x2 + 1 + 噪声

    # 拟合模型
    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    # 打印模型参数
    print("模型参数：")
    print(f"回归系数：{model.coefficients}")
    print(f"截距项：{model.intercept}")

    # 预测
    y_pred = model.predict(X)

    # 评估模型
    r2 = model.score(X, y)
    print(f"R² 值：{r2:.4f}")