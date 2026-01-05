import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 设置随机种子以确保结果可重现
torch.manual_seed(42)
np.random.seed(42)

# 1. 数据预处理 - 使用 sklearn 内置糖尿病数据集
diabetes = load_diabetes()
X = diabetes.data  # 特征数据
y = diabetes.target  # 目标值

# 将回归目标转换为二分类问题（以均值为阈值）
y_binary = (y > np.median(y)).astype(float)

# 转换为 PyTorch 张量
x_data = torch.from_numpy(X).float()
y_data = torch.from_numpy(y_binary).view(-1, 1).float()

# 数据标准化
scaler = StandardScaler()
x_data_np = scaler.fit_transform(x_data.numpy())
x_data = torch.from_numpy(x_data_np).float()

# 数据集划分
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.2, random_state=42
)

# 初始化变量用于记录训练过程
epoch_list = []
loss_list = []
accuracy_list = []

# 2. 模型构建
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear1 = nn.Linear(10, 6)  # 注意：diabetes数据集有10个特征
        self.linear2 = nn.Linear(6, 3)
        self.linear3 = nn.Linear(3, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()  # Sigmoid 通常在输出层用于二分类问题

    def forward(self, x):
        x = self.relu(self.linear1(x))
        x = self.relu(self.linear2(x))
        x = self.sigmoid(self.linear3(x))  # 输出概率值
        return x

# 3. 模型训练
# 实例化模型、损失函数和优化器
model = Model()
criterion = nn.BCELoss()  # BCELoss 期望输入是概率值和二进制（0-1）标签的浮点数据表示
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 训练模型
for epoch in range(1000):
    model.train()  # 设置模型为训练模式
    optimizer.zero_grad()  # 清零梯度
    y_pred = model(x_train)  # 使用训练数据进行预测
    loss = criterion(y_pred, y_train)  # 计算损失
    loss.backward()  # 反向传播
    optimizer.step()  # 更新权重

    # 计算训练准确率（用于监控训练过程）
    train_predicted_labels = (y_pred > 0.5).float()  # 将概率值转换为二进制标签（浮点型）
    train_accuracy = (train_predicted_labels == y_train).sum().item() / y_train.size(0)

    # 记录损失和准确率
    epoch_list.append(epoch)
    loss_list.append(loss.item())
    accuracy_list.append(train_accuracy)

    # 打印损失和准确率（每100个周期一次）
    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.6f}, Training Accuracy: {train_accuracy:.4f}")

# 4. 模型评估
model.eval()  # 设置模型为评估模式
with torch.no_grad():  # 禁止梯度计算以节省内存和计算资源
    y_test_pred = model(x_test)  # 使用测试数据进行预测
    test_predicted_labels = (y_test_pred > 0.5).float()  # 将概率值转换为二进制标签（浮点型）
    test_accuracy = (test_predicted_labels == y_test).sum().item() / y_test.size(0)
    print(f"Test Accuracy: {test_accuracy:.4f}")

# 绘制准确率图
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(epoch_list, accuracy_list)
plt.xlabel("Epoch")
plt.ylabel("Training Accuracy")
plt.title("Training Accuracy over Epochs")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(epoch_list, loss_list, color='red')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss over Epochs")
plt.grid(True)

plt.tight_layout()
plt.show()

