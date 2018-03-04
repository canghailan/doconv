# 文档格式转换服务

## 字体
* [Aodbe Source Serif Pro](https://github.com/adobe-fonts/source-serif-pro)
  * [Roman](https://github.com/adobe-fonts/source-serif-pro/releases/download/variable-fonts/SourceSerifVariable-Roman.otf)
* [Aodbe Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro/)
  * [Roman](https://github.com/adobe-fonts/source-sans-pro/releases/download/variable-fonts/SourceSansVariable-Roman.otf)
  * [Italic](https://github.com/adobe-fonts/source-sans-pro/releases/download/variable-fonts/SourceSansVariable-Italic.otf)
* [Aodbe Source Code Pro](https://github.com/adobe-fonts/source-code-pro)
  * [Roman](https://github.com/adobe-fonts/source-code-pro/releases/download/variable-fonts/SourceCodeVariable-Roman.otf)
  * [Italic](https://github.com/adobe-fonts/source-code-pro/releases/download/variable-fonts/SourceCodeVariable-Italic.otf)
* [Aodbe Source Han Serif 思源宋体](https://github.com/adobe-fonts/source-han-serif)
  * [Simplified Chinese 简体中文 ExtraLight + Light + Regular + Medium](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifSC_EL-M.zip)
  * [Simplified Chinese 简体中文 SemiBold + Bold + Heavy](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifSC_SB-H.zip)
  * [Traditional Chinese 繁體中文 ExtraLight + Light + Regular + Medium](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifTC_EL-M.zip)
  * [Traditional Chinese 繁體中文 SemiBold + Bold + Heavy](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifTC_SB-H.zip)
  * [Japanese 日本語 ExtraLight + Light + Regular + Medium](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifJ_EL-M.zip)
  * [Japanese 日本語 SemiBold + Bold + Heavy](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifJ_SB-H.zip)
  * [Korean 한국어 ExtraLight + Light + Regular + Medium](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifK_EL-M.zip)
  * [Korean 한국어 SemiBold + Bold + Heavy](https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifK_SB-H.zip)
* [Aodbe Source Han Sans 思源黑体](https://github.com/adobe-fonts/source-han-sans)
  * [Simplified Chinese 简体中文](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansSC.zip)
  * [Traditional Chinese 繁體中文](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansTC.zip)
  * [Japanese 日本語](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansJ.zip)
  * [Korean 한국어](https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansK.zip)
* [Google Noto Emoji](https://github.com/googlei18n/noto-emoji)
  * [Regular](https://raw.githubusercontent.com/googlei18n/noto-emoji/master/fonts/NotoEmoji-Regular.ttf)
  * [Color](https://raw.githubusercontent.com/googlei18n/noto-emoji/master/fonts/NotoColorEmoji.ttf)
* [文鼎字库](http://www.arphic.com.cn/)
  * 商用免费
    * 文鼎细上海宋
    * 文鼎中楷
    * 文鼎简报宋
    * 文鼎简中楷
* [文泉驿](https://sourceforge.net/projects/wqy)
* [IBM Plex](https://github.com/IBM/plex)
* [Google Roboto](https://github.com/google/roboto)
* [Google Noto](https://github.com/googlei18n/noto-fonts)
* [Google Noto CJK](https://github.com/googlei18n/noto-cjk)
* [FiraCode](https://github.com/tonsky/FiraCode)
* [方正字库](http://www.foundertype.com/index.php/FindFont/index.html)
  * 个人免费
    * 方正黑体简体
    * 方正书宋简体
    * 方正仿宋简体
    * 方正楷体简体
  * 不可商用
    * 微软雅黑
* [Apple San Francisco](https://github.com/AppleDesignResources/SanFranciscoFont)
  * 不可商用

### 字体安装
```shell
mkdir -p /usr/share/fonts/truetype /usr/share/fonts/opentype
apt-get -y install fontconfig
fc-cache -fv
```

### 字体参考资料
[免费中文字体](http://wiki.ubuntu.org.cn/%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87%E5%AD%97%E4%BD%93)


## [LibreOffice](https://libreoffice.org/)
官方仓库中版本过低，下载安装最新版本
```shell
apt-get install -y openjdk-8-jre-headless libglu1-mesa libxinerama1 libdbus-glib-1-2 libcairo2 libsm6
curl -OL 'http://download.documentfoundation.org/libreoffice/stable/6.0.2/deb/x86_64/LibreOffice_6.0.2_Linux_x86-64_deb.tar.gz'
dpkg -i LibreOffice*/DEBS/*.deb
```

## [unoconv](https://github.com/dagwieers/unoconv)
官方仓库中版本过低，下载安装最新版本
```shell
curl -OL 'https://raw.githubusercontent.com/dagwieers/unoconv/0.8.2/unoconv'
```

## [ImageMagick](https://www.imagemagick.org/)

## [Pandoc](https://pandoc.org/)
官方仓库中版本过低，下载安装最新版本
```shell
curl -OL 'https://github.com/jgm/pandoc/releases/download/2.1.2/pandoc-2.1.2-1-amd64.deb'
```

## [TexLive](https://www.tug.org/texlive/)
TODO
```shell
DEBIAN_FRONTEND=noninteractive
apt-get install -yq texlive
```

## [Apache httpd](https://httpd.apache.org/)
启用静态文件、CGI

## [Supervisor](http://supervisord.org/)
* Apache
* unoconv

## 使用方法
```http
POST http://localhost/cgi-bin/worker.cgi
Content-Type: text/plain;charset=utf-8

mkdir -p /workspace/1/ \
&& cd /workspace/1/ \
&& curl -o a.ppt -O http://localhost/1.pptx \
&& unoconv -f pdf a.ppt \
&& convert a.pdf a.jpg
```

## TODO
* 字体配置待优化
* 镜像大小待优化
* CGI脚本待优化，目前未考虑安全及易用性问题
* 文档待完善

## 附录：阿里云Docker镜像
```shell
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get -y update
sudo apt-get -y install docker-ce

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": [""]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```