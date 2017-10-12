# python开发配置自用

## 安装anaconda3
#### 官网下载anaconda3
[官网地址](https://www.anaconda.com/download/)
#### 安装anaconda
默认安装、手动添加环境变量即可。一般添加~/anaconda3 和 ~/anaconda3/script即可
注意：不要安装在带空格的目录下，不要使用管理员权限安装，不要安装一些需要权限的地方
#### 配置国内镜像
```powershell
# 添加Anaconda的清华TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# 设置搜索下载时显示通道地址
conda config --set show_channel_urls yes
```
#### 安装机器学习相关库
```powershell
conda install numpy scipy scikit-learn pandas matplotlib
```
#### 额外：环境管理相关
```powershell
#查看当前系统下的环境
conda info -e
#创建新环境,如果不指定版本则安装最新版本
conda create -n py27 python =2.7
#创建新环境的同时安装相关包
conda create -n py27 numpy matplotlib python=2.7
# 切换到新环境  linux/Mac 下需要使用source activate env_name
activate py27
#退出环境，也可以使用`activate root`切回root环境
deactivate py27
```

#### 在jupyter上安装2.7的kernel

首先在安装好另外版本的python(如2.7)后，先安装ipykernel，如下所示：

```powershell
conda install --prefix=~\envs\py27 ipykernel
```

然后激活该kernel，在该kernel下进行进一步安装

```powershell
activate ~\envs\py27

python -m ipykernel install --user
```



## 安装MySQL

