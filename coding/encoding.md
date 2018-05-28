# encoding

see
- https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/
- https://www.zhihu.com/question/23374078

ascii
- 1963, ascii: 7b(0-127) encoding for english alphabets and control characters.
~~~~
control
00 ~ 1F 

printable
20 ~ 20: sp ! " # $ % & ' ( )
2A ~ 2F: * + , - . /
30 ~ 39: 0-9
3A ~ 40: : ; < = > ? @
41 ~ 5A: A-Z
5B ~ 60: [ \ ] ^ _ `
61 ~ 7A: a-z
7B ~ 7E: { | } ~
~~~~

ascii variations
- ascii variations: use 8th bit for control characters, use multiple bytes for asian characters etc.
- gb2312->gbk->gb18030 vs big5.

unicode
- unicode, ucs-2 = utf-16: to support all characters in the world, 16b encoding,
- bom: to support both little/big endian for 16b encoding, place U+FEFF at start.
- unicode, utf-8: 1-4B, where 1B character same with ascii.
~~~~
U+ 0000 ~ U+ 007F: 0XXXXXXX # 1+7b
U+ 0080 ~ U+ 07FF: 110XXXXX 10XXXXXX # 5+11b
U+ 0800 ~ U+ FFFF: 1110XXXX 10XXXXXX 10XXXXXX # 8+16b
U+10000 ~ U+1FFFF: 11110XXX 10XXXXXX 10XXXXXX 10XXXXXX # 11+21b
~~~~
- utf-8 with bom: not require or recommend, only used to support legacy system e.g. excel.

# encoding in ruby

see: https://ruby-doc.org/core-2.5.0/Encoding.html

script encoding
- target: each script code file
- default: utf-8 since v2.0
- get: keyword __ENCODING__
- set: magic comment e.g. # encoding: UTF-8

locale encoding
- Encoding::locale_charmap -> string: platform dependent.
- Encoding::find(string|'external'|'internal'|'locale') -> enc

filesystem encoding
- Encoding::find('filesystem') -> enc

external encoding
- target: each IO objects for read
- default: Encoding::default_external=os locale
- global get: Encoding::default_external
- global set: ruby -E Shift-JIS, (not recommend) Encoding::default_external=
- get: IO#external_encoding
- set: IO#set_encoding

internal encoding
- target: each IO objects for processing, transcode when read
- default: nil(no transcoding)
- global get: Encoding::default_internal
- global set: ruby -E Shift-JIS:UTF-8
- get: IO#internal_encoding
- set: IO#set_encoding
