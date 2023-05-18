FROM ubuntu:latest

RUN apt update && apt install -y wget curl build-essential

# download mecab
RUN FILE_ID=0B4y35FiV1wh7cENtOXlicTFaRUE && \
  FILE_NAME=mecab-0.996.tar.gz && \
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null && \
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" && \
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

# download dic
RUN FILE_ID=0B4y35FiV1wh7X2pESGlLREpxdXM && \
  FILE_NAME=mecab-jumandic-7.0-20130310.tar.gz && \
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null && \
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" && \
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

# download CRF++
RUN FILE_ID=0B4y35FiV1wh7QVR6VXJ5dWExSTQ && \
  FILE_NAME=CRF++-0.58.tar.gz && \
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null && \
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" && \
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

# download cabocha
RUN FILE_ID=0B4y35FiV1wh7SDd1Q1dUQkZQaUU && \
  FILE_NAME=cabocha-0.69.tar.bz2 && \
  curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null && \
  CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)" && \
  curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}

# configure mecab
RUN tar zxfv mecab-0.996.tar.gz && cd mecab-0.996 && ./configure --enable-utf8-only && make && make check && make install && ldconfig && sed -i -e "s/^dicdir.*/dicdir =  \/usr\/local\/lib\/mecab\/dic\/jumandic\//g" /usr/local/etc/mecabrc

# configure dic
RUN tar zxfv mecab-jumandic-7.0-20130310.tar.gz && cd mecab-jumandic-7.0-20130310 && ./configure --with-charset=utf8 && make && make install

# configure CRF++
RUN tar zxfv CRF++-0.58.tar.gz && cd CRF++-0.58 && ./configure && make && make install && ldconfig

# configure cabocha
RUN tar xf cabocha-0.69.tar.bz2 && cd cabocha-0.69 && ./configure --with-posset=juman --with-charset=utf8 --enable-utf8-only && make && make check && make install && ldconfig


# RUN echo "太郎は花子が読んでいる本を次郎に渡した" | cabocha -d /usr/local/lib/mecab/dic/jumandic/

