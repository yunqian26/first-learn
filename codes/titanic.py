import numpy as py
import pandas as pd
import matplotlib as pl
import matplotlib.pyplot as plt
from pylsp.plugins.pylint_lint import build_args_stdio
if __name__== '__main__':
    test=pd.read_csv('D:\\anaconda3\\Lib\\site-packages\\test.csv')
    test=test.drop(columns=['Fare'],axis=1)# 删除两行无用行
    test=test.drop(columns=['Ticket'],axis=1)
    test=test.drop(columns=['Cabin'],axis=1)
    test['Sex']=test['Sex'].map({'male':0,'female':1})
    test['Embarked']=test['Embarked'].map({'S':0,'C':1,'Q':2})
    test['Age'].fillna(test['Age'].mean(),inplace=True)
    #制作标签Alone：是否单独出行
    test['Alone']=0
    test['Alone'][test['SibSp']+test['Parch']==0]=1
    #删除Sibsp与Parch
    test=test.drop(columns=['SibSp'],axis=1)
    test=test.drop(columns=['Parch'],axis=1)
    ##数据部分如上，接下来为绘图
    #性别与存活率
    survival_rates_sex=test.groupby ('Sex') ['Survived'].mean()#存活率计算
    survival_rates_sex.plot(kind='bar', color=['c', 'y'])#表格绘制，bar表示条形图，color表示颜色
    plt.title('Survival Rate by Sex on Titanic')#表格名字
    plt.xlabel('Sex')#表格x轴名字
    plt.ylabel('Survival Rate')#表格y轴名字
    plt.xticks(ticks=[0,1],labels=['Male','Female'])#表格x轴各元素名
    plt.show()#显示图表
    #年龄与存活率
    survival_number_age=test.groupby ('Age') ['Survived'].sum()
    survival_number_age.plot(color='r')
    plt.title=('Survival Number by Age on Titanic')
    plt.xlabel('Age')
    plt.ylabel('Survival Number')
    plt.show()