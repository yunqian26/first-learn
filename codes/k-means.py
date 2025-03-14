import numpy as np
import matplotlib.pyplot as plt
def kmeans(X, K, max_iters=100, tol=1e-4):
    """
    K-Means算法实现
    :param X: 数据集，形状为 (n_samples, n_features)
    :param K: 簇的数量
    :param max_iters: 最大迭代次数
    :param tol: 收敛阈值，当质心的变化小于该值时停止迭代
    :return: 簇分配结果、质心
    """
    # 随机初始化质心
    np.random.seed(42)  # 设置随机种子以保证结果可复现
    centroids = X[np.random.choice(X.shape[0], K, replace=False)]

    for i in range(max_iters):
        # 分配阶段：计算每个数据点到质心的距离，并分配到最近的簇
        distances = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        cluster_assignments = np.argmin(distances, axis=1)

        # 更新阶段：重新计算每个簇的质心
        new_centroids = np.array([X[cluster_assignments == k].mean(axis=0) for k in range(K)])

        # 检查收敛：如果质心变化小于阈值，则停止迭代
        if np.linalg.norm(new_centroids - centroids) < tol:
            break

        centroids = new_centroids

    return cluster_assignments, centroids


# 示例：使用K-Means算法
if __name__ == "__main__":
    # 生成模拟数据
    np.random.seed(99)
    X = np.vstack([
        np.random.normal(loc=[0, 0], scale=1.0, size=(100, 2)),
        np.random.normal(loc=[5, 5], scale=1.0, size=(100, 2)),
        np.random.normal(loc=[0, 5], scale=1.0, size=(100, 2))
    ])

    # 运行K-Means算法
    K = 3
    cluster_assignments, centroids = kmeans(X, K)

    # 打印结果
    print("簇分配结果：", cluster_assignments)
    print("质心：", centroids)

    # 可视化结果（需要matplotlib库）


    plt.scatter(X[:, 0], X[:, 1], c=cluster_assignments, cmap='viridis', marker='o')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=100)
    plt.title("K-Means Clustering")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()