# python开发配置自用

## 安装anaconda3
#### 官网下载anaconda3
[官网地址](https://www.anaconda.com/download/)
#### 安装anaconda
默认安装、手动添加环境变量即可。一般添加~/anaconda3 和 ~/anaconda3/script即可
注意：不要安装在带空格的目录下，不要使用管理员权限安装，不要安装一些需要权限的地方
#### 配置国内镜像
```shell
# 添加Anaconda的TUNA镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
# 设置搜索时显示通道地址
conda config --set show_channel_urls yes
```
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#### 安装机器学习相关库
```shell
conda install 包名
```
## 安装MySQL