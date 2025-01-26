### Pandas库
##### series数据结构
>类似于一维数组，由索引与数据组成，可存储任何类型数据，并通过标签来访问元素

* 特点
>每个元素都有对应索引值，并可通过索引值访问
>可容纳整数、浮点数、字符串、Python对象等
>大小再创建后不变，除非通过append或delete改变
>支持数学运算、统计分析、字符串等操作
>可包含缺失数据，使用NaN来表示缺失或无值
>多个series数据进行运算回自动根据索引对齐数据

* 创建一个series
>使用`pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)`为原型函数，返回值为一个series变量
>>参数说明：
data：Series 的数据部分，可以是列表、数组、字典(自动将键作为索引，值作为数据)、标量值等。如果不提供此参数，则创建一个空的 Series。
index：Series 的索引部分，用于对数据进行标记。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 Series 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
name：Series 的名称，用于标识 Series 对象。如果提供了此参数，则创建的 Series 对象将具有指定的名称。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。
fastpath：是否启用快速路径。默认为 False。启用快速路径可能会在某些情况下提高性能。

##### dataframe数据
* 特点
>
> 类似于二维表格或数据库中的数据表
> 具有行列、可视为多个series对象组成的字典
> 不同列可包含不同数据类型
> 可以添加或删除列
> 自动对齐

* 创建一个dataframe
> `pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)`
>> 参数说明
data：DataFrame 的数据部分，可以是字典、二维数组、Series、DataFrame 或其他可转换为 DataFrame 的对象。如果不提供此参数，则创建一个空的 DataFrame。
index：DataFrame 的行索引，用于标识每行数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
columns：DataFrame 的列索引，用于标识每列数据。可以是列表、数组、索引对象等。如果不提供此参数，则创建一个默认的整数索引。
dtype：指定 DataFrame 的数据类型。可以是 NumPy 的数据类型，例如 np.int64、np.float64 等。如果不提供此参数，则根据数据自动推断数据类型。
copy：是否复制数据。默认为 False，表示不复制数据。如果设置为 True，则复制输入的数据。

##### CSV文件
* CSV（Comma-Separated Values，逗号分隔值，有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本形式存储表格数据（数字和文本）
* `pandas.read_csv()`是从CSV文件读取数据并加载为datraframe`DataFrame.to_csv()`为将dataframe写入到CSV文件
* read_csv常用参数
|参数|说明|默认值|
|---|---|---|
|filepath_or_buffer|CSV 文件的路径或文件对象（支持 URL、文件路径、文件对象等）|必需参数|
|sep|定义字段分隔符，默认是逗号（,），可以改为其他字符，如制表符（\t）|','|
|header|指定行号作为列标题，默认为 0（表示第一行），或者设置为 None 没有标题|0|
|names|	自定义列名，传入列名列表|None|
|index_col|	用作行索引的列的列号或列名|None|
|usecols|读取指定的列，可以是列的名称或列的索引|None|
|dtype|	强制将列转换为指定的数据类型|None|
|skiprows|跳过文件开头的指定行数，或者传入一个行号的列表|None|
|nrows|读取前 N 行数据|None|
|na_values|指定哪些值应视为缺失值（NaN）|None|
|skipfooter|跳过文件结尾的指定行数|0|
|encoding|文件的编码格式（如 utf-8，latin1 等）|None|

##### excel文件
* `pd.read_excel()`用于读取excel文件，返回dataframe
* `DataFrame.to_excel()`用于将dataframe写入excel
* `pd.ExcelFile()`加载excel文件并访问表单
* `pd.ExcelWriter()`写入多个dataframe到同一excel文件不同表单

### 数据清洗
数据清洗与预处理的常见步骤：

1.缺失值处理：识别并填补缺失值，或删除含缺失值的行/列。
2.重复数据处理：检查并删除重复数据，确保每条数据唯一。
3.异常值处理：识别并处理异常值，如极端值、错误值。
4.数据格式转换：转换数据类型或进行单位转换，如日期格式转换。
5.标准化与归一化：对数值型数据进行标准化（如 Z-score）或归一化（如 Min-Max）。
6.类别数据编码：将类别变量转换为数值形式，常见方法包括 One-Hot 编码和标签编码。
7.文本处理：对文本数据进行清洗，如去除停用词、词干化、分词等。
8.数据抽样：从数据集中抽取样本，或通过过采样/欠采样处理类别不平衡。
9.特征工程：创建新特征、删除不相关特征、选择重要特征等。

#### 清洗空值
* 如果我们要删除包含空字段的行，可以使用 dropna() 方法，语法格式如下：<br>`DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)`
* 参数说明：
axis：默认为 0，表示逢空值剔除整行，如果设置参数 axis＝1 表示逢空值去掉整列。
how：默认为 'any' 如果一行（或一列）里任何一个数据有出现 NA 就去掉整行，如果设置 how='all' 一行（或列）都是 NA 才去掉这整行。
thresh：设置需要多少非空值的数据才可以保留下来的。
subset：设置想要检查的列。如果是多个列，可以使用列名的 list 作为参数。
inplace：如果设置 True，将计算得到的值直接覆盖之前的值并返回 None，修改的是源数据。

* 可使用`.isnull()`判断是否为空单元返回值为布尔值
* 也可用`fillna()`方法替换空字段`.fillna(替换后内容,inplace=True)`，也可指定某一列替换，只需在调用dataframe时加上 `['列名字']`即可
* 可调用`mean()`计算列的平均值`median()`计算列的中位数`mode()`计算列的众数
* 可使用`duplicated()`若对应数据为重复，则会返回True，否则为False`drop_duplicates()`用于删除重复数据
* 以下为常用数据清洗与预处理常见方法
|操作|方法/步骤|说明|常用函数/方法|
|--|--|--|--|
|缺失值处理|填充缺失值|使用指定的值（如均值、中位数、众数等）填充缺失值。|df.fillna(value)|
||删除缺失值	|删除包含缺失值的行或列。|df.dropna()|
|重复数据处理|删除重复数据|删除 DataFrame 中的重复行。|df.drop_duplicates()|
|异常值处理|异常值检测（基于统计方法）|通过 Z-score 或 IQR 方法识别并处理异常值。|自定义函数（如基于 Z-score 或 IQR）|
||替换异常值|使用合适的值（如均值或中位数）替换异常值。|自定义函数（如替换异常值）|
|数据格式转换|转换数据类型|将数据类型从一个类型转换为另一个类型，如将字符串转换为日期。|df.astype()|
||日期时间格式转换|转换字符串或数字为日期时间类型。|pd.to_datetime()|
|标准化与归一化|标准化|将数据转换为均值为0，标准差为1的分布。|StandardScaler()|
||归一化|将数据缩放到指定的范围（如 [0, 1]）。|MinMaxScaler()|
|类别数据编码|标签编码|将类别变量转换为整数形式。|LabelEncoder()|
||独热编码（One-Hot Encoding）|将每个类别转换为一个新的二进制特征|pd.get_dummies()|
|文本数据处理|去除停用词|从文本中去除无关紧要的词，如 "the" 、 "is" 等。|自定义函数（基于 `nltk` 或 `spaCy`）|
||词干化与词形还原|提取词干或恢复单词的基本形式。|nltk.stem.PorterStemmer()|
||分词|将文本分割成单词或子词。|nltk.word_tokenize()|
|数据抽样|随机抽样|从数据中随机抽取一定比例的样本。|df.sample()|
||上采样与下采样|通过过采样（复制少数类样本）或欠采样（减少多数类样本）来平衡数据集中的类别分布。|`SMOTE()`（上采样）； `RandomUnderSampler()`（下采样）|
|特征工程|特征选择|选择对目标变量有影响的特征，去除冗余或无关特征。|SelectKBest()|
||特征提取|从原始数据中创建新的特征，提升模型的预测能力。|PolynomialFeatures()|
||特征缩放|对数值特征进行缩放，使其具有相同的量级。|MinMaxScaler()` 、 `StandardScaler()|
|类别特征映射|特征映射|将类别变量映射为对应的数字编码。|自定义映射函数|
|数据合并与连接|合并数据|将多个 DataFrame 按照某些列合并在一起，支持内连接、外连接、左连接、右连接等。|pd.merge()|
||连接数据|将多个 DataFrame 进行行或列拼接。|pd.concat()|
|数据重塑|数据透视表|将数据根据某些维度进行分组并计算聚合结果。|pd.pivot_table()|
||数据变形|改变数据的形状，如从长格式转为宽格式或从宽格式转为长格式。|df.melt()` 、 `df.pivot()|
|数据类型转换与处理|字符串处理|对字符串数据进行处理，如去除空格、转换大小写等。|`str.replace()` 、 `str.upper()` 等|
||分组计算|按照某个特征分组后进行聚合计算。|df.groupby()|
|缺失值预测填充|使用模型预测填充缺失值|使用机器学习模型（如回归模型）预测缺失值，并填充缺失数据。|自定义模型（如 `sklearn.linear_model.LinearRegression`）|
|时间序列处理|时间序列缺失值填充|使用时间序列的方法（如前向填充、后向填充）填充缺失值。|df.fillna(method='ffill')|
||滚动窗口计算|使用滑动窗口进行时间序列数据的统计计算（如均值、标准差等）。|df.rolling(window=5).mean()|
|数据转换与映射|数据映射与替换|将数据中的某些值替换为其他值。|df.replace()|