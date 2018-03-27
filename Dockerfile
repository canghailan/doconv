FROM ubuntu:latest

LABEL maintainer="canghailan@gmail.com"

WORKDIR /doconv/
COPY supervisord.conf /etc/supervisor/conf.d/
COPY graph.json /usr/lib/cgi-bin/graph.json
COPY worker.py /usr/lib/cgi-bin/worker.cgi

RUN apt-get update \
 && apt-get install -y curl unzip fontconfig supervisor apache2 imagemagick openjdk-8-jre-headless libglu1-mesa libxinerama1 libdbus-glib-1-2 libcairo2 libsm6 fonts-arphic-* \
 && echo "download fonts" \
 && mkdir -p /tmp/fonts/ /usr/share/fonts/truetype /usr/share/fonts/opentype \
 && echo "download source-sans-pro" \
 && curl -o /usr/share/fonts/opentype/SourceSansVariable-Italic.otf -OL 'https://github.com/adobe-fonts/source-sans-pro/releases/download/variable-fonts/SourceSansVariable-Italic.otf' \
 && curl -o /usr/share/fonts/opentype/SourceSansVariable-Roman.otf -OL 'https://github.com/adobe-fonts/source-sans-pro/releases/download/variable-fonts/SourceSansVariable-Roman.otf' \
 && echo "download source-serif-pro" \
 && curl -o /usr/share/fonts/opentype/SourceSerifVariable-Roman.otf -OL 'https://github.com/adobe-fonts/source-serif-pro/releases/download/variable-fonts/SourceSerifVariable-Roman.otf' \
 && echo "download source-code-pro" \
 && curl -o /usr/share/fonts/opentype/SourceCodeVariable-Roman.otf -OL 'https://github.com/adobe-fonts/source-code-pro/releases/download/variable-fonts/SourceCodeVariable-Roman.otf' \
 && curl -o /usr/share/fonts/opentype/SourceCodeVariable-Italic.otf -OL 'https://github.com/adobe-fonts/source-code-pro/releases/download/variable-fonts/SourceCodeVariable-Italic.otf' \
 && echo "download source-han-sans" \
 && curl -o /tmp/fonts/SourceHanSansSC.zip -OL 'https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansSC.zip' \
 && curl -o /tmp/fonts/SourceHanSansTC.zip -OL 'https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansTC.zip' \
 && curl -o /tmp/fonts/SourceHanSansJ.zip -OL 'https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansJ.zip' \
 && curl -o /tmp/fonts/SourceHanSansK.zip -OL 'https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansK.zip' \
 && echo "download source-han-serif" \
 && curl -o /tmp/fonts/SourceHanSerifSC_EL-M.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifSC_EL-M.zip' \
 && curl -o /tmp/fonts/SourceHanSerifSC_SB-H.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifSC_SB-H.zip' \
 && curl -o /tmp/fonts/SourceHanSerifTC_EL-M.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifTC_EL-M.zip' \
 && curl -o /tmp/fonts/SourceHanSerifTC_SB-H.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifTC_SB-H.zip' \
 && curl -o /tmp/fonts/SourceHanSerifJ_EL-M.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifJ_EL-M.zip' \
 && curl -o /tmp/fonts/SourceHanSerifJ_SB-H.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifJ_SB-H.zip' \
 && curl -o /tmp/fonts/SourceHanSerifK_EL-M.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifK_EL-M.zip' \
 && curl -o /tmp/fonts/SourceHanSerifK_SB-H.zip -OL 'https://github.com/adobe-fonts/source-han-serif/raw/release/OTF/SourceHanSerifK_SB-H.zip' \
 && echo "download noto-emoji" \
 && curl -o /usr/share/fonts/truetype/NotoEmoji-Regular.ttf -OL 'https://raw.githubusercontent.com/googlei18n/noto-emoji/master/fonts/NotoEmoji-Regular.ttf' \
 && curl -o /usr/share/fonts/truetype/NotoColorEmoji.ttf -OL 'https://raw.githubusercontent.com/googlei18n/noto-emoji/master/fonts/NotoColorEmoji.ttf' \
 && echo "install fonts" \
 && unzip "/tmp/fonts/*.zip" -d /tmp/fonts/ \
 && find /tmp/fonts/ -name "*.otf" | xargs -I {} cp {} /usr/share/fonts/opentype \
 && fc-cache -fv \
 && echo "install LibreOffice" \
 && curl -o /tmp/LibreOffice.tar.gz -OL 'http://download.documentfoundation.org/libreoffice/stable/6.0.2/deb/x86_64/LibreOffice_6.0.2_Linux_x86-64_deb.tar.gz' \
 && tar -xzvf /tmp/LibreOffice.tar.gz -C /tmp/ \
 && dpkg -i /tmp/LibreOffice*/DEBS/*.deb \
 && echo "install pandoc" \
 && curl -o /tmp/pandoc.deb -OL 'https://github.com/jgm/pandoc/releases/download/2.1.2/pandoc-2.1.2-1-amd64.deb' \
 && dpkg -i /tmp/pandoc.deb \
 && echo "install unoconv" \
 && curl -o /usr/local/bin/unoconv -OL 'https://raw.githubusercontent.com/dagwieers/unoconv/0.8.2/unoconv' \
 && chmod a+x /usr/local/bin/unoconv \
 && echo "configure apache" \
 && mkdir -p /etc/apache2/logs/ \
 && cp -f /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/ \
 && chmod a+x /usr/lib/cgi-bin/worker.cgi \
 && echo "configure supervisord" \
 && mkdir -p /var/log/supervisor/ \
 && echo "configure WORKDIR" \
 && chmod a+rwx /doconv \
 && ln -s /doconv /var/www/html/ \
 && echo "clean" \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf /tmp/*

EXPOSE 80
CMD ["/usr/bin/supervisord"]